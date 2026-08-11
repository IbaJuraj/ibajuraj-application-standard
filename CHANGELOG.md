# Changelog – IbaJuraj Application Standard

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
