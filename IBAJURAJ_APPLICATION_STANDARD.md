# IbaJuraj Application Standard

**Verzia:** 1.7.0  
**Stav:** Release Candidate 2  
**Dátum RC2:** 29. augusta 2026  
**Vlastník:** IbaJuraj  
**Aktuálna verejná autorita:** 1.6.4 (`standard-v1.6.4`, commit `5e2901945287165a8902f28fb1d3b5a87b6eeb92`)

> RC2 nahrádza RC1 pre ďalšiu adopciu. Kým nebude vydaný finálny tag `standard-v1.7.0`, stabilnou verejnou verziou zostáva 1.6.4.

## 1. Záväznosť
`MUST`/`MUST NOT` blokuje release bez platnej ADR výnimky. `SHOULD`/`SHOULD NOT` vyžaduje zdôvodnenie. `MAY` je voliteľné. `CONFORMANCE_CATALOG.json` je normatívny machine-readable register aplikovateľnosti a minimálneho typu dôkazu.

## 2. Piliere RC2
1. Whole-App Adaptive Layout.
2. Viewport Edge Utilization.
3. Native/Custom Bottom Navigation Contract.
4. Screen-Family Audit.
5. Machine-Verifiable Cross-App Conformance.

## 3. Kľúčové spoločné kontrakty

### O aplikácii
- Settings: **O aplikácii** + **Verzia, súkromie a štandard** + runtime `<version> (<build>)`.
- Version card: `<AppName> v<version> – Build <build>.` z autoritatívnych runtime metadata.
- Standard card: iba `IbaJuraj Application Standard` + `Verzia <standardVersion>`; interný tag/SHA/adoption level sa používateľovi nezobrazujú.
- Vývojár: `IbaJuraj Apps.`; web/privacy používajú spoločné odkazy.

### Appearance
- Bezpečne aplikovateľná téma sa prejaví okamžite na aktuálnej obrazovke: checkmark, selected state a surface/background v tom istom render cykle.
- Uložená hodnota a vykreslený stav musia zostať v parite po návrate/relaunchi.

### Adaptivita a viewport
- Každá user-facing obrazovka je adaptive by default a primárne container-driven; device-name/`UIScreen.main.bounds` branching nie je layout foundation, ak existuje reálna container geometry.
- Primary root header sa kotví čo najvyššie po top safe area; baseline extra inset je **0–4 pt**. Peer roots používajú rovnaký safe-area-relative anchor.
- Fixed/custom bottom chrome ide na najnižšiu bezpečnú pozíciu; celý bottom safe-area inset sa automaticky nemení na prázdny pás.
- **Bar position a scroll content clearance sú nezávislé.** Posledný obsah musí ísť celý nad chrome; typická koncová rezerva je 16–24 pt.
- Horizontal space sa využíva adaptívne. Veľký displej nemá znamenať iba viac prázdna; malé množstvo obsahu však môže prirodzene nechať prázdnu plochu.
- Adaptívny layout nesmie spôsobovať layout thrashing ani viditeľné lagovanie.

### Bottom navigation
- Native variant necháva platforme výšku/safe area.
- Custom floating baseline: približne 60–66 pt surface, min. 44×44 pt touch target, typický 50 pt primary action, radius približne 28 pt; hodnoty sú baseline, nie rigidný frame.
- Centrálna akcia nesmie zbytočne nafúknuť celý bar. Custom bar môže bezpečne penetrovať bottom safe area pri ochrane Home Indicatora.

### Screen-family audit
`STANDARD_CONFORMANCE.json` deklaruje konkrétne obrazovky v relevantných family: `SCREEN-ROOT`, `SCREEN-SETTINGS`, `SCREEN-ABOUT`, `SCREEN-DETAIL`, `SCREEN-FORM`, `SCREEN-SEARCH`, `SCREEN-SHEET`, `SCREEN-FULLSCREEN`, `SCREEN-ONBOARDING`, `SCREEN-STATES`, `SCREEN-BOTTOM-NAV`. Každá family má `pass/pending/exception`; `pass` potrebuje evidence, `exception` existujúci ADR a `pending` blokuje Level 4.

### Conformance
Static PASS nie je runtime PASS. Každé aplikovateľné MUST/MUST NOT potrebuje static/unit/UI/runtime evidence alebo platnú ADR exception. Level 4 vyžaduje nulové release-blocking pending pravidlá aj nulové pending screen families.

## 4. Normatívny register pravidiel
Každé ID nižšie je záväzné podľa úrovne uvedenej v nadpise; presná aplikovateľnosť a verification mode sú v `CONFORMANCE_CATALOG.json`.


### STD-IDENTITY-001 — One runtime source for marketing version and build — MUST

### STD-IDENTITY-002 — IbaJuraj Apps identity and shared links — MUST

### STD-IDENTITY-003 — App and Standard metadata are separate — MUST

### STD-COMPONENT-001 — Shared role uses shared geometry — MUST

### STD-COMPONENT-002 — No unexplained local geometry drift — MUST NOT

### STD-COMPONENT-003 — Semantic exceptions are documented — MUST

### STD-COMPONENT-004 — Minimum 44x44 touch target — MUST

### STD-COMPONENT-005 — Meaningful text fits without scale-factor rescue — MUST

### STD-SETTINGS-001 — Direct Settings entry on primary roots — MUST

### STD-SETTINGS-002 — Shared appearance control meaning — MUST

### STD-APPEARANCE-001 — Theme applies immediately on same screen — MUST

### STD-APPEARANCE-002 — Checkmark/model/render state parity — MUST

### STD-APPEARANCE-003 — Theme selection persists — MUST

### STD-ABOUT-001 — Settings About row contract — MUST

### STD-ABOUT-002 — About version sentence contract — MUST

### STD-ABOUT-003 — Public Standard version only — MUST

### STD-ABOUT-004 — Developer card contract — MUST

### STD-ABOUT-005 — Web and privacy links — MUST

### STD-ABOUT-006 — Shared About test identifiers — MUST

### STD-ADAPT-001 — Whole app adaptive by default — MUST

### STD-ADAPT-002 — Container-driven layout foundation — MUST

### STD-ADAPT-003 — Safe-area-driven positioning — MUST

### STD-ADAPT-004 — Use available space when beneficial — MUST

### STD-ADAPT-005 — Stable semantic content anchors — MUST

### STD-ADAPT-006 — Dynamic Type adaptive layout — MUST

### STD-ADAPT-007 — Longest-localization stress test — MUST

### STD-ADAPT-008 — Fixed tokens not fixed device layout — MUST

### STD-ADAPT-009 — Window/orientation adaptation — MUST

### STD-ADAPT-010 — iPad/compatibility runtime matrix — MUST

### STD-ADAPT-011 — No device-name branching as layout foundation — MUST NOT

### STD-ADAPT-012 — Adaptive calculator keypad — MUST

### STD-NAV-001 — Bottom navigation mode declared — MUST

### STD-NAV-002 — Native tab variant — MUST

### STD-NAV-003 — Custom baseline geometry — MUST

### STD-NAV-004 — Primary action does not inflate bar — MUST

### STD-NAV-005 — Adaptive custom bar width — MUST

### STD-NAV-006 — Custom bar safe area — MUST

### STD-NAV-007 — Bottom content clearance — MUST

### STD-NAV-008 — Custom bar Dynamic Type — MUST

### STD-NAV-009 — Custom bar test identifiers — MUST

### STD-NESTED-NAV-001 — Back and native swipe where applicable — MUST

### STD-NESTED-NAV-002 — No navigation loops/dead ends — MUST

### STD-LOC-001 — Localization parity — MUST

### STD-LOC-002 — Single shared localization meaning — MUST

### STD-A11Y-001 — VoiceOver semantics — MUST

### STD-A11Y-002 — No color-only meaning — MUST

### STD-A11Y-003 — Reduce Motion/Increase Contrast — MUST

### STD-FORM-001 — Required/optional fields — MUST

### STD-FORM-002 — Validation timing — MUST

### STD-FORM-003 — Progressive disclosure — MUST

### STD-FORM-004 — Keyboard dismissal — MUST

### STD-DATA-001 — Single source of truth — MUST

### STD-DATA-002 — Schema/migration coverage — MUST

### STD-DATA-003 — Sync/local/backup/export semantics — MUST

### STD-DATA-004 — Traceability of authoritative data — MUST

### STD-PRIVACY-001 — Privacy manifest coverage — MUST

### STD-PRIVACY-002 — Privacy policy/App Store parity review — MUST

### STD-SECURITY-001 — Security state machine — MUST

### STD-DEBUG-001 — Production isolation of debug/mock controls — MUST

### STD-DEBUG-002 — Runtime defect regression evidence — MUST

### STD-AI-001 — Grounded verified generated assistance — MUST

### STD-AI-002 — Safe low-confidence fallback — MUST

### STD-CONF-001 — STANDARD_CONFORMANCE.json exists — MUST

### STD-CONF-002 — Every applicable MUST has evidence — MUST

### STD-CONF-003 — Common validator passes — MUST

### STD-CONF-004 — Shared UI test identifiers — MUST

### STD-CONF-005 — Static PASS not substituted for runtime proof — MUST

### STD-CONF-006 — Release conformance report — MUST

### STD-RELEASE-001 — Source hygiene — MUST

### STD-RELEASE-002 — Localization gate — MUST

### STD-RELEASE-003 — Whole-family regression scope — MUST

### STD-RELEASE-004 — Native build/runtime gate distinction — MUST

### STD-ADAPT-013 — Adaptive density uses useful available space — MUST

### STD-ADAPT-014 — System geometry remains stable across data states — MUST

### STD-ADAPT-015 — Adaptive layout avoids layout thrashing and unnecessary invalidation — MUST

### STD-VIEWPORT-001 — Primary root header starts at safe-area plus shared minimal inset — MUST

### STD-VIEWPORT-002 — Root nested sheet and fullscreen header families are explicit — MUST

### STD-VIEWPORT-003 — Fixed/custom bottom chrome uses lowest safe viewport position — MUST

### STD-VIEWPORT-004 — Bottom chrome position and content clearance are independent — MUST

### STD-VIEWPORT-005 — Horizontal viewport is adaptively utilized — MUST

### STD-VIEWPORT-006 — No unexplained fixed edge waste — MUST

### STD-VIEWPORT-007 — Layout responds to live system safe-area changes — MUST

### STD-VIEWPORT-008 — Peer primary roots share safe-area-relative top anchor — MUST

### STD-SCREEN-001 — Screen-family inventory is declared — MUST

### STD-SCREEN-002 — Every applicable screen family has completed audit state — MUST

### STD-SCREEN-003 — Each screen family passes viewport audit dimensions — MUST

### STD-SCREEN-004 — Shared screen chrome exposes stable test identifiers — MUST

### STD-NAV-010 — Custom bar may safely penetrate bottom safe area instead of reserving blank band — MUST

### STD-NAV-011 — Custom bar position and scroll clearance are independently calculated — MUST

### STD-A11Y-004 — Reduce Transparency has readable fallback — MUST

### STD-FORM-005 — Keyboard keeps active field and required action reachable — MUST

### STD-FORM-006 — Keyboard and bottom chrome do not create overlap or double clearance — MUST


## 5. RC2 semantic clarifications
- **STD-ADAPT-004/013:** bezpečne využiteľný voľný priestor sa má primerane využiť bez narušenia hierarchie.
- **STD-ADAPT-015:** zakázané je adaptívne riešenie, ktoré spôsobuje zbytočné opakované merania, invalidácie alebo lagovanie.
- **STD-VIEWPORT-001/008:** root title/header sa viaže na aktuálnu top safe area + shared minimal inset, nie na absolútne Y zariadenia.
- **STD-VIEWPORT-003/STD-NAV-010:** custom bottom chrome môže vstúpiť do bottom safe area, ak Home Indicator nekoliduje s obsahom ani 44×44 touch targetom.
- **STD-VIEWPORT-004/STD-NAV-011:** fyzická poloha bottom chrome a scroll content clearance sa počítajú samostatne.
- **STD-VIEWPORT-006:** nevysvetlený hardcoded edge padding/spacer, ktorý iba znižuje užitočný viewport, je defect.
- **STD-FORM-006:** keyboard a fixed/custom bottom chrome nesmú vytvoriť overlap ani dvojitú rezervu.
- **STD-CONF-005:** grep/parser/manifest dôkaz nenahrádza UI/runtime dôkaz behaviorálneho pravidla.

## 6. Minimálna runtime matrix
Small/regular/large iPhone container; Accessibility Dynamic Type; Light/Dark; najdlhšia podporovaná lokalizácia; keyboard/form state; scroll endpoint nad bottom chrome; iPad portrait/landscape/window sizes, ak je podporovaný; iPad compatibility pre kritický flow, ak relevantné.

## 7. Adopcia
RC2 nahrádza RC1 pre ďalšiu adopciu. Poradie je v `ADOPTION_PLAN_RC2.md`. Po úspešnom cross-app audite sa odstráni RC marker, `standard.json.status` sa nastaví na `active`, doplní sa release date a vydá sa tag `standard-v1.7.0`.
