# Process and Position Design · `[ORG]AIOC-PPD`

> **Process and Position Design in one page**
>
> Process and Position Design (PPD) takes an organisation's decided target operating model and designs how its work runs and the positions that carry it. It is the stage after the Target Operating Model (TOM), and a part of its own.
>
> **What goes in:** the decided TOM release, handed over directly by `[ORG]AIOC-TOM`, role register first; the organisation's other sources, only from Source Lifecycle; answers to what they do not say, asked only through the Chief of Staff of Source Lifecycle.
>
> **The link with TOM goes both ways.** PPD never changes the TOM release. Each defect goes straight back to TOM as a return: cannot use, missing what; contradiction found; assumption invalid; request kind unsupported. The elements it touches wait; the rest goes on.
>
> **What comes out, processes first:** the process architecture and the process book; the decision-rights register and the authority matrix; the policy register; the controls catalogue and the segregation-of-duties check; the position register with a generated job description and competence profile for every position; the objectives cascade; organisation charts, forums with charters and tiers, and the review calendar; structure scenarios when asked for; the workload of each position, its peak load, and end-to-end times; the crosswalk from today's organisation; the walkthrough report; the Decision Package. The organisation decides each element. The release is filed in Source Lifecycle and handed to the next stage.
>
> **Positions only.** PPD designs positions, never people. It makes no choice of what fills a position; that belongs to a later stage.

The writing repository of **`[ORG]AIOC-PPD`, Process and Position Design**: the mother text of the 49GAION Library part of the same name (49GAION Operating Protocol §17 and Standard §3.1, item 3, both proposed on 15 October 2026). In each organisation this repository is named `<org>aioc-ppd` (Naming Standard R9). It is written for any organisation and holds no organisation data.

**Status: draft `v0.1.0`, 15 October 2026. Nothing here has run; every fixed test reads `NOT_RUN`.**

## Where to read

| File | What it is |
|---|---|
| [`blueprint/PPD-BLUEPRINT.md`](blueprint/PPD-BLUEPRINT.md) | the blueprint, on the 49GAION AIOC Blueprint Template at `e89ed1d`: identity, card, placement, positions, the ten stages with their inputs, outputs and done-tests (§5.0), every capability, the human decisions (§13), Cells and Pods (§17), the release parts (Annex A), returns (Annex B) |
| [`tests/TEST-PPD.md`](tests/TEST-PPD.md) | the fixed test, written before use: 94 cases and the Design Lead's seat test |
| [`contracts/`](contracts/) | the return contract between design stages, with valid and must-fail examples |
| [`cards/`](cards/) | the unit cards of its seven Pods and seventeen Cells, and the bot identity cards of its sixteen AI Cells, generated from the blueprint |
| [`docs/HISTORY.md`](docs/HISTORY.md) | why this stage exists and how leading practice runs it |
| [`upstream/PROPOSALS.md`](upstream/PROPOSALS.md) | the changes this AIOC needs from `[ORG]AIOC-TOM`, `[ORG]AIOC-SL` and 49GAION |
| [`decisions/`](decisions/) | the decision records of this repository |

## Checks

```
python3 tools/make_cards.py <49GAION-protocol>/spec/schemas
python3 tools/check_contracts.py
```

Both must report 0 errors and 0 failures.

## How a change is made

A change is a pull request, reviewed by someone other than its writer. A decided text is never edited; a change is a new version that names what it supersedes.

*Powered by 49GAION*
