![Energy Engineering Evidence Atlas: original vector system illustration](assets/hero-25d.svg)

The profile connects research, open implementations, validation vocabulary, and upstream contributions. A small synthetic battery exercise introduces the evidence questions used to choose a project.

**[Native-source lesson guide](docs/portfolio/) · [Offline interactive lab](docs/index.html) · [Lesson configuration](docs/lesson-config.json) · [Configuration schema](docs/lesson-config.schema.json) · [Portfolio at rezwankhan.tech](https://rezwankhan.tech)**

## Previous animations

[Open the previous-animation gallery](https://mohammadrezwankhan.github.io/mohammadrezwankhan/animations/) · [Local gallery](docs/animations/index.html)

Earlier animated artwork, waveform demos, and original interactive experiences are linked alongside the current animations.

## Your first interactive result

1. Download or clone this repository and open `docs/index.html` in a modern browser.
2. Select **Module 1**, apply its preset, and compare the declared checkpoint with the plotted result.
3. Change one slider, inspect the model assumptions, then export the configuration or telemetry for your notes.

The browser lab runs offline with no packages, accounts, or live data feeds. Its numbers are deterministic teaching simulations. Each checkpoint states its model time and tolerance; passing it demonstrates agreement with that model, not field calibration or production readiness.

## Four-module learning path

| Module | Investigation | Approximate time |
|---|---|---:|
| 1. Turn a battery question into an evidence route | Use units and scope to select a relevant project from the profile. | 12 min |
| 2. Find the energy-inventory boundary | Recognize that an apparently steady current request cannot continue after depletion. | 15 min |
| 3. Separate scale from validation | Explain how a capacity change affects duration without validating a larger physical pack. | 15 min |
| 4. Create an evidence-led project brief | Write a reproducible study question with a clear evidence tier and source of record. | 18 min |

**Who this is for:** Researchers, students, collaborators, and engineers finding a relevant model or evidence workflow.

### Continue into the implementation

- [README.md](README.md)
- [CONTRIBUTING.md](CONTRIBUTING.md)
- [LICENSE](LICENSE)

### Explore or run the source

No native runtime: this is a profile and evidence directory. Follow each linked repository’s own setup instructions.

```bash
git show HEAD:README.md
git show HEAD:CONTRIBUTING.md
```

These commands come from the audited source revision. Runtime requirements and the project's own validation limits are documented below; the standalone browser lab does not execute these commands.

The detailed project guide below remains the source for installation, supported features, licences, and scientific limits. The browser equations and laboratory settings do not change the original application or numerical engine.

<details>
<summary>Project documentation, installation, attribution, and existing validation</summary>

<!-- markdownlint-disable MD013 MD033 MD041 MD060 -->

<div align="center">

<h1>Mohammad Rezwan Khan</h1>

<a href="https://mrkhan.co.technology/">
  <picture>
    <source media="(prefers-reduced-motion: reduce)" srcset="./assets/engineering-hero-v2.webp">
    <img src="./assets/engineering-hero.gif" alt="Engineering in motion: battery physics, executable models, review evidence, and hybrid energy systems" width="100%">
  </picture>
</a>

<sub>Physics → models → evidence → energy systems. Illustrative; no live data.</sub>

<br>

[Portfolio](https://mrkhan.co.technology/) ·
[Publications](https://mrkhan.co.technology/publications/) ·
[LinkedIn](https://www.linkedin.com/in/mohammadrezwankhan) ·
[ORCID](https://orcid.org/0000-0002-1532-0598)

</div>

I turn **battery thermal behavior, power-conversion constraints, and QA
requirements** into auditable engineering decisions. My work connects
lithium-ion battery models, BESS delivery evidence, and smart-grid control from
physical assumptions to reproducible tests.

**Electrical R&D engineer** · **PhD in Energy Technology, Aalborg University**<br>
**MATLAB/Simulink + Python** · Battery systems · BESS QA/QC · Smart grids

> **Current mission:** build inspectable energy-system tools that help
> researchers and engineers move from assumptions to defensible results.

## Research → Implementation

The DOI anchors the scientific record; the linked repositories expose selected
equations, assumptions, tests, and engineering limits.

| Research record | Open implementation |
|---|---|
| [Thermal Management of Battery Systems in Electric Vehicle and Smart Grid Application](https://doi.org/10.5278/vbn.phd.engsci.00174) — PhD thesis | [Energy Lab](https://github.com/mohammadrezwankhan/matlab-simulink-energy-lab) |
| [An Online Framework for State of Charge Determination of Battery Systems Using a Combined System Identification Approach](https://doi.org/10.1016/j.jpowsour.2013.07.092) — *Journal of Power Sources* | [Battery dynamics and SOC estimation](https://github.com/mohammadrezwankhan/matlab-simulink-energy-lab) |
| [Design of a Unified Controller Framework for Grid-tied and Grid-forming Battery Energy Storage System](https://doi.org/10.1109/IECON49645.2022.9968382) — IEEE IECON | [BESS control models](https://github.com/mohammadrezwankhan/matlab-simulink-energy-lab) · [Grid-service playbook](https://github.com/mohammadrezwankhan/smart-grid-storage-playbook) |

[Browse all 17 publications](https://mrkhan.co.technology/publications/) ·
[Verify the ORCID record](https://orcid.org/0000-0002-1532-0598)

## Selected Engineering Work

| Project | Engineering question | Evidence you can inspect |
|---|---|---|
| **[MATLAB Simulink Energy Lab](https://github.com/mohammadrezwankhan/matlab-simulink-energy-lab)** | How do battery, converter, and BESS-control models behave under explicit checks? | Historical [2026-10-06 README snapshot](https://github.com/mohammadrezwankhan/matlab-simulink-energy-lab/blob/5cc54c8c453da6f6e54b514fa83bcfe7a01e48e1/README.md#start-in-60-seconds): 20 Base MATLAB checks, 25 general checks plus one unified-BESS entry point (26 total), and a 31-result focused BESS suite. Latest release [v0.11.0](https://github.com/mohammadrezwankhan/matlab-simulink-energy-lab/releases/tag/v0.11.0) cites validation at exact source [`c23d7ff`](https://github.com/mohammadrezwankhan/matlab-simulink-energy-lab/tree/c23d7ffd137ee614ea3fdaf4ac4e257a3a1edafe); neither source is a current-`main` validation claim. |
| **[VoltRL](https://github.com/mohammadrezwankhan/voltrl)** | How should battery arbitrage be benchmarked without information leakage? | Synthetic and historical protocols; regenerated experiments; pinned dependencies; provenance and checksum audits. |
| **[HelioForge Energy Lab](https://github.com/mohammadrezwankhan/helioforge-energy-lab)** | How do hybrid-energy assumptions translate into a bounded dispatch and storage calculation? | [Standalone browser preview](https://mkgrid.co.technology/); local Python API; scenario and energy-balance tests; browser/API checks; explicit synthetic-data and screening limits. |
| **[ZephyrTrade](https://github.com/mohammadrezwankhan/zephyrtrade)** | How do wind-forecast and direct-offer strategies change hypothetical revenue? | [Standalone browser preview](https://mktrade.co.business/); reproducible synthetic fixtures; Python/browser numerical parity; Linux CI; no live prices or order execution. |
| **[Battery Cycle-Life Analyzer](https://github.com/mohammadrezwankhan/battery-cycle-life-analyzer)** | How can capacity fade and bounded end-of-life be compared transparently? | Installable package; CLI; notebook; external CSV schema; CI and tests; explicit synthetic-demo limits. |
| **[BESS QA/QC Toolkit](https://github.com/mohammadrezwankhan/bess-qaqc-toolkit)** | What evidence is required from supplier review through handover? | FAT/SAT and commissioning templates; executable readiness audits; structured evidence gates. |
| **[Datacenter Twin Lab](https://github.com/mohammadrezwankhan/datacenter-twin-lab)** | How do utility outages, generator failures, and finite battery reserves affect power continuity? | Local-first Python simulator; [zero-install browser demo](https://khanlab.co.technology/); [24 lessons (12 continuity, 12 infrastructure) and 18 synthetic scenarios](https://github.com/mohammadrezwankhan/datacenter-twin-lab/blob/424cf5349ea1f53d5d207a2d48af689774d878dc/README.md); energy-balance checks; sensitivity analysis and exportable reports. |
| **[Smart Grid Storage Playbook](https://github.com/mohammadrezwankhan/smart-grid-storage-playbook)** | How do grid-service requests meet power, energy, SoC, frequency, and voltage constraints? | Executable grid-support references; constraint-aware examples; unit tests; documented boundaries. |

**Start here:** the [Energy Lab](https://github.com/mohammadrezwankhan/matlab-simulink-energy-lab)
connects 1RC/2RC battery dynamics, thermal models, SOC estimation, power
conversion, and grid-tied/grid-forming BESS control in one deterministically
regression-tested reference repository with explicit validation limits.

## Project Maturity and Validation

These labels describe the evidence currently published; they are not claims of
hardware qualification, grid-code compliance, or field validation.

| Repository | Lifecycle | Published evidence tier | Stable API | Release/archive |
|---|---|---|---|---|
| Energy Lab | Active reference | Regression-tested; numerically verified; synthetic holdout evaluated | Not applicable | Versioned GitHub releases |
| Battery Cycle-Life Analyzer | Alpha package | Unit-tested; synthetic holdout evaluated | No | Versioned package repository |
| VoltRL | Research artifact | Protocol audited; synthetic and historical backtests | No | Commit-bound result bundles |
| HelioForge Energy Lab | Research preview | Synthetic scenario and conservation checks; Python 3.11–3.13 CI; browser/API tests; no field validation | No | [2026-09-30 source prerelease](https://github.com/mohammadrezwankhan/helioforge-energy-lab/releases/tag/preview-2026.09.30.1) |
| ZephyrTrade | Research preview | Synthetic backtests; Python 3.11/3.12 CI; browser/native numerical parity; no market-performance validation | No | [2026-09-30 source prerelease](https://github.com/mohammadrezwankhan/zephyrtrade/releases/tag/preview-2026.09.30) |
| BESS QA/QC Toolkit | Draft toolkit | Parser/test verified; policy checks exercised on reference data | No | Repository snapshots |
| Datacenter Twin Lab | Research alpha | Deterministic synthetic scenarios; energy-accounting checks; browser/native output equality; no facility validation | No | [v2.0.0 release](https://github.com/mohammadrezwankhan/datacenter-twin-lab/releases/tag/v2.0.0), source commit `424cf5349ea1f53d5d207a2d48af689774d878dc`; historical `main` CI [failed on 2026-10-12](https://github.com/mohammadrezwankhan/datacenter-twin-lab/actions/runs/38314821223) at [`6c40b70`](https://github.com/mohammadrezwankhan/datacenter-twin-lab/commit/6c40b7010f69c8f12414530c7a776b98e3883729) |
| Smart Grid Storage Playbook | Living handbook | Unit-tested reference calculations | Not applicable | Repository snapshots |

**Validation vocabulary:** *unit-tested* means function-level expected behavior;
*regression-tested* means deterministic outputs reproduced in CI; *numerically
verified* means analytic, conservation, or convergence checks; and *synthetic
holdout evaluated* means evaluation on generated unseen profiles. I reserve
*measured-data validated*, *independently replicated*, *HIL/field evaluated*,
and *qualified/certified* for projects that publish evidence meeting those
stronger definitions.

## Selected Upstream Contributions

### Merged

| Upstream project | Contribution |
|---|---|
| [EMHASS](https://github.com/davidusb-geek/emhass) | [PR #1039](https://github.com/davidusb-geek/emhass/pull/1039): added the missing heat-topology guide. |

### Under review

| Upstream project | Contribution |
|---|---|
| [GitHub Advisory Database](https://github.com/github/advisory-database) | [PR #8819](https://github.com/github/advisory-database/pull/8819): correct a malformed CVSS 4 vector. |

## Open Collaboration Priorities

- Traceable physical-cell datasets and held-out measured validation for battery
  parameter-identification models.
- Validation-based cycle-life model selection with uncertainty intervals for
  end-of-life and remaining-useful-life estimates.
- Reproducible BESS acceptance evidence spanning FAT, SAT, commissioning,
  energization, and handover.

**Core tools:** MATLAB · Simulink · Python · NumPy/SciPy · Jupyter · GitHub Actions<br>
**Domains:** electro-thermal modeling · BMS/SOC estimation · power electronics ·
BESS assurance · grid-forming control

I welcome substantive collaboration around models, validation datasets, BESS
engineering evidence, and reproducible energy-system research. Start with the
[Energy Lab roadmap](https://github.com/mohammadrezwankhan/matlab-simulink-energy-lab#what-should-come-next)
or a focused [open issue](https://github.com/mohammadrezwankhan/matlab-simulink-energy-lab/issues).

<div align="center">

**Battery insight. Engineering evidence. Grid impact.**

[Website](https://mrkhan.co.technology/) ·
[LinkedIn](https://www.linkedin.com/in/mohammadrezwankhan) ·
[ORCID](https://orcid.org/0000-0002-1532-0598) ·
[GitHub repositories](https://github.com/mohammadrezwankhan?tab=repositories)

</div>

## Energy Evidence Atlas

[![Conceptual cell-to-grid assembly linking battery cells, modules, BESS assurance, power conversion and the electrical load](assets/energy-evidence-atlas.webp)](https://mrkhan.co.technology/energy-evidence-atlas/)

**Follow an engineering question from the physical system to its source evidence.**

The [Energy Evidence Atlas](https://mrkhan.co.technology/energy-evidence-atlas/) brings
my existing energy projects into a visual reading map, with a searchable project
finder, research-to-code trails, commit-pinned sources and explicit limitations.
The optional 3D assembly is conceptual; it does not represent selected equipment
or establish hardware, facility or grid-code validation.

- [Explore the cell-to-grid system tour](https://mrkhan.co.technology/energy-evidence-atlas/#atlas).
- [Find a model or toolkit](https://mrkhan.co.technology/energy-evidence-atlas/#projects).
- [Read source records and engineering limits](https://mrkhan.co.technology/energy-evidence-atlas/evidence/).
- [Try the bounded reserve calculation](https://mrkhan.co.technology/energy-evidence-atlas/#browser-lab), then open the linked Datacenter Twin Lab for its full documented scenarios.

## Energy learning workspace

Explore the [self-paced learning workspace](https://mrkhan.co.technology/energy-evidence-atlas/#learning) alongside the [cell-to-grid 3D tour](https://mrkhan.co.technology/energy-evidence-atlas/#atlas):

- **Battery & thermal:** [MATLAB Simulink Energy Lab](https://github.com/mohammadrezwankhan/matlab-simulink-energy-lab) and [Battery Cycle-Life Analyzer](https://github.com/mohammadrezwankhan/battery-cycle-life-analyzer).
- **Assurance & continuity:** [BESS QA/QC Toolkit](https://github.com/mohammadrezwankhan/bess-qaqc-toolkit) and [Datacenter Twin Lab](https://github.com/mohammadrezwankhan/datacenter-twin-lab).
- **Dispatch & markets:** [VoltRL](https://github.com/mohammadrezwankhan/voltrl), [HelioForge Energy Lab](https://github.com/mohammadrezwankhan/helioforge-energy-lab), and [ZephyrTrade](https://github.com/mohammadrezwankhan/zephyrtrade).

Progress is self-paced and stored locally in your browser. This workspace offers no certification; synthetic examples are for exploration and do not constitute field validation.

## Public browser demo collection

Explore [69 browser demos on MKLab](https://mklab.co.technology/) (catalogue checked 2026-10-17) for energy, learning, civic information and everyday planning. Each app includes usage steps and visible limits.

The new source repositories remain private; the public website provides synthetic browser editions. Use fictional information only. These demos do not establish clinical, legal, financial or emergency-service readiness.

## Public laboratories and current source records

- **[MKLab](https://mklab.co.technology/)**: Explore 69 public browser demos for energy, learning, civic information and everyday planning. Fictional or synthetic demonstrations, not medical, financial, legal or emergency services. Some source repositories are private.
- **[Intelligent UI](https://mrkhan.co.technology/#intelligent-ui)**: Local, no API; deterministic approved-source routing, no connected AI, and not an engineering approval.
- **[HelioForge Energy Lab](https://mkgrid.co.technology/)**: Explore hybrid-energy architectures, linked lessons and bundled scenario results. The hosted preview shows bundled examples. New numerical runs require the separate local Python application; no calibrated plant control.
- **[ZephyrTrade](https://mktrade.co.business/)**: Compare wind-market strategies and calculate hypothetical offers from synthetic observations. Synthetic historical data, not live prices, order execution or investment recommendations.
- **[Datacenter Twin Lab](https://khanlab.co.technology/)**: Learn electrical continuity through 24 lessons, including 12 continuity and 12 infrastructure lessons, with 18 synthetic scenarios and inspectable energy ledgers. Uncalibrated synthetic electrical model; not facility safety, certified uptime or live equipment control.

New MKLab additions include [Shomonnoy](https://mklab.co.technology/apps/shomonnoy/), GridLoom Europe, Solmora Grid, Threadmark, Ionweave Control and JolPulse. Use their published synthetic-data boundaries; no operational forecast, charging-control or flood-warning claim is made.

- [battery-power-models](https://github.com/mohammadrezwankhan/battery-power-models/tree/0d8532d478fe7dc5a0da019796cd346786ffdcf0): 6 unit tests in the linked CI run. [CI evidence](https://github.com/mohammadrezwankhan/battery-power-models/actions/runs/35528764843).
- [battery-cycle-life-analyzer](https://github.com/mohammadrezwankhan/battery-cycle-life-analyzer/tree/65df747ccf1ff0d2427ab8ba321b4c6839d0ad3b): 94 passed and 6 skipped tests per Python matrix job. [CI evidence](https://github.com/mohammadrezwankhan/battery-cycle-life-analyzer/actions/runs/36689059076).
- [battery-thermal-modeling-notes](https://github.com/mohammadrezwankhan/battery-thermal-modeling-notes/tree/afef3c2b52ab769fc20b53a07d41e0133c482b67): 84 unit tests in the linked CI run. [CI evidence](https://github.com/mohammadrezwankhan/battery-thermal-modeling-notes/actions/runs/35528751642).
- [voltrl](https://github.com/mohammadrezwankhan/voltrl/tree/a2f7eed0886a5a4844e8db2764c0bfd88615d1d8): 67 benchmark tests; bundle audits are separate checks. [CI evidence](https://github.com/mohammadrezwankhan/voltrl/actions/runs/35528755213).
- [smart-grid-storage-playbook](https://github.com/mohammadrezwankhan/smart-grid-storage-playbook/tree/caf54a81b4d76aa09a2ab8069d343c44e0e5467b): 151 unit tests in the linked CI run. [CI evidence](https://github.com/mohammadrezwankhan/smart-grid-storage-playbook/actions/runs/35528758460).
- [zephyrtrade](https://github.com/mohammadrezwankhan/zephyrtrade/tree/2d5461331a6bf752409e11f3a487700a363bd072): 86 passed tests per Python matrix job. [CI evidence](https://github.com/mohammadrezwankhan/zephyrtrade/actions/runs/36950218335).
- [datacenter-twin-lab](https://github.com/mohammadrezwankhan/datacenter-twin-lab/tree/a01d0d5c79f53726baa6147ef830a12856d97ad9): 150 Python tests per matrix job; 88 browser journeys and 18 export checks are separate suites. [CI evidence](https://github.com/mohammadrezwankhan/datacenter-twin-lab/actions/runs/37106356093).

Source and CI records reviewed 7 October 2026. Counts refer to individual jobs at linked commits, not totals across matrix jobs. [Current portfolio catalogue](https://mrkhan.co.technology/models/#browser-labs).

## Complete public repository directory

Snapshot checked **18 October 2026**: **17 owned public repositories — 12 non-forks (including this profile), 5 forks**. These counts exclude private and collaborator-owned repositories and are separate from the 69 MKLab demos. [Browse the live GitHub repository list](https://github.com/mohammadrezwankhan?tab=repositories) or the [portfolio directory and dated source records](https://mrkhan.co.technology/models/#repository-directory). Workflow results apply to their linked commits; they are not independent validation.

| Repository | Type | Stable release at review |
|---|---|---|
| [battery-cycle-life-analyzer](https://github.com/mohammadrezwankhan/battery-cycle-life-analyzer) | Non-fork | [v0.2.0](https://github.com/mohammadrezwankhan/battery-cycle-life-analyzer/releases/tag/v0.2.0) |
| [battery-power-models](https://github.com/mohammadrezwankhan/battery-power-models) | Non-fork | No stable release listed |
| [battery-thermal-modeling-notes](https://github.com/mohammadrezwankhan/battery-thermal-modeling-notes) | Non-fork | No stable release listed |
| [bess-qaqc-toolkit](https://github.com/mohammadrezwankhan/bess-qaqc-toolkit) | Non-fork | No stable release listed |
| [datacenter-twin-lab](https://github.com/mohammadrezwankhan/datacenter-twin-lab) | Non-fork | [v2.0.0](https://github.com/mohammadrezwankhan/datacenter-twin-lab/releases/tag/v2.0.0) |
| [helioforge-energy-lab](https://github.com/mohammadrezwankhan/helioforge-energy-lab) | Non-fork | No stable release listed |
| [matlab-simulink-energy-lab](https://github.com/mohammadrezwankhan/matlab-simulink-energy-lab) | Non-fork | [v0.11.0](https://github.com/mohammadrezwankhan/matlab-simulink-energy-lab/releases/tag/v0.11.0) |
| [mohammadrezwankhan](https://github.com/mohammadrezwankhan/mohammadrezwankhan) | Non-fork | No stable release listed |
| [smart-grid-storage-playbook](https://github.com/mohammadrezwankhan/smart-grid-storage-playbook) | Non-fork | No stable release listed |
| [thermoweave-battery-digital-twin](https://github.com/mohammadrezwankhan/thermoweave-battery-digital-twin) | Non-fork | No stable release listed |
| [voltrl](https://github.com/mohammadrezwankhan/voltrl) | Non-fork | [v1.1.0](https://github.com/mohammadrezwankhan/voltrl/releases/tag/v1.1.0) |
| [zephyrtrade](https://github.com/mohammadrezwankhan/zephyrtrade) | Non-fork | No stable release listed |
| [advisory-database](https://github.com/mohammadrezwankhan/advisory-database) | Fork | No stable release listed |
| [awesome-battery-data](https://github.com/mohammadrezwankhan/awesome-battery-data) | Fork | No stable release listed |
| [awesome-MATLAB](https://github.com/mohammadrezwankhan/awesome-MATLAB) | Fork | No stable release listed |
| [awesome-power-analysis](https://github.com/mohammadrezwankhan/awesome-power-analysis) | Fork | No stable release listed |
| [emhass](https://github.com/mohammadrezwankhan/emhass) | Fork | No stable release listed |

</details>
