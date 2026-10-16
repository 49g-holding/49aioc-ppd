# DR-0004 · PPD v0.4.0: the chain connected on both sides; every return ends

- **Date:** 2026-10-16
- **Decided by:** the governing seat (GOV), in conversation with `[ORG]AIOC-OCO` (the decider is a position)
- **Source:** the directions of GOV of 15 October 2026, recorded at 49GAION as `49GAION/DR-0016` (items 4 and 5), `DR-0017` (item 8) and `DR-0018`: returns between design stages go back and forth until each ends, by a decision or set aside and carried forward, so that the output arrives; Delivery and Implementation is the stage after this one. And the direction of GOV of 16 October 2026 to connect the chain in this order, so that the blueprints, engineering and documents of the human cycle are complete (translated).
- **Relation:** builds on DR-0001 to DR-0003; it supersedes this AIOC's own return contract, `contracts/release-return.schema.json` v0.1, by the Library's.

## Decision

1. **One contract for returns.** Every return, to `[ORG]AIOC-TOM` and from `[ORG]AIOC-DI`, follows the Library's design return contract, pinned by commit and hash in `contracts/PINS.json`. This AIOC keeps no copy of it.
2. **Every return ends.** A return counts its rounds and ends answered by release, answered by decision, set aside by decision and carried forward as a known defect or a decided assumption, or withdrawn. An element carried forward on a set-aside return is marked with its basis in the release and listed in the Decision Package.
3. **Told directly.** Each decided PPD Release is announced to `[ORG]AIOC-DI` by a release notice, by reference, naming the TOM Release it rests on (`contracts/release-notice.schema.json`).
4. **Returns from DI.** They are received and carried to an end as the TOM blueprint `v0.5.0` §5.10 does for this AIOC's returns: admission, a brief made by code, rounds, escalation, an answer, and a classification by the PPD Design Lead, never by the Chief of Staff. A defect DI finds in the TOM Release is DI's to return to TOM.
5. **What changes.** Blueprint §0, §1, §2, §4.2, §4.4, §5, §5.1, §5.10, §5.11 (new), §6, §8 to §15, §17, Annexes A to E; the contracts and their checker; TEST-PPD v2 (cases 98 to 104, PDL-6; case 27 struck); the cards.

*Powered by 49GAION*
