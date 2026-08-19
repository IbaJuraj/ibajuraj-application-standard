# IbaJuraj Standard 1.6.1 – release checklist

## Metadata a zdroj pravdy

- [ ] `STANDARD_VERSION`, `standard.json`, dokumenty a adopčný súbor majú zhodnú verziu.
- [ ] Tag má tvar `standard-v1.6.1` a existuje v autoritatívnom repozitári.
- [ ] Marketingová verzia a build aplikácie sa načítavajú z build nastavení alebo `Bundle`.
- [ ] Runtime verzia, tag a úroveň adopcie pochádzajú z jedného zdroja.
- [ ] Nevydaná verzia nie je prezentovaná ako aktívne prijatá.

## Spoločný UX kontrakt

- [ ] Hlavný root title používa spoločný token `appPage.title` a podnadpis `appPage.subtitle`.
- [ ] Title/subtitle nepoužíva lokálnu pevnú bodovú veľkosť ani `minimumScaleFactor`.
- [ ] Side-by-side audit potvrdil rovnakú typografickú rolu root headera naprieč aplikáciami.
- [ ] Nastavenia sú vpravo hore na hlavnej úvodnej obrazovke a nie sú samostatným tabom.
- [ ] Vzhľad používa priamy segmented control, ak ho aplikácia podporuje.
- [ ] Kontakt a O aplikácii sú v poslednej sekcii Pomoc a informácie.
- [ ] Bežné vnorené obrazovky používajú push, systémovú šípku a swipe-back.
- [ ] Sheet/full-screen cover zostal iba pre transakčné workflow.
- [ ] Settings riadky používajú spoločné tokeny a responzívne trailing hodnoty.
- [ ] Navigačná plocha chráni inline titulok pred presvitaním alebo prekrývaním posúvaného obsahu.
- [ ] Interné a externé prechody používajú odlišné sémantické indikátory.
- [ ] Informačné riadky a súhrnné skratky používajú zodpovedajúci grouped a adaptívny variant.
- [ ] Settings row, ikonové dlaždice, grouped radius, section spacing a divider inset používajú presné spoločné geometry tokeny.
- [ ] Karta Vzhľad a segmented control majú rovnakú základnú geometriu ako v ostatných aplikáciách IbaJuraj.
- [ ] Kontakt a O aplikácii používajú spoločné `contact.*` a `about.*` tokeny bez lokálneho zväčšovania paddingu alebo výšky.
- [ ] Side-by-side screenshot audit spoločných obrazoviek bol vykonaný aspoň proti jednej už zosúladenej referenčnej aplikácii.

## Kvalita

- [ ] `bash Checks/validate-standard.sh` alebo produktový ekvivalent prešiel.
- [ ] Čistý build a automatické testy prešli.
- [ ] `TEST_MATRIX.md` je vyplnená a dôkazy sú uložené.
- [ ] VoiceOver, Dynamic Type, kontrast a Reduce Motion boli manuálne overené.
- [ ] Lokalizované počty a plurálové tvary boli overené vo všetkých podporovaných jazykoch.
- [ ] Migrácia z aktuálnej verejnej App Store verzie prešla.

## Súkromie a podpora

- [ ] Privacy Manifest každého distribuovaného targetu bol skontrolovaný.
- [ ] Verejné odkazy zodpovedajú `SUPPORT_AND_LINKS.md`.
- [ ] Kontaktná URL funguje od aplikácie po predvyplnený formulár.
- [ ] Telegram nie je jediným kanálom a obrazovka upozorňuje na citlivé údaje.

## Release artefakt

- [ ] Aktualizované release notes, changelog a migrácia.
- [ ] `SHA256SUMS.txt` bol vytvorený až po poslednej obsahovej zmene.
- [ ] Release neobsahuje `.DS_Store`, `__MACOSX`, cache, tajomstvá ani nepotrebné archívy.
- [ ] Aktívne výnimky majú vlastníka, rozsah a dátum revízie.


## IbaJuraj Standard 1.5.0 gate

- [ ] root hierarchy a progressive disclosure audit,
- [ ] search/filter/segmented role audit,
- [ ] bottom-navigation safe-area audit,
- [ ] primary CTA + empty-state audit,
- [ ] context menu + destructive action audit,
- [ ] badge/favorite adaptive contrast audit,
- [ ] user-defined label audit, ak produkt rozlišuje viac rovnakých objektov,
- [ ] Form & Editor direct-flow + disabled Save explanation audit,
- [ ] async/sync state audit,
- [ ] iPad responsive audit pre iPad-capable target,
- [ ] VoiceOver + large Dynamic Type + Reduce Motion audit,
- [ ] source hygiene: unused files, >430-line review, root responsibilities, current validator paths,
- [ ] Xcode compile po každom cross-file Swift extension refaktore.
## IbaJuraj Standard 1.5.1 – Neutral Surface Gate

- [ ] Light root background zodpovedá spoločnému `color.appBackground`.
- [ ] Dark root background zodpovedá spoločnému `color.appBackground`.
- [ ] Light card/tile surface zodpovedá `color.cardSurface`.
- [ ] Dark card/tile surface zodpovedá `color.cardSurface`.
- [ ] Primary/secondary text role používajú spoločné semantic tokens.
- [ ] V bežných neutrálnych roliach nie sú neodôvodnené custom gray/opacity farby.
- [ ] Screenshot parity Light/Dark je zaznamenaná v runtime audite.
- [ ] Brand surfaces a favorite/badge indikátory spĺňajú kontrast.
## IbaJuraj Standard 1.5.2 – User Theme & Accent Gate

- [ ] Ak produkt nemá vlastnú Farebnú tému, Predvolený neutral contract ostáva bez zmeny.
- [ ] Ak produkt má Farebnú tému, Predvolená voľba obnoví family-neutral root background.
- [ ] Vzhľad a Farebná téma nie sú uložené v jednom spoločnom enum/state kľúči.
- [ ] Farebná téma má čitateľný Light/Dark variant alebo je jasne obmedzená na kompatibilný appearance.
- [ ] Preview tmavých aj svetlých tém je viditeľný v Settings.
- [ ] Plné accent tlačidlá/badge používajú kontrastný foreground, nie bezpodmienečne biely.
- [ ] Runtime dôkaz obsahuje Predvolenú + aspoň jednu svetlú a jednu tmavú používateľskú tému.



## IbaJuraj Standard 1.6.0 – About & Summary Density Gate

- [ ] O aplikácii zobrazuje marketingovú verziu a build.
- [ ] IbaJuraj Application Standard sa používateľovi zobrazuje iba ako `Verzia X.Y.Z`.
- [ ] Interný Level/tag/runtime gate nie je v bežnom About UI.
- [ ] Summary/Na prvý pohľad neprimerane nevytláča hlavnú akciu z prvého viewportu.

## Standard 1.6.0 final gate

- [ ] Settings sú priamo dostupné z každého primárneho rootu bez nutnosti prepnúť tab.
- [ ] Stavová terminológia je konzistentná medzi rootom, zoznamom a detailom.
- [ ] Kritické karty s jediným objektom používajú priame CTA na objekt, ak je to bezpečné.
- [ ] FAB/overlay, navigation surface a safe area neprekrývajú obsah ani hlavné akcie.

- [ ] Primary root titles and Settings actions share the same vertical baseline/top inset across all main tabs.


## IbaJuraj Standard 1.6.1 – Whole-App Integrity Gate

- [ ] Kompatibilitné, update a diagnostické runtime metadata používajú skutočný `Bundle`/build source of truth; žiadna historická hardcoded hodnota neovplyvňuje rozhodovanie.
- [ ] Back + swipe-back je konzistentný pre celé rodiny detailov a pre vstupy z rootu, katalógu, vyhľadávania aj deep-linku.
- [ ] Dlhé katalógy majú overený section context, safe-area správanie a prípadný pinned header.
- [ ] Root surfaces používajú rovnaký semantic background token; neexistuje paralelné lokálne neutrálne pozadie bez výnimky.
- [ ] Outcome-first/practical-first detail neodkladá hlavný výsledok za dlhý technický alebo právny blok.
- [ ] Sémantické farby zodpovedajú významu; danger nie je dekoratívne synonymum pre veľkú sankciu.
- [ ] `NOVÉ` a obdobné dočasné označenia majú životný cyklus.
- [ ] Časovo závislé vstupy rešpektujú reálne dátové pokrytie.
- [ ] Všetky publikované položky katalógu prešli completeness invariantmi a reprezentatívne navigačné mosty vedú na správny cieľ.
- [ ] Dátum/verzia právneho alebo dátového overenia pochádza zo zdroja konkrétneho balíka, nie z hardcoded fallbacku.
- [ ] Produkčné UI neobsahuje interné technické/auditné vety.
- [ ] Dynamic Type audit neodhalil bežný text fixovaný na neadaptívnu bodovú veľkosť bez zdokumentovanej výnimky.
