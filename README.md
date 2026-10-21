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

## RC4 consolidation — before app adoption

The 138 rule IDs are unchanged. Use `--phase development` for targeted checks, `--phase release-candidate` for nominated production candidates, and `--phase post-release` for supported monitoring. Omitting `--phase` conservatively defaults to release-candidate.

- `STD-DIAG-001`: internal/developer Full App Check **or equivalent external CI diagnostic**.
- `STD-LOC-005`: only when the app offers an in-app language selector, otherwise N/A.
- `STD-AUTH-SOURCE-001`: offline legal/normative sources; source/freshness/staleness evidence for live external feeds.
- `STD-SHARE-001`: persistent shared content, not access-control-only flows.
- `STD-POSTRELEASE-001`: mandatory after production release if monitoring is supported; does not block prior RC submissions.
- Every rule has a descriptive machine-readable title; inherited titles are non-normative labels.

For `unit`, `ui`, `runtime` and passed screen families, a test name or Markdown gate link is **PENDING, not PASS**, until matched by execution evidence with exact app/version/build/sourceRevision/phase, timestamp, runner, check ID, device/OS when applicable and SHA256-verified raw artifact.

See [EXECUTION_EVIDENCE_CONTRACT.md](EXECUTION_EVIDENCE_CONTRACT.md) for the declaration and acceptance semantics. These candidate rules are not automatically retroactive to apps pinned to stable 1.8.0.

```bash
python3 Checks/validate-app-conformance.py --app-root /path/to/app --standard-root . --phase development
python3 Checks/validate-app-conformance.py --app-root /path/to/app --standard-root . --phase release-candidate
python3 Checks/validate-app-conformance.py --app-root /path/to/app --standard-root . --phase post-release
```
