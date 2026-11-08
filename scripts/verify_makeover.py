"""Verify the content-preservation and safe-artifact contract for the makeover."""
from pathlib import Path
import hashlib
import re
import subprocess
import xml.etree.ElementTree as ET
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
BASE = "823b6c20381fb4e3684fb1171a0b4638dea6e871"
original_bytes = subprocess.check_output(["git", "show", f"{BASE}:README.md"], cwd=ROOT)
snapshot = ROOT / "README.before-makeover-2026-11-08.md"
assert snapshot.read_bytes() == original_bytes, "Original README snapshot changed"
original = original_bytes.decode()
current = (ROOT / "README.md").read_text()
structural = {
    "<details>", "</details>",
    "<summary>Project documentation, installation, attribution, and existing validation</summary>",
    "<!-- markdownlint-disable MD013 MD033 MD041 MD060 -->",
}
legacy_gif_line = '    <img src="./assets/engineering-hero.gif" alt="Engineering in motion: battery physics, executable models, review evidence, and hybrid energy systems" width="100%">'
structural.add(legacy_gif_line.strip())
assert "[Open the original full-motion artwork](assets/engineering-hero.gif)" in current
missing = [line for line in original.splitlines()
           if line.strip() and line.strip() not in structural and line not in current]
assert not missing, f"Original content missing: {missing}"
urls = lambda value: set(re.findall(r"https?://[^\s<>\)\"]+", value))
assert urls(original) <= urls(current), "Original external links lost"
changed = subprocess.check_output(
    ["git", "diff", "--name-only", BASE], cwd=ROOT, text=True
).splitlines()
assert not any(p.startswith(".github/") for p in changed), "Existing CI changed"
assert not any(line.startswith("D\t") for line in subprocess.check_output(
    ["git", "diff", "--name-status", BASE], cwd=ROOT, text=True
).splitlines()), "Tracked content deleted"

assets = ROOT / "assets/makeover"
required_svg = ["avatar.svg", "avatar-static.svg", "profile-banner.svg",
                "profile-banner-static.svg", "social-preview.svg"]
for name in required_svg:
    path = assets / name
    doc = ET.parse(path)
    for element in doc.iter():
        tag = element.tag.split("}")[-1]
        assert tag not in {"script", "foreignObject"}, f"Unsafe SVG tag in {name}"
        for key, value in element.attrib.items():
            assert not key.lower().startswith("on"), f"SVG handler in {name}"
            if key.split("}")[-1] in {"href", "src"}:
                assert not value.startswith(("http:", "https:", "//")), f"External SVG resource in {name}"
    if name in {"avatar.svg", "profile-banner.svg", "social-preview.svg"}:
        text = path.read_text()
        assert "infinite" in text and "prefers-reduced-motion" in text, f"Missing motion fallback: {name}"

with Image.open(assets / "avatar.png") as avatar:
    assert avatar.width == avatar.height and avatar.width < 3000
assert (assets / "avatar.png").stat().st_size < 1_000_000
posters = [assets / "social-preview.png"] + sorted((assets / "social").glob("*.png"))
assert len(posters) == 7, f"Expected profile and six repository posters, got {len(posters)}"
for path in posters:
    with Image.open(path) as poster:
        assert poster.size == (1280, 640), f"Wrong poster dimensions: {path}"
    assert path.stat().st_size < 1_000_000, f"Oversized social preview: {path}"
with Image.open(assets / "avatar.gif") as icon:
    assert icon.n_frames > 1 and icon.info.get("loop") == 0, "Icon GIF does not loop indefinitely"

gallery = ROOT / "docs/brand/index.html"
html = gallery.read_text()
assert not re.search(r"<!-- (AVATAR_SVG|BANNER_SVG|SIZE_ROWS|COMPANION_ART) -->", html)
assert 'id="motion-toggle"' in html and "prefers-reduced-motion" in html
assert "visibilitychange" in html and "IntersectionObserver" in html
for match in re.finditer(r'(?:src|href)="([^"#]+)"', html):
    target = match.group(1)
    if not re.match(r"[a-zA-Z]+:", target) and not target.startswith("//"):
        assert (gallery.parent / target).exists(), f"Missing gallery asset: {target}"

print("Original snapshot SHA-256:", hashlib.sha256(original_bytes).hexdigest())
print(f"Preserved {len(urls(original))} external URLs and every original prose line (legacy GIF retained as an on-demand link)")
print("Verified SVG safety, infinite GIF loop, seven 1280x640 posters under 1 MB, and gallery resources")
print("Existing tracked assets and CI configuration retained")
