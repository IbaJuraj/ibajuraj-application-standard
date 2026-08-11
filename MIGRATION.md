# Migrácia IbaJuraj Application Standard

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
