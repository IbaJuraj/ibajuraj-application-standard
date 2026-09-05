# Adoption Plan – IbaJuraj Application Standard 1.8.0 RC1

## Goal
Prove the new 1.8.0 contract families in real applications before final promotion.

## 1. Peňaženka Kariet – primary adoption
Current source line at RC1 creation: v1.5.3 / Build 79, with Build 78 Production CloudKit and same-device continuity evidence already available.

### Required RC1 work
- adopt Standard 1.8.0 RC1 metadata/conformance without losing existing Build 79 functionality,
- add/verify in-app language selector if retained in product scope:
  - Automatic/System,
  - Slovak,
  - Czech,
  - English,
  - German,
  - Polish,
  - Hungarian,
- prove switching/relaunch does not modify card/wallet raw data, IDs or cloud bindings,
- six-language main-flow and localized search smoke,
- verify Production personal iCloud sync,
- verify Production shared-wallet activation/rebind,
- preserve Xcode ↔ TestFlight same-device continuity,
- use the real 32-card library for performance smoke,
- clean source/release root according to STD-RELEASE-005/006,
- update app `STANDARD_CONFORMANCE.json` and runtime evidence.

### Acceptance
Peňaženka may be submitted to App Store only after its own release gates pass. Its RC1 adoption evidence is then suitable as the primary promotion proof for Standard 1.8.0.

## 2. Strážca Termínov – secondary adoption
Current authoritative development line at RC1 creation: v1.57.0 / Build 112.

### Required RC1 work
- audit stable local identity for Person, Vehicle, VehicleSet, Document and Deadline,
- audit Development/Production membership/share/invitation identity separation,
- create targeted continuity fix build only if the audit finds environment coupling,
- Production CloudKit readiness and real sharing smoke,
- one-device Xcode ↔ TestFlight continuity,
- root build-history cleanup/archive,
- localization/runtime closure.

## 3. Lex Drive – applicability audit
- preserve public v1.13.0 / Build 226 unless a real new scope exists,
- check new localization/search/release/performance rules for applicability,
- do not force backend continuity rules where no environment-specific user-data backend exists.

## 4. Kalkulačka 2v1 – applicability audit
- current review line remains v1.14.0 / Build 59,
- no new calculator build solely for Standard RC1 while App Store review is active,
- audit localization selector behavior against STD-LOC-005 if the product uses its own selector,
- confirm locale-neutral persisted settings/history identifiers,
- apply release-root hygiene at the next justified build.

## Promotion order
1. Publish 1.8.0 RC1 as GitHub prerelease.
2. Finish Peňaženka Kariet against RC1 and collect real runtime evidence.
3. Audit/adopt Strážca Termínov.
4. Run Lex/Kalkulačka applicability checks.
5. If no semantic change is needed, prepare final 1.8.0 promotion package.
6. If a normative ambiguity or contract change is found, create RC2 instead of editing published RC1 semantics.
