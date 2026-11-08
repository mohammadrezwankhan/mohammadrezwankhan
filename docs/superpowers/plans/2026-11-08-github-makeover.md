# GitHub Makeover Implementation Plan

> **For agentic workers:** Use superpowers:executing-plans for coordinated execution, with a dedicated asset implementer and a fresh final reviewer.

**Goal:** Publish a distinctive, content-preserving GitHub identity with lightweight infinite motion and coordinated repository posters.

**Architecture:** Native profile Markdown references self-contained SVGs. GitHub Pages serves the optional motion gallery; static PNGs are uploaded through native account/repository settings.

**Tech Stack:** Markdown, SVG/CSS, static HTML/JavaScript, Python/Pillow, Node Sharp and Playwright.

**Spec:** `docs/superpowers/specs/2026-11-08-github-makeover-design.md`

## Global Constraints

- Preserve all existing substantive content and assets.
- Preserve private visibility and existing workflow security and required gates.
- Do not invent validation, popularity, commercial, or publication claims.
- Respect reduced motion; supply static fallback and a pause control in the gallery.
- Profile/social settings must be verified after mutation.

## Review Focus

- Mobile readers can identify the person and choose a repository.
- Expanding retained evidence reveals usable original links.
- Animations do not require scripts, external fonts, or external resources within SVGs.
- Gallery pause and OS reduced-motion settings stop continuous movement.
- All social-preview uploads are below GitHub's size limit and preserve a readable safe area.

### Task 1: Preserve and reorder content

- [ ] Save an exact baseline README sibling snapshot.
- [ ] Reorder existing sections, bring identity/research/collaboration forward, and add six short project routes.
- [ ] Verify substantive text and link retention against the baseline.

### Task 2: Produce the visual assets

- [ ] Generate script-free animated/static SVGs, optimised GIF fallback, and upload PNGs under `assets/makeover/`.
- [ ] Generate one original companion artwork and record source/prompt provenance.
- [ ] Record a reproducible generator and byte-size manifest.
- [ ] Inspect actual renders and loop/reduced-motion behaviour.

### Task 3: Add the motion gallery

- [ ] Add `docs/brand/` with accessible previews, a working pause control, and asset downloads.
- [ ] Keep existing labs and previous animations linked.
- [ ] Verify desktop/mobile layouts, links, pause, and reduced motion.

### Task 4: Review and publish

- [ ] Run existing guide validation and the focused content/asset checks.
- [ ] Obtain independent review, resolve material defects, document the finished design and research decisions.
- [ ] Publish via a branch and pull request; respect required checks.
- [ ] Upload the avatar/static social posters and curate pins through authenticated GitHub UI.
- [ ] Verify published profile, Pages, settings, and remote check outcomes; provide links and measured size savings.
