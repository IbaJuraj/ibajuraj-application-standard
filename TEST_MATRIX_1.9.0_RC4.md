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
