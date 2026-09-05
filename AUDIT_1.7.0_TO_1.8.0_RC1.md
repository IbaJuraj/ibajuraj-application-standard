# Audit – IbaJuraj Application Standard 1.7.0 → 1.8.0 RC1

**Dátum:** 2026-09-05  
**Základ:** aktívny `standard-v1.7.0` / commit `109d824f564361af9b2204412ab3b6484843e055`  
**Kandidát:** `standard-v1.8.0-rc1`

## Versioning decision
Podľa `GOVERNANCE.md` je PATCH určený pre clarification/hardening bez novej contract family, kým MINOR je určený pre novú kompatibilnú contract family. IJAS-0027 a IJAS-0028 pridávajú nové cross-app data/backend contract families, preto bol pôvodne zvažovaný 1.7.1 scope povýšený na **1.8.0**.

## Zachované z 1.7.0
- všetkých 96 stabilných `STD-*` pravidiel,
- whole-app adaptive layout,
- viewport edge utilization,
- bottom navigation,
- screen-family audit,
- header/system chrome ownership,
- accessibility/form/data/privacy/debug/AI/conformance/release kontrakty,
- zásada Static PASS != runtime PASS.

Žiadne publikované 1.7.0 rule ID nebolo odstránené ani významovo predefinované.

## Nové pravidlá – 12
### Localization
- `STD-LOC-003` localization-ready semantic keys,
- `STD-LOC-004` locale-aware formatting/pluralization,
- `STD-LOC-005` in-app language selector contract,
- `STD-LOC-006` locale-neutral persisted identifiers,
- `STD-LOC-007` localized search parity,
- `STD-LOC-008` storefront/runtime-language independence.

### Release hygiene
- `STD-RELEASE-005` current root excludes superseded build docs,
- `STD-RELEASE-006` historical evidence archived/consolidated, not silently deleted.

### Data/backend/performance
- `STD-DATA-005` stable local identity across Development/Production environment changes,
- `STD-BACKEND-001` Production schema/config/permissions readiness,
- `STD-BACKEND-002` real TestFlight/Production smoke and local-safe backend failure,
- `STD-PERF-001` representative real-volume runtime performance gate.

**Catalog total:** 108 rules.

## Evidence motivating 1.8.0
### Peňaženka Kariet
- localization expansion from SK/CZ to SK/CS/EN/DE/PL/HU exposed the need for localization-first architecture and a consistent language-selection contract,
- user requirement to switch languages in-app for runtime review/screenshots motivated explicit optional selector rules,
- persisted card/wallet data must remain stable regardless of UI language,
- single physical iPhone alternates Xcode and TestFlight/App Store, requiring environment-safe data continuity,
- Production CloudKit sync/sharing failed until Development schema/index/security-role changes were deployed to Production; the same TestFlight binary then worked,
- runtime with 32 real cards exposed scroll performance behavior not visible in a small fixture.

### Strážca Termínov
- person-first sharing/membership model has the same Development/Production continuity risk,
- long-lived build history exposed root documentation hygiene debt.

## Compatibility
1.8.0 RC1 is backward-compatible at the Standard level. New rules are capability-scoped where appropriate. Apps without an in-app selector or environment-specific backend do not inherit those specific runtime obligations.

A domain migration is required only if an adopting app currently uses localized labels as persistent identity, environment-specific remote IDs as sole domain identity, or another architecture that violates an applicable new rule.

## Known RC1 gates
- Standard repository validators and CI must pass on the RC1 head.
- Peňaženka Kariet is the primary real adoption proof.
- Strážca Termínov is the secondary data/backend continuity proof.
- Representative applicability audit is required for Lex Drive and Kalkulačka 2v1 before final promotion.
- Any semantic ambiguity requiring a contract change creates RC2 rather than silently editing RC1 after publication.

## Audit result
**RC1 package design:** PASS for candidate creation.  
**Final 1.8.0 promotion:** PENDING cross-app adoption/runtime evidence.
