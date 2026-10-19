# DR-0006 · PPD v0.5.1: the Chief of Staff takes its COS code

- **Date:** 2026-10-19
- **Decided by:** the governing seat (GOV) of 49GAION, in conversation with `[ORG]AIOC-OCO` (the decider is a position)
- **Source:** `49GAION/DR-0028`, Naming Standard R16, item 5: a mother blueprint moves its Chief of Staff Cell to its COS code at its next version. The direction of the governing seat of 19 October 2026 (translated): "Do it", on the Operating Core Office's report that each mother moves to its COS code at its next version.
- **Relation:** builds on DR-0005; it supersedes nothing.

## Decision

1. **The code.** The Chief of Staff Cell `[ORG]CELL-PCS` takes the code `[ORG]CELL-COSPPD`: COS and the initials of `[ORG]AIOC-PPD` (Naming Standard R16, item 2). Its full name, role card, ports, authority and cases do not change.
2. **The old code.** `[ORG]CELL-PCS` is retired (Naming Standard R5) and never issued again. It is kept in the new card's lineage (`relation: derived`) and in `tools/make_cards.py` as a withdrawn code.
3. **The test.** The part test `TEST-PPD-PCS` is named `TEST-PPD-COSPPD`; its cases and its owner do not change.
4. **The check.** `tools/make_cards.py` accepts a Cell marked `code_rule: "R16"` only when it is the Chief of Staff and its code is COS and the AIOC's initials.
5. **The version.** Blueprint `v0.5.1`; every card takes the new version. Nothing else changes.
6. **Instances.** A Chief of Staff Cell installed in an `[ORG]AION` moves only by entries in that organisation's unit register (R16, item 5). None is moved here.
7. **The Library pin** moves only by a pull request to `49GAION-protocol` after this merges.

*Powered by 49GAION*
