# IJAS-0025 – Localization-First Architecture and Storefront Independence

**Stav:** accepted  
**Navrhovateľ:** IbaJuraj  
**Dátum:** 2026-09-03  
**Rozšírené:** 2026-09-05  
**Dotknuté aplikácie:** všetky nové IbaJuraj aplikácie; existujúce aplikácie pri pridaní ďalšieho jazyka  
**Schválená candidate verzia štandardu:** 1.8.0 RC1

## Problém
Aplikácia môže začať iba v jednom jazyku a až neskôr dostať ďalšie lokalizácie. Ak sú používateľské texty, pluralizácia alebo locale formátovanie natvrdo zapísané v Swift kóde, druhý jazyk si vyžiada neúmerný refaktor a môže spôsobiť miešanie jazykov, nesprávne fallbacky alebo locale chyby.

Samostatný problém je zamieňanie App Store distribučného územia s jazykom aplikácie. Rozsah distribúcie a množina podporovaných runtime jazykov sú nezávislé produktové rozhodnutia.

Pri Peňaženke Kariet sa navyše ukázala praktická potreba vlastného in-app prepínača jazyka pre rýchle overovanie a vytváranie reálnych lokalizovaných screenshotov. Takýto selector však nesmie vytvoriť druhý nekompatibilný localization systém ani meniť dáta.

## Schválený kontrakt
1. Nová IbaJuraj aplikácia MUST byť localization-ready od prvého produkčného buildu, aj keď má pri štarte iba jeden jazyk.
2. User-facing texty MUST byť získavané cez lokalizačné zdroje (`String Catalog`, `Localizable.strings` alebo ekvivalent) a nemajú byť natvrdo uložené v business/persistence logike, okrem vedome zdokumentovaných technických alebo právne presných konštánt.
3. Lokalizačné kľúče SHOULD byť jazykovo neutrálne, stabilné a semantické.
4. Primárny/fallback jazyk aplikácie MAY byť slovenčina alebo iný produktovo zvolený jazyk. Jazyk fallbacku je nezávislý od jazyka identifikátorov v kóde.
5. Dátumy, čísla, meny, percentá a ďalšie locale-sensitive hodnoty MUST používať aktuálny/deklarovaný locale používateľa alebo explicitný doménový locale. Hardcoded `sk_SK` MUST NOT byť všeobecným UI formatterom.
6. Pluralizácia MUST používať lokalizačný pluralization mechanizmus alebo locale-aware varianty.
7. App Store storefront/territory availability MUST byť oddelená od podporovaných runtime jazykov aplikácie.
8. Pri pridaní novej lokalizácie MUST release gate overiť parity používateľských textov, fallbacky, locale formátovanie, pluralizáciu a longest-localization layout stress test.
9. Jazyk systému alebo per-app language nastavenie iOS SHOULD byť rešpektované. Vlastný paralelný selector je MAY a potrebuje konkrétny produktový/testovací dôvod.
10. Ak vlastný in-app language selector existuje, MUST obsahovať **Automaticky / Podľa systému** a všetky runtime podporované jazyky.
11. Výber vlastného jazyka MUST byť perzistentný; návrat na Automaticky MUST znovu rešpektovať iOS/per-app jazyk.
12. Zmena jazyka MUST NOT meniť alebo migrovať doménové dáta, raw enum values, stabilné UUID, database/AppStorage keys, CloudKit record/share identity, transportné metadata, deep-link identity ani barcode/QR payload iba kvôli lokalizácii.
13. Ak aplikácia nevie bezpečne prepnúť celý runtime okamžite, MUST mať deterministické relaunch správanie a zrozumiteľnú informáciu pre používateľa.
14. Ak aplikácia obsahuje vyhľadávanie, nová runtime lokalizácia MUST pokrývať používateľské názvy a relevantné search aliases/synonymá tak, aby bolo vyhľadávanie v danom jazyku funkčné.

## Rozsah
Do spoločného Standardu patrí localization-ready architektúra, semantic keys, locale-aware formátovanie/pluralizácia, fallback politika, voliteľný language selector contract, locale-neutral persistence identity, search parity a nezávislosť jazykov od App Store území.

Produktové zostáva:
- ktoré konkrétne jazyky aplikácia podporuje,
- v ktorých krajinách je aplikácia distribuovaná,
- názov aplikácie a App Store metadata pre jednotlivé lokalizácie,
- či selector aplikuje jazyk okamžite alebo cez relaunch, ak je výsledok deterministický a bezpečný,
- explicitné doménové výnimky, kde je pevný locale súčasťou dátovej/právnej definície.

## Migrácia
Existujúca jednojazyčná aplikácia nemusí byť okamžite prepisovaná. Najneskôr pred pridaním druhého jazyka však musí inventarizovať user-facing stringy, zaviesť lokalizačné zdroje, odstrániť všeobecné hardcoded locale formattery, migrovať pluralizáciu a overiť fallback/layout.

Aplikácia s vlastným language selectorom musí oddeliť display language selection od perzistentných doménových/raw identít.

## Automatická kontrola
- linter hardcoded user-facing literálov,
- audit hardcoded `Locale(identifier:)` mimo allowlistu,
- localization key parity,
- test locale formatting/pluralization,
- test raw-ID stability pri prepnutí jazyka,
- search alias smoke per locale,
- UI/runtime selector Automatic → supported locales → Automatic.

## Rozhodnutie
**Výsledok:** accepted pre 1.8.0 RC1  
**Odôvodnenie:** opakovaný cross-app localization debt a reálna potreba bezpečného prepínania jazyka bez zásahu do dát.  
**Schválená verzia:** 1.8.0 RC1
