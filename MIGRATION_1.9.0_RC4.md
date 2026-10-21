# Migration to IbaJuraj Application Standard 1.9.0 RC4

**Candidate only.** Public stable authority and stable metadata remain `1.8.0`. No automatic migration of application databases or user data.

1. Preserve all 134 RC3 rule objects and add only the four RC4 scoped contracts; pin `standardVersion: 1.9.0` and `standardCandidate: RC4` in the app's candidate conformance manifest.
2. Declare Boolean capabilities `hasPortableBackup`, `hasUserRestore` and `hasAppUpdateNotice`. The existing `hasCloudSharingOrAccessControl` selects shared-content parity. Declare true **only for features the app actually exposes**; missing/false = N/A.
3. Export-only does not imply restore; restoring an externally supplied backup does not imply the app can also export. No capability is imposed solely because an optional shared Swift Package exists.
4. For portable backup, audit versioned format/manifest, off-database data, authenticated encryption according to sensitivity, independent recovery-key handling and intentional secret exclusions.
5. For restore, require read-only preflight and user consent, migration compatibility, staged commit/checkpoint, safe rollback and isolated-device content comparison before saying full recovery PASS.
6. For cloud sharing, test invitation and membership separately from delivered recipient records; verify no destructive empty initial sync, subsequent edits/conflicts and revoke on two real accounts.
7. For update notices, test App Store/TestFlight/private provider correctness, last attempt vs last successful check, shorter bounded retry, per-version snooze and correct localized URL. Non-App-Store private apps are N/A without a real provider.
8. Existing native iPad support belongs to `STD-ADAPT-*` / `STD-SCREEN-*` adoption and iPad matrix, not a new RC4 rule ID.
9. Adopt shared security utilities only after application-specific secret/storage/CloudKit review; domains retain distinct credentials, keys, identities and merge policies.
10. Re-run the candidate validators and record exact-app-version/build/device/OS evidence. Full release-quality check is for release candidates, not each small development revision.

**Initial pilots:** TradeBook 269 R8 cross-device backup/restore on iPad (still runtime pending); Strážca 134 recipient content parity after accepted invite (still pending); Peňaženka 92 shared-wallet two-account lifecycle (still pending); store apps update service checks before later release builds.

No RC4 rule or proposal is already a production feature merely because it is documented here.

## Consolidation addendum — before adopting candidate

1. **Do not silently repin existing apps.** Stable 1.8.0 and RC3 app evidence remain tied to their actual catalog. 1.9.0 RC4 is a separate candidate with 138 IDs preserved.
2. Explicitly declare `hasInAppLanguageSelector` only for a custom in-app picker, `hasPersistentSharedContent` only for durable recipient-shared records, `hasAuthoritativeFunctionalSources` for functional normative references, and `hasRemoteInviteShareAccessFlow` for networked invitation flows. Persistent content requires cloud sharing/access control capability.
3. Versioned legal/normative citations remain verifiable offline. Dynamic external/API data preserve identity, retrieval time, freshness/stale state; never claim stale cached data is live.
4. A safe developer-only external CI Full App Check is an alternative to a diagnostic view embedded in the app (`STD-DIAG-001`).
5. Run `--phase development` for ordinary work; **explicit `--phase release-candidate` is mandatory in nominated release workflows**; `--phase post-release` is for enabled production feedback.
6. Add exact app `version`, `build`, 40-hex commit or 64-hex source-tree revision and `executionEvidence.file` in `STANDARD_CONFORMANCE.json`. Use real executed result metadata and hashed primary logs/artifacts per [EXECUTION_EVIDENCE_CONTRACT.md](EXECUTION_EVIDENCE_CONTRACT.md).
7. Record missing execution as PENDING, failure/mismatched build or tampered file as FAIL. Manual device proof is still required for cross-device backup/CloudKit acceptance; no synthetic test fixture is a runtime PASS.
8. Post-release monitoring MUST is not a pre-release blocker; it becomes applicable after release.
9. No automatic user-data migration, app build increment, version switch or secret copying occurs from Standard candidate adoption.

## RC4 phase/N/A/SHOULD correction — 21 Oct 2026

- Existing `STD-RELEASE-002/003/004/005` and `STD-SCREEN-002/003/004` are RC-phase contracts. Missing development UI/runtime evidence is reported as **PENDING**, never as genuine PASS or a release block (exit 0 if there are no actual validation errors).
- Release-candidate runs require explicit Boolean risk-related capability flags; omission gives FAIL rather than silent N/A. Validate true/false values against actual shipped app features independently.
- `STD-LOC-005` and `STD-COMPACT-001` remain SHOULD: optional `recommendations` accepts `{ "decision": "adopted" }` or `{ "decision": "deferred", "reason": "..." }`. Missing rationale warns without blocking.
- Wrong version, tampered/mismatched execution evidence or failing test remains FAIL regardless of phase.
- Stable 1.8.0, the count of 138 candidate IDs and all app binaries remain unchanged.
