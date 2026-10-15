# Contracts

**`[ORG]AIOC-PPD` v0.1.0 · 15 October 2026.**

| Contract | File | Between |
|---|---|---|
| Release return | `release-return.schema.json` (`urn:49gaion:library:ppd:release-return:v0.1`) | this AIOC and `[ORG]AIOC-TOM`; the next stage and this AIOC |
| Release notice | field list below; a schema is a build item | `[ORG]AIOC-TOM` and this AIOC; this AIOC and the next stage |
| Needs request, needs answer, needs status, Missing Report, source reference | as published by `[ORG]AIOC-TOM` `v0.4.0` (`contracts/` of the writing repository of `[ORG]AIOC-TOM`), by path and hash, until Source Lifecycle adopts them | this AIOC and `[ORG]AIOC-SL` |

**Release notice.** `release_id`; `manifest_sha256`; `filed_ref` (source ID, version and hash of the filed copy in Source Lifecycle); `from` (the sending AIOC's code); `supersedes` (the release ID it replaces, if any); `sent_at`.

`python3 tools/check_contracts.py` checks every example in `examples/`: each `valid-*` must validate, each `must-fail-*` must be refused and have its reason in `examples/MUST-FAIL-REASONS.json`.

*Powered by 49GAION*
