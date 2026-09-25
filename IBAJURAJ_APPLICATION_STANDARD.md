# IbaJuraj Application Standard

**Verzia:** 1.9.0 RC2  
**Stav:** Candidate / RC  
**Dátum vydania:** 25. septembra 2026  
**Vlastník:** IbaJuraj  
**Stable verejná autorita:** 1.8.0 (`standard-v1.8.0`)  
**Candidate vetva:** `standard-1.9.0-rc2`

> Verzia 1.9.0 RC2 je kandidát na ďalšiu minor verziu. Stabilnou autoritou zostáva 1.8.0. RC2 zachováva všetkých 121 pravidiel RC1 a pridáva Release Candidate Quality Gate, interný Full App Check, release-diff/risk audit, release visual matrix, riadenú AI review vrstvu, evidence bundle a post-release feedback loop. Kandidátsky katalóg má 131 pravidiel.

## 1. Záväznosť

`MUST`/`MUST NOT` blokuje release bez platnej ADR výnimky. `SHOULD` vyžaduje zdôvodnenie. Static PASS nenahrádza runtime PASS.

Candidate pravidlá sa používajú na adopciu a validáciu, kým nie je príslušná minor verzia promovovaná na stable.

## 2. Integrácia 1.9 RC2

1.9.0 RC2 má **131 pravidiel**:
- 119 pravidiel zdedených zo stabilnej 1.8.0 bez zmeny ich významu,
- 2 pravidlá pridané v RC1: `STD-ASYNC-002` a `STD-AUTH-SOURCE-001`,
- 10 nových pravidiel RC2 pre Release Candidate Quality Gate a Intelligent Self-Audit.

Plný whole-app audit sa **nevyžaduje po každom malom vývojovom builde**. Je povinný pri builde explicitne nominovanom ako Release Candidate pre App Store/store/produkčné nasadenie.

Referenčná implementačná architektúra sa nazýva **IbaJuraj Release Inspector / Quality Engine**. Názov ani zdieľanie kódu nie sú normatívne; normatívne sú správanie, rozsah, dôkazy a release gate.

RC2 zachováva root-title family clarification z RC1 bez nového rule ID.

## 3. Async remote contract

### STD-ASYNC-002 — Remote invite/share/access responsiveness — MUST

Ak aplikácia vykonáva vzdialené invite/share/access operácie, ktoré môžu čakať na sieť alebo backend, tieto operácie NESMÚ blokovať interaktívnu odozvu UI/MainActor.

Platí najmä:

- remote orchestration má bežať na dedikovanom actor/executor alebo ekvivalentnej non-UI izolácii,
- otvorenie invite/access obrazovky NESMIE čakať na dokončenie remote prípravy,
- dlhšie operácie MUSIA mať viditeľný progress stav (`Pripravujem…`, `Ruším…` alebo ekvivalent),
- zvyšok obrazovky má zostať interaktívny, pokiaľ tomu nebráni bezpečnostná alebo dátová konzistencia,
- retry a reconciliation MUSIA prebiehať asynchrónne,
- úspech remote destructive/access mutácie sa naďalej smie prezentovať až po potvrdenej remote truth podľa `STD-CLOUD-001`,
- dočasné zlyhania musia zachovať retry/reconciliation podľa `STD-CLOUD-002`,
- runtime audit musí zahŕňať create/publish, cancel/revoke a retry/reconcile flow, ak ich aplikácia podporuje.

Referenčný dôvod zavedenia: runtime audit Strážca Termínov Build 120 Phase 14A R12, kde CloudKit invite/cancel flow vykazoval približne 10-sekundový UI lag pri orchestration izolovanej na `MainActor`.

Schválený návrh: `Proposals/IJAS-0034-async-remote-invite-responsiveness.md`.

## 4. Authoritative source contract

### STD-AUTH-SOURCE-001 — Authoritative functional source is available offline and externally traceable — MUST

Ak aplikácia používa právny, regulačný, normatívny alebo iný autoritatívny zdroj ako súčasť funkčného používateľského výsledku:

- MUSÍ lokálne sprístupniť použitú reprezentáciu zdroja bez závislosti od internetového pripojenia,
- MUSÍ jasne identifikovať zdroj a konkrétnu použitú časovú/verznú identitu,
- MUSÍ pri právnom alebo obdobne normatívnom obsahu sprístupniť presnú citáciu alebo doslovné znenie ustanovenia, z ktorého výsledok vychádza,
- MUSÍ uviesť účinnosť alebo verziu použitú pri výsledku, ak sa zdroj v čase mení,
- MUSÍ uchovať alebo sprístupniť dátum/verifikačnú stopu overenia, ak aplikácia používa verifikovaný obsah,
- externý oficiálny zdroj MÔŽE byť dostupný ako doplnkový odkaz, ale NESMIE byť jediným spôsobom zobrazenia autoritatívneho podkladu,
- používateľský názov, skrátený opis alebo praktické vysvetlenie NESMIE nahradiť identifikáciu autoritatívneho podkladu.

Konkrétna informačná hierarchia, názvy právnych rolí a vizuálna navigácia zostávajú produktové. Referenčným príkladom je Lex Drive Build 232, kde právny reťazec priestupku musí zostať dohľadateľný na presnú lokálnu/offline citáciu aj bez prístupu na Slov-Lex.

Schválený návrh: `Proposals/IJAS-0033-authoritative-source-offline-citation-contract.md`.

## 5. Release Candidate Quality Gate & Intelligent Self-Audit

### STD-RELEASE-006 — Release Candidate Quality Gate cadence — MUST
Kompletný whole-app release audit MUSÍ prebehnúť na builde explicitne nominovanom na App Store/store/produkčné odoslanie. Bežné vývojové buildy nepotrebujú celý release audit; postačuje Build/Test a cielená regresia zmenených alebo rizikových oblastí. Materiálna zmena po uzavretí RC gate zneplatňuje release evidence predchádzajúceho buildu a nový RC MUSÍ gate zopakovať.

### STD-DIAG-001 — Internal Full App Check — MUST
Každá aplikácia MUSÍ mať interný/developer-only Full App Check spustiteľný na presnom RC builde. Kontrola MUSÍ byť nedestruktívna voči reálnym používateľským dátam a podľa applicability preveriť inicializáciu, persisted-data integrity, migrácie, navigation/destination registry, lokalizačnú integritu, výpočty/business rules, sync/API, deep links a cache/configuration. Write-path testy používajú izolované alebo syntetické fixtures, prípadne reverzibilný testovací kontext. Diagnostický vstup NESMIE byť bežnou produkčnou používateľskou funkciou, pokiaľ produkt výslovne neponúka bezpečnú diagnostiku.

### STD-DIAG-002 — Structured diagnostic findings and severity — MUST
Každý nález MUSÍ mať stabilné ID, dotknutý komponent, očakávaný a pozorovaný stav, dôkaz alebo reprodukčný kontext, vysvetlenie a severity: **BLOCKER / ERROR / WARNING / INFO**. BLOCKER a ERROR blokujú release bez platnej výnimky/ADR. WARNING vyžaduje review. INFO je neblokujúce. Known exceptions MUSIA zostať explicitné a dohľadateľné.

### STD-RELEASE-007 — Release diff and risk-based coverage — MUST
RC audit MUSÍ porovnať kandidáta s posledným reálne publikovaným produkčným/App Store baseline a identifikovať zmeny zdrojového kódu, dátového modelu/schémy, migrácií, konfigurácie, dependencies, UI, lokalizácií a feature flags podľa applicability. High-risk zmeny dostávajú rozšírené testovanie.

### STD-TEST-002 — Critical user journeys and resilience scenarios — MUST
RC gate MUSÍ preverovať reprezentatívne end-to-end používateľské scenáre, nie iba izolované obrazovky. Podľa capabilities zahŕňa reštart/persistenciu a relevantné failure scenáre: offline stav, timeout, zamietnuté oprávnenie, prerušený import/zápis, poškodený vstup, sync failure/conflict a upgrade zo staršieho persisted stavu.

### STD-UI-001 — Release visual/runtime matrix — MUST
Zmenené a high-risk používateľské surfaces MUSIA byť overené na reprezentatívnych device/viewport triedach a podľa applicability v Light/Dark, relevantnom Dynamic Type a podporovaných lokalizáciách. Screenshot/image-diff automatizácia MÔŽE pomáhať, ale nejednoznačný vizuálny nález vyžaduje ľudské review.

### STD-AI-003 — AI release review is advisory, explainable and non-autonomous — MUST
Ak RC audit používa AI, každý AI nález MUSÍ uviesť dôvod, podporný kontext/dôkaz a confidence. AI MÔŽE prioritizovať, vysvetľovať a navrhovať opravu, ale NESMIE potichu meniť produkčné dáta, obsah ani kód a NESMIE byť jediným základom finálneho release PASS/FAIL. AI-only blocking finding vyžaduje deterministické potvrdenie alebo explicitné ľudské potvrdenie.

### STD-AI-004 — AI release review uses data minimization — MUST
AI review MUSÍ používať syntetické, anonymizované alebo minimalizované dáta ako predvolený režim. Secrets, credentials, authentication tokens a ekvivalentný citlivý materiál sa AI NESMÚ odosielať. Logy, screenshoty a importované datasety sa pred AI analýzou MUSIA sanitizovať, ak môžu obsahovať súkromné používateľské údaje.

### STD-EVIDENCE-002 — RC Evidence Bundle and release baseline — MUST
Každý RC gate MUSÍ vytvoriť exportovateľný Evidence Bundle naviazaný na presnú app version/build a Standard candidate. Bundle obsahuje najmenej súhrn kontrol, findings, exceptions, release diff/risk scope, runtime/UI evidence a AI review summary, ak bola AI použitá. Build reálne publikovaný do produkcie/App Store sa stáva ďalším release baseline.

### STD-POSTRELEASE-001 — Production feedback loop — MUST
Ak aplikácia podporuje post-release monitoring, privacy-respecting crash/error/performance signály MUSIA byť po release vyhodnotené a významné regresie MUSIA vstúpiť do ďalšieho release baseline a test scope.

### Release Inspector modes
- **Development Check** — Build/Test + cielené kontroly; bez povinného celého auditu po každom malom builde.
- **Full App Check** — interný in-app diagnostický sweep.
- **Release Check** — plný RC gate: deterministic + app-specific + user journeys + visual/runtime + release diff + evidence + optional AI review.
- **Post-Release Monitoring** — produkčný feedback loop tam, kde je podporovaný.

Release Check môže byť PASS iba ak sú povinné deterministic/runtime gates PASS, nezostáva unresolved BLOCKER/ERROR bez platnej výnimky, WARNING findings sú reviewnuté, AI findings nie sú použité ako autonómny dôkaz a Evidence Bundle je kompletný.

Schválený návrh: `Proposals/IJAS-0035-release-candidate-quality-gate-intelligent-self-audit.md`.

## 6. Root-title adaptive family clarification

Peer root obrazovky používajú jednu spoločnú root-title family. Výsledná veľkosť title tokenu MUSÍ vychádzať z reálne dostupnej šírky viewport-u alebo kontajnera, nie z názvu konkrétneho zariadenia. Na tom istom viewport-e MUSIA peer root titles používať rovnaký výsledný size token. Adaptácia MÁ preferovať celý názov bez `…` pomocou breakpointov, clamped veľkosti, tightening alebo primeraného scale fallbacku.

Nested/system navigation headers tvoria samostatnú family. Referenčné hodnoty 28 / 30 / 32 pt v `DESIGN_TOKENS.md` sú príklad implementácie, nie cross-app povinné čísla.

## 7. Zdedené 1.8 kontrakty

1.8.0 zostáva stabilnou autoritou pre localization-first architektúru, release-root hygiene, data continuity, Production backend readiness, runtime performance, async stale-callback safety, derived-state ordering, remote truth/reconciliation, corrupt-state recovery, relationship-aware deletion, upgrade-path gate, permission parity, runtime evidence, compact-surface integrity a biometrickú bezpečnostnú semantiku.

### Biometrické odomykanie – záväzná semantika `STD-SECURITY-001`

Ak aplikácia ponúka lokálny zámok a biometriu (Face ID, Touch ID, Optic ID alebo ekvivalent), platí jednotný model IbaJuraj Apps:

- biometria je primárny spôsob odomknutia,
- pri nedostupnosti, lockoute alebo zlyhaní biometrie MUSÍ byť dostupné systémové overenie vlastníka zariadenia pomocou kódu/hesla zariadenia,
- samostatný PIN aplikácie NESMIE byť povinnou podmienkou zapnutia biometrie,
- app PIN MÔŽE existovať iba ako voliteľná doplnková ochrana, ak má produktový význam,
- PIN aplikácie, ak existuje, MUSÍ byť uložený bezpečne (Keychain alebo ekvivalent), nikdy v čitateľnom tvare,
- zámok sa NESMIE znovu aktivovať pri bežnej internej navigácii; viaže sa na skutočný lifecycle prechod aplikácie,
- opakované biometrické dialógy počas už prebiehajúcej autentifikácie sa MUSIA blokovať.

## 8. Normatívny register

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
### STD-AUTH-SOURCE-001 — Authoritative functional source is available offline and externally traceable — MUST
### STD-PRIVACY-001 — MUST
### STD-PRIVACY-002 — MUST
### STD-SECURITY-001 — App lock uses biometrics with system device authentication fallback; app PIN is not a prerequisite — MUST
### STD-DEBUG-001 — MUST
### STD-DEBUG-002 — MUST
### STD-AI-001 — MUST
### STD-AI-002 — MUST
### STD-AI-003 — AI release review is advisory, explainable and non-autonomous — MUST
### STD-AI-004 — AI release review uses data minimization — MUST
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
### STD-RELEASE-006 — Release Candidate Quality Gate cadence — MUST
### STD-RELEASE-007 — Release diff and risk-based coverage — MUST
### STD-DATA-005 — Single-device Xcode ↔ TestFlight/App Store ↔ Xcode data continuity — MUST
### STD-BACKEND-001 — Production backend schema/index/permission/config is explicitly ready — MUST
### STD-BACKEND-002 — Real TestFlight/Production read/write/sync/share smoke follows app capabilities — MUST
### STD-BACKEND-003 — Server-side fixes and binary fixes are explicitly distinguished — MUST
### STD-PERF-001 — Runtime performance is tested with representative real-volume data — MUST
### STD-ASYNC-001 — Stale async completion cannot overwrite newer state — MUST
### STD-ASYNC-002 — Remote invite/share/access operations do not block interactive UI/MainActor responsiveness — MUST
### STD-DERIVED-001 — Authoritative mutation precedes one coherent derived-state rebuild — MUST
### STD-CLOUD-001 — Remote destructive/access success follows confirmed remote truth — MUST
### STD-CLOUD-002 — Security/access mutations have durable retry or reconciliation — MUST
### STD-DATA-006 — Corrupt persisted state fails safely without destructive empty overwrite — MUST
### STD-DATA-007 — Destructive deletion is relationship-aware — MUST
### STD-DATA-008 — Persisted-data app has production-to-candidate upgrade-path gate — MUST
### STD-TEST-001 — Material deterministic engines require automated regression coverage — MUST
### STD-TEST-002 — Critical user journeys and resilience scenarios — MUST
### STD-UI-001 — Release visual/runtime matrix — MUST
### STD-DIAG-001 — Internal Full App Check — MUST
### STD-DIAG-002 — Structured diagnostic findings and severity — MUST
### STD-PERM-001 — Disabled feature and permission exposure remain in parity — MUST
### STD-EVIDENCE-001 — Runtime evidence is build-scoped and regressions remain traceable — MUST
### STD-EVIDENCE-002 — RC Evidence Bundle and release baseline — MUST
### STD-POSTRELEASE-001 — Production feedback loop — MUST
### STD-COMPACT-001 — Compact surfaces define content priority and destination integrity — SHOULD

## 9. Machine-readable applicability

Candidate 1.9.0 RC2 rozširuje `CONFORMANCE_CATALOG.json` na **131 pravidiel**.

Nové capability väzby:
- `hasAIReleaseReview` → `STD-AI-003`, `STD-AI-004`,
- `hasPostReleaseMonitoring` → `STD-POSTRELEASE-001`.

Ostatné nové RC2 pravidlá sú cross-app release-quality kontrakty. Konkrétny check set je capability-aware: aplikácia netestuje subsystém, ktorý nemá, ale MUSÍ mať RC evidence pre to, čo reálne podporuje.

## 10. Release stav

`standard-v1.8.0` zostáva stabilná verejná autorita.

`standard-1.9.0-rc2` je candidate vetva na implementáciu, audit a cross-app validáciu. Promotion na stable 1.9.0 vyžaduje validný 131-rule katalóg, pilotnú adopciu Release Inspector gate, review AI/privacy contractov a cross-app applicability/runtime evidence.
