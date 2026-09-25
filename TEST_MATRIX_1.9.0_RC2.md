# IbaJuraj Application Standard 1.9.0 RC2 — Test Matrix

## Cadence
- Small development build: Build/Test + targeted regression.
- High-risk change: expanded targeted checks.
- App Store/store/production RC: full Release Candidate Quality Gate.
- Material change after RC gate: new exact-build gate.

## Full App Check
Verify internal/developer-only access, non-destructive behavior, applicable data/migration/navigation/localization/business-rule/sync/API/deep-link/cache checks, structured findings and traceable exceptions.

## Release diff/risk
Compare with last published baseline; map source, dependency, data model/schema, migration, config/flag, UI and localization changes to blast radius and test scope.

## Journeys/resilience
Run critical end-to-end flows plus applicable restart/persistence, offline, timeout, permission-denied, interrupted import/write, corrupt-input, sync-conflict and old-data upgrade scenarios.

## UI/runtime
Review changed/high-risk surfaces on representative viewports, Light/Dark, relevant Dynamic Type and localization stress states; resolve ambiguous visual findings manually.

## AI
When enabled: reason/evidence/confidence present; no secrets/tokens; private inputs sanitized; no autonomous mutation; AI-only blockers corroborated or human-confirmed.

## Evidence
Exact app version/build, Standard candidate, check summary, findings, exceptions, release diff/risk scope, runtime/UI evidence and AI summary when used.
