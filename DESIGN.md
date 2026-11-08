---
name: Rezwan energy-core identity
description: The existing pixel emblem extended into a lightweight GitHub identity and artwork gallery.
colors:
  ink: "#100b18"
  panel: "#1d1327"
  line: "#50335f"
  paper: "#fff6c8"
  muted: "#cbb7d9"
  amber: "#ff9f1c"
  violet: "#a66ac1"
  yellow: "#ffe66d"
  core-shadow: "#231331"
  core-violet: "#5c2a72"
  core-coral: "#d94a4a"
  art-violet: "#ac83c3"
  art-muted: "#b6a7c1"
  art-line: "#392445"
typography:
  display:
    fontFamily: 'ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif'
    fontSize: "clamp(32px, 4.5vw, 58px)"
    lineHeight: 1.07
    letterSpacing: "-0.025em"
  headline:
    fontSize: "clamp(25px, 3vw, 36px)"
    lineHeight: 1.2
    letterSpacing: "-0.02em"
  body:
    fontFamily: 'ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif'
    fontSize: "17px"
    lineHeight: 1.6
  label:
    fontSize: "15px"
rounded:
  control: "8px"
  artwork: "12px"
spacing:
  control-block: "10px"
  control-inline: "18px"
  paragraph: "20px"
  navigation: "24px"
  section: "56px"
components:
  primary-link:
    backgroundColor: "{colors.amber}"
    textColor: "{colors.ink}"
    rounded: "{rounded.control}"
    padding: "10px 18px"
  primary-link-hover:
    backgroundColor: "{colors.yellow}"
    textColor: "{colors.ink}"
  motion-toggle:
    backgroundColor: "{colors.panel}"
    textColor: "{colors.paper}"
    rounded: "{rounded.control}"
    padding: "10px 18px"
  artwork-frame:
    backgroundColor: "{colors.panel}"
    rounded: "{rounded.artwork}"
    width: "100%"
  gallery-navigation:
    textColor: "{colors.paper}"
  project-row:
    textColor: "{colors.paper}"
    padding: "23px 0"
  pixel-core:
    width: "100%"
---

# Design System: Rezwan energy-core identity

## Overview

**Creative North Star: "Battery insight becomes engineering evidence."**

The existing amber, cream, coral, and violet pixel energy core anchors the identity. Crisp geometry, a dark field, readable type, and two restrained moving signals connect the artwork without turning it into a scientific result.

The GitHub profile uses native Markdown hierarchy; the optional gallery carries the custom CSS. Textual identity, project routes, and evidence remain readable outside the artwork. The refresh preserves the original engineering material and earlier visuals.

**Key Characteristics:**

- Recognisable source emblem and fixed typography.
- Compact, self-contained assets with static alternatives.
- Clear routes into source, methods, evidence, and limitations.

This record is extracted from [the product brief](PRODUCT.md), [design spec](docs/superpowers/specs/2026-11-08-github-makeover-design.md), [gallery template](scripts/templates/brand.html), and [asset generator](scripts/makeover/generate.py). It documents the implemented source, not completed live acceptance.

## Colors

The frontmatter records the actual values. In the gallery, `ink` is the page field, `panel` the control/artwork surface, `paper` primary text, `muted` secondary text, and `line` structural separators. `amber` marks the primary action and keyboard focus; its hover becomes `yellow`. `violet` supplies the scrollbar accent.

The canonical emblem uses `ink`, `core-shadow`, `core-violet`, `core-coral`, `amber`, `yellow`, and `paper`. The vector compositions additionally use `art-violet`, `art-muted`, and `art-line`. Keep these artwork colors distinct from the gallery's brighter interface tokens; do not silently normalize the two palettes.

## Typography

The gallery uses the system sans-serif stack, without a font download. Its display and section scales are in the frontmatter; project titles are 20px/1.3, navigation and notes are 14px, and body paragraphs are capped at 68ch. At the 700px breakpoint, the intro title becomes 38px and loses its forced line break.

The SVG generator outlines URW Gothic Demi for display lettering and Nimbus Sans Regular/Bold for supporting lettering. These are build inputs from `/usr/share/fonts/opentype/urw-base35`, not web fonts. Preserve SVG titles/descriptions and the equivalent HTML/Markdown text because outlines are not selectable text. GitHub controls typography on the native profile.

## Layout

The gallery container is `min(1120px, calc(100% - 48px))`. The intro pairs a 270px emblem column with text across a 64px gap. Sections use 56px vertical spacing; project rows use `1.25fr 1fr auto` columns and 24px gaps. The details area has two columns separated by 56px.

At widths up to 700px, the container has 16px side margins, the intro and project rows stack, the emblem becomes 160px, and sections use 38px vertical spacing. These are source-defined responsive rules; desktop/mobile browser acceptance remains separate.

## Elevation & Depth

Surfaces are flat. Dark tonal fields, thin dividers, and outlined artwork provide hierarchy; the authored gallery has no box-shadow vocabulary. The pixel core remains the dominant object without adding UI glow, gradients, or simulated chart depth.

## Shapes

Keep the emblem's rectilinear 48×48 grid intact. Interface controls use the `control` radius; artwork frames use `artwork`. The wide SVG is intentionally edge-to-edge inside its frame: composition margins live inside its viewBox, rather than in additional wrapper padding.

## Components

- **Primary link:** amber with dark text, a 46px minimum height, and a yellow hover. Secondary controls use the panel surface. Keyboard focus is a 3px amber outline offset by 6px.
- **Motion control:** the gallery's button exposes `aria-pressed` and a status message. Source logic pauses on manual request, document hiding, and offscreen artwork; reduced motion disables animation and smooth scrolling. It is a gallery feature, not custom behavior injected into GitHub.
- **Navigation and project rows:** visible text links connect to the profile, portfolio, retained learning material, and six repository READMEs. Each repository remains responsible for its own setup and evidence.
- **Identity assets:** two signal markers complete a 12-second linear loop; the core and lettering stay fixed. GIF alternatives use 48 frames at 250ms and `loop=0`; GIF files cannot themselves evaluate reduced-motion preferences.
- **Static uploads:** use the 500×500 avatar PNG and 1280×640 opaque social-preview PNGs. Do not infer animated native-avatar or social-card playback from acceptance of GIF uploads. The profile's authored `<picture>` supplies the static SVG for reduced motion; destination rendering still needs verification.

### Reproduction and preservation

The canonical geometry is [pixel-core.json](scripts/makeover/pixel-core.json). Build with Python/Pillow/fontTools, the URW fonts above, Node, and Sharp. `generate.py` invokes `render.mjs`; use `CODEX_PRIMARY_RUNTIME_NODE` if the bundled Node path is unavailable, and make Sharp resolvable locally or through `CODEX_PRIMARY_RUNTIME_NODE_MODULES`.

```sh
python3 scripts/makeover/generate.py
python3 scripts/build_brand_gallery.py
python3 scripts/verify_makeover.py
python3 scripts/portfolio/validate_guide.py
git diff --check
```

Edit the gallery template and rebuild its generated HTML. The [manifest](assets/makeover/manifest.json) records output dimensions, bytes, and SHA-256 hashes; repeatability of exact raster bytes also depends on font/library versions. The separate [generated-art provenance](assets/makeover/generated-art.origin.json) records the companion image's prompt, reference, source hash, and export settings. Its AI generation is non-deterministic and is not reproduced by the procedural generator.

The [original README snapshot](README.before-makeover-2026-11-08.md) preserves baseline `823b6c20381fb4e3684fb1171a0b4638dea6e871`. The focused verifier checks retained prose/links, the on-demand legacy animation, safe assets, local gallery resources, and unchanged existing CI. The six companion README drafts likewise preserve exact original suffixes and sibling snapshots. See the [change record](docs/profile-makeover-2026-11-08.md) for scope and evidence.

## Do's and Don'ts

### Do

- Do retain the canonical pixel geometry and the user's recognisable identity.
- Do keep names, project choices, scientific limits, and links readable outside artwork.
- Do retain static assets, reduced-motion behavior, and the gallery pause control.
- Do regenerate derived files from their sources and preserve provenance and snapshots.

### Don't

- Don't treat abstract signal paths as telemetry, model results, or validation evidence.
- Don't claim native GitHub avatar or social-card animation without observed support.
- Don't change project engines, private visibility, required checks, or publishing protections for presentation work.
- Don't describe source inspection or detector output as completed live browser acceptance.

### Handoff state — 8 November 2026

Context loading ran once at the task root before checkout and found no project context. Direction seed `7691169f`, candidate 3, was degraded/local-only with no challenger boards; the user's existing emblem and requested lightweight SVG direction governed the work, not an independently approved replacement brand.

The detector ran exactly once against `docs/brand/index.html`. Its skip-link hover contrast finding was real; `.skip:hover { color: var(--ink); }` is now in the authored template, with rendered confirmation pending. The `.wide-art` cramped-padding finding was judged a false positive because the artwork has intentional intrinsic safe margins. No detector rerun or browser check is represented by this documentation.

The publication plan is to land assets and the gallery first, verify the Pages URL, then publish the reordered profile README. Live desktop/mobile rendering, motion and reduced-motion behavior, native upload results, and remote CI acceptance remain publication checks; this file does not mark them complete.
