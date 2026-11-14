#!/usr/bin/env python3
"""Extend existing reading surfaces with the canonical pixel-core identity.

No model, lesson configuration, workflow or archived asset is regenerated.
Run from a clean checkout; supply one or more --repository paths.
"""
from __future__ import annotations

import argparse
import colorsys
import hashlib
import json
from pathlib import Path
import re
import subprocess
import xml.etree.ElementTree as ET

HERE = Path(__file__).resolve().parent
PROFILE = HERE.parents[1]
PALETTE = ['#100b18', '#231331', '#5c2a72', '#d94a4a', '#ff9f1c', '#ffe66d', '#fff6c8']
SVG_NS = '{http://www.w3.org/2000/svg}'
SOURCE = PROFILE / 'assets/makeover/avatar-static.svg'
source_root = ET.fromstring(SOURCE.read_text())
source_group = next(g for g in source_root.findall(f'{SVG_NS}g') if g.get('transform'))
CORE = ''.join(f'<path fill="{p.get("fill")}" d="{p.get("d")}"/>' for p in source_group)
assert [p.get('fill') for p in source_group] == PALETTE[1:]


def core(x: float, y: float, size: float) -> str:
    """The existing six path strings, under uniform scale and translation only."""
    return f'<g data-canonical-core="48" transform="translate({x:g} {y:g}) scale({size / 48:g})">{CORE}</g>'


def avatar() -> str:
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" width="48" height="48" '
            'role="img" aria-labelledby="avatar-title"><title id="avatar-title">Rezwan pixel energy core</title>'
            '<rect width="48" height="48" fill="#100b18"/>' + core(0, 0, 48) + '</svg>\n')


def champion(animated: bool) -> str:
    motion = '''<style>
.brand-signal{animation:brand-signal-travel 4.8s cubic-bezier(.22,1,.36,1) 1 both;transform-box:view-box}
.brand-signal.second{animation-name:brand-return-travel}
.brand-edge{animation:brand-edge-light 4.8s ease-out 1 both}
@keyframes brand-signal-travel{0%,100%{transform:translate(0,0);opacity:.6}35%{transform:translate(62px,-31px);opacity:1}70%{transform:translate(125px,-62px);opacity:.6}}
@keyframes brand-return-travel{0%,100%{transform:translate(0,0);opacity:.6}35%{transform:translate(-62px,-31px);opacity:1}70%{transform:translate(-125px,-62px);opacity:.6}}
@keyframes brand-edge-light{0%,100%{opacity:.55}45%{opacity:1}}
@media(prefers-reduced-motion:reduce){.brand-signal,.brand-edge{animation:none!important}}
</style>''' if animated else ''
    return ('''<svg xmlns="http://www.w3.org/2000/svg" width="560" height="360" viewBox="0 0 560 360" role="img" aria-labelledby="champion-title champion-desc">
<title id="champion-title">Rezwan energy-core champion in 2.5D</title>
<desc id="champion-desc">The unchanged original pixel avatar stands above layered isometric planes. Square signals are illustrative brand motion, not a measurement or simulation. The complete composition remains visible without motion.</desc>
''' + motion + '''
<rect width="560" height="360" fill="#100b18"/>
<path d="M280 215 481 279 280 346 79 279Z" fill="#231331"/>
<path d="M82 260 280 326 478 260v15l-198 66-198-66Z" fill="#231331" stroke="#5c2a72" stroke-width="1.2"/>
<path d="M280 194 478 260 280 326 82 260Z" fill="#231331" stroke="#5c2a72" stroke-width="1.4"/>
<path d="M139 239 280 286 421 239v13l-141 47-141-47Z" fill="#5c2a72"/>
<path d="M280 192 421 239 280 286 139 239Z" fill="#231331" stroke="#ff9f1c" stroke-width="1.2"/>
<path d="M280 286v13m0 27v15" stroke="#ff9f1c" stroke-width="1.2"/>
<path class="brand-edge" d="m82 260 198 66 198-66" fill="none" stroke="#ff9f1c" stroke-width="2"/>
<path d="M93 279 155 248 218 217M467 279 405 248 342 217" fill="none" stroke="#5c2a72" stroke-width="2"/>
<path d="M166 34 189 21h223v225l-23 13Z" fill="#5c2a72" opacity=".65"/>
<path d="M166 34h223v225H166Z" fill="#100b18"/>
''' + core(161, 21, 240) + '''
<rect class="brand-signal" x="89" y="275" width="8" height="8" fill="#ffe66d"/>
<rect class="brand-signal second" x="463" y="275" width="8" height="8" fill="#ff9f1c"/>
<path d="M67 261h10m406 0h10M280 349v7" stroke="#d94a4a" stroke-width="2"/>
</svg>\n''')


SPECIAL = {
    '#00e5ff': '#ff9f1c', '#00e676': '#ffe66d', '#10b981': '#ffe66d',
    '#f59e0b': '#ff9f1c', '#8b5cf6': '#5c2a72', '#f43f5e': '#d94a4a',
    '#083344': '#231331', '#064e3b': '#231331', '#451a03': '#231331',
    '#2e1065': '#5c2a72', '#4c0519': '#231331', '#0a192f': '#100b18',
    '#0d1828': '#231331', '#182d41': '#5c2a72', '#ff6d00': '#ff9f1c',
    '#00b0ff': '#ffe66d', '#ffab00': '#ff9f1c', '#448aff': '#ffe66d',
    '#007b8b': '#5c2a72', '#08734e': '#5c2a72', '#8b5200': '#5c2a72',
    '#6444a6': '#5c2a72', '#a91d43': '#5c2a72', '#005fcc': '#5c2a72',
}


def brand_hex(match: re.Match[str]) -> str:
    token = match.group().lower()
    if token in PALETTE:
        return token
    if token in SPECIAL:
        return SPECIAL[token]
    raw = token[1:]
    if len(raw) in (3, 4):
        raw = ''.join(c * 2 for c in raw)
    alpha = raw[6:]
    rgb = [int(raw[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    hue, light, saturation = colorsys.rgb_to_hls(*rgb)
    if light > .66:
        value = '#fff6c8'
    elif light < .08:
        value = '#100b18'
    elif light < .19:
        value = '#231331'
    elif saturation > .55:
        value = '#ff9f1c' if hue < .5 else '#d94a4a' if hue > .8 else '#ffe66d'
    elif light < .36:
        value = '#5c2a72'
    else:
        value = '#fff6c8'
        alpha = alpha or 'b8'
    return value + alpha


def recolor(text: str) -> str:
    text = re.sub(r'#[0-9a-fA-F]{8}\b|#[0-9a-fA-F]{6}\b|#[0-9a-fA-F]{4}\b|#[0-9a-fA-F]{3}\b', brand_hex, text)
    def rgb_replace(match: re.Match[str]) -> str:
        prefix, r, g, b, rest = match.groups()
        color = brand_hex(re.match(r'.+', '#' + ''.join(f'{int(x):02x}' for x in (r, g, b))))
        vals = ','.join(str(int(color[i:i+2], 16)) for i in (1, 3, 5))
        return prefix + vals + rest
    return re.sub(r'(rgba?\(\s*)(\d+)\s*,\s*(\d+)\s*,\s*(\d+)([^)]*\))', rgb_replace, text)


def restyle_svg(text: str, add_seal: bool = False) -> str:
    text = recolor(text)
    text = re.sub(r'(animation\s*:\s*[-\w]+)\s+[\d.]+s\s+([^;}]*?)\s+infinite', r'\1 4.8s \2 1 both', text)
    # Badge and tag backgrounds stay dark in both themes. Keep their preserved
    # values legible without changing ordinary text on the light canvas.
    if re.search(r'aria-labelledby="section-\d+-title', text):
        text = re.sub(r'(<text\b[^>]*)(>\d{2}</text>)',
                      r'\1 class="brand-on-dark"\2', text)
    if 'aria-labelledby="tag-' in text:
        text = text.replace('class="v"', 'class="v brand-on-dark"')
    if 'class="brand-on-dark"' in text or 'class="v brand-on-dark"' in text:
        text = text.replace('</svg>', '<style>.brand-on-dark{fill:#fff6c8}</style></svg>')
    theme = '''<style>
:root{--bg:#100b18;--bg-top:#231331;--surface:#231331;--surface-2:#231331;--ink:#fff6c8;--muted:#fff6c8;--grid:#5c2a72;--outline:#5c2a72;--shadow:#100b18;--accent:#ff9f1c}
@media(prefers-color-scheme:light){:root{--bg:#fff6c8;--bg-top:#fff6c8;--surface:#fff6c8;--surface-2:#ffe66d;--ink:#231331;--muted:#5c2a72;--grid:#5c2a72;--outline:#5c2a72;--shadow:#5c2a72;--accent:#5c2a72}}
</style>'''
    # The existing SVG retains all labels and connectivity; only paint changes.
    if '--bg:' in text:
        text = text.replace('</svg>', theme + '</svg>')
    if add_seal:
        text = text.replace('</svg>', '<g data-brand-decoration="true" aria-hidden="true">' + core(810, 375, 86) + '</g></svg>')
    ET.fromstring(text)
    return text


RENDERER_OLD = "const primary = hex(domain.primary, palette.primary), secondary = hex(domain.secondary, palette.secondary), surface = hex(domain.surface, palette.surface);"
RENDERER_NEW = "const primary = '#ff9f1c', secondary = '#ffe66d', surface = '#100b18'; // Canonical avatar palette; model/config unchanged."


def head_file(repo: Path, path: Path) -> str:
    return subprocess.check_output(['git', 'show', f'HEAD:{path.as_posix()}'], cwd=repo).decode()


def write(repo: Path, relative: str, content: str) -> None:
    path = repo / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)


def apply_repository(repo: Path) -> dict:
    asset_dir = 'docs/visuals/brand-uniformity'
    for name, value in [('avatar.svg', avatar()), ('champion.svg', champion(True)),
                        ('champion-static.svg', champion(False)), ('brand.css', (HERE / 'brand.css').read_text())]:
        write(repo, asset_dir + '/' + name, value)
        if name.endswith('.svg'):
            write(repo, 'assets/brand-uniformity/' + name, value)
    manifest = {'canonical_repository': 'mohammadrezwankhan/mohammadrezwankhan',
                'canonical_grid': 'scripts/makeover/pixel-core.json',
                'canonical_grid_sha256': hashlib.sha256((PROFILE / 'scripts/makeover/pixel-core.json').read_bytes()).hexdigest(),
                'foreground_paths_sha256': hashlib.sha256(CORE.encode()).hexdigest(),
                'palette': PALETTE, 'motion_seconds': 4.8, 'motion_iterations': 1,
                'purpose': 'Decorative identity; no numerical or validation claim.'}
    write(repo, asset_dir + '/manifest.json', json.dumps(manifest, indent=2) + '\n')

    # Branded copies keep historical originals and their archive manifests intact.
    mapping = {}
    original_assets = [repo / 'assets/hero-25d.svg', repo / 'assets/portfolio/hero-25d.svg']
    original_assets += sorted((repo / 'assets/svg-2.5d').rglob('*.svg'))
    for path in original_assets:
        if not path.exists():
            continue
        rel = path.relative_to(repo)
        target = Path('assets/brand-uniformity') / rel.relative_to('assets')
        write(repo, str(target), restyle_svg(path.read_text(), rel == Path('assets/hero-25d.svg')))
        mapping[rel.as_posix()] = target.as_posix()
    for path in sorted((repo / 'docs/visuals').rglob('*.svg')):
        if 'brand-uniformity' in path.parts:
            continue
        rel = path.relative_to(repo)
        target = Path(asset_dir) / rel.relative_to('docs/visuals')
        write(repo, str(target), restyle_svg(path.read_text()))
        mapping[rel.as_posix()] = target.as_posix()

    pages = [('docs/index.html', 'dashboard'), ('docs/portfolio/index.html', 'portfolio'), ('docs/native-lessons.html', 'catalog')]
    for rel, surface in pages:
        path = repo / rel
        if not path.exists():
            continue
        html = head_file(repo, Path(rel))
        blocks = []
        def stash_script(match: re.Match[str]) -> str:
            blocks.append(match.group())
            return f'<!-- preserved-script-{len(blocks)-1} -->'
        html = re.sub(r'<script\b[^>]*>[\s\S]*?</script\s*>', stash_script, html, flags=re.I)
        # Only paint-bearing CSS/SVG content is recolored; prose stays byte-exact.
        html = re.sub(r'<style\b[^>]*>[\s\S]*?</style\s*>', lambda m: recolor(m.group()), html, flags=re.I)
        html = re.sub(r'<svg\b[^>]*>[\s\S]*?</svg\s*>', lambda m: restyle_svg(m.group()), html, flags=re.I)
        prefix = '../visuals/brand-uniformity/' if surface == 'portfolio' else 'visuals/brand-uniformity/'
        html = re.sub(r'<html\b', f'<html data-avatar-brand="{surface}"', html, count=1)
        html = html.replace('</head>', f'<link rel="stylesheet" href="{prefix}brand.css">\n</head>', 1)
        img = f'<img class="brand-avatar" data-brand-decoration="true" src="{prefix}avatar.svg" width="48" height="48" alt="">'
        if surface == 'dashboard':
            html = html.replace('<svg class="brand-icon"', img + '<svg class="brand-icon"', 1)
        elif surface == 'portfolio':
            html = html.replace('<span class="mark"', img + '<span class="mark"', 1)
            art = champion(True).replace('<svg ', '<svg class="champion-art" data-brand-decoration="true" aria-hidden="true" ', 1)
            html = html.replace('<div class="isometric">', art + '<div class="isometric">', 1)
        else:
            html = re.sub(r'(<nav class="surface-nav"[^>]*>)', lambda m: m.group() + img, html, count=1)
            html = html.replace('src="visuals/', 'src="visuals/brand-uniformity/')
            html = html.replace('visuals/brand-uniformity/brand-uniformity/', 'visuals/brand-uniformity/')
        for index, script in enumerate(blocks):
            if surface == 'dashboard' and RENDERER_OLD in script:
                script = script.replace(RENDERER_OLD, RENDERER_NEW)
            html = html.replace(f'<!-- preserved-script-{index} -->', script)
        write(repo, rel, html)

    # Repoint only existing Markdown image references; copy, links and alt text remain.
    # Profile's old artwork is explicitly historical and retains its original reference.
    if repo.name != 'mohammadrezwankhan':
        readme = head_file(repo, Path('README.md'))
        for old, new in mapping.items():
            readme = readme.replace('](' + old + ')', '](' + new + ')')
        write(repo, 'README.md', readme)
    csp = repo / 'scripts/browser-csp.mjs'
    if csp.exists():
        subprocess.run(['node', str(csp), '--write', *(p for p, _ in pages)], cwd=repo, check=True, capture_output=True)
    return {'repository': repo.name, 'pages': [p for p, _ in pages], 'palette': PALETTE, 'artwork_copies': len(mapping)}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repository', action='append', type=Path, required=True)
    args = parser.parse_args()
    for repository in args.repository:
        print(json.dumps(apply_repository(repository.resolve())))
