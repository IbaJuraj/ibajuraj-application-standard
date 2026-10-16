# IbaJuraj Application Standard 1.9.0 RC4 — Candidate Release Notes

**Candidate date:** 16 October 2026  
**Stable authority:** `standard-v1.8.0`  
**Candidate branch:** `standard-1.9.0-rc4-data-continuity-updates`  
**Proposed tag:** `standard-v1.9.0-rc4` — NOT created

RC4 preserves the 134 RC3 candidate contracts and adds four machine-readable rules, for **138** total. It is a non-breaking candidate and does not modify stable metadata.

## New normative scope

- `STD-BACKUP-001`: portable backup manifest/scope/completeness, authenticated integrity/encryption when personal/financial data are involved, safe recovery-key lifecycle and secret exclusions.
- `STD-BACKUP-002`: compatible staged restore, destructive-operation preview, rollback, corruption tests and **independent second-device recovery evidence**.
- `STD-SHARE-001`: actual delivered content parity after invitation, protection against empty-owner overwrite, follow-up sync/edit/revoke.
- `STD-UPDATE-001`: distribution channel identity, meaningful version comparison, successful-check TTL vs bounded failure retry, version-scoped snooze and non-blocking localized UX.

## Not new requirements

Native iPad/adaptive layout was already specified; this candidate does not force all iPhone apps to support iPad. Existing RC3 AI provider/fallback/read-only and release audit cadence remain unchanged. Common Swift packages are optional.

## Promotion prerequisites

Candidate/static validation; independent app native/runtime proof; correct handling of financial/history/off-DB data, invite/content truth, and provider update failure/snooze. No stable tag, version or app build change is implied.
