# Adoption Plan — IbaJuraj Application Standard 1.9.0 RC4

Candidate status only; no automatic app code changes, data migrations, build increments or mandated common package.

1. **TradeBook 2.1.0 / Build 269 R8:** current Xcode Build/Test and encrypted iPhone export are PASS. Finish isolated iPad cross-device restore, finance/history/off-DB parity, schema migration and rollback before declaring `STD-BACKUP-002` PASS. iPad native UI is existing adaptive Standard adoption. Store update notice = N/A until a real channel exists.
2. **Strážca Termínov 1.61.0 / Build 134:** invitation and membership runtime PASS, shared content receipt still pending. Test recipient owner-verified Octavia plus six terms, subsequent edit and revoke. Existing backup needs sensitivity review before claiming authenticated encrypted archive. Improve update notice at its next planned build.
3. **Peňaženka Kariet 1.5.4 / Build 92:** one-off card transport is distinct from shared-wallet two-account sync. Add full lifecycle acceptance; consider encrypted personal archive/recovery and correct app-specific version notice.
4. **Lex Drive:** App Store notice via shared service at next logical build; legal effective-date/actor/content correctness still owned by separate deterministic legal audit.
5. **Kalkulačka 2v1:** update notice only if feature enabled; existing Voice permission/feature parity remains under stable `STD-PERM-001`.
6. Cross-app security/dependency and exact-build conformance audit before extraction to an optional `IbaJuraj DataKit` or `App Update Kit`. Keep key material, CloudKit containers, sync identities, and domain-specific merge policies per app.
7. Promote neither RC4 nor shared utilities to stable before nominated release-quality evidence. Minimize app build churn: fix via grouped logical builds/revisions.
