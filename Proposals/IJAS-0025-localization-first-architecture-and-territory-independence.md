# IJAS-0025 – Localization-First Architecture and Storefront Independence

**Stav:** proposed
**Navrhovateľ:** IbaJuraj
**Dátum:** 2026-09-03
**Dotknuté aplikácie:** všetky nové IbaJuraj aplikácie; existujúce aplikácie pri pridaní ďalšieho jazyka
**Navrhovaná verzia štandardu:** 1.7.1

## Problém

Aplikácia môže začať iba v jednom jazyku a až neskôr dostať ďalšie lokalizácie. Ak sú používateľské texty, pluralizácia alebo locale formátovanie natvrdo zapísané v Swift kóde, druhý jazyk si vyžiada neúmerne veľký refaktor a môže spôsobiť miešanie jazykov, nesprávne pády/fallbacky alebo locale chyby.

Samostatný problém je zamieňanie App Store distribučného územia s jazykom aplikácie. Aplikácia môže byť dostupná napríklad iba na Slovensku a v Česku a pritom podporovať slovenčinu, češtinu aj angličtinu pre používateľov, ktorí majú zariadenie alebo konkrétnu aplikáciu nastavenú na angličtinu.

## Dôkazy a príklady

Pri Peňaženke Kariet v1.5.2 sa pri príprave českej lokalizácie ukázalo, že nestačí pridať jeden `Localizable` súbor: časť používateľských textov, pluralizácie a locale správania bola naviazaná priamo na slovenčinu (`sk_SK`, slovenské tvary počtu kariet, hardcoded používateľské texty). To by pri budúcej angličtine opäť vyžadovalo ďalší refaktor.

Požadovaný produktový model Peňaženky je zároveň: distribúcia iba Slovensko + Česko, ale podporované jazyky SK + CZ + neskôr EN. Jazyk aplikácie preto nesmie byť odvodený od storefront krajiny.

## Navrhované pravidlo

1. Nová IbaJuraj aplikácia MUST byť localization-ready od prvého produkčného buildu, aj keď má pri štarte iba jeden jazyk.
2. User-facing texty MUST byť získavané cez lokalizačné zdroje (`String Catalog`, `Localizable.strings` alebo ekvivalent) a nemajú byť natvrdo uložené v business/UI logike, okrem vedome zdokumentovaných technických alebo právne presných konštánt.
3. Lokalizačné kľúče SHOULD byť jazykovo neutrálne a stabilné; preferovaný tvar je anglický/semantický identifikátor (napr. `shared_wallet.title`), nie používateľský slovenský text ako API kľúč.
4. Primárny/fallback jazyk aplikácie MAY byť slovenčina alebo iný produktovo zvolený jazyk. Jazyk fallbacku je nezávislý od jazyka identifikátorov v kóde.
5. Dátumy, čísla, meny, percentá a ďalšie locale-sensitive hodnoty MUST používať aktuálny/deklarovaný locale používateľa alebo explicitný doménový locale. Hardcoded `sk_SK` MUST NOT byť všeobecným UI formatterom.
6. Pluralizácia MUST používať lokalizačný pluralization mechanizmus alebo locale-aware varianty; one-language helper typu `karta/karty/kariet` nesmie byť spoločným riešením po pridaní ďalšieho jazyka.
7. App Store storefront/territory availability MUST byť oddelená od podporovaných jazykov aplikácie. Podpora `en` nesmie automaticky znamenať distribúciu v anglicky hovoriacich krajinách a obmedzenie distribúcie na SK/CZ nesmie blokovať angličtinu v aplikácii.
8. Pri pridaní novej lokalizácie MUST release gate overiť parity používateľských textov, fallbacky, locale formátovanie, pluralizáciu a longest-localization layout stress test.
9. Jazyk systému alebo per-app language nastavenie iOS SHOULD byť rešpektované bez vlastného paralelného jazykového prepínača, pokiaľ produkt nemá konkrétny dôvod na vlastný selector.

**Záväznosť:** MUST / MUST NOT podľa bodov vyššie; SHOULD pre naming kľúčov a preferenciu systémového language selection.

## Rozsah

Do spoločného Standardu patrí localization-ready architektúra, oddelenie semantic key od user-facing textu, locale-aware formatovanie, pluralizácia, fallback politika, release parity a nezávislosť jazykov od App Store území.

Produktové zostáva:
- ktoré konkrétne jazyky aplikácia podporuje,
- v ktorých krajinách je aplikácia distribuovaná,
- názov aplikácie a App Store metadata pre jednotlivé lokalizácie,
- explicitné doménové výnimky, kde je pevný locale súčasťou dátovej/právnej definície.

## Migrácia

Existujúca jednojazyčná aplikácia nemusí byť okamžite prepisovaná len kvôli prijatiu pravidla. Najneskôr pred pridaním druhého jazyka však musí:
- inventarizovať všetky user-facing stringy,
- presunúť ich do lokalizačných zdrojov,
- zaviesť stabilné semantic keys,
- odstrániť všeobecné hardcoded locale formattery,
- migrovať pluralizáciu na locale-aware mechanizmus,
- overiť fallback a layout v každom podporovanom jazyku.

Nové aplikácie majú túto architektúru zaviesť od začiatku, aby sa migrácia neskôr nevyžadovala.

## Kompatibilita a riziká

Pravidlo je spätne kompatibilné a nemení produktový obsah. Rizikom prijatia je mierne vyššia počiatočná disciplína pri tvorbe stringov. Rizikom odmietnutia je rastúci localization debt, miešanie jazykov, nesprávne pluralizácie/formátovanie a opakované refaktory pri každej novej lokalizácii.

## Automatická kontrola

Čiastočne áno:
- linter môže hľadať podozrivé hardcoded user-facing literály v `Text`, `Label`, alertoch a buttonoch,
- statický audit môže blokovať všeobecné `Locale(identifier: "sk_SK")` mimo allowlistu,
- release skript môže kontrolovať parity localization keys medzi podporovanými lokalizáciami,
- testy môžu meniť `Locale`/jazyk a overovať pluralizáciu/formátovanie,
- UI testy môžu spustiť longest-localization a fallback smoke test.

## Rozhodnutie

Vyplní sa po posúdení.

**Výsledok:**
**Odôvodnenie:**
**Schválená verzia:**
