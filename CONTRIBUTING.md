# Contributing

**`[ORG]AIOC-PPD` v0.1.0 · 15 October 2026.**

1. **One change, one pull request**, reviewed by someone other than its writer.
2. **Positions, never people.** No person's name in any file. Who occupies a position is top management's own mechanism, never here (49GAION Standard §1.1, item 9).
3. **No organisation data.** This repository is written for any organisation. An organisation's values, sources and run records live in its own records repository.
4. **Cite every rule** to its source: a 49GAION text by section and version, a carried rule by the TOM blueprint section and version (blueprint Annex E). Never invent a fact, a version or a score. `NOT_RUN` is never PASS.
5. **The blueprint governs the cards.** Edit the card data block of blueprint §17 only, then run `python3 tools/make_cards.py <49GAION-protocol/spec/schemas>`. It must report 0 errors.
6. **Contracts are schemas.** A change to `contracts/` keeps every example as expected, adds an example for any new case, and gives each must-fail example its reason in `contracts/examples/MUST-FAIL-REASONS.json`. `python3 tools/check_contracts.py` must report 0 failures.
7. **Decided texts are never edited.** A change is a new version that names what it supersedes.
8. **English only, plain and short.**

*Powered by 49GAION*
