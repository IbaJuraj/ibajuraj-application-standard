## 1.6.0 → 1.6.1

Verzia 1.6.1 je spätne kompatibilná PATCH aktualizácia bez migrácie doménových používateľských dát.

- Nahraďte hardcoded runtime build/verziu v kompatibilitných, update a diagnostických službách hodnotou z autoritatívnych build metadát alebo `Bundle`.
- Overte všetky rodiny push detailov: Back a systémový swipe-back musia fungovať konzistentne z každého vstupu.
- Dlhé katalógy môžu zaviesť pinned section headers a collapsing title tam, kde zlepšujú orientáciu.
- Detaily s rozhodnutím/následkom presuňte na outcome-first/practical-first hierarchiu; sekundárne procesné a zdrojové údaje použite cez progressive disclosure.
- Ak sa používa badge `NOVÉ`, pridajte centrálne pravidlo expirácie/lifecycle.
- Dátumy pre časovo verziované pravidlá obmedzte na rozsah, pre ktorý existuje kompatibilný overený obsah.
- Vyhľadávanie doplňte o navigačné mosty, ak výsledok pozná konkrétny cieľ.
- Level 3+ katalógy doplňte o completeness test všetkých publikovaných položiek a behaviorálne route testy.
- Doménová dátová migrácia nie je potrebná.


## 1.6.0 – primary-root Settings, state clarity and root header alignment

- Každý primárny root s vlastnou hlavičkou doplňte o rovnaký `gearshape.fill` vstup do systémových Nastavení; používateľ nemá prechádzať na iný tab iba kvôli Nastaveniam.
- Skontrolujte, že rovnaký stav používa rovnaké používateľské znenie na roote, v zozname aj detaile a že záporné technické intervaly nie sú priamo zobrazované používateľovi.
- Ak kritická karta identifikuje jeden objekt, preferujte priame otvorenie jeho detailu pred všeobecným zoznamom.
- Žiadna migrácia doménových dát nie je potrebná.

## 1.5.2 → 1.6.0

Verzia 1.6.0 je spätne kompatibilná MINOR aktualizácia bez migrácie doménových dát.

- V **O aplikácii** zobrazte pri aplikácii marketingovú verziu aj build.
- Pri **IbaJuraj Application Standard** zobrazte používateľovi iba `Verzia X.Y.Z`; level, tag a runtime/audit stav ponechajte iba v interných metadátach.
- Skontrolujte všetky detailné obrazovky so sekciou **Na prvý pohľad** a znížte zbytočnú vertikálnu výšku summary metrík tak, aby hlavná úloha detailu nebola vytláčaná bez obsahového dôvodu.
- Nevyžaduje sa zmena uložených používateľských dát.

# Migrácia IbaJuraj Application Standard

## 1.5.1 → 1.5.2

Verzia 1.5.2 je spätne kompatibilná patch aktualizácia. Spresňuje správanie explicitne používateľom volených produktových farebných tém a kontrast plných accent surfaces.

### Povinný adopčný audit pre aplikáciu s Farebnou témou

1. Zachovať Predvolenú tému ako spoločný neutral `color.appBackground`.
2. Oddeliť persistentný stav Vzhľadu od persistentného stavu produktovej Farebnej témy.
3. Každá používateľská téma musí zostať čitateľná v podporovanom Light/Dark režime alebo musí byť jasne obmedzená na kompatibilný appearance režim.
4. `cardSurface`, primary/secondary text, separator a disabled semantic roly zostávajú podľa spoločného kontraktu, ak nejde o explicitnú product/brand surface.
5. Na plných accent tlačidlách vybrať foreground podľa kontrastu voči fillu.
6. Runtime overiť Predvolenú tému a minimálne jednu svetlú a jednu tmavú produktovú tému.

### Kompatibilita

- Nevyžaduje migráciu doménových používateľských dát.
- Aplikácia s historicky zlúčeným appearance/theme stavom MAY vykonať jednorazovú migráciu preference kľúčov pri prvom štarte.

## 1.5.0 → 1.5.1

Verzia 1.5.1 je spätne kompatibilná patch aktualizácia bez dátovej migrácie. Zavádza povinný Neutral Surface & Text Color Contract a Light/Dark parity gate.

### Povinný adopčný audit

1. Zmapovať root background na spoločný `color.appBackground`.
2. Zmapovať neutrálne grouped cards/tiles na `color.cardSurface`.
3. Zjednotiť primary, secondary, separator a disabled semantic text/surface roly.
4. Odstrániť alebo odôvodniť lokálne custom gray/opacity neutrálne farby.
5. Zachovať produktové/brand farby iba na produktových semantic/brand surfaces.
6. Vykonať screenshot parity audit v Light aj Dark Mode.
7. Zaznamenať každú zámernú odchýlku ako Standard Exception.

### Kompatibilita

- Nevyžaduje zmenu persistentných doménových modelov.
- Nevyžaduje zmenu navigačnej štruktúry ani počtu tabov.
- Môže vyžadovať vizuálnu úpravu neutrálneho pozadia, dlaždíc a textov.

## 1.4.1 → 1.5.0

Verzia 1.5.0 je spätne kompatibilná minor aktualizácia. Sama osebe nevyžaduje dátovú migráciu. Adopčný build SHOULD vykonať audit spoločných UX a source-hygiene oblastí.

### Povinný adopčný audit

1. Skontrolovať root hierarchy: title/subtitle/settings a jednu dominantnú obsahovú prioritu.
2. Skontrolovať duplicitu stavových badgeov, textov a CTA; použiť progressive disclosure tam, kde obsah zbytočne súperí.
3. Zjednotiť search/filter/segmented roly a primary CTA varianty podľa 1.5.0 tokenov pri prirodzenej úprave obrazoviek.
4. Skontrolovať empty states, context menu a deštruktívne akcie.
5. Skontrolovať kontrast badgeov/obľúbenosti na produktových farbách.
6. Ak produkt potrebuje rozlíšiť viac rovnakých objektov, zvážiť voliteľné používateľské pole Označenie bez pevného zoznamu hodnôt.
7. Pre iPad-capable target vykonať responsive audit portrait + landscape a overiť max-width/adaptívny grid.
8. Skontrolovať Form & Editor flow, disabled Save vysvetlenie a zbytočné medziobrazovky.
9. Skontrolovať async/sync používateľské stavy, aby „Synchronizované“ znamenalo potvrdený výsledok.
10. Vykonať source-hygiene audit: workflow súbory nad ~430 riadkov, root-view zodpovednosti, nepoužívané produkčné súbory, zastarané validátory a cross-file access control po refaktore.
11. Overiť VoiceOver poradie, veľký Dynamic Type a Reduce Motion pre primárne flow.

### Kompatibilita

- Persistentné doménové modely sa nemenia iba kvôli adopcii 1.5.0.
- Produktové názvy, počet tabov, farby a doménové IA zostávajú vo vlastníctve produktu.
- Existujúce komponenty MAY migrovať postupne pri prirodzenej úprave, ak nemajú aktuálny accessibility alebo integrity problém.

## 1.4.0 → 1.5.0

Verzia 1.5.0 je spätne kompatibilná patch aktualizácia bez dátovej migrácie. Zjednocuje typografiu hlavného root headera naprieč aplikáciami.

Pri adopcii aplikácia:

1. nahradí lokálnu pevnú veľkosť hlavného root názvu rolou `.largeTitle.weight(.bold)`,
2. nahradí lokálnu váhu alebo veľkosť podnadpisu rolou `.subheadline` so sekundárnou farbou,
3. nastaví 6 pt medzeru medzi title a subtitle,
4. odstráni `minimumScaleFactor` a bodové override z tejto spoločnej roly,
5. overí Dynamic Type a prirodzené zalomenie dlhého podnadpisu,
6. vykoná side-by-side screenshot audit aspoň proti jednej zosúladenej aplikácii.

Používateľské dáta sa nemenia.

---

## 1.3.1 → 1.4.0

Verzia 1.4.0 je spätne kompatibilná minor aktualizácia. Nemení používateľské dátové modely. Zavádza presný spoločný geometrický kontrakt pre **Nastavenia**, **Vzhľad**, **Kontakt** a **O aplikácii**, aby rovnaké komponenty nepôsobili v jednej aplikácii kompaktnejšie a v druhej vzdušnejšie.

Aplikácia pri adopcii vykoná tento audit:

1. porovná root Nastavení s centrálnymi tokenmi a odstráni lokálne rozmery pre rovnaké settings komponenty,
2. nastaví settings row na 16 pt horizontálny padding, 10 pt vertikálny padding, 36 × 36 pt ikonovú dlaždicu a minimálnu výšku 56 pt,
3. overí správne poradie modifierov: padding pred `frame(minHeight: 56)`,
4. zjednotí kartu **Vzhľad** na header padding 16/10 pt a segmented control s minimálnou 44 pt dotykovou výškou, 16 pt horizontálnym a 10 pt spodným paddingom,
5. zjednotí grouped-card radius 22 pt, section spacing 24 pt a divider inset 64 pt,
6. zjednotí hlavné kontaktné akcie na 16 pt padding, 42 × 42 pt ikonu, radius 20 pt a 12 pt medzeru medzi kartami,
7. zjednotí **O aplikácii** na 18 pt radius, 16 pt padding, 24 pt ikonový stĺpec a 12 pt medzery medzi samostatnými akčnými kartami,
8. ponechá produktovo odlišný obsah, ale overí, že rovnaký komponent s rovnakým počtom riadkov má rovnakú základnú výšku naprieč aplikáciami,
9. vykoná side-by-side runtime audit najmenej v Tmavom a Svetlom režime a pri default Dynamic Type,
10. uloží screenshotové dôkazy pre Nastavenia, Kontakt a O aplikácii.

Používateľské dáta sa nemigrujú. Zmena je vizuálna a komponentová; aplikácie môžu prejsť na 1.4.0 v najbližšom plánovanom UI builde.

---

## 1.3.0 → 1.3.1

Verzia 1.3.1 je spätne kompatibilná patch aktualizácia. Nemení používateľské dátové modely ani produktovú navigačnú architektúru. Spresňuje čitateľnosť navigačných plôch, zoskupovanie informačného obsahu, sémantiku odkazov, adaptívne súhrnné skratky a lokalizované počty.

Aplikácia pri adopcii vykoná tento audit:

1. overí, že obsah pri posúvaní nepresvitá cez navigačný titulok ani s ním vizuálne nesúperí,
2. použije chevron pre interný push prechod a `arrow.up.right.square` pre odkaz mimo aplikácie,
3. zoskupí tri a viac rovnocenných vysvetľujúcich riadkov do jednej informačnej karty s oddeľovačmi,
4. pri dvojici rovnocenných súhrnných skratiek použije kompaktné dvojstĺpcové rozloženie a pri nedostatku priestoru ich zloží pod seba,
5. ponechá obsahový nadpis vnorených informačných obrazoviek na úrovni `.title2` alebo nižšej, ak nejde o zámerný hero obsah,
6. overí plurálové tvary počtov pre nulu, jednu a viac položiek vo všetkých podporovaných jazykoch,
7. zopakuje kontroly vo Svetlom, Tmavom a Automatickom vzhľade vrátane Dynamic Type.

Používateľské dáta sa nemigrujú. Zmena adopcie pozostáva z UX auditu, aktualizácie lokálnej kópie štandardu a release dôkazov.

---

## 1.2.0 → 1.3.0

Verzia 1.3.0 je spätne kompatibilná minor aktualizácia. Nemení používateľské dátové modely. Spresňuje spoločnú hlavičku, navigáciu Nastavení, Vzhľad, Kontakt, O aplikácii, responzívne texty, privacy release gate a merateľnú adopciu.

Aplikácia pri adopcii vykoná tento audit:

1. ponechá vstup do Nastavení vpravo hore na hlavnej úvodnej obrazovke; nemusí ho pridávať do každého tabu,
2. použije `header.action.*` tokeny alebo ponechá spätne kompatibilný 48 pt variant z 1.2.0,
3. ponechá najviac dve kruhové akcie na jednej strane hlavičky a gear ako pravú krajnú akciu,
4. zobrazí **Automaticky / Svetlý / Tmavý** priamo v root Nastavení, ak aplikácia voľbu vzhľadu podporuje,
5. otvorí bežné vnorené Nastavenia push navigáciou; sheet ponechá iba pre transakčný workflow,
6. overí rovnaký návrat systémovou šípkou aj swipe-back gestom vrátane neuložených zmien,
7. presunie Kontakt a O aplikácii do poslednej sekcie **Pomoc a informácie**, ak sú dostupné,
8. použije kompaktnú kontaktnú obrazovku s formulárom, Telegramom a upozornením na citlivé údaje,
9. overí kontaktnú URL od aplikácie po predvyplnený formulár na webe,
10. odstráni `minimumScaleFactor` zo settings názvov a trailing hodnôt; pri nedostatku priestoru použije zalomenie alebo vertikálny variant,
11. odstráni rozhodovanie layoutu podľa `UIScreen.main.bounds` alebo modelu zariadenia,
12. centralizuje runtime verziu, build, tag štandardu a úroveň adopcie,
13. použije presný názov adopcie, napríklad `Level 2 – Shared UX`,
14. skontroluje Privacy Manifest každého app, widget a extension targetu vrátane required-reason API,
15. uloží automatické a manuálne release dôkazy podľa `TEST_MATRIX.md` a `RELEASE_CHECKLIST.md`.

Produktové migračné body:

- **Kalkulačka 2v1:** nevydaný draft 1.3.0 nesmie byť označený ako aktívny; lokálny token register sa musí zlúčiť s úplným centrálnym registrom, nie ho nahradiť.
- **Lex Drive:** ponechať priamy segmented Vzhľad; odstrániť duplicitnú všeobecnú voľbu vzhľadu z produktovej obrazovky výsledkov a trailing hodnoty nezmenšovať.
- **Strážca Termínov:** migrovať bežný settings strom zo sheet/full-screen cover na push navigáciu a doplniť required-reason API deklarácie.
- **Peňaženka Kariet:** nahradiť `UIScreen`-based klasifikáciu kontajnerovým layoutom, zjednotiť settings komponenty a doplniť Privacy Manifest.

Dočasný 48 pt kruh Nastavení z 1.2.0 zostáva platný. Nové implementácie SHOULD používať preferovaný 42 pt vizuál v povolenom rozsahu 42–48 pt a minimálnu 44 × 44 pt hit area. Presná nekompatibilná náhrada starého tokenu sa odkladá na budúcu major verziu.

---

## 1.1.0 → 1.2.0

Verzia 1.2.0 je spätne kompatibilná minor aktualizácia. Nevyžaduje migráciu používateľských dát ani zmenu produktových doménových modelov. Aplikácia však môže odstrániť tab Nastavení a nahradiť ho spoločným vstupom vpravo hore; hlavné pracovné taby zostávajú produktové.

Aplikácia pri adopcii 1.2.0 vykoná audit:

1. vstupu do Nastavení cez `gearshape.fill` vpravo hore a odstránenia Nastavení zo spodnej navigácie,
2. samostatnej push obrazovky Nastavení so šípkou späť a swipe-back,
3. grouped-card vizuálu, spoločných ikonových dlaždíc, section headers, chevronov, status hodnôt a priameho segmented prepínača Vzhľadu,
4. adaptívneho rozloženia na kompaktnom, štandardnom a veľkom iPhone,
5. dlaždíc, kariet a zoznamových riadkov podľa ich sémantickej roly,
6. obsahu pri Dynamic Type, dlhších lokalizáciách a orientácii na šírku,
7. stavov načítavania, chyby, obnovy a spätnej väzby po akcii,
8. zachovania rozpracovaných formulárov a platného navigačného stavu,
9. životného cyklu údajov, zálohy, exportu a synchronizácie, ak ich aplikácia používa,
10. dátumov, časových pásiem a upozornení, ak ich aplikácia používa,
11. systémových oprávnení, výkonu a release testovacej matice,
12. lokálneho `APP_STANDARD_ADOPTION.md`, úrovne adopcie a aktívnych výnimiek.

Produktové migračné body:

- **Kalkulačka 2v1:** presunúť ikonu Nastavení vpravo hore, nahradiť modal plnohodnotnou push obrazovkou a použiť spoločný grouped-card systém.
- **Lex Drive:** oddeliť systémové Nastavenia od obrazovky Moje; História, Obľúbené a právny kontext MAY zostať v Moje.
- **Strážca Termínov:** odstrániť Nastavenia zo spodného tab baru a pridať spoločný vstup vpravo hore.
- **Peňaženka Kariet:** odstrániť Nastavenia zo spodnej navigácie a pridať spoločný vstup vpravo hore.

Nové obrazovky prijaté po vydaní 1.2.0 používajú nové spoločné pravidlá okamžite. Existujúce obrazovky sa auditujú v najbližšom plánovanom builde; dočasná odchýlka musí byť evidovaná ako výnimka.

---

## 1.0.0 → 1.1.0

Verzia 1.1.0 je spätne kompatibilná minor aktualizácia. Samotné prijatie štandardu nevyžaduje migráciu používateľských dát.

Aplikácia pri adopcii 1.1.0 skontroluje:

1. pomenovanie a umiestnenie spoločných položiek Nastavení,
2. zbytočné medziobrazovky pri jednoduchých voľbách,
3. návrat späť a systémový swipe-back na bežných vnorených obrazovkách,
4. používanie modálnych akcií iba pri skutočných modálnych workflow,
5. spoločný spôsob schovania klávesnice,
6. priamy Kontakt a podporu,
7. pri lokálnom zámku biometriu, PIN, autolock a lifecycle správanie,
8. Dynamic Type a pravé stavové hodnoty v Nastaveniach,
9. lokálny `APP_STANDARD_ADOPTION.md` a verziu lokálnej kópie štandardu.

Každá aplikácia prijíma verziu 1.1.0 samostatným auditovaným buildom; publikovanie centrálneho štandardu samo osebe nemení používanú verziu v aplikácii.

---

## Historická migrácia autoritatívneho zdroja z `ibajuraj.github.io/standard`

### Cieľ

Jediný autoritatívny zdroj IbaJuraj Application Standardu je:

```text
https://github.com/IbaJuraj/ibajuraj-application-standard
```

### Bezpečné poradie

1. Vytvoriť a naplniť nový repozitár.
2. Overiť GitHub Action.
3. Vytvoriť tag a Release konkrétnej verzie.
4. Až potom upraviť `ibajuraj.github.io`.
5. V starom priečinku `standard/` nenechať druhú nezávislú autoritatívnu kópiu.
6. Nahradiť ju krátkym oznámením a odkazom na nový repozitár, prípadne ju udržiavať iba ako automaticky generované zrkadlo.
7. Následne aktualizovať odkazy a adopčné súbory v aplikáciách.

### Dôležité pravidlo

Obsah štandardu sa po migrácii upravuje iba v tomto repozitári. Web IbaJuraj Apps môže štandard prezentovať alebo naň odkazovať, ale nesmie sa stať druhým zdrojom pravdy.

### 1.6.0 – Root header baseline
Primary root screens must migrate to one shared root-title top inset/baseline and matching trailing Settings action geometry.

## Migrácia 1.6.1 → 1.6.2

Ide o prezentačný PATCH bez migrácie používateľských dát.

1. Identifikujte obrazovky používajúce rovnaký produktový header pattern (napr. Home a vnorené search/assistant obrazovky).
2. Odstráňte lokálne `padding(.top)`, `offset(y:)` a vlastné safe-area kompenzácie, ktoré menia baseline rovnakého headeru.
3. Presuňte geometriu do zdieľaného header komponentu alebo tokenov `appPage.headerFamily.*`.
4. Back akciu implementujte v stabilnom leading slote bez posunu title/trailing action.
5. Runtime porovnajte referenčný root a aspoň jednu vnorenú obrazovku v Light/Dark a pri podporovanom Dynamic Type.
