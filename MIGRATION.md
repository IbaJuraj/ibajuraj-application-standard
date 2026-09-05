# Migration – IbaJuraj Application Standard 1.7.0 → 1.8.0 RC1

1. Keep all 1.7.0 requirements unless explicitly clarified by a new 1.8.0 rule.
2. Update the local Standard snapshot/pin to candidate `1.8.0` / `standard-v1.8.0-rc1` only for RC adoption work.
3. Update `STANDARD_CONFORMANCE.json` from the 1.8.0 template and add relevant capability flags.
4. Preserve the existing screen-family inventory and runtime evidence discipline from 1.7.0.
5. If localization applies, verify localization resources, fallback, locale-aware number/date/currency/percent formatting and pluralization.
6. If localization + persisted data apply, separate localized display labels from raw enum/database/AppStorage/transport/CloudKit identifiers.
7. If an in-app language selector exists, add Automatic/System mode, all runtime-supported languages, persisted selection and deterministic whole-app application/relaunch behavior.
8. If search + localization apply, add localized names/aliases and representative per-language search smoke tests.
9. Keep runtime-supported languages independent from App Store storefront/territory availability and product-page localization.
10. Clean the current source/release root: retain current authoritative build/release docs; archive or consolidate superseded build-specific files without deleting unique regression/migration evidence.
11. If an environment-specific backend exists, inventory stable local domain IDs separately from Development/Production record/share/token/binding identity.
12. Ensure missing remote representation in one environment cannot delete, reset or duplicate the stable local object.
13. Make environment-specific backend binding recreatable/rebindable without re-entering domain data.
14. Verify Production backend schema/resources, indexes, permissions/security roles, entitlements/configuration and deployment state before distribution.
15. Run a real TestFlight/Production read/write/sync/share smoke according to app capabilities.
16. Run the single-device Xcode → TestFlight/App Store → Xcode continuity test, preferably with the same build where practical.
17. For persistent-data apps, define a representative real-volume dataset and run critical scroll/search/filter/sort/root-switch performance smoke.
18. Record backend-only fixes separately from binary fixes; do not create a new app build solely because a server-side deployment fixed the same binary unless another binary change is required.
19. Run the common Standard validator, catalog validator and app conformance validator.
20. Do not claim Level 4 or final 1.8.0 adoption while a release-blocking new rule is pending.

## App-specific focus

### Peňaženka Kariet
- six-language runtime + optional in-app selector,
- stable card/wallet IDs independent of Development/Production cloud bindings,
- Production CloudKit schema/index/security-role evidence,
- single-device continuity,
- representative 32-card performance smoke.

### Strážca Termínov
- stable Person/Vehicle/VehicleSet/Document/Deadline identity,
- Development/Production membership/share/invitation separation,
- Production CloudKit readiness,
- single-device continuity and localization closure,
- release-root history hygiene.

No domain migration is required solely because the Standard version changes. Domain migration is required only if an app currently violates a newly applicable data/backend identity contract.
