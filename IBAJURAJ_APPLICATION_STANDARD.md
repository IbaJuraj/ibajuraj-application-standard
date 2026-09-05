# IbaJuraj Application Standard

**Verzia:** 1.8.0 RC1  
**Stav:** Release Candidate  
**RC dátum:** 5. septembra 2026  
**Vlastník:** IbaJuraj  
**Aktuálna verejná autorita:** 1.7.0 (`standard-v1.7.0`)  
**Kandidát:** 1.8.0 RC1 (`standard-v1.8.0-rc1`)

> 1.8.0 RC1 je kompatibilné MINOR rozšírenie nad aktívnym Standardom 1.7.0. Zachováva všetkých 96 pravidiel 1.7.0 a pridáva nové spoločné kontrakty pre localization-first architektúru a prepínač jazyka, čistotu release balíkov, single-device Development/Production kontinuitu dát, pripravenosť produkčného backendu a performance test s reprezentatívnym objemom dát. RC1 nie je verejná autorita, kým nebude po adopcii povýšený na finálny 1.8.0.

## 1. Záväznosť
`MUST`/`MUST NOT` blokuje release bez platnej ADR výnimky. `SHOULD`/`SHOULD NOT` vyžaduje zdôvodnenie. `MAY` je voliteľné. `CONFORMANCE_CATALOG.json` je normatívny machine-readable register aplikovateľnosti a minimálneho typu dôkazu.

## 2. Piliere 1.8.0
1. Whole-App Adaptive Layout.
2. Viewport Edge Utilization.
3. Native/Custom Bottom Navigation Contract.
4. Screen-Family Audit.
5. Header & System-Chrome Ownership.
6. Machine-Verifiable Cross-App Conformance.
7. Localization-First Architecture & Language Selection.
8. Release Package Root Hygiene.
9. Single-Device Development/Release Data Continuity.
10. Production Backend Environment Readiness.
11. Representative-Data Runtime Performance.

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

### Header a system chrome ownership
- Každá obrazovka má jedného autoritatívneho vlastníka headeru. Systémový navigation title a druhý custom page title s rovnakou funkciou sa nekombinujú.
- Navigation title sa neopakuje ekvivalentným page/section headingom (`Kontakt` + `KONTAKT`, `O aplikácii` + `O APLIKÁCII`). Section header musí pomenovať užšiu semantickú skupinu obsahu.
- Sheet používa jednu koherentnú hierarchiu title/subtitle/dismissal action. Prázdny systémový navbar rezervovaný iba kvôli `X`/`Zrušiť` a druhý veľký custom title pod ním je defect.
- Aplikácia nekreslí vizuálnu imitáciu platform-owned chrome (napr. vlastný Home Indicator), ak daný systémový prvok poskytuje iOS.

### Bottom navigation
- Native variant necháva platforme výšku/safe area.
- Custom floating baseline: približne 60–66 pt surface, min. 44×44 pt touch target, typický 50 pt primary action, radius približne 28 pt; hodnoty sú baseline, nie rigidný frame.
- Centrálna akcia nesmie zbytočne nafúknuť celý bar. Custom bar môže bezpečne penetrovať bottom safe area pri ochrane Home Indicatora.

### Localization-first architektúra
- Nová aplikácia je localization-ready od prvého produkčného buildu, aj keď má iba jeden jazyk.
- User-facing text patrí do String Catalogu/Localizable zdrojov alebo ekvivalentnej lokalizačnej vrstvy; business a persistence logika nesmie závisieť od konkrétneho používateľského prekladu.
- Lokalizačné kľúče majú byť stabilné, jazykovo neutrálne a semantické.
- Dátumy, čísla, meny, percentá a pluralizácia používajú aktívny locale alebo explicitný doménový locale; všeobecné UI nesmie byť pevne viazané na `sk_SK`.
- Podporované runtime jazyky a App Store storefront/territory availability sú nezávislé rozhodnutia.

### In-app language selector
- Vlastný prepínač jazyka je `MAY`; používa sa, ak prináša reálnu produktovú/testovaciu hodnotu.
- Ak existuje, musí obsahovať **Automaticky / Podľa systému** a všetky runtime podporované jazyky.
- Výber sa perzistuje; návrat na Automaticky znovu rešpektuje iOS/per-app jazyk.
- Prepnutie jazyka nesmie migrovať, meniť ani prepisovať doménové dáta.
- Ak aplikácia nevie bezpečne prepnúť celý runtime okamžite, musí mať deterministické relaunch správanie a používateľsky zrozumiteľnú informáciu.

### Locale-neutral persistence
- Raw enum values, AppStorage/UserDefaults keys, databázové identifikátory, stabilné UUID, CloudKit record/share identity, transportné kľúče, deep-link identity a barcode/QR payloady sa neprekladajú iba kvôli zmene UI jazyka.
- Lokalizuje sa prezentačná vrstva; doménová identita zostáva stabilná.

### Localized search parity
- Ak aplikácia podporuje vyhľadávanie, nová lokalizácia zahŕňa používateľské názvy, relevantné synonymá/aliasy a locale-sensitive normalizáciu tam, kde je to potrebné.
- Lokalizované UI bez funkčného vyhľadávania v danom jazyku nie je plná localization parity.

### Release package root hygiene
- Root aktuálneho source/release balíka obsahuje iba aktuálne autoritatívne projektové súbory a malú sadu aktuálnych build/release dokumentov.
- Supersedované `BUILD_*`, runtime acceptance a podobné checkpointy sa archivujú alebo konsolidujú; nesmú sa neobmedzene hromadiť v root priečinku.
- Historický dôkaz o významnej regresii, migrácii alebo release rozhodnutí sa nesmie potichu zmazať; archivuje sa alebo sa jeho podstatný obsah prenesie do changelogu.

### Single-device Development/Release data continuity
- Aplikácia s persistentnými dátami a environment-specific backendom musí zachovať stabilnú lokálnu doménovú identitu pri striedaní Xcode ↔ TestFlight/App Store ↔ Xcode na tom istom zariadení, pokiaľ používateľ aplikáciu/dáta výslovne nevymaže.
- Development a Production record/share/token identity nie sú zameniteľné a nesmú byť jedinou identitou doménového objektu.
- Chýbajúca remote reprezentácia v aktuálnom prostredí nesmie sama o sebe zmazať, duplikovať alebo resetovať lokálny objekt.
- Cloud/backend väzba pre aktuálne prostredie musí byť recreatable/rebindable bez opätovného zadávania doménových dát.

### Production backend environment readiness
- Pred distribuovaným release musí byť overené, že Production prostredie obsahuje požadovanú schému, indexy, permissions/security roles, konfiguráciu a ďalšie server-side prerequisites, ktoré Development build automaticky nevytvára v Production.
- TestFlight/Production smoke má overiť reálny read/write/sync/share path podľa capability aplikácie.
- Backendová chyba nesmie zničiť bezpečne zachované lokálne dáta; UI má rozlíšiť lokálny stav od cloudového/produkčného zlyhania.
- Serverová/schema oprava sa nemá automaticky zamieňať za potrebu nového binárneho buildu; release evidence má zaznamenať, čo sa zmenilo na serveri a čo v binárke.

### Representative-data performance
- Runtime performance gate pre aplikáciu s persistentnými dátami používa reprezentatívny reálny objem dát, nie iba empty/small fixture.
- Smoke test má zahŕňať aspoň kritické scroll/search/filter/sort/root-switch flow, ktoré sa s rastúcim objemom dát môžu zhoršovať.
- Konkrétny počet položiek je produktový; musí však zodpovedať reálnemu alebo realistickému high-volume použitiu.

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
### STD-HEADER-001 — Each screen has one authoritative header owner — MUST
### STD-HEADER-002 — Navigation title is not duplicated by equivalent page or section heading — MUST NOT
### STD-HEADER-003 — Sheet title subtitle and dismissal action form one coherent header hierarchy — MUST
### STD-CHROME-001 — App does not imitate platform-owned system chrome — MUST NOT

### STD-LOC-003 — Localization-ready architecture uses stable semantic localization keys — MUST
### STD-LOC-004 — Locale-aware formatting and pluralization follow the active locale — MUST
### STD-LOC-005 — In-app language selector includes Automatic/System mode and all runtime-supported languages — MUST
### STD-LOC-006 — Persisted identifiers and transport keys remain locale-neutral — MUST
### STD-LOC-007 — Localized search terms and aliases provide language parity — MUST
### STD-LOC-008 — Runtime language support and App Store storefront availability are independent — MUST
### STD-RELEASE-005 — Current package root excludes superseded build-specific documentation — MUST
### STD-RELEASE-006 — Historical release and regression evidence is archived or consolidated, not silently deleted — MUST
### STD-DATA-005 — Stable local domain identity survives Development/Production environment changes — MUST
### STD-BACKEND-001 — Production backend schema configuration and permissions are verified before distribution — MUST
### STD-BACKEND-002 — Production/TestFlight smoke proves real backend paths and local-safe failure behavior — MUST
### STD-PERF-001 — Runtime performance gate uses representative real-volume data — MUST

## 5. 1.8.0 RC1 semantic clarifications
- **STD-LOC-003:** source language môže byť slovenčina; požiadavka je na stabilnú localization layer a semantic identity, nie na anglický UI text.
- **STD-LOC-004:** explicitný pevný locale je prípustný, ak je súčasťou doménovej/právnej definície; nesmie byť nevedomým defaultom celého UI.
- **STD-LOC-005:** vlastný selector nie je povinný. Ak existuje, musí ponúknuť systémový režim a všetky runtime jazyky; prepnutie nesmie meniť dáta.
- **STD-LOC-006:** display label a raw value sú rozdielne vrstvy. Lokalizácia nesmie meniť raw enum, UUID, database key, CloudKit identity ani transportný payload iba kvôli UI jazyku.
- **STD-LOC-007:** search parity znamená funkčné používateľské vyhľadávanie v každom deklarovanom runtime jazyku, nie absolútnu identickosť každej synonymickej frázy.
- **STD-LOC-008:** App Store product-page localization a runtime localization sú samostatné release povrchy.
- **STD-RELEASE-005/006:** história sa od aktívneho rootu oddeľuje, nie bez stopy maže.
- **STD-DATA-005:** povinný single-device test preferuje ten istý app build v Xcode a TestFlight, ak je to prakticky možné, aby sa oddelil environment switch od verziovej migrácie.
- **STD-BACKEND-001:** pri CloudKit patrí do parity najmä Production record types, indexy a security roles; pri inom backende ekvivalentné server-side prerequisites.
- **STD-BACKEND-002:** ak serverová oprava sama vyrieši TestFlight flow, nový binárny build nie je automaticky potrebný; dôkaz však musí zachytiť presnú server-side zmenu.
- **STD-PERF-001:** konkrétny počet položiek nie je normatívny. Ak 32 reálnych položiek reprezentuje produkčné použitie aplikácie, test môže používať 32; iný produkt môže potrebovať výrazne viac alebo menej.

Zachované 1.7.0 clarifications zostávajú v platnosti:
- **STD-ADAPT-004/013:** bezpečne využiteľný voľný priestor sa má primerane využiť bez narušenia hierarchie.
- **STD-ADAPT-015:** zakázané je adaptívne riešenie, ktoré spôsobuje zbytočné opakované merania, invalidácie alebo lagovanie.
- **STD-VIEWPORT-001/008:** root title/header sa viaže na aktuálnu top safe area + shared minimal inset, nie na absolútne Y zariadenia.
- **STD-VIEWPORT-003/STD-NAV-010:** custom bottom chrome môže vstúpiť do bottom safe area, ak Home Indicator nekoliduje s obsahom ani 44×44 touch targetom.
- **STD-VIEWPORT-004/STD-NAV-011:** fyzická poloha bottom chrome a scroll content clearance sa počítajú samostatne.
- **STD-VIEWPORT-006:** nevysvetlený hardcoded edge padding/spacer, ktorý iba znižuje užitočný viewport, je defect.
- **STD-FORM-006:** keyboard a fixed/custom bottom chrome nesmú vytvoriť overlap ani dvojitú rezervu.
- **STD-CONF-005:** grep/parser/manifest dôkaz nenahrádza UI/runtime dôkaz behaviorálneho pravidla.
- **STD-HEADER-001:** jedna screen family môže používať native alebo custom header, nie dve paralelné vrstvy s rovnakou rolou.
- **STD-HEADER-002:** section heading je prípustný iba ak zužuje význam; opakovanie názvu obrazovky v inom case/icon štýle je defect.
- **STD-HEADER-003:** sheet musí mať jeden vizuálny top anchor; dismissal action nesmie sama vytvoriť prázdny navigation band nad druhým title.
- **STD-CHROME-001:** platform-owned affordance sa nesmie imitovať dekoratívnou kópiou; ak aplikácia potrebuje vlastný drag handle, musí mať vlastnú funkciu a nesmie predstierať Home Indicator.

## 6. Minimálna runtime matrix 1.8.0 RC1
Small/regular/large iPhone container; Accessibility Dynamic Type; Light/Dark; každý podporovaný runtime jazyk alebo reprezentatívny full-language pass + longest strings; keyboard/form state; scroll endpoint nad bottom chrome; iPad portrait/landscape/window sizes, ak je podporovaný; iPad compatibility pre kritický flow, ak relevantné.

Navyše podľa capability:
- **in-app language selector:** Automatic/System → každý podporovaný jazyk → Automatic/System; relaunch; bez straty alebo migrácie dát,
- **localized search:** reprezentatívny dotaz/alias v každom runtime jazyku,
- **environment-specific backend:** Xcode/Development → TestFlight/Production → Xcode/Development na jednom zariadení, ideálne s rovnakým buildom; real Production sync/share/read/write smoke,
- **persistent data:** reprezentatívny real-volume dataset a scroll/search/filter/sort smoke,
- **release package:** root-hygiene audit + archivácia supersedovaných build evidence.

## 7. Adopcia a promotion gate
1.8.0 RC1 môže byť použitý na implementačnú/adopčnú prácu, ale aktívna verejná autorita zostáva 1.7.0.

Primárna adopcia RC1:
1. **Peňaženka Kariet** — localization selector, 6-jazykový runtime, Production CloudKit parity, single-device continuity a 32-card performance evidence.
2. **Strážca Termínov** — single-device data continuity, Production CloudKit/membership readiness, root hygiene a localization closure.
3. Následný reprezentatívny audit Lex Drive/Kalkulačka podľa aplikovateľných nových pravidiel.

Promotion na finálny **1.8.0** vyžaduje:
- Standard repository validator PASS,
- aspoň jednu reálnu adopciu dokazujúcu nové conformance pravidlá,
- vyriešenie známych RC1 ambiguít,
- žiadny známy cross-app blocker vyžadujúci RC2,
- aktualizáciu candidate metadata na `active`, finálny tag `standard-v1.8.0` a finálny release audit.
