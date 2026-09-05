# IbaJuraj Application Standard 1.8.0 RC1

**Release candidate date:** 5 September 2026  
**Candidate tag:** `standard-v1.8.0-rc1`  
**Active stable Standard remains:** `standard-v1.7.0`

## Summary
1.8.0 RC1 is a backward-compatible MINOR expansion over 1.7.0. It keeps the validated 96-rule 1.7.0 set and adds 12 rules for localization architecture, language selection, release-package hygiene, single-device data continuity, Production backend readiness and representative-data performance.

## Highlights
- localization-ready architecture and stable semantic localization keys,
- locale-aware formatting and pluralization,
- optional in-app language selector with Automatic/System mode,
- no data migration or raw-ID changes caused only by UI language switching,
- localized search parity,
- runtime languages independent from App Store storefront availability,
- clean current release root with archived build history,
- stable local domain IDs independent from Development/Production cloud bindings,
- single-device Xcode ↔ TestFlight/App Store ↔ Xcode continuity gate,
- explicit Production backend schema/index/permission/config readiness,
- real TestFlight/Production read/write/sync/share smoke according to app capabilities,
- explicit distinction between server-side fixes and binary fixes,
- runtime performance testing with representative real-volume datasets.

## Rule count
- 1.7.0: 96 rules
- 1.8.0 RC1: **108 rules**

## Accepted proposals
- IJAS-0025 Localization-First Architecture and Storefront Independence
- IJAS-0026 Release Package Root Hygiene and Build History Archive
- IJAS-0027 Single-Device Development/Release Data Continuity
- IJAS-0028 Production Backend Environment Readiness

## Primary evidence
Peňaženka Kariet supplies the main real-world motivation:
- six-language localization expansion,
- planned in-app language selector,
- 32-card real-data performance testing,
- Xcode/TestFlight same-device continuity,
- Production CloudKit schema deployment required before the same TestFlight build could sync/share successfully.

Strážca Termínov supplies the secondary cross-app case for persistent identity, sharing/membership environments and release-root history hygiene.

## Publication model
RC1 should be published as a **GitHub prerelease**, not as the new stable `releases/latest` authority. The active stable Standard remains 1.7.0 until the adoption/promotion gate is complete.

After RC1 publication:
1. finish Peňaženka Kariet against RC1,
2. audit/adopt Strážca Termínov,
3. run representative applicability checks in Lex Drive and Kalkulačka 2v1,
4. resolve any RC ambiguity,
5. promote to final `standard-v1.8.0` only when governance requirements are satisfied.
