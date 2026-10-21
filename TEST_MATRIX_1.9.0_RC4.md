# IbaJuraj Application Standard 1.9.0 RC4 — Test Matrix

Existing RC3 Release Inspector and AI tests remain applicable. New obligations are **capability-scoped**.

## Candidate and applicability
- [ ] Exactly 138 unique IDs; inherited 134 RC3 rule objects byte-semantic unchanged.
- [ ] `hasPortableBackup`, `hasUserRestore` and `hasAppUpdateNotice` flags are Booleans (not "false" strings).
- [ ] All four rules N/A when corresponding capabilities are false; enabled capability missing evidence FAIL.
- [ ] `hasUserRestore` can be true while `hasPortableBackup` false (import-only workflow).
- [ ] Stable `1.8.0` metadata/tag unchanged.

## STD-BACKUP-001 portable archive
- [ ] Versioned manifest includes DB/history, relevant off-database state and user-visible exclusions.
- [ ] Confidential/personal archive has authenticated encryption; tamper/corrupt/partial/empty wrong-key cases reject safely.
- [ ] No auth tokens, API secrets, wallet seeds, raw recovery key or Keychain credentials exported/logged.
- [ ] Snapshot consistency, including committed SQLite WAL rows if the app uses SQLite.
- [ ] Exported filename exists, >0 bytes and verified — distinctly **export PASS**, not restore PASS.

## STD-BACKUP-002 restore
- [ ] Read-only preview of counts/identities/version/migration compatibility and replacement consequences.
- [ ] Incompatible schema, missing archive segments, wrong key and insufficient storage fail without deleting current state.
- [ ] Isolated staging, safe activation, checkpoint retained until successful verification.
- [ ] Fault injection at extraction, data replacement, preferences update, cold start and rollback.
- [ ] **Isolated device/runtime:** source and target parity for users, assets, balances, finance history, DeFi, folders, settings and off-DB persisted state as applicable.
- [ ] Explicitly excluded secrets are marked to be re-entered; original device remains unaffected.

## STD-SHARE-001 two-account cloud sharing
- [ ] Owner creates share, invite accepted, role/membership recognized.
- [ ] Real recipient obtains **correct record count and stable IDs**; delayed membership/snapshot order covered.
- [ ] Empty recipient local state cannot erase owner records.
- [ ] Later owner and recipient edits, conflict, retry and revoke verified; owner retains unshared data.
- [ ] One-off e-mail/SMS card sharing tested and recorded separately from shared wallet lifecycle.

## STD-UPDATE-001 app version update notices
- [ ] Mock: equal/older/newer store release; correct app identifier and valid URL.
- [ ] Offline/timeout/invalid JSON/non-2xx/provider errors: record attempt, preserve prior successful-check, retry with bounded backoff.
- [ ] Successful 24h or declared TTL throttle; normal update does not block startup.
- [ ] Snooze same version persists and suppresses repetitive alerts; newly published version handled separately.
- [ ] Check after unlock; manual Settings check; appropriate storefront/language, Dynamic Type, VoiceOver.
- [ ] Private app without provider is N/A; no fake public App Store version.

## Existing iPad/adaptive coverage (no additional ID)
- [ ] Native iPad layout when supported, portrait/landscape, reduced/multitasking window and low-memory device.
- [ ] Compatibility mode app is not falsely labeled fully native.

Evidence separation: Static PASS != Xcode Build/Test PASS != recovery/sharing runtime PASS. Whole-app audit only for nominated release candidates per `STD-RELEASE-006`.

## Consolidated applicability and executed-evidence tests

- [ ] All **138 rule IDs** remain unique; all have nonempty descriptive title and valid recursive capability/phase conditions.
- [ ] `STD-LOC-005` N/A without in-app selector even if localized; `STD-SHARE-001` N/A with access-only CloudKit but mandatory for persistent recipient-shared content.
- [ ] Persistent shared content requires `hasCloudSharingOrAccessControl=true`.
- [ ] `STD-AUTH-SOURCE-001`: offline cited legal/normative data distinct from time-stamped live source/stale fallback.
- [ ] `--phase development` excludes release-only checks, while `--phase release-candidate` requires them and `--phase post-release` checks monitoring when applicable.
- [ ] An implemented rule with only a test name/link, no executed evidence = PENDING (exit 2 for release blockers), not PASS.
- [ ] Explicit failing run, mismatched app version/build/sourceRevision/phase, missing runner/date/device, missing artifact, escaped path, or SHA256 mismatch = FAIL (exit 1).
- [ ] Screen family pass requires an executed UI check result, otherwise PENDING; fixture outputs distinguish synthetic from true native runtime.
- [ ] Final `SHA256SUMS.txt` covers every file except itself, and GitHub CI passes on the exact reviewed commit.
See [EXECUTION_EVIDENCE_CONTRACT.md](EXECUTION_EVIDENCE_CONTRACT.md); a SHA256-matching self-asserted log alone does not prove physical runtime behavior.

## Grouped correction regression — 21 Oct 2026
- [ ] Seven historical release/screen contracts do not appear in development conformance but do apply in release-candidate.
- [ ] Pending development unit and screen evidence is visible as PENDING, exits 0 with no other errors and does not claim release PASS.
- [ ] Omitted critical feature flags fail RC (exit 1), not silent N/A; optional development warning remains nonblocking.
- [ ] Missing/adopted/deferred SHOULD decision and missing deferral rationale produce only relevant nonblocking warnings.
- [ ] Missing RC release rule, explicit failed result, build/source mismatch, or artifact hash tampering still fail.
