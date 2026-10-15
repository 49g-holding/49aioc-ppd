# Proposals from Process and Position Design

**From `[ORG]AIOC-OCO` · 15 October 2026 · drafts, not yet proposed.** Generalised: no organisation's name or data. A change to another AIOC is made through OCO and approved by the Cell carrying `[ORG]HOAC-TM`; a change to 49GAION reaches it only as a pull request merged by its governing seat.

## 1. To `[ORG]AIOC-TOM`: the direct link

- **Current text.** TOM blueprint `v0.4.1` §2.2 and §6: "The next design stages read the TOM Release from Source Lifecycle, never from this AIOC." `docs/OUTPUT.md` §14: the next stage reads the filed release from Source Lifecycle; "An organisation gives each role to a person in its own holders register." `docs/CARRIED-RULES.md` §4.4, item 5: a return is filed into Source Lifecycle, and the Requesting Authority opens a new run that cites it.
- **Proposed text.**
  - (a) On filing a decided release, TOM also sends a **release notice** to `[ORG]AIOC-PPD` through the gateway (`contracts/README.md` of this repository). The filed copy in Source Lifecycle stays the record.
  - (b) TOM receives **returns** from `[ORG]AIOC-PPD` directly, under `contracts/release-return.schema.json`, through a new port on its Chief of Staff, and shows them on its Panel with their ages. Each return is also filed into Source Lifecycle by PPD, so a revised Design Request can cite it.
  - (c) `docs/OUTPUT.md` §14, "Used on its own": "An organisation may stop here; how its positions are occupied is top management's own mechanism" (Standard §1.1, item 9), in place of the holders-register sentence.
- **Reason and evidence.** The governing seat's direction that PPD is linked to the TOM itself (`decisions/DR-0001`); the no-natural-person rule (`49GAION/DR-0013`).
- **Parts and tests affected.** TOM blueprint §1 card, §2.2, §6, §17 (two ports on `[ORG]CELL-TCS`); `docs/OUTPUT.md` §14; `docs/CARRIED-RULES.md` §4.4; TEST-TOM (new cases). To be made as TOM `v0.5.0`.

## 2. To `[ORG]AIOC-SL`: an origin kind and a filing scope

- **Proposed text.** Add the origin kind `process and position design`, and let `[ORG]AIOC-PPD` file sources of that kind and of kind `design report` (its returns), under the same rules as TOM's filings.
- **Parts and tests affected.** SL blueprint §5.8; PRD FR-43 (filing by a connected part), at its next opening.

## 3. To 49GAION: the Target Operating Model in the Library

- **Current text.** Standard §3.1, item 3 (proposed, DR-0014) and Protocol §17 (proposed) name "the part that designs the target operating model". The Library has no card for it.
- **Proposed text.** The Library card and Protocol section drafted in the `upstream/` folder of the TOM writing repository, updated for the direct link of item 1.
- **Reason and evidence.** The Library names the stage after the target operating model but not the target operating model itself.
- **Parts and tests affected.** Protocol (a new section), `library/cards/`, TEST-TOM.

## 4. To 49GAION: one return contract for every design stage

- **Proposed text.** `contracts/release-return.schema.json` of this repository becomes a Library contract that every design stage uses toward the stage before it.
- **Reason and evidence.** The same five return kinds already run between TOM and the stage after it; each later stage needs the same.
- **Parts and tests affected.** A Library contract and its examples; the Library cards README.

*Powered by 49GAION*
