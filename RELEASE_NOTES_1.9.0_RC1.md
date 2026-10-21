# IbaJuraj Application Standard 1.9.0 RC1

**Candidate date:** 17 September 2026  
**Stable authority remains:** 1.8.0 (`standard-v1.8.0`)  
**Proposed candidate tag:** `standard-v1.9.0-rc1`

## Summary

Version 1.9.0 RC1 is a compatible candidate that preserves all 119 stable 1.8.0 rules and adds two new release-blocking rules, for a total of **121 machine-readable rules**.

## New rules

### `STD-ASYNC-002 — Remote invite/share/access responsiveness — MUST`

Apps with remote invite/share/access flows must keep interactive UI/MainActor responsiveness while remote work is pending. Long-running remote work must expose visible progress and must not weaken confirmed-remote-truth or durable retry/reconciliation semantics.

### `STD-AUTH-SOURCE-001 — Authoritative functional source is available offline and externally traceable — MUST`

Apps that use legal, regulatory, normative or equivalent authoritative sources as part of a functional result must make the used source basis available locally/offline, identify the exact version/effective date, expose exact citation or verbatim provision where applicable, and preserve verification provenance. An official external website remains supplemental, not the only access path.

## Clarified without a new rule ID

The root-title adaptive family is clarified so peer root screens use one shared title family driven by available viewport/container width. Full titles should be preferred over device-specific sizing or isolated truncation.

## Relationship to existing rules

- `STD-ASYNC-001` continues to govern stale async completion safety.
- `STD-CLOUD-001` continues to require confirmed remote truth before presenting remote destructive/access success.
- `STD-CLOUD-002` continues to require durable retry or reconciliation.
- `STD-DATA-004` continues to govern authoritative versioned-data correctness; `STD-AUTH-SOURCE-001` adds the user-facing offline citation and traceability contract.

## Reference adoption

- Strážca Termínov v1.59.0 / Build 120 Phase 14A R12 is the first implementation reference for `STD-ASYNC-002`.
- Lex Drive Build 232 is the first reference case for `STD-AUTH-SOURCE-001`, including offline legal citation and legal-chain traceability.

Final RC publication still requires exact-build runtime evidence for applicable paths and a green validation workflow on the final candidate commit.

## Candidate status

This RC does not replace the public stable authority. Until promotion:

- `STANDARD_VERSION` and `standard.json` continue to describe stable 1.8.0,
- `CONFORMANCE_CATALOG.json` describes candidate 1.9.0 RC1 with 121 rules,
- the proposed RC tag must not be created until the candidate checklist is complete and the exact final candidate commit has green validation.
