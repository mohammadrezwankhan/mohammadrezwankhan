"""Regression checks for committed reruns and decoration recovery.

Run with python -m unittest discover -s scripts/brand-uniformity -p 'test_*.py'.
The Git fixture commits real generated output before exercising a second run.
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import re
import subprocess
import tempfile
import unittest
import xml.etree.ElementTree as ET

SPEC = spec_from_file_location('brand_generator', Path(__file__).with_name('generate.py'))
GEN = module_from_spec(SPEC)
SPEC.loader.exec_module(GEN)

ORIGINAL_SCRIPT = '<script>const label = "#00e5ff <img class=\\"brand-avatar\\">";\n' + GEN.RENDERER_OLD + '\n</script>'
ORIGINAL_JSON = '<script type="application/json">{ "physical_limit": 3, "paint": "#00e5ff" }</script>'
SVG = '<svg xmlns="http://www.w3.org/2000/svg" aria-labelledby="section-01-title"><style>:root{--bg:#083344}</style><title id="section-01-title">Physical boundary</title><text x="2" y="3">01</text></svg>'


class GeneratorRegressionTests(unittest.TestCase):
    def test_svg_write_preserves_only_an_exact_single_terminal_lf(self):
        # Removing the narrow write guard must reproduce the web editor's
        # otherwise-identical SVG losing its appended terminal LF on rerun.
        content = '<svg xmlns="http://www.w3.org/2000/svg"><title>Exact text</title></svg>'
        with tempfile.TemporaryDirectory() as directory:
            repo = Path(directory)
            target = repo / 'assets/brand-uniformity/hero.svg'
            target.parent.mkdir(parents=True)
            for existing, expected in (
                (content + '\n', content + '\n'),
                (content, content),
                (content + '\n\n', content),
                (content + '\r\n', content),
                (content.replace('Exact text', 'Different text') + '\n', content),
                (content.replace('</title>', ' </title>') + '\n', content),
            ):
                with self.subTest(existing=existing):
                    target.write_bytes(existing.encode())
                    GEN.write(repo, 'assets/brand-uniformity/hero.svg', content)
                    self.assertEqual(target.read_bytes(), expected.encode())
            html = repo / 'docs/index.html'
            html.parent.mkdir(parents=True)
            html.write_text(content + '\n')
            GEN.write(repo, 'docs/index.html', content)
            self.assertEqual(html.read_bytes(), content.encode(), 'No tolerance for other output types')

    def test_committed_rerun_preserves_pages_assets_scripts_and_json(self):
        # Reintroducing unconditional injection must duplicate output on run two.
        with tempfile.TemporaryDirectory() as directory:
            repo = Path(directory) / 'fixture'
            repo.mkdir()
            def git(*args):
                return subprocess.run(['git', *args], cwd=repo, check=True, capture_output=True)
            git('init', '-q')
            git('config', 'user.name', 'Fixture')
            git('config', 'user.email', 'fixture@example.invalid')
            pages = {'docs/index.html': '<svg class="brand-icon" xmlns="http://www.w3.org/2000/svg"></svg>',
                     'docs/portfolio/index.html': '<span class="mark">Original mark</span><div class="isometric">Original topology</div>',
                     'docs/native-lessons.html': '<nav class="surface-nav"></nav><img src="visuals/original.svg" alt="Original diagram">'}
            for path, body in pages.items():
                target = repo / path
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text('<!doctype html><html lang="en"><head><style>p{color:#00e5ff}</style></head><body><p>Unchanged equations &amp; limits.</p><img class="original-art" data-brand-decoration="true" src="original.svg" alt="Original content">' + body + SVG + ORIGINAL_SCRIPT + ORIGINAL_JSON + '</body></html>')
            (repo / 'README.md').write_text('Original prose [link](docs/index.html)\n')
            asset = repo / 'assets/hero-25d.svg'
            asset.parent.mkdir()
            asset.write_text(SVG)
            git('add', '.')
            git('commit', '-qm', 'baseline')
            GEN.apply_repository(repo)
            first = {p.relative_to(repo): p.read_bytes() for p in repo.rglob('*') if p.is_file() and '.git' not in p.parts}
            for name in pages:
                html = (repo / name).read_text()
                self.assertEqual(html.count('data-avatar-brand='), 1)
                self.assertEqual(html.count('class="brand-avatar" data-brand-decoration="true"'), 1)
                self.assertIn(ORIGINAL_JSON, html)
                expected_script = ORIGINAL_SCRIPT.replace(GEN.RENDERER_OLD, GEN.RENDERER_NEW) if name == 'docs/index.html' else ORIGINAL_SCRIPT
                self.assertIn(expected_script, html)
                self.assertIn('Unchanged equations &amp; limits.', html)
            git('add', '.')
            git('commit', '-qm', 'generated')
            try:
                GEN.apply_repository(repo)
            except ET.ParseError as error:
                self.fail(f"Committed branded input must remain valid XML: {error}")
            second = {p.relative_to(repo): p.read_bytes() for p in repo.rglob('*') if p.is_file() and '.git' not in p.parts}
            self.assertEqual(first.keys(), second.keys())
            for path in first:
                with self.subTest(path=path):
                    self.assertEqual(first[path], second[path], 'Committed branded input must be a fixed point')
            # Recover an already duplicated legacy injection without discarding
            # unrelated artwork, then reach the same normal generated output.
            for name in pages:
                target = repo / name
                html = target.read_text()
                for pattern in (r' data-avatar-brand="[^"]*"',
                                r'<link rel="stylesheet" href="[^"]*brand\.css">\n',
                                r'<img class="brand-avatar" data-brand-decoration="true"[^>]*>',
                                r'<svg class="champion-art" data-brand-decoration="true"[^>]*>[\s\S]*?</svg>\n'):
                    html = re.sub(pattern, lambda m: m.group() * 2, html, count=1)
                target.write_text(html)
            git('add', '.')
            git('commit', '-qm', 'legacy duplicate decorations')
            GEN.apply_repository(repo)
            for name in pages:
                with self.subTest(legacy_page=name):
                    self.assertEqual((repo / name).read_bytes(), first[Path(name)])

    def test_svg_restyling_does_not_duplicate_theme_classes_or_seals(self):
        first = GEN.restyle_svg(SVG, add_seal=True)
        try:
            rerun = GEN.restyle_svg(first, add_seal=True)
        except ET.ParseError as error:
            self.fail(f"Restyled SVG must remain valid XML on rerun: {error}")
        self.assertEqual(rerun, first)
        # Repeated exact generated styles/seals collapse, not original elements.
        styles = re.findall(r'<style>[\s\S]*?</style>', first)[1:]
        seal = '<g data-brand-decoration="true" aria-hidden="true">' + GEN.core(810, 375, 86) + '</g>'
        duplicate = first.replace('</svg>', ''.join(styles) + seal + '</svg>')
        self.assertEqual(GEN.restyle_svg(duplicate, add_seal=True), first)
        # Recovery also collapses only the generator's known repeated additions.
        decorated = first.replace('</svg>', GEN.core(1, 1, 1) + '</svg>')
        second = GEN.restyle_svg(decorated, add_seal=True)
        self.assertIn(GEN.core(1, 1, 1), second, 'Non-decoration source artwork must remain')
        self.assertEqual(GEN.restyle_svg(second, add_seal=True), second)



if __name__ == '__main__':
    unittest.main()
