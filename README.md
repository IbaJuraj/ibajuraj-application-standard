# IbaJuraj Application Standard 1.9.0 RC4

This branch contains the **candidate IbaJuraj Application Standard 1.9.0 RC4**. Stable public authority remains **1.8.0** (`standard-v1.8.0`).

RC4 is a non-breaking extension of RC3: **134 inherited candidate rules unchanged + four capability-scoped rules = 138 candidate rules**.

## New cross-app contracts

- `STD-BACKUP-001` — portable archives: complete scope/manifest, integrity, authenticated encryption where sensitive, safe handling of recovery keys and excluded secrets.
- `STD-BACKUP-002` — restore preflight: compatible schema, read-only preview, atomic/transactional activation, rollback and **actual cross-device restore proof**.
- `STD-SHARE-001` — recipient data parity: accepted invitation is not evidence that shared records arrived; no empty owner overwrite, edits/conflicts/revoke verified.
- `STD-UPDATE-001` — accurate update provider/channel, last-success vs attempt retry, version-scoped snooze and non-blocking localized notice.

Existing iPad/viewport rules, AI governance and Release Inspector cadence are preserved without redundant rule IDs. `IbaJuraj DataKit` and `App Update Kit` are optional patterns, not mandated dependencies.

## Validate

~~~bash
bash Checks/validate-standard.sh
python3 Checks/validate-conformance-catalog.py
python3 -m unittest Checks/test_validate_app_conformance.py
~~~

## Governance

- Public stable: `main` / `standard-v1.8.0` (unmodified).
- RC4 candidate: `standard-1.9.0-rc4-data-continuity-updates`.
- Proposed tag: `standard-v1.9.0-rc4` — **not published**.
- RC3 Draft PR #12 remains a predecessor, not a stable release.
- Static PASS ≠ Build/Test PASS ≠ device-level data recovery/shared-content PASS. Promotion requires independent app evidence.
