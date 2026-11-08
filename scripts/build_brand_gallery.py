"""Build the self-contained gallery from the authored SVG and raster assets."""
from pathlib import Path
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "assets/makeover"
OUT = ROOT / "docs/brand"
OUT.mkdir(parents=True, exist_ok=True)
(OUT / "assets").mkdir(exist_ok=True)


def inline_svg(name, prefix):
    value = (SOURCE / name).read_text()
    value = re.sub(r"<\?xml.*?\?>", "", value, flags=re.S)
    for identifier in re.findall(r'\bid="([^"]+)"', value):
        value = value.replace(f'id="{identifier}"', f'id="{prefix}-{identifier}"')
        value = value.replace(f'#{identifier})', f'#{prefix}-{identifier})')
        value = value.replace(f'href="#{identifier}"', f'href="#{prefix}-{identifier}"')
    value = re.sub(r'aria-labelledby="([^"]+)"',
                   lambda match: 'aria-labelledby="' + ' '.join(f'{prefix}-{token}' for token in match[1].split()) + '"', value)
    return value


names = ["avatar.svg", "avatar-static.svg", "avatar.png", "avatar.gif",
         "profile-banner.svg", "profile-banner-static.svg", "social-preview.svg", "social-preview.png"]
for name in names:
    shutil.copy2(SOURCE / name, OUT / "assets" / name)

html = (ROOT / "scripts/templates/brand.html").read_text()
html = html.replace("<!-- AVATAR_SVG -->", inline_svg("avatar.svg", "icon"))
html = html.replace("<!-- BANNER_SVG -->", inline_svg("profile-banner.svg", "banner"))
rows = []
for label, name in [("Animated icon SVG", "avatar.svg"), ("Animated banner SVG", "profile-banner.svg"),
                    ("Looping icon GIF", "avatar.gif"), ("Social-preview PNG", "social-preview.png")]:
    rows.append(f"<tr><td>{label}</td><td>{(SOURCE / name).stat().st_size / 1024:.1f} KiB</td></tr>")
html = html.replace("<!-- SIZE_ROWS -->", "\n".join(rows))
art = SOURCE / "generated-art.webp"
companion = ""
if art.exists():
    shutil.copy2(art, OUT / "assets" / art.name)
    companion = '''<section aria-labelledby="concept-heading"><h2 id="concept-heading">A second expression of the core.</h2><p>An original generated concept artwork, inspired by the same pixel energy-core identity.</p><div class="artwork"><img src="assets/generated-art.webp" alt="Original conceptual energy-core companion artwork" width="1280" height="640" loading="lazy"></div><div class="download-row"><a href="assets/generated-art.webp" download>Download companion artwork</a></div></section>'''
html = html.replace("<!-- COMPANION_ART -->", companion)
(OUT / "index.html").write_text(html)
print(f"Built gallery: {len(html.encode()):,} bytes; {len(names)} supporting assets")
