# Profile evidence refresh implementation plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans for implementation, with independent evidence and final review agents.

**Goal:** Publish an accurate, distinctive GitHub profile with the merged advisory contribution, its Analyst credit, and a readable champion diagram.

**Architecture:** Native Markdown links and tables remain the source of readable claims. Two static SVG layouts visualize the same evidence relationship. A dated evidence record links the underlying PR, advisory, release, and CI sources.

**Tech stack:** Markdown, SVG, GitHub connector, direct vector rendering for visual verification.

**Spec:** ../specs/2026-11-12-profile-evidence-design.md

## Global constraints

Preserve existing identity, project scope, scientific limitations, and archived material. Add no formal award or validation claims. Preserve CI permissions, checks, and gates. Use verified public sources only.

## Review focus

Check status versus merge state, analyst versus reporter credit, historical versus current CI, diagram edge meaning, mobile legibility, local links, and concurrent edits before publication.

## Tasks

- [x] Confirm current README, account permission, PR merge metadata, advisory credit, other selected contributions, releases, and public directory.
- [x] Update README contribution ordering, current references, dated snapshots, and misleading profile boilerplate.
- [x] Add desktop/mobile SVG evidence circuit and text equivalent.
- [x] Add a dated public evidence record; preserve archived references.
- [x] Check local links against the full authenticated tree, SVG XML and safety, contrast, desktop/mobile vector rendering, and diff whitespace. This is a documentation change; no new application tests are needed.
- [x] Obtain independent review of final changes.
- [ ] Publish using normal GitHub checks; verify the default-branch README and report exact commit and CI outcomes.

## Execution decisions

Chromium's local sockets were blocked, and elevated execution was unavailable. Direct static vector renders at desktop/mobile sizes provide visual evidence; a live GitHub browser walkthrough is not claimed. Publication and final remote-check outcomes belong to the pull request and task handoff so the checklist does not claim success before the checks run.
