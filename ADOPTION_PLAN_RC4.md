# Adoption Plan — IbaJuraj Application Standard 1.9.0 RC4

Candidate status only; no automatic app code changes, data migrations, build increments or mandated common package.

1. **TradeBook 2.1.0 / Build 269 R8:** current Xcode Build/Test and encrypted iPhone export are PASS. Finish isolated iPad cross-device restore, finance/history/off-DB parity, schema migration and rollback before declaring `STD-BACKUP-002` PASS. iPad native UI is existing adaptive Standard adoption. Store update notice = N/A until a real channel exists.
2. **Strážca Termínov 1.61.0 / Build 134:** invitation and membership runtime PASS, shared content receipt still pending. Test recipient owner-verified Octavia plus six terms, subsequent edit and revoke. Existing backup needs sensitivity review before claiming authenticated encrypted archive. Improve update notice at its next planned build.
3. **Peňaženka Kariet 1.5.4 / Build 92:** one-off card transport is distinct from shared-wallet two-account sync. Add full lifecycle acceptance; consider encrypted personal archive/recovery and correct app-specific version notice.
4. **Lex Drive:** App Store notice via shared service at next logical build; legal effective-date/actor/content correctness still owned by separate deterministic legal audit.
5. **Kalkulačka 2v1:** update notice only if feature enabled; existing Voice permission/feature parity remains under stable `STD-PERM-001`.
6. Cross-app security/dependency and exact-build conformance audit before extraction to an optional `IbaJuraj DataKit` or `App Update Kit`. Keep key material, CloudKit containers, sync identities, and domain-specific merge policies per app.
7. Promote neither RC4 nor shared utilities to stable before nominated release-quality evidence. Minimize app build churn: fix via grouped logical builds/revisions.

## Implementation sequence after Standard-only consolidation

1. Finish candidate documentation, validation and exact-head GitHub CI **before** changing any application.
2. Validate central Compliance Gate using Kalkulačka v1.15.0 Build 64 source as an adoption pilot; evidence still needs real executed native tests where applicable.
3. Integrate pin/build/source/evidence reports in logically grouped tool updates for Lex Drive, Strážca Termínov, Peňaženka Kariet and TradeBook, preserving their existing baseline and production data.
4. Keep backup restore on iPad and two-account cloud content parity as separate live runtime acceptance tasks, not as automatic results of Standard CI.
5. Release audit applies to nominated app release candidates; avoid separate application builds for every small requirement.
6. Stable Standard 1.8.0 remains current public authority until independent approval and promotion of 1.9.0.

## Authoritative governance/adoption status addendum — 22 October 2026

The older build references above describe the **initial** pilots and are historical. Approved [IJAS-0041](Proposals/IJAS-0041-central-standard-promotion-vs-app-release-adr.md) separates the Standard's C-01...C-07 **central promotion** from each app's exact-build release gate; it does not weaken mandatory contracts.

| App | Most recent working source baseline on 21 Oct 2026 | Real acceptance still not evidenced |
|---|---|---|
| Calculator | 1.15.0 Build64 R6 | Pilot validator logic PASS; original executed RC evidence / 7 screen families and full app RC PENDING |
| TradeBook | 2.1.0 Build280 | B280 native Xcode and second-device full-state restore/rollback PENDING; earlier B279 native check is not B280 |
| Strážca Termínov | 1.62.0 Build135 R2 | Xcode PASS/PASS and widget/deep link runtime PASS; recipient content parity / edit / revoke and backup restore PENDING |
| Peňaženka Kariet | 1.6.0 Build94 R8 | Owner-side B78 flow PASS historically; two-account persistent-wallet lifecycle and second-device recovery PENDING; precise R8 native artifact to reconcile |
| Lex Drive | 1.23.0 Build325 (RC validation pending) | Exact-native, legal temporal integrity and release inspector PENDING |

Cross-app applicability and capabilities are to be reviewed against source, not guessed from false flags. App update notices with real providers remain mandatory at applicable app RC; absence of a true provider demands independent N/A justification. RC3 AI/Release Inspector requirements remain mandatory where applicable.

**Central required next:** positive Calculator exact-build native/UI execution evidence, read-only cross-app capability audit, latest-head CI+SHA and release authorization. No unnecessary application builds, no synthetic evidence and no stable promotion while central gates are pending.
