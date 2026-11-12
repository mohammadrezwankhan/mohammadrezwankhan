# Profile evidence and change record — 12 November 2026

This refresh checks the public profile against authenticated GitHub records and primary public sources. Status is a dated observation. It does not promise that branches, counts, CI, or external sites will remain unchanged.

## Advisory correction and credit

[Advisory Database PR #8819](https://github.com/github/advisory-database/pull/8819) was authored by `mohammadrezwankhan` and merged at **2026-11-12 18:15:40 UTC** (**19:15:40 Europe/Paris**). GitHub reports `merged: true` and merge commit [`f2006c77463e4e52fb8acee3806f3368fb6e920d`](https://github.com/github/advisory-database/commit/f2006c77463e4e52fb8acee3806f3368fb6e920d).

The patch removes only the final slash from the CVSS 4.0 vector in [GHSA-78fc-9688-w8xw](https://github.com/advisories/GHSA-78fc-9688-w8xw). The metric values and assessed score are unchanged. The [current advisory JSON](https://github.com/github/advisory-database/blob/main/advisories/github-reviewed/2026/05/GHSA-78fc-9688-w8xw/GHSA-78fc-9688-w8xw.json) contains the corrected vector; the [public advisory Credits section](https://github.com/advisories/GHSA-78fc-9688-w8xw) lists `mohammadrezwankhan` as **Analyst**. The web advisory, rather than the repository JSON, is the source for that credit.

This supports a contribution to advisory metadata. It does not establish discovery of the vulnerability, remediation of the OpenMRS application, or a formal award. The profile therefore describes the exact change and the published Analyst role.

## Verified merged upstream work

| Contribution | Merged at (UTC) | Merge commit | Verified scope |
|---|---|---|---|
| [Advisory Database #8819](https://github.com/github/advisory-database/pull/8819) | 2026-11-12 18:15:40 | [`f2006c7`](https://github.com/github/advisory-database/commit/f2006c77463e4e52fb8acee3806f3368fb6e920d) | Remove the malformed vector's trailing slash. |
| [Bifrost #6503](https://github.com/maximhq/bifrost/pull/6503) | 2026-08-25 14:49:07 | [`6a92afb`](https://github.com/maximhq/bifrost/commit/6a92afb9f0a89247ea67a29dc4fd42a20263ba06) | Route OpenCode Zen and Go Responses requests to `/v1/responses`; add regression coverage. |
| [Flowsint #217](https://github.com/reconurge/flowsint/pull/217) | 2026-08-25 07:31:56 | [`5548403`](https://github.com/reconurge/flowsint/commit/554840386f89c003bbe960da0387490b01fcb826) | Recognize one leading `@` in imported usernames while preserving normalization and hash exclusions. |
| [EMHASS #1039](https://github.com/davidusb-geek/emhass/pull/1039) | 2026-08-01 13:50:06 | [`57f9175`](https://github.com/davidusb-geek/emhass/commit/57f9175bf7d72be82aab31bfe40dfa8b5b5d4427) | Add the heat-topology guide and connect thermal documentation. |

Each PR's authenticated metadata identifies `mohammadrezwankhan` as author and reports `merged: true`. Three resource-list submissions remained open: [awesome-power-analysis #1](https://github.com/anderson-optimization/awesome-power-analysis/pull/1), [awesome-MATLAB #48](https://github.com/mikecroucher/awesome-MATLAB/pull/48), and [awesome-battery-data #2](https://github.com/pauljgasper/awesome-battery-data/pull/2). Open submissions are presented separately.

## Other consistency corrections

- **Datacenter Twin Lab:** the maturity table now links [v2.0.1](https://github.com/mohammadrezwankhan/datacenter-twin-lab/releases/tag/v2.0.1), published 26 October 2026, and the successful [Tests run on 10 November](https://github.com/mohammadrezwankhan/datacenter-twin-lab/actions/runs/42916534472) at [`a92128eaa85621ccc5691254f32e335a882f0795`](https://github.com/mohammadrezwankhan/datacenter-twin-lab/commit/a92128eaa85621ccc5691254f32e335a882f0795). This CI observation applies to that commit. The native README still states 24 lessons and 18 synthetic scenarios.
- **HelioForge:** the maturity table now links the [30 October source release](https://github.com/mohammadrezwankhan/helioforge-energy-lab/releases/tag/cold-load-repair-20261030-a071652), targeting [`a071652ab2b59bafd9a43245cd4620103dcf6eba`](https://github.com/mohammadrezwankhan/helioforge-energy-lab/commit/a071652ab2b59bafd9a43245cd4620103dcf6eba). The release retains synthetic screening and outstanding independent/field acceptance limits.
- **Public original directory:** the authenticated query `user:mohammadrezwankhan fork:false is:public` returned the same 12 owned public originals, including the profile, on 12 November. All twelve were unarchived. Forks and private repositories are outside this count. [Equivalent public query](https://github.com/search?q=user%3Amohammadrezwankhan+fork%3Afalse+is%3Apublic&type=repositories).
- **Historical test counts:** the seven original commit-bound test-count entries remain, with the existing 7 October review date. Their heading now explicitly identifies historical source snapshots.
- **MKLab:** the 69-demo count remains only as the dated 17 October catalogue observation. The repeated undated count has been removed. A fresh live count could not be independently established in this review.
- **Profile guide:** replaced generic text that implied a native engine or detailed installation guide below with an accurate description of this profile repository and its separate illustrative browser exercise.
- **Publication count:** the [publications page](https://mrkhan.co.technology/publications/) continues to list 17 outputs; the profile count is retained.

## Historical references retained

These records remain useful historical evidence and are not presented as the latest state:

- [Datacenter v2.0.0](https://github.com/mohammadrezwankhan/datacenter-twin-lab/releases/tag/v2.0.0), source [`424cf5349ea1f53d5d207a2d48af689774d878dc`](https://github.com/mohammadrezwankhan/datacenter-twin-lab/commit/424cf5349ea1f53d5d207a2d48af689774d878dc).
- [Datacenter main CI failure on 12 October](https://github.com/mohammadrezwankhan/datacenter-twin-lab/actions/runs/38314821223) at [`6c40b7010f69c8f12414530c7a776b98e3883729`](https://github.com/mohammadrezwankhan/datacenter-twin-lab/commit/6c40b7010f69c8f12414530c7a776b98e3883729).
- [HelioForge 30 September prerelease](https://github.com/mohammadrezwankhan/helioforge-energy-lab/releases/tag/preview-2026.09.30.1).
- The [pre-makeover README](../README.before-makeover-2026-11-08.md) and all pre-existing artwork and learning material remain unchanged.

## Diagram and presentation

“Championing engineering you can inspect” describes an engineering practice. The circuit joins two independent paths into public evidence: research-informed tools and upstream contributions. A feedback path represents opportunities for inspection and improvement. It claims no award or completed independent validation.

The original pixel banner remains intact. The new [desktop SVG](../assets/profile-evidence-circuit.svg) and [mobile SVG](../assets/profile-evidence-circuit-mobile.svg) use the existing plum, cream, amber, and violet palette. Both are static, self-contained vector geometry with accessible titles and descriptions. The README provides a complete text equivalent and ordinary links outside the artwork.

## Verification scope

Local checks resolved 25 document/asset references against the authenticated repository tree, confirmed four merged contribution rows, parsed both SVGs, checked for unsafe or external SVG content, and found no whitespace errors. Diagram text contrast is at least 9.63:1. Direct vector renders were inspected at 830-pixel desktop and 358-pixel mobile widths; the diagram labels were adjusted after the first pass. Independent review found no critical or important issues.

Full Chromium page rendering was blocked by the environment's local-socket restrictions, and its approval policy disallowed an elevated browser run. Direct SVG rendering is therefore the visual evidence here; this record does not claim a live GitHub browser walkthrough.

Authenticated API checks covered account/repository identity, each merged PR, selected releases and CI, public originals, the current profile tree, and existing workflow outcomes. Source-based checks and local rendering establish document consistency; they are not a human screen-reader walkthrough, scientific replication, hardware qualification, or validation of third-party applications.

The baseline profile was [`df86d1c74ab3c23275b2ee9aa7fb6ccf29bfa383`](https://github.com/mohammadrezwankhan/mohammadrezwankhan/commit/df86d1c74ab3c23275b2ee9aa7fb6ccf29bfa383). Its latest [Profile maintenance run](https://github.com/mohammadrezwankhan/mohammadrezwankhan/actions/runs/42667048745) and [Human authorship policy run](https://github.com/mohammadrezwankhan/mohammadrezwankhan/actions/runs/42469871480) succeeded. These baseline outcomes are distinct from checks of the refresh itself, recorded on its pull request and commit.
