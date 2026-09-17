# IbaJuraj Application Standard

**Verzia:** 1.8.0  
**Stav:** Active / Stable  
**Dátum vydania:** 15. septembra 2026  
**Vlastník:** IbaJuraj  
**Stable verejná autorita:** 1.8.0 (`standard-v1.8.0`)

> Verzia 1.8.0 je finálna stabilná autorita. Zachováva validovaný 119-rule machine-readable katalóg RC2 a finalizuje bezpečnostnú semantiku biometrického odomykania v rámci existujúceho pravidla `STD-SECURITY-001`.

## 1. Záväznosť

`MUST`/`MUST NOT` blokuje release bez platnej ADR výnimky. `SHOULD` vyžaduje zdôvodnenie. Static PASS nenahrádza runtime PASS.

## 2. Integrácia 1.8

1.8.0 má **119 pravidiel**:
- presne zachovaných 96 machine-readable pravidiel 1.7.0,
- 12 pravidiel formalizujúcich publikovaný scope RC1,
- 11 pravidiel hardeningu RC2.

Finálna verzia nemení identitu pravidiel oproti RC2. Bezpečnostné zjednotenie biometrie je normatívne spresnenie existujúceho `STD-SECURITY-001`, nie nový rule ID.

## 3. RC1 formalized scope

Localization-first architektúra, locale-aware formátovanie/pluralizácia, Automatic/System selector contract, stable IDs pri language switch, localized search parity, storefront independence, release-root hygiene, single-device continuity, Production backend readiness/smoke, server-vs-binary fix distinction a representative-data performance.

## 4. RC2 hardening + final security clarification

Async stale-callback safety; authoritative mutation→derived rebuild; remote truth + durable reconciliation; corrupt-state recovery; relationship-aware deletion; upgrade-path gate; deterministic engine tests; disabled-feature/permission parity; build-scoped runtime evidence; compact-surface priority/deep-link integrity.

### Biometrické odomykanie – záväzná semantika `STD-SECURITY-001`

Ak aplikácia ponúka lokálny zámok a biometriu (Face ID, Touch ID, Optic ID alebo ekvivalent), platí jednotný model IbaJuraj Apps:

- biometria je primárny spôsob odomknutia,
- pri nedostupnosti, lockoute alebo zlyhaní biometrie MUSÍ byť dostupné systémové overenie vlastníka zariadenia pomocou kódu/hesla zariadenia,
- samostatný PIN aplikácie NESMIE byť povinnou podmienkou zapnutia biometrie,
- app PIN MÔŽE existovať iba ako voliteľná doplnková ochrana, ak má produktový význam,
- PIN aplikácie, ak existuje, MUSÍ byť uložený bezpečne (Keychain alebo ekvivalent), nikdy v čitateľnom tvare,
- zámok sa NESMIE znovu aktivovať pri bežnej internej navigácii; viaže sa na skutočný lifecycle prechod aplikácie,
- opakované biometrické dialógy počas už prebiehajúcej autentifikácie sa MUSIA blokovať.

## 5. Normatívny register

### STD-IDENTITY-001 — MUST
### STD-IDENTITY-002 — MUST
### STD-IDENTITY-003 — MUST
### STD-COMPONENT-001 — MUST
### STD-COMPONENT-002 — MUST NOT
### STD-COMPONENT-003 — MUST
### STD-COMPONENT-004 — MUST
### STD-COMPONENT-005 — MUST
### STD-SETTINGS-001 — MUST
### STD-SETTINGS-002 — MUST
### STD-APPEARANCE-001 — MUST
### STD-APPEARANCE-002 — MUST
### STD-APPEARANCE-003 — MUST
### STD-ABOUT-001 — MUST
### STD-ABOUT-002 — MUST
### STD-ABOUT-003 — MUST
### STD-ABOUT-004 — MUST
### STD-ABOUT-005 — MUST
### STD-ABOUT-006 — MUST
### STD-ADAPT-001 — MUST
### STD-ADAPT-002 — MUST
### STD-ADAPT-003 — MUST
### STD-ADAPT-004 — MUST
### STD-ADAPT-005 — MUST
### STD-ADAPT-006 — MUST
### STD-ADAPT-007 — MUST
### STD-ADAPT-008 — MUST
### STD-ADAPT-009 — MUST
### STD-ADAPT-010 — MUST
### STD-ADAPT-011 — MUST NOT
### STD-ADAPT-012 — MUST
### STD-NAV-001 — MUST
### STD-NAV-002 — MUST
### STD-NAV-003 — MUST
### STD-NAV-004 — MUST
### STD-NAV-005 — MUST
### STD-NAV-006 — MUST
### STD-NAV-007 — MUST
### STD-NAV-008 — MUST
### STD-NAV-009 — MUST
### STD-NESTED-NAV-001 — MUST
### STD-NESTED-NAV-002 — MUST
### STD-LOC-001 — MUST
### STD-LOC-002 — MUST
### STD-A11Y-001 — MUST
### STD-A11Y-002 — MUST
### STD-A11Y-003 — MUST
### STD-FORM-001 — MUST
### STD-FORM-002 — MUST
### STD-FORM-003 — MUST
### STD-FORM-004 — MUST
### STD-DATA-001 — MUST
### STD-DATA-002 — MUST
### STD-DATA-003 — MUST
### STD-DATA-004 — MUST
### STD-PRIVACY-001 — MUST
### STD-PRIVACY-002 — MUST
### STD-SECURITY-001 — App lock uses biometrics with system device authentication fallback; app PIN is not a prerequisite — MUST
### STD-DEBUG-001 — MUST
### STD-DEBUG-002 — MUST
### STD-AI-001 — MUST
### STD-AI-002 — MUST
### STD-CONF-001 — MUST
### STD-CONF-002 — MUST
### STD-CONF-003 — MUST
### STD-CONF-004 — MUST
### STD-CONF-005 — MUST
### STD-CONF-006 — MUST
### STD-RELEASE-001 — MUST
### STD-RELEASE-002 — MUST
### STD-RELEASE-003 — MUST
### STD-RELEASE-004 — MUST
### STD-ADAPT-013 — MUST
### STD-ADAPT-014 — MUST
### STD-ADAPT-015 — MUST
### STD-VIEWPORT-001 — MUST
### STD-VIEWPORT-002 — MUST
### STD-VIEWPORT-003 — MUST
### STD-VIEWPORT-004 — MUST
### STD-VIEWPORT-005 — MUST
### STD-VIEWPORT-006 — MUST
### STD-VIEWPORT-007 — MUST
### STD-VIEWPORT-008 — MUST
### STD-SCREEN-001 — MUST
### STD-SCREEN-002 — MUST
### STD-SCREEN-003 — MUST
### STD-SCREEN-004 — MUST
### STD-NAV-010 — MUST
### STD-NAV-011 — MUST
### STD-A11Y-004 — MUST
### STD-FORM-005 — MUST
### STD-FORM-006 — MUST
### STD-HEADER-001 — Each screen has one authoritative header owner — MUST
### STD-HEADER-002 — Navigation title is not duplicated by equivalent page or section heading — MUST NOT
### STD-HEADER-003 — Sheet title subtitle and dismissal action form one coherent header hierarchy — MUST
### STD-CHROME-001 — App does not imitate platform-owned system chrome — MUST NOT
### STD-LOC-003 — Localization-ready architecture and stable semantic localization keys — MUST
### STD-LOC-004 — Locale-aware formatting and pluralization — MUST
### STD-LOC-005 — Optional in-app language selector supports Automatic/System mode — SHOULD
### STD-LOC-006 — Language switching does not migrate domain data or change stable raw IDs — MUST
### STD-LOC-007 — Localized search has feature parity across supported runtime languages — MUST
### STD-LOC-008 — Runtime languages are independent from App Store territory availability — MUST
### STD-RELEASE-005 — Current release root is clean and superseded build history is archived — MUST
### STD-DATA-005 — Single-device Xcode ↔ TestFlight/App Store ↔ Xcode data continuity — MUST
### STD-BACKEND-001 — Production backend schema/index/permission/config is explicitly ready — MUST
### STD-BACKEND-002 — Real TestFlight/Production read/write/sync/share smoke follows app capabilities — MUST
### STD-BACKEND-003 — Server-side fixes and binary fixes are explicitly distinguished — MUST
### STD-PERF-001 — Runtime performance is tested with representative real-volume data — MUST
### STD-ASYNC-001 — Stale async completion cannot overwrite newer state — MUST
### STD-DERIVED-001 — Authoritative mutation precedes one coherent derived-state rebuild — MUST
### STD-CLOUD-001 — Remote destructive/access success follows confirmed remote truth — MUST
### STD-CLOUD-002 — Security/access mutations have durable retry or reconciliation — MUST
### STD-DATA-006 — Corrupt persisted state fails safely without destructive empty overwrite — MUST
### STD-DATA-007 — Destructive deletion is relationship-aware — MUST
### STD-DATA-008 — Persisted-data app has production-to-candidate upgrade-path gate — MUST
### STD-TEST-001 — Material deterministic engines require automated regression coverage — MUST
### STD-PERM-001 — Disabled feature and permission exposure remain in parity — MUST
### STD-EVIDENCE-001 — Runtime evidence is build-scoped and regressions remain traceable — MUST
### STD-COMPACT-001 — Compact surfaces define content priority and destination integrity — SHOULD

## 6. Inherited 1.7.0 semantics

Všetky normatívne významy, semantic clarifications, layout/header/chrome kontrakty a runtime matrix z finálneho 1.7.0 zostávajú zdedené, pokiaľ ich 1.8.0 výslovne nerozširuje alebo nespresňuje. Machine-readable aplikovateľnosť všetkých 119 pravidiel je zachovaná v `CONFORMANCE_CATALOG.json`.

## 7. Release stav

`standard-v1.8.0` je stabilná autorita. Aplikácie majú pri najbližšom plánovanom release vykonať applicability audit voči 1.8.0 a osobitne zosúladiť biometrický fallback s `STD-SECURITY-001`.

## 8. Accepted next-minor work — 1.9.0 RC1

Táto sekcia je informatívna pre plánovaný next-minor scope a **nemení stabilnú autoritu 1.8.0 ani jej 119-rule katalóg**.

### STD-AUTH-SOURCE-001 — Authoritative source is available offline and externally traceable — planned MUST

Ak aplikácia používa právny, regulačný, normatívny alebo iný autoritatívny zdroj ako súčasť funkčného používateľského výsledku, použitý podklad musí byť dostupný aj bez internetového pripojenia, musí byť identifikovaný konkrétnou verziou/účinnosťou a musí byť spätne dohľadateľný na verifikačnú stopu. Pri právnom alebo obdobne normatívnom obsahu musí byť dostupná presná citácia alebo doslovné znenie použitého ustanovenia. Externý oficiálny web môže byť doplnkový odkaz, ale nesmie byť jediným spôsobom zobrazenia autoritatívneho podkladu.

Schválený návrh: `Proposals/IJAS-0033-authoritative-source-offline-citation-contract.md`.
