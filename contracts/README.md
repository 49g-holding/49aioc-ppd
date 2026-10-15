# Contracts

**`[ORG]AIOC-PPD` v0.4.0 · 16 October 2026.**

| Contract | File | Between |
|---|---|---|
| Design return | the Library's `library/contracts/design-return.schema.json` of `49GAION-protocol`, pinned by commit and hash in `PINS.json`; this AIOC keeps no copy. It supersedes this AIOC's own `release-return.schema.json` v0.1 | this AIOC and `[ORG]AIOC-TOM`; `[ORG]AIOC-DI` and this AIOC |
| Release notice, received | the TOM's `contracts/release-notice.schema.json` (`urn:49gaion:library:tom:release-notice:v0.5`), pinned by hash in `PINS.json` | `[ORG]AIOC-TOM` and this AIOC |
| Release notice, sent | `release-notice.schema.json` (`urn:49gaion:library:ppd:release-notice:v0.4`) | this AIOC and `[ORG]AIOC-DI` |
| Needs request, needs answer, needs status, Missing Report, source reference | as published by `[ORG]AIOC-TOM` `v0.4.0` (`contracts/` of the writing repository of `[ORG]AIOC-TOM`), by path and hash, until Source Lifecycle adopts them | this AIOC and `[ORG]AIOC-SL` |

`python3 tools/check_contracts.py --design-return <path>` checks, for each schema here, the examples in `examples/<schema>/` (each `valid-*` validates; each `must-fail-*` is refused where its entry in that folder's `MUST-FAIL-REASONS.json` says; a notice's ID is its content address), and validates `examples/design-return/` against the Library's contract at the pinned commit.

*Powered by 49GAION*
