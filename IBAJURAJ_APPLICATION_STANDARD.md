# IbaJuraj Application Standard

**Verzia:** 1.7.0  
**Stav:** Release Candidate 1 – pred publikovaním  
**Dátum RC:** 28. augusta 2026  
**Vlastník:** IbaJuraj  
**Predchádzajúca autoritatívna verzia:** 1.6.4 (`standard-v1.6.4`, commit `5e2901945287165a8902f28fb1d3b5a87b6eeb92`)

> Tento balík je kandidát na IbaJuraj Application Standard 1.7.0. Kým nebude po adopcii a audite publikovaný tag `standard-v1.7.0`, autoritatívnou verejnou verziou zostáva 1.6.4.

## 1. Účel

Tento štandard určuje spoločné produktové, UX, technické, obsahové, bezpečnostné, prístupnostné a release pravidlá pre aplikácie IbaJuraj. Nevynucuje identické obrazovky. Zjednocuje roly, geometriu spoločných komponentov, správanie, kvalitu a spôsob overovania.

Verzia 1.7.0 zavádza tri nové nadradené piliere:

1. **Whole-App Adaptive Layout Contract** – adaptívna musí byť celá aplikácia, nie iba vybrané komponenty.
2. **Bottom Navigation & Floating Tab Bar Contract** – spoločný základ spodnej navigácie s natívnym a custom variantom.
3. **Machine-Verifiable Cross-App Conformance** – stabilné ID pravidiel, spoločný validator, UI-test identifikátory a povinný dôkaz implementácie.

## 2. Normatívny základ a spätná kompatibilita

1.7.0 je **MINOR** release. Všetky požiadavky 1.6.4 zostávajú v platnosti, pokiaľ ich 1.7.0 výslovne nenahrádza alebo nespresňuje. Pri adopcii sa musí aplikácia posudzovať kumulatívne.

Pre audit histórie je základ 1.6.4 identifikovaný tagom a commitom uvedeným vyššie. Súbor `AUDIT_1.6.4_TO_1.7.0.md` uvádza nové a sprísnené pravidlá.

## 3. Hierarchia pravidiel

1. **IbaJuraj Application Standard** – spoločné pravidlá pre všetky aplikácie.
2. **Product Standard** – pravidlá konkrétnej aplikácie alebo domény.
3. **ADR** – schválená technická alebo produktová výnimka.
4. **Build Scope** – rozsah jedného buildu.

Pri konflikte platí vyššia úroveň. Produktový štandard môže spoločné pravidlo rozšíriť, nie potichu obísť.

## 4. Záväznosť

- **MUST / MUST NOT** – povinné; porušenie blokuje release alebo vyžaduje platnú výnimku.
- **SHOULD / SHOULD NOT** – odporúčané; odchýlka má byť zdôvodnená.
- **MAY** – voliteľné.

Každé nové alebo zmenené MUST/MUST NOT pravidlo od 1.7.0 má stabilné `STD-*` ID. ID sa používa v `CONFORMANCE_CATALOG.json`, testoch, audite a release reporte.

## 5. Spoločná identita a runtime metadata

### STD-IDENTITY-001 — Jeden runtime zdroj verzie a buildu — MUST
Marketingová verzia a build MUST pochádzať z autoritatívnych build nastavení alebo `Bundle`. Hodnoty MUST NOT byť samostatne hardcoded vo view, diagnostike, synchronizácii alebo kompatibilitných kontrolách.

### STD-IDENTITY-002 — Spoločná identita — MUST
Používateľské systémové surface MUST používať značku **IbaJuraj Apps** a spoločné odkazy podľa `SUPPORT_AND_LINKS.md`.

### STD-IDENTITY-003 — Produktové metadata sú oddelené od Standardu — MUST
Verzia aplikácie/build a verzia IbaJuraj Application Standard sú dve rôzne identity a MUST byť prezentované oddelene.

## 6. Spoločné UX a component families

### STD-COMPONENT-001 — Shared role, shared geometry — MUST
Komponenty s rovnakou sémantickou rolou MUST používať spoločnú komponentovú rodinu alebo spoločný geometry contract. Rozdielna obrazovka sama osebe nie je dôvodom na inú výšku, radius, padding, icon container alebo trailing geometriu.

### STD-COMPONENT-002 — No local geometry drift — MUST NOT
Lokálne `frame`, `padding`, `cornerRadius`, symbol size alebo offset MUST NOT obchádzať autoritatívny token/shared component bez zdokumentovaného dôvodu.

### STD-COMPONENT-003 — Semantic exceptions — MUST
Zámerná odchýlka MAY existovať iba pre inú sémantickú rolu alebo schválenú produktovú výnimku. Vizuálna odchýlka bez významového dôvodu je defect.

### STD-COMPONENT-004 — Minimum touch target — MUST
Interaktívny prvok MUST mať efektívnu dotykovú plochu aspoň **44 × 44 pt**.

### STD-COMPONENT-005 — Text fit — MUST
Dôležitý používateľský text MUST zostať čitateľný v podporovaných lokalizáciách a Dynamic Type. `minimumScaleFactor` MUST NOT byť primárnym riešením významového textu.

Preferované poradie adaptácie textu: **wrap → komponent rastie → HStack/VStack restack → zníženie počtu stĺpcov → scroll/fallback prezentácia**.

## 7. Settings a spoločné systémové surface

### STD-SETTINGS-001 — Priamy vstup do Nastavení — MUST
Ak aplikácia má systémové Nastavenia a vlastný root header, Nastavenia MUST byť dostupné z každého primárneho rootu priamou systémovou akciou, typicky `gearshape.fill` vpravo hore. Samostatný Settings tab v hlavnej spodnej navigácii SHOULD NOT byť použitý iba kvôli dostupnosti Nastavení.

### STD-SETTINGS-002 — Appearance contract — MUST, ak aplikácia podporuje appearance
Základné `Automaticky / Svetlý / Tmavý` MUST používať spoločnú segmentovanú rolu alebo ekvivalentný priamy systémový výber. Ak produkt podporuje vlastné farebné témy, tie sú sekundárna produktová voľba.

### STD-APPEARANCE-001 — Live application of selection — MUST
Výber vzhľadu alebo farebnej témy, ktorého výsledok je možné bezpečne aplikovať bez restartu, MUST aktualizovať aktuálnu obrazovku okamžite. Používateľ MUST NOT potrebovať odísť o krok späť, aby sa presunul checkmark, zmenilo pozadie alebo aktualizoval selected state.

### STD-APPEARANCE-002 — Selection state parity — MUST
Vizuálny selected state, uložená hodnota a reálne vykreslený vzhľad MUST reprezentovať tú istú hodnotu v tom istom render cykle.

### STD-APPEARANCE-003 — Persisted selection — MUST
Po okamžitej zmene MUST zvolená hodnota zostať zachovaná po návrate, relaunchi a pri podporovanom sync modeli.

## 8. O aplikácii – cross-app contract

Táto sekcia definuje používateľský formát, aby spoločná systémová obrazovka nebola v každej aplikácii iná.

### STD-ABOUT-001 — Settings row — MUST
V Nastaveniach musí existovať položka:

- title: **`O aplikácii`** (lokalizovaný ekvivalent),
- subtitle: **`Verzia, súkromie a štandard`** (lokalizovaný ekvivalent),
- trailing value: **`<marketingVersion> (<build>)`**.

Príklady:
- `1.11 (53)`
- `1.11.0 (195)`

Trailing value MUST pochádzať z runtime metadata.

### STD-ABOUT-002 — Version card — MUST
Po otvorení `O aplikácii` musí spoločná dlaždica **Verzia** zobrazovať jednu prirodzenú používateľskú vetu:

`<AppName> v<marketingVersion> – Build <build>.`

Príklady:
- `Kalkulačka 2v1 v1.11 – Build 53.`
- `Lex Drive v1.11.0 – Build 195.`
- `Strážca Termínov v1.56.0 – Build 105.`

Názov aplikácie, marketingVersion a build MUST byť generované z autoritatívnej identity/runtime metadata, nie duplikované v textoch.

### STD-ABOUT-003 — Standard card — MUST
Dlaždica musí mať:

- title: **`IbaJuraj Application Standard`**,
- subtitle: **`Verzia <standardVersion>`**.

Používateľovi sa MUST NOT zobrazovať interný tag (`standard-v...`), commit hash ani adoption level.

### STD-ABOUT-004 — Developer card — MUST
Spoločná rola:
- title: **`Vývojár`**,
- subtitle: **`IbaJuraj Apps.`**

### STD-ABOUT-005 — Web a privacy — MUST
Obrazovka MUST poskytovať platný Web IbaJuraj Apps a Ochrana súkromia. Produkt MAY pridať doménové položky, napríklad právne upozornenie.

### STD-ABOUT-006 — Shared test identifiers — MUST
Ak platforma podporuje accessibility identifiers, spoločné surface MUST publikovať minimálne:

- `ij.settings.about.row`
- `ij.about.version.card`
- `ij.about.standard.card`
- `ij.about.developer.card`
- `ij.about.web.row`
- `ij.about.privacy.row`

Identifikátory sú určené pre UI testy a MUST NOT meniť používateľský text.

## 9. Whole-App Adaptive Layout Contract

### STD-ADAPT-001 — Whole-app adaptive by default — MUST
Každá používateľská obrazovka MUST byť adaptívna. Platí pre rooty, detaily, formuláre, Settings, sheets, modaly, search, gridy, karty, tab bary, FAB, onboarding, empty/error states a klávesnice.

### STD-ADAPT-002 — Container-driven layout — MUST
Layout MUST byť primárne odvodený od **aktuálne dostupného kontajnera**, safe area, Dynamic Type a obsahových potrieb. Konkrétny model zariadenia alebo `UIScreen.main.bounds` MUST NOT byť primárnym zdrojom layout rozhodnutí, ak je dostupná reálna container geometry.

### STD-ADAPT-003 — Safe-area driven positioning — MUST
Horné a spodné systémové surface, klávesnica, floating prvky a obsah MUST používať aktuálne safe-area insets alebo layout guides. Pevné kompenzácie pre konkrétny model zariadenia sú neprípustné bez zdokumentovanej výnimky.

### STD-ADAPT-004 — Adaptive use of free space — MUST
Adaptivita neznamená iba „nič sa neoreže“. Ak má komponent objektívne dostupný priestor a jeho zväčšenie zlepší použiteľnosť bez narušenia hierarchie, layout SHOULD tento priestor primerane využiť.

Príklad: Calculator Key môže na väčšom kontajneri zväčšiť hit surface smerom do strán a nadol, ak horný anchor klávesnice zostane stabilný a výsledkový panel nie je vytlačený.

### STD-ADAPT-005 — Stable content anchors — MUST
Adaptívne zväčšovanie MUST zachovať významové anchory. Zväčšenie spodného ovládacieho regiónu MUST NOT posunúť jeho hornú hranicu do obsahu, ak produktový layout definuje túto hranicu ako ochrannú.

### STD-ADAPT-006 — Dynamic Type — MUST
Komponent sa pri väčšom texte musí prispôsobiť. Pri nedostatku miesta sa najprv mení layout, nie významový text. Surface MAY narásť, grid MAY prejsť na menej stĺpcov a row MAY prejsť na viac riadkov.

### STD-ADAPT-007 — Localization stress — MUST
Najdlhšia podporovaná lokalizácia MUST byť súčasťou release auditu pre spoločné navigačné dlaždice, segmenty, Settings rows, hlavné CTA a bottom navigation labels.

### STD-ADAPT-008 — Fixed tokens are allowed — MUST
Pevná hodnota je povolená pre design token alebo bezpečnostnú hranicu (napr. 44 pt touch minimum, radius, referenčná icon size). Pevná hodnota MUST NOT byť použitá ako náhrada reálnej dostupnej geometry tam, kde by spôsobila clipping, nadmernú prázdnu plochu alebo nevyužitý priestor.

### STD-ADAPT-009 — Window/orientation adaptability — MUST, ak je podporované
Ak aplikácia podporuje landscape, iPad multitasking alebo meniacu sa veľkosť okna, layout MUST reagovať na zmenu kontajnera bez relaunchu.

### STD-ADAPT-010 — iPad support/compatibility — MUST
Ak je iPad podporovaný ako target, musí prejsť portrait aj landscape runtime matrix. Ak iPhone-only aplikácia môže byť systémom spustená v iPad compatibility presentation, kritické pracovné obrazovky MUST zostať použiteľné a nesmú clipovať.

### STD-ADAPT-011 — No device-name branching as foundation — MUST NOT
Podmienky typu „iPhone X/14/Pro Max → layout“ MUST NOT byť základným layout systémom. Breakpoint MAY byť odvodený od dostupnej šírky/výšky, size class, Dynamic Type alebo explicitného capability contextu.

### STD-ADAPT-012 — Shared adaptive calculator-key principle — MUST, ak existuje calculator keypad
Calculator keys MUST používať dostupnú šírku aj výšku s minimom 44 pt a rozumným maximum clampom. Pri adaptívnom raste MUST byť testované, že výsledkový/percentuálny obsah zostáva nedotknutý.

## 10. Bottom Navigation & Floating Tab Bar Contract

Aplikácia môže používať **Native Tab Navigation** alebo **Custom Floating Navigation**. Produktový počet tabov, názvy a doménové ikony nie sú spoločným pravidlom.

### STD-NAV-001 — Variant declaration — MUST
Aplikácia s bottom navigation MUST v `STANDARD_CONFORMANCE.json` deklarovať `bottomNavigationMode`: `native`, `custom` alebo `none`.

### STD-NAV-002 — Native variant — MUST, ak `native`
Natívny variant SHOULD používať systémový `TabView`/platformový tab bar. Aplikácia MUST NOT ručne emulovať systémovú výšku alebo safe-area správanie, ak produktová potreba nevyžaduje custom surface.

### STD-NAV-003 — Custom baseline geometry — MUST, ak `custom`
Custom floating navigation používa spoločnú baseline geometriu:

- tab content minimum: **48–52 pt** podľa compact/regular density,
- outer internal padding: približne **4 pt**,
- referenčná surface výška: približne **60–66 pt** pri štandardnom texte,
- bar radius: referenčne **28 pt**,
- selected item radius: referenčne približne **22 pt**,
- icon-to-label spacing: približne **3 pt**,
- label: typicky `caption2`, semibold alebo ekvivalentná sémantická rola,
- každý tab: efektívny hit target aspoň **44 × 44 pt**.

60–66 pt je **baseline interval, nie rigidný frame**. Dynamic Type alebo platformová zmena MAY surface zväčšiť.

### STD-NAV-004 — Primary floating action — MUST, ak existuje
Globálna primary action (napr. `+`) SHOULD mať referenčnú veľkosť okolo **50 pt** a MUST NOT svojou veľkosťou nútiť celý navigation surface do neprimerane väčšej výšky.

Povolené riešenia:
- samostatný floating action overlay,
- centrálna integrovaná akcia, ak bar zachová spoločnú základnú geometriu.

### STD-NAV-005 — Adaptive width — MUST
Floating bar MUST reagovať na dostupnú šírku. Na úzkom kontajneri sa redukuje interný spacing/padding skôr než touch target alebo čitateľnosť. Na širokom kontajneri SHOULD mať rozumnú maximálnu šírku a nemá sa bezdôvodne natiahnuť cez celý displej.

### STD-NAV-006 — Safe area — MUST
Vertikálna poloha bottom navigation sa MUST odvodzovať od reálnej bottom safe area.

### STD-NAV-007 — Content clearance — MUST
Scrollovateľný obsah MUST používať bottom clearance podľa reálnej výšky navigation surface + safe area. Posledný interaktívny obsah musí byť možné vytiahnuť celý nad bar. Po úplnom doscrollovaní SHOULD zostať približne **16–24 pt** vizuálnej rezervy.

### STD-NAV-008 — Dynamic Type — MUST
Pri Accessibility Dynamic Type sa custom navigation MAY zväčšiť alebo zmeniť interné usporiadanie. Text MUST NOT byť zmenšovaný pod podporovanú sémantickú rolu iba na zachovanie pevnej výšky.

### STD-NAV-009 — Shared test identifier — MUST, ak `custom`
Custom bar MUST publikovať `ij.bottomnav.container`. Globálna primary action, ak existuje, MUST publikovať `ij.bottomnav.primaryAction`.

## 11. Navigácia

### STD-NESTED-NAV-001 — Back + native swipe — MUST
Vnorená obrazovka MUST mať zrozumiteľnú cestu späť. Na iOS push navigácia MUST zachovať native edge-swipe back, ak technická výnimka nie je zdokumentovaná.

### STD-NESTED-NAV-002 — No loops/dead ends — MUST
Navigácia MUST NOT vytvárať slučku, ktorá používateľa vracia na rovnaký zoznam namiesto detailu, ani slepý koniec bez zmysluplného návratu.

## 12. Lokalizácia a prístupnosť

### STD-LOC-001 — Localization parity — MUST
Každý nový alebo zmenený používateľský text MUST byť prítomný vo všetkých deklarovaných podporovaných lokalizáciách pred release.

### STD-LOC-002 — No source-string drift — MUST
Spoločný systémový význam (napr. `O aplikácii`, `Verzia, súkromie a štandard`) MUST používať jeden lokalizačný kľúč/autoritatívnu definíciu, nie viac paralelných textov.

### STD-A11Y-001 — VoiceOver — MUST
Interaktívne ovládanie MUST mať zrozumiteľný label/trait a nesmie byť zlúčené s informačným textom tak, že CTA stratí samostatnú akciu.

### STD-A11Y-002 — Contrast and non-color meaning — MUST
Farba MUST NOT byť jediným nositeľom stavu. Selected/error/critical stav musí mať aj text, symbol alebo inú informáciu.

### STD-A11Y-003 — Reduce Motion / Increase Contrast — MUST
Shared component families MUST zostať funkčné pri Reduce Motion a Increase Contrast.

## 13. Formuláre a editory

### STD-FORM-001 — Required vs optional — MUST
Povinné a voliteľné údaje musia byť rozlíšiteľné bez spoliehania iba na farbu.

### STD-FORM-002 — Validation timing — MUST
Inline chyba SHOULD byť pri konkrétnom poli a SHOULD NOT byť zobrazovaná ako aktívna chyba predtým, než používateľ mal reálnu možnosť pole vyplniť, ak formulár nie je v stave pokusu o uloženie.

### STD-FORM-003 — Progressive disclosure — MUST
Zriedkavé technické alebo advanced polia SHOULD byť schované pod `Ďalšie možnosti` alebo ekvivalent, ak ich permanentné zobrazenie znižuje použiteľnosť bežného flow.

### STD-FORM-004 — Keyboard dismissal — MUST
Formulár MUST umožniť pohodlné skrytie klávesnice bez straty rozpracovaných údajov.

## 14. Dáta, migrácie, sync a autoritatívnosť

### STD-DATA-001 — Single source of truth — MUST
Pre každý autoritatívny údaj alebo pravidlo musí existovať jeden zdroj pravdy. View MUST NOT vytvoriť paralelný dátový model pre rovnaký význam.

### STD-DATA-002 — Schema and migration — MUST
Persistované používateľské dáta MUST mať kompatibilitný/migračný plán. Aktualizácia z verejne dostupnej verzie musí byť testovaná.

### STD-DATA-003 — Sync vs backup vs export — MUST
Synchronizácia, lokálne uloženie, záloha a export MUST byť používateľsky odlíšené a jedna funkcia sa nesmie vydávať za inú.

### STD-DATA-004 — Traceability — MUST, ak doména používa autoritatívne/verziované dáta
Výsledok SHOULD byť dohľadateľný k stabilnej identite záznamu, verzii/časovej platnosti a stavu overenia.

## 15. Privacy, security a vývojové režimy

### STD-PRIVACY-001 — Privacy manifest — MUST
Každý distribuovaný target musí mať alebo zdediť správny Privacy Manifest a deklarovať required-reason API podľa skutočného použitia.

### STD-PRIVACY-002 — Privacy policy parity — MUST
Ak sa zmení spracovanie údajov, musí sa aktualizovať privacy manifest, používateľská zásada ochrany súkromia a App Store privacy odpoveď podľa potreby.

### STD-SECURITY-001 — Security state machine — MUST, ak app lock existuje
Biometria, PIN a autolock musia tvoriť konzistentný stavový model. Funkcia, ktorá bez aktívnej ochrany nemôže bezpečne fungovať, nesmie vyzerať aktívne.

### STD-DEBUG-001 — Production isolation — MUST
Mock, stub, AI Test, debug routing, interné score a diagnostické ovládanie MUST NOT byť dostupné v produkčnom používateľskom UI.

### STD-DEBUG-002 — Regression hardening — MUST
Potvrdená runtime chyba s rozumným rizikom opakovania MUST dostať regresný test alebo zdokumentovanú výnimku, ak automatizácia nie je primeraná.

## 16. Generated/AI assistance

Ak aplikácia používa generovanú pomoc:

### STD-AI-001 — Grounded/verified input — MUST
Autoritatívne fakty, právne závery, sankcie alebo časové pravidlá musia byť deterministicky overené pred generovaním používateľského textu, ak doména vyžaduje verifikovateľnosť.

### STD-AI-002 — Safe fallback — MUST
Pri nízkej dôvere alebo nedostatku overených dát sa systém musí bezpečne vrátiť na klasický/overený flow alebo priznať obmedzenie. Nesmie prezentovať najbližšiu nesúvisiacu odpoveď ako definitívnu.

## 17. Machine-Verifiable Cross-App Conformance

### STD-CONF-001 — Conformance manifest — MUST
Každá aplikácia adoptujúca 1.7.0 musí mať `STANDARD_CONFORMANCE.json` podľa `STANDARD_CONFORMANCE_TEMPLATE.json`.

Manifest deklaruje:
- app/product identity,
- pin Standardu,
- capability flags,
- podporované lokalizácie,
- implementačné dôkazy,
- testy a runtime gates,
- výnimky s ADR.

### STD-CONF-002 — Every applicable MUST has evidence — MUST
Každé aplikovateľné MUST/MUST NOT pravidlo z `CONFORMANCE_CATALOG.json` musí mať jeden z výsledkov:

- `static` – overené spoločným validatorom,
- `unit` – overené XCTest/unit testom,
- `ui` – overené UI testom,
- `runtime` – explicitný manuálny runtime gate,
- `exception` – schválená výnimka s existujúcim ADR.

Tichý `not implemented`, chýbajúci záznam alebo nezdôvodnené `not applicable` je FAIL.

### STD-CONF-003 — Common validator — MUST
Pred release musí prejsť:

`python3 Checks/validate-app-conformance.py --app-root <path> --standard-root <path>`

Validator musí minimálne overiť:
- pin Standardu,
- úplnosť aplikovateľných MUST pravidiel,
- existenciu deklarovaných evidence súborov/tokenov,
- výnimky a ADR,
- localization parity a povinné kľúče,
- runtime metadata/build deklaráciu, ak je nakonfigurovaná,
- runtime gate coverage pre pravidlá, ktoré nemožno overiť staticky.

### STD-CONF-004 — Stable UI identifiers — MUST
Spoločné systémové surface definované týmto Standardom musia používať spoločné accessibility/test IDs, ak ich platforma podporuje. UI testy potom nesmú byť závislé od prekladu používateľského textu.

### STD-CONF-005 — Static test is not runtime proof — MUST
Static PASS nesmie byť prezentovaný ako runtime PASS. Správanie typu live theme update, swipe-back, clipping, safe area, scroll clearance alebo Dynamic Type vyžaduje unit/UI/runtime dôkaz podľa katalógu.

### STD-CONF-006 — Release conformance report — MUST
Release-ready build musí mať report vo forme:

`applicable MUST: X / PASS X / exceptions Y / runtime pending Z`

Ak `runtime pending > 0` pre release-blocking pravidlá, build nie je Level 4 Full Adoption.

## 18. Adaptive Runtime Test Matrix

Minimálna matica pre všetky iPhone aplikácie:

1. **Small iPhone container** – najmenší podporovaný alebo ekvivalentný dostupný kontajner.
2. **Regular iPhone** – bežný referenčný kontajner.
3. **Large iPhone** – veľký/Pro Max kontajner.
4. **Accessibility Dynamic Type** – minimálne jeden veľký accessibility size.
5. **Light + Dark**.
6. **Najdlhšia podporovaná lokalizácia** pre relevantné shared surfaces.
7. **Keyboard/form state**, ak aplikácia obsahuje formuláre.

Ak aplikácia podporuje iPad:
- iPad portrait,
- iPad landscape,
- dostupné multitasking/window sizes podľa podporovaného deployment targetu.

Ak iPhone-only aplikácia môže bežať v iPad compatibility presentation, kritické workflow musí prejsť compatibility testom.

## 19. Release gate a adoption levels

- **Level 0 – Declared:** Standard iba uvedený.
- **Level 1 – Identity:** runtime identity, odkazy a verzovanie zjednotené.
- **Level 2 – Shared UX:** spoločné Settings/About/component roles implementované.
- **Level 3 – Quality Gates:** statické, unit/UI a runtime gate mechanizmy existujú a prešli pre aktuálny scope.
- **Level 4 – Full Adoption:** všetky aplikovateľné MUST pravidlá majú PASS alebo schválenú výnimku; žiadny release-blocking runtime gate nie je pending.

Aplikácia MUST NOT deklarovať Level 4 iba na základe statického validatora.

## 20. Release hygiene

### STD-RELEASE-001 — Source hygiene — MUST
Release package nesmie obsahovať `.DS_Store`, user-specific Xcode state, build artifacts, secrets ani reálne citlivé testovacie údaje.

### STD-RELEASE-002 — Localization gate — MUST
Zmenený používateľský copy musí prejsť parity kontrolou vo všetkých podporovaných lokalizáciách.

### STD-RELEASE-003 — Regression scope — MUST
Build, ktorý mení shared component family alebo common Settings/About surface, musí auditovať všetky použitia danej rodiny v aplikácii, nie iba nahlásený screenshot.

### STD-RELEASE-004 — Native build gate — MUST
Static parser/validator nenahrádza Xcode build a fyzický/runtime test tam, kde je potrebný. Release report musí tieto stavy rozlišovať.

## 21. Migračné pravidlo 1.6.4 → 1.7.0

Aplikácie sa migrujú v samostatných buildoch. Odporúčaný postup:

1. pridať/aktualizovať `APP_STANDARD_ADOPTION.md`,
2. pridať `STANDARD_CONFORMANCE.json`,
3. zapnúť common conformance validator,
4. opraviť About/Settings contract,
5. vykonať whole-app adaptive audit,
6. deklarovať a overiť bottom-navigation variant,
7. doplniť UI/runtime testy pre pravidlá, ktoré static validator nevie dokázať,
8. až potom zvýšiť adoption level.

Product-specific obsah sa nemení iba kvôli 1.7.0, ak ho nový contract nezasahuje.

## 22. Stav RC1

RC1 sa má najprv aplikovať na dohodnuté aplikácie. Ak aplikácia odhalí chybu alebo nejednoznačnosť v contracte, opraví sa Standard pred publikovaním finálneho tagu. Po úspešnej adopcii sa RC status odstráni, `standard.json` sa prepne na `active` a vytvorí sa tag `standard-v1.7.0`.
