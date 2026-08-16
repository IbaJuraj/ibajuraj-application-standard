# Changelog – IbaJuraj Application Standard

## 1.6.0 – 2026-08-16

### Added
- používateľský About metadata contract: verzia aplikácie + build, pri IbaJuraj Application Standard iba `Verzia X.Y.Z`,
- zákaz zobrazovania interného adoption level/runtime gate/audit stavu v bežnom About UI,
- kompaktný kontrakt pre súhrnné sekcie typu `Na prvý pohľad` a prioritu hlavnej ďalšej akcie.

### Compatibility
- spätne kompatibilná MINOR aktualizácia bez migrácie doménových používateľských dát,
- vyžaduje iba úpravu prezentačných komponentov tam, kde aplikácia zobrazuje interné metadata alebo neprimerane vysoký summary blok.

## 1.5.2 – 2026-08-14

### Changed
- spresnený Neutral Surface kontrakt: explicitná používateľská farebná téma MAY zmeniť root/background surface, zatiaľ čo Predvolená téma MUST zostať family-neutral,
- ak aplikácia ponúka Vzhľad aj Farebnú tému, obe voľby MUST používať oddelený persistentný stav a kompatibilné Light/Dark varianty,
- plné accent tlačidlá a badge MUST voliť foreground podľa kontrastu namiesto pevnej bielej,
- runtime gate pre aplikácie s farebnými témami overuje Predvolenú, jednu svetlú a jednu tmavú tému.

### Compatibility
- spätne kompatibilný patch release,
- bez povinnej migrácie doménových používateľských dát; aplikácia MAY vykonať jednorazovú migráciu starého theme preference modelu.

## 1.5.1 – 2026-08-13

### Added
- povinný Neutral Surface & Text Color Contract pre spoločné Light/Dark neutrálne plochy a textové roly,
- semantic tokeny `color.appBackground`, `color.cardSurface`, `color.textPrimary`, `color.textSecondary`, `color.separator` a `color.disabled`,
- povinný Light/Dark screenshot parity gate v runtime audite,
- explicitná brand-surface výnimka s adaptívnym kontrastom.

### Changed
- plná adopcia od 1.5.1 vyžaduje zhodný vizuálny výsledok rovnakej neutrálnej role naprieč aplikáciami alebo zaznamenanú výnimku,
- bežné neutral text/surface roly SHOULD používať systémové semantic colors namiesto lokálnych gray/opacity hodnôt.

### Compatibility
- spätne kompatibilný patch release,
- bez povinnej migrácie používateľských dát.

## 1.5.0 – 2026-08-13

- zavedený princíp „zjednocovať správanie a geometriu, nie produktovú identitu“,
- kodifikovaná hierarchia root obrazoviek a pravidlo jednej dominantnej priority/CTA,
- zavedený progressive-disclosure kontrakt a limity vizuálnej hustoty,
- zjednotené sémantické roly search fieldov, filter chips a segmented controls,
- spresnené pravidlá bottom navigácie a voliteľnej centrálnej globálnej akcie,
- zavedené spoločné primary CTA, empty-state a context-menu pravidlá,
- zavedený adaptívny badge/label kontrast vrátane obľúbenosti na brand surfaces,
- zavedené voliteľné používateľské označenie pre viac rovnakých objektov bez pevného zoznamu rolí,
- rozšírené responsive pravidlá pre iPad, landscape a adaptívne gridy,
- zavedené motion/haptics pravidlá a Reduce Motion gate,
- zavedený Form & Editor kontrakt vrátane vysvetlenia disabled Save a priameho edit flow,
- zavedené explicitné async a používateľsky čitateľné sync states,
- rozšírený accessibility quality gate o VoiceOver poradie a veľký Dynamic Type,
- zavedený source-hygiene audit vrátane ~430-line review threshold, root-view zodpovedností, unused-file auditu a cross-file Swift access-control kontroly,
- rozšírené design tokeny, referenčné vzory, testovacia matica a release checklist,
- verzia 1.5.0 je spätne kompatibilná minor aktualizácia a sama osebe nevyžaduje migráciu používateľských dát.

## 1.5.0 – 2026-08-13

- zavedený spoločný typografický kontrakt pre hlavné názvy koreňových pracovných obrazoviek,
- `appPage.title` je zjednotený na `.largeTitle.weight(.bold)` s Dynamic Type,
- `appPage.subtitle` je zjednotený na `.subheadline` so sekundárnou farbou,
- zjednotená 6 pt medzera medzi hlavným názvom a podnadpisom,
- zakázané lokálne pevné bodové veľkosti a `minimumScaleFactor` pre túto spoločnú typografickú rolu,
- rozšírená testovacia matica, referenčné vzory a release checklist o side-by-side kontrolu title/subtitle páru,
- verzia 1.5.0 je spätne kompatibilná patch aktualizácia a nevyžaduje migráciu používateľských dát.

## 1.4.0 – 2026-08-13

- zavedený presný spoločný geometrický kontrakt pre Nastavenia naprieč aplikáciami IbaJuraj,
- kodifikované rozmery settings row: 56 pt minimálna výška, 16/10 pt padding a 36 × 36 pt ikonová dlaždica,
- spresnené poradie SwiftUI modifierov, aby sa padding nepripočítaval nad spoločnú minimálnu výšku,
- zjednotená geometria karty Vzhľad a segmented controlu Automaticky / Svetlý / Tmavý,
- zjednotená geometria kontaktnej obrazovky vrátane 42 × 42 pt ikonových boxov, 16 pt paddingu, 20 pt radiusu a 12 pt medzier,
- zjednotená geometria obrazovky O aplikácii vrátane 18 pt radiusu, 16 pt paddingu, 24 pt ikonového stĺpca a 12 pt medzier medzi akčnými kartami,
- doplnené pravidlo, že produktovo odlišný obsah nesmie meniť základnú geometriu rovnakého komponentového variantu,
- rozšírená testovacia matica a release checklist o side-by-side porovnanie spoločných obrazoviek,
- verzia 1.4.0 je spätne kompatibilná minor aktualizácia a nevyžaduje migráciu používateľských dát.

## 1.3.1 – 2026-08-11

- spresnená ochrana navigačného titulku pred presvitajúcim alebo prekrývajúcim sa posúvaným obsahom,
- zavedený grouped-card vzor pre tri a viac rovnocenných informačných riadkov,
- odlíšená sémantika interného prechodu pomocou chevronu od externého odkazu pomocou `arrow.up.right.square`,
- doplnený kompaktný adaptívny vzor dvojice súhrnných skratiek, ktorý sa pri nedostatku priestoru zloží pod seba,
- spresnená typografická hierarchia vnorených informačných obrazoviek; obsahový nadpis nemá súperiť s navigačným titulkom,
- doplnená povinnosť lokalizovať počty položiek podľa plurálových pravidiel podporovaného jazyka,
- rozšírené referenčné vzory, testovacia matica a release brány o nové vizuálne a navigačné kontroly,
- verzia 1.3.1 je spätne kompatibilná patch aktualizácia a nevyžaduje migráciu používateľských dát.

## 1.3.0 – 2026-08-10

- spresnené, že spoločný vstup do Nastavení je povinný na hlavnej úvodnej obrazovke, nie v každom produktovom tabe,
- zavedený spoločný kontrakt hlavičky s najviac dvomi akciami na jednej strane a Nastaveniami ako pravou krajnou akciou,
- pridané nové `header.action.*` tokeny s preferovaným 42 pt vizuálom, povoleným rozsahom 42–48 pt a minimálnou 44 pt dotykovou plochou,
- zachovaný spätne kompatibilný 48 pt settings entry variant z 1.2.0,
- spresnená architektúra a odporúčané poradie sekcií Nastavení,
- kodifikovaný priamy segmented Vzhľad podľa vzoru Lex Drive,
- zavedený kompaktný spoločný vzor obrazovky Kontakt s formulárom, Telegramom a upozornením na citlivé údaje,
- doplnená kontaktná URL zmluva pre bezpečné predvyplnenie webového formulára,
- zjednotená obrazovka O aplikácii a jeden runtime zdroj verzie, buildu, tagu a adopcie,
- sprísnená push navigácia, systémová šípka, swipe-back a rovnaké správanie pri neuložených zmenách,
- zakázané používanie sheet/full-screen cover ako náhrady bežného settings stromu,
- zakázané rozhodovanie layoutu podľa `UIScreen.main.bounds` a zmenšovanie settings textov cez `minimumScaleFactor`,
- doplnený produktový variant Calculator Key bez násilného zjednotenia rozmerov rôznych rolí,
- rozšírený privacy release gate pre každý app, widget a extension target,
- sprísnené presné názvy úrovní adopcie a požiadavka uložených release dôkazov pre Level 3 a 4,
- pridaná testovacia matica, release checklist, referenčné vzory a návrh IJAS-0005,
- verzia 1.3.0 je spätne kompatibilná minor aktualizácia a nevyžaduje migráciu používateľských dát.

## 1.2.0 – 2026-08-09

- zavedený spoločný vstup do Nastavení cez `gearshape.fill` vpravo hore a pravidlo, že spodná navigácia obsahuje iba hlavné pracovné časti,
- zjednotený grouped-card vizuál Nastavení vrátane ikonových dlaždíc, typografie, section headers, chevronov, stavových hodnôt a priameho segmented prepínača Vzhľadu,
- doplnené pravidlá adaptívneho rozloženia podľa dostupného priestoru namiesto konkrétneho modelu zariadenia,
- zavedené spoločné sémantické varianty dlaždíc, kariet a riadkov bez vynútenia identického produktového vzhľadu,
- doplnené pravidlá minimálnych rozmerov, obsahovej výšky, Dynamic Type a adaptívneho počtu stĺpcov,
- zavedená spoločná hierarchia informácií v kartách a pravidlá pre produktový variant vernostnej karty,
- rozšírené pravidlá dizajnových tokenov, spätnej väzby, chýb, obnovy a zachovania rozpracovanej práce,
- doplnené pravidlá dátového životného cyklu, dátumu a času, upozornení, systémových oprávnení, výkonu a stability,
- zavedené úrovne adopcie a spoločná testovacia matica zariadení, orientácie, lokalizácie, prístupnosti a sieťových stavov,
- opravený neúplný obsah repozitára a doplnené chýbajúce GitHub workflow a šablóny,
- opravený register SHA-256 kontrolných súčtov a rozšírená automatická validácia release,
- zjednotený normatívny jazyk MUST / MUST NOT / SHOULD / SHOULD NOT / MAY a používateľské pomenovanie položky Kontakt,
- verzia 1.2.0 je spätne kompatibilná minor aktualizácia a sama osebe nevyžaduje migráciu používateľských dát.

## 1.1.0 – 2026-08-07

- zavedená spoločná architektúra a pomenovanie systémových Nastavení,
- doplnené pravidlo minimálnej navigačnej hĺbky,
- doplnené pravidlá pre push vs. modal a systémový swipe-back na iOS,
- zjednotený spôsob explicitného schovania klávesnice v rodine IbaJuraj aplikácií,
- doplnené pravidlá pre krátke stavové hodnoty v Nastaveniach,
- doplnený priamy model Kontakt bez zbytočného medzikroku,
- doplnený spoločný model biometrie, voliteľného PIN-u a automatického uzamknutia,
- doplnené lifecycle pravidlo, aby interná navigácia nespúšťala opakované biometrické overenie,
- doplnené release kontroly navigácie, klávesnice a lokálneho zámku,
- rozšírený zoznam produktových doplnkov o Kalkulačku 2v1 a Peňaženku Kariet,
- verzia 1.1.0 je spätne kompatibilná s 1.0.0 a sama osebe nevyžaduje dátovú migráciu.

## 1.0.0 – 2026-07-31

- vytvorený prvý spoločný autoritatívny štandard,
- zavedené úrovne MUST / SHOULD / MAY,
- definovaná hierarchia spoločného a produktového štandardu,
- doplnené pravidlá pre UX, obsah, prístupnosť, dáta, migrácie, synchronizáciu, súkromie, bezpečnosť, testovanie a release,
- zavedený register spoločných odkazov podpory,
- zavedený proces živého štandardu, návrhov a výnimiek,
- prvá adopcia: Strážca Termínov v1.53 Build 43 a Lex Drive v1.5 Build 120A.
