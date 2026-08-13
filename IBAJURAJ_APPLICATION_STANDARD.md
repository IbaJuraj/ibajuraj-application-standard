# IbaJuraj Application Standard

**Verzia:** 1.5.1  
**Stav:** autoritatívny spoločný štandard  
**Platnosť od:** 13. augusta 2026  
**Vlastník:** IbaJuraj

## 1. Účel

Tento štandard určuje spoločné produktové, UX, technické, obsahové, bezpečnostné a release pravidlá pre aplikácie IbaJuraj. Nevynucuje identický vzhľad ani rovnakú informačnú architektúru. Zabezpečuje, aby aplikácie pôsobili ako jedna rodina, boli dôveryhodné, prístupné, udržateľné a mali jednotnú podporu.

## 2. Hierarchia pravidiel

1. **IbaJuraj Application Standard** – spoločné pravidlá pre všetky aplikácie.
2. **Product Standard** – pravidlá konkrétnej aplikácie alebo domény.
3. **Architecture Decision Record (ADR)** – zdôvodnená technická výnimka alebo rozhodnutie.
4. **Build Scope** – konkrétny rozsah jedného buildu; MUST rešpektovať vyššie pravidlá, ak ich nemení schválený návrh.

Pri konflikte platí vyššia úroveň. Produktový štandard môže spoločné pravidlo rozšíriť, nie potichu obísť.

## 3. Záväznosť

- **MUST** – povinné; porušenie blokuje release alebo vyžaduje schválenú výnimku.
- **MUST NOT** – zakázané; porušenie blokuje release alebo vyžaduje schválenú výnimku.
- **SHOULD** – odporúčané; odchýlka musí mať uvedený dôvod.
- **SHOULD NOT** – neodporúčané; použitie musí mať uvedený dôvod.
- **MAY** – voliteľné.

Záväznosť pravidla určuje iba jedno z týchto veľkými písmenami zapísaných kľúčových slov. Slovenské modálne slovesá vo vysvetľujúcom texte nevytvárajú samostatnú úroveň záväznosti.

## 4. Spoločná identita

- MUST používať značku **IbaJuraj** ako spoločnú autorskú a produktovú identitu.
- MUST načítavať marketingovú verziu a build z autoritatívnych build nastavení alebo `Bundle`; hodnoty MUST NOT byť ručne duplikované v používateľskom kóde.
- MUST používať jednotné verejné odkazy definované v `SUPPORT_AND_LINKS.md`.
- SHOULD zobrazovať názov aplikácie, verziu, build, web, ochranu súkromia a podporu v časti O aplikácii.

## 5. Produktové princípy

- MUST existovať jeden zdroj pravdy pre každý druh údajov.
- MUST byť jasné vlastníctvo údajov a životný cyklus objektu.
- MUST oddeliť identitu údajov od ich prezentácie.
- MUST zabrániť vzniku paralelnej architektúry pre rovnakú funkciu.
- SHOULD dodržiavať **Action over Information** – používateľ má dostať ďalší zmysluplný krok, nie iba pasívny údaj.
- SHOULD dodržiavať **3-sekundové pravidlo** – hlavný stav a najdôležitejšia akcia majú byť pochopiteľné približne do troch sekúnd.
- MUST predchádzať slepým koncom; prázdny alebo chybový stav má ponúknuť riešenie.
- SHOULD uprednostniť kontextovú akciu pred zbytočným presúvaním používateľa medzi obrazovkami.

## 6. Dizajn a UX

### 6.1 Spoločné roly, nie identické obrazovky

Aplikácie môžu mať rozdielny počet tabov, navigáciu, dashboard a doménové komponenty. Spoločné majú byť významy a kvalita základných prvkov:

- typografické roly,
- rozostupy a dotykové plochy,
- primárne a sekundárne akcie,
- informačné, varovné a kritické stavy,
- prázdne, chybové, načítavacie a offline stavy,
- Nastavenia, Pomoc a O aplikácii.

Spoločný štandard MUST zjednocovať **správanie, geometriu a sémantické roly**, nie produktový obsah ani vizuálnu identitu. Lex Drive MAY zostať právne strohý, Strážca Termínov MAY používať bohatšiu stavovú signalizáciu a Peňaženka Kariet MAY používať vizuál značiek, ak rovnaké používateľské roly zostávajú ovládateľné rovnakým spôsobom.

### 6.2 Povinné pravidlá

- MUST podporovať Dynamic Type bez straty obsahu alebo funkcie.
- MUST mať minimálnu dotykovú plochu 44 × 44 bodov pre interaktívne prvky.
- MUST nepoužívať farbu ako jediný nositeľ významu.
- MUST používať konkrétne názvy akcií; neurčité „Pokračovať“ alebo „OK“ iba tam, kde je výsledok jednoznačný.
- MUST pri deštruktívnej akcii pomenovať objekt a následok.
- SHOULD používať systémové komponenty Apple, ak produktová potreba nevyžaduje vlastné riešenie.
- SHOULD obmedziť veľké monolitické view súbory a deliť ich podľa zodpovedností.


### 6.3 Spoločné systémové nastavenia

Ak aplikácia obsahuje systémové Nastavenia, spoločné funkcie MUST používať rovnaký význam a predvolené pomenovanie naprieč rodinou aplikácií. Produkt môže sekcie vynechať, ak danú funkciu nemá; štandard neurčuje rovnaký počet položiek ani rovnaké poradie pre všetky produkty.

#### 6.3.1 Spoločný vstup do Nastavení

- Nastavenia MUST byť dostupné cez tlačidlo so symbolom `gearshape.fill` vpravo hore na hlavnej obrazovke aplikácie.
- Hlavná obrazovka je predvolený vstupný root produktu. Tlačidlo Nastavení MAY byť dostupné aj na ďalších primárnych rootoch, ale tento štandard to nevyžaduje.
- Spodná navigácia MUST obsahovať iba hlavné pracovné časti produktu a MUST NOT obsahovať samostatný tab systémových Nastavení.
- Produktová obrazovka typu **Moje** MAY zostať pre históriu, obľúbené položky, profil alebo doménový kontext, ale MUST NOT byť jediným kontajnerom systémových Nastavení.
- Tlačidlo Nastavení MUST používať spoločný vizuálny rozsah, kruhový kontajner, odsadenie od safe area, pressed state a accessibility label podľa `DESIGN_TOKENS.md`.
- Nastavenia MUST byť samostatnou plnohodnotnou obrazovkou otvorenou bežnou push navigáciou. MUST používať šípku späť a systémový swipe-back; MUST NOT byť bežným modálom s tlačidlom **Zavrieť** alebo **Hotovo**.

#### 6.3.2 Spoločná hlavička a akcie

- Akcia Nastavení MUST byť pravou krajnou akciou hlavičky hlavnej obrazovky.
- Jedna strana hlavičky SHOULD obsahovať najviac dve samostatné kruhové akcie; ďalšie sekundárne akcie SHOULD byť zlúčené do menu alebo presunuté do obsahu.
- Vizuálny kruh a dotyková plocha MUST používať `header.action.*` tokeny. Vizuálny kruh MAY byť menší než dotyková plocha.
- Názov obrazovky alebo aplikácie MUST zostať čitateľný a MUST sa neprekrývať s akciami ani pri dlhšej lokalizácii a Dynamic Type.
- Hlavička MUST používať sémantický surface a dostatočný kontrast; produktový akcent MAY zvýrazniť stav, ale SHOULD NOT meniť systémovú akciu na dominantné CTA.
- Animovaný pressed state MUST rešpektovať Reduce Motion.

#### 6.3.3 Spoločný vizuálny systém Nastavení

- Nastavenia MUST používať grouped-card rozloženie so spoločnými rozmermi, zaoblením, ikonovými dlaždicami, typografiou, section headers, chevronmi, stavovými hodnotami a hustotou podľa `DESIGN_TOKENS.md`.
- Riadok s vnorenou obrazovkou MUST používať spoločný trailing chevron.
- Krátka aktuálna hodnota SHOULD byť zobrazená vpravo, ak používateľovi pomáha pochopiť stav bez otvorenia detailu.
- Jednoduchá voľba MUST NOT vytvárať zbytočnú medziobrazovku. Ak aplikácia ponúka vzhľad **Automaticky / Svetlý / Tmavý**, výber MUST byť priamo na hlavnej obrazovke Nastavení ako segmented control.
- Zjednotenie vizuálu MUST NOT meniť produktový obsah Nastavení; aplikácia zobrazuje iba relevantné položky a sekcie.
- Root Nastavení MUST používať systémový navigation title **Nastavenia**. MAY používať veľký titulok; vnorené obrazovky SHOULD používať inline titulok so systémovou šípkou späť.
- Opakované neinteraktívne vysvetlenia s rovnakou vizuálnou rolou SHOULD byť zoskupené do jednej karty s vnútornými oddeľovačmi. Samostatné vysoké karty SHOULD zostať iba pre samostatnú akciu, stav alebo významovo dominantnú funkciu.
- Spoločné Nastavenia rodiny aplikácií MUST používať rovnakú geometriu komponentov pre rovnakú sémantickú rolu. Riadok typu settings row, ikonová dlaždica, section spacing, group radius a divider inset MUST používať presné tokeny z `DESIGN_TOKENS.md`; produktový obsah MAY byť odlišný.
- Implementácia `settings.row.minimumHeight` MUST aplikovať vnútorný padding pred minimálnym `frame(minHeight:)`, aby sa padding nepripočítal nad spoločnú minimálnu výšku a nevznikali rozdielne hustoty medzi aplikáciami.
- Dve aplikácie MAY mať rozdielny počet položiek alebo dlhší text, ale rovnaký komponent pri rovnakom obsahu a Dynamic Type MUST mať rovnakú základnú výšku, odsadenie, ikonovú geometriu a radius.

Ak sú príslušné funkcie dostupné, sekcie SHOULD používať toto poradie:

- **Aplikácia** – vzhľad, jazyk, haptika a všeobecné správanie,
- **Produktové nastavenia** – funkcie špecifické pre danú aplikáciu,
- **Zdieľanie** – ľudia, roly, členstvo a pozvánky, ak ich produkt podporuje,
- **Údaje a zabezpečenie** – zámok, synchronizácia, záloha, export a ochrana údajov,
- **Pomoc a informácie** – kontakt, návod, súkromie a informácie o aplikácii; táto sekcia SHOULD byť posledná.

Spoločné názvy a princípy:

- **Vzhľad** – iba ak aplikácia ponúka voľbu Automaticky / Svetlý / Tmavý; výber MUST byť dostupný priamo ako segmented control bez medziobrazovky.
- **Upozornenia** – stav a cesta k systémovým alebo produktovým nastaveniam upozornení.
- **Zabezpečenie** – biometria, PIN aplikácie a automatické uzamknutie, ak ich produkt podporuje.
- **Synchronizácia cez iCloud** – stav a ovládanie osobnej synchronizácie, ak ju produkt podporuje.
- **Ľudia a zdieľanie** – iba ak produkt podporuje zdieľanie alebo členstvo.
- **Zálohy** – vytvorenie, obnova a vysvetlenie rozsahu zálohy.
- **Export údajov** – vytvorenie používateľskej prenosnej kópie, ak ju produkt podporuje.
- **Ochrana súkromia** – priamy vstup do aktuálnych informácií o spracovaní údajov.
- **Kontakt** – SHOULD viesť priamo do kontaktnej obrazovky a SHOULD NOT byť skrytý za zbytočnou medziobrazovkou.
- **O aplikácii** – verzia, súkromie, štandard a právne/informačné údaje relevantné pre produkt.

- Položky **Kontakt** a **O aplikácii** SHOULD byť v poslednej sekcii a SHOULD zachovať rovnaké relatívne umiestnenie naprieč aplikáciami.

Krátka stavová hodnota napravo od riadku, napríklad **Automaticky**, **Aktívna**, **Povolené** alebo **Iba ja**, MUST zostať čitateľná pri podporovaných veľkostiach textu a MUST NOT sa lámať po jednotlivých písmenách.

- Text riadku a trailing hodnota MUST NOT používať `minimumScaleFactor` ako náhradu adaptívneho rozloženia.
- Ak sa trailing hodnota nezmestí vedľa názvu, MUST sa bezpečne zalomiť alebo presunúť pod názov bez straty významu.
- Chevron MUST byť použitý iba na riadku, ktorý otvára ďalšiu obrazovku alebo systémový cieľ; switch MUST byť použitý iba pre okamžitú binárnu voľbu.
- Deštruktívna farba MUST byť vyhradená pre akciu, ktorá skutočne odstraňuje údaje alebo má iný závažný následok.

#### 6.3.4 Vzhľad

- Ak aplikácia ponúka voľbu vzhľadu, root Nastavení MUST zobraziť segmented control **Automaticky / Svetlý / Tmavý** bez ďalšej medziobrazovky.
- Zmena MUST byť aplikovaná okamžite bez reštartu aplikácie.
- Režim **Automaticky** MUST sledovať aktuálny systémový vzhľad.
- Produktová farebná téma MAY byť samostatnou voľbou, ale jej názov a popis MUST jasne odlíšiť farebnú tému od svetlého alebo tmavého vzhľadu.
- Vybraný segment MUST mať nefarený nositeľ stavu a dostatočný kontrast vo všetkých podporovaných témach.
- Karta **Vzhľad** MUST používať spoločnú geometriu `settings.appearance.*`: header s ikonou a názvom, systémový segmented control s minimálnou 44 pt dotykovou výškou, identické horizontálne odsadenie a identický horný/spodný padding naprieč aplikáciami.
- Segmented control MUST NOT byť lokálne zväčšovaný alebo zmenšovaný produktovým paddingom, ak ide o rovnakú voľbu **Automaticky / Svetlý / Tmavý**.

#### 6.3.5 Kontakt

- Obrazovka Kontakt MUST byť bežnou push obrazovkou a MUST byť dostupná priamo z časti **Pomoc a informácie**.
- MUST obsahovať krátke vysvetlenie a jasný odkaz na kontaktný formulár.
- SHOULD obsahovať samostatnú sekundárnu možnosť **Telegram komunita**.
- Hlavné kontaktné možnosti SHOULD byť najviac dve; ďalšie informácie SHOULD zostať sekundárne.
- MUST obsahovať upozornenie, aby používateľ neposielal heslá, celé kópie dokladov ani iné citlivé údaje.
- MAY obsahovať produktovo prispôsobenú sekciu **Čo môžete poslať**.
- Odkaz na ochranu súkromia MAY byť kompaktný textový odkaz, ak je zásada dostupná aj vo formulári a v Nastaveniach.
- Kontaktný odkaz SHOULD preniesť identifikátor aplikácie, verziu, build a typ podnetu podľa zmluvy v `SUPPORT_AND_LINKS.md`; technické údaje pridané k správe MUST byť používateľovi viditeľné.
- Ak externý odkaz nemožno otvoriť, aplikácia MUST zobraziť zrozumiteľnú chybu a SHOULD ponúknuť alternatívny kontaktný kanál.
- Hlavné kontaktné akcie MUST používať spoločnú geometriu `contact.action.*`: rovnakú ikonovú dlaždicu, vnútorný padding, radius a medzeru medzi kartami. Produktový text MAY meniť výslednú výšku iba vtedy, keď sa reálne zalomí na viac riadkov.
- Úvodný blok a sekcia **Čo môžete poslať** SHOULD používať rovnakú informačnú hustotu a spacing ako ostatné IbaJuraj aplikácie; produktový obsah MAY byť odlišný.

#### 6.3.6 O aplikácii

- Obrazovka O aplikácii SHOULD obsahovať názov aplikácie, marketingovú verziu, build a prijatú verziu IbaJuraj Application Standardu.
- Marketingová verzia a build MUST byť načítané z autoritatívnych build nastavení alebo `Bundle`.
- Verzia, tag a úroveň adopcie štandardu MUST pochádzať z jedného runtime zdroja metadát a MUST zodpovedať `APP_STANDARD_ADOPTION.md`.
- Nevydaná alebo draft verzia MUST NOT byť prezentovaná ako aktívne prijatý štandard.
- Obrazovka MAY ponúkať **Ohodnotiť aplikáciu** a **Zdieľať aplikáciu** a SHOULD poskytovať prístup k ochrane súkromia a relevantným právnym informáciám.
- Rovnaké typy informačných a akčných riadkov na obrazovke **O aplikácii** MUST používať spoločnú geometriu `about.*`: rovnaký radius, padding, ikonový stĺpec a medzery medzi kartami.
- Základný blok metadata SHOULD obsahovať minimálne **Verzia**, **IbaJuraj Application Standard** a **Vývojár**. Odkazy a produktové položky ako **Web IbaJuraj Apps**, **Ochrana súkromia**, **Novinky**, **Stav aplikácie**, **Právne upozornenie**, **Ohodnotiť aplikáciu** alebo **Zdieľať aplikáciu** MAY byť pridané podľa produktu, ale pri rovnakej sémantickej roli MUST používať rovnaký komponentový variant.

### 6.4 Navigácia: push, modal a návrat

- Bežná vnorená obrazovka v hierarchii MUST používať natívnu push navigáciu a systémovú šípku späť, nie tlačidlo `Hotovo`.
- Na iOS MUST bežná push navigácia zachovať systémové gesto potiahnutia z ľavého okraja späť. Výnimka vyžaduje zdokumentovaný technický alebo bezpečnostný dôvod.
- Šípka aj gesto MUST viesť na tú istú predchádzajúcu obrazovku a MUST zachovať jej platný stav a pozíciu posunu.
- Ak návrat môže zahodiť neuložené zmeny, šípka aj gesto MUST vyvolať rovnaké uloženie alebo rovnaké potvrdenie následku.
- Vlastná hlavička alebo vlastné tlačidlo späť MUST NOT neúmyselne deaktivovať systémové gesto.
- `Zrušiť`, `Uložiť`, `Vytvoriť`, `Prijať` alebo obdobné akcie patria formulárom a skutočným modálnym workflow.
- `Hotovo` MUST NOT byť použité ako náhrada navigácie späť.
- Sheet alebo full-screen cover MUST byť použitý iba pre ohraničenú transakčnú úlohu, napríklad výber, editor, import, export alebo potvrdenie; MUST NOT nahrádzať bežný navigačný strom Nastavení.
- Aplikácia SHOULD minimalizovať navigačnú hĺbku a SHOULD NOT vytvárať medziobrazovku, ktorá iba sprostredkuje jednu jednoduchú voľbu alebo jediný cieľ.
- Interný cieľ otvorený push navigáciou MUST používať trailing `chevron.right`; ikona externého odkazu, napríklad `arrow.up.right.square`, MUST byť vyhradená pre URL alebo cieľ mimo aktuálneho navigačného stromu aplikácie.
- Posúvateľný obsah MAY prechádzať pod navigačnú lištu iba vtedy, ak zostáva titulok aj obsah jednoznačne čitateľný. Navigačný surface MUST zabrániť tomu, aby sa text pod lištou vizuálne prekrýval alebo súťažil s navigation title.

### 6.5 Adaptívne rozloženie

- Rozloženie MUST reagovať na reálne dostupný priestor, safe area, orientáciu, veľkosť textu a lokalizovaný obsah; MUST NOT sa rozhodovať podľa názvu konkrétneho modelu zariadenia ani podľa globálnej hodnoty `UIScreen.main.bounds`.
- Spoločné komponenty MUST používať minimálne rozmery a obsahovú výšku namiesto pevnej maximálnej výšky, ktorá môže orezať obsah.
- Obsah MUST NOT byť zmenšený pod čitateľnú veľkosť iba preto, aby sa zachoval počet stĺpcov alebo pevný tvar obrazovky.
- Viacstĺpcová mriežka MUST znížiť počet stĺpcov, ak dlaždice nedosiahnu minimálnu šírku alebo ak obsah pri Dynamic Type prestane byť čitateľný.
- Dlaždice v jednom riadku MUST mať rovnakú šírku a spoločnú minimálnu výšku; jednotlivý riadok MAY zväčšiť výšku podľa najvyššieho obsahu.
- Na veľkom displeji SHOULD obsah používať rozumnú maximálnu šírku alebo väčšie okraje namiesto nekontrolovaného rozťahovania.
- Vlastná navigácia, plávajúca akcia, klávesnica ani safe area MUST NOT zakrývať posledný obsah alebo dôležitú akciu.
- Dve rovnocenné súhrnné skratky MAY zostať vedľa seba, ak každá zachová minimálnu šírku 150 pt; pri nedostatku priestoru alebo accessibility texte MUST prejsť na vertikálne rozloženie.

### 6.6 Sémantické varianty dlaždíc a kariet

Spoločná rodina komponentov rozlišuje minimálne tieto roly:

- **Navigation Tile** – vstup do kategórie, situácie alebo hlavnej akcie,
- **Entity Card** – náhľad konkrétneho dokumentu, vozidla, poistenia alebo iného objektu,
- **Wallet Card** – vizuálny náhľad vernostnej, členskej alebo obdobnej karty,
- **Feature Card** – dominantná odporúčaná, kritická alebo produktová akcia,
- **List Row** – opakovateľný výsledok alebo položka zoznamu.
- **Summary Shortcut** – kompaktný vstup zobrazujúci názov a krátky počet alebo stav, typicky v rovnocennej dvojici,
- **Calculator Key** – doménový ovládací prvok kalkulačky s vlastnou maticou rozloženia.

- Komponenty s rovnakou sémantickou rolou SHOULD používať rovnaký veľkostný variant, odsadenie, zaoblenie, ikonový kontajner a typografickú hierarchiu.
- Komponenty s rozdielnou rolou MUST NOT byť nútené do rovnakej výšky alebo pomeru strán iba kvôli vizuálnej uniformite.
- Wallet Card MAY používať produktovo významný pomer strán, ale MUST používať spoločné pravidlá minimálnej čitateľnosti, dotykovej plochy, odsadenia a adaptácie.
- Calculator Key MAY používať produktové rozmery a typografiu, ale MUST zachovať minimálnu dotykovú plochu, accessibility label a použiteľný adaptívny variant.
- Rovnaký variant MUST zostať vizuálne konzistentný v rámci jednej mriežky alebo sekcie.
- Presné spoločné hodnoty MUST byť čítané z `DESIGN_TOKENS.md` alebo zodpovedajúcej implementácie IbaJuraj Foundation, nie opakovane zapisované v jednotlivých obrazovkách.

### 6.7 Hierarchia informácií a vizuálna hustota

Karta alebo dlaždica SHOULD zobrazovať informácie v poradí:

1. rozpoznateľná identita,
2. hlavný názov alebo stav,
3. najdôležitejší sekundárny kontext,
4. stavová alebo ďalšia akcia, ak je potrebná.

- Dôležitý názov, stav alebo akcia MUST NOT byť skrytá iba na zachovanie kompaktnej výšky.
- Technické identifikátory, úplné čísla, dlhé vysvetlenia a sekundárne metadata SHOULD zostať v detaile, ak nie sú potrebné na rozpoznanie položky.
- Stav MUST NOT byť komunikovaný iba farbou.
- Celá interaktívna dlaždica SHOULD byť jednou zrozumiteľnou dotykovou plochou; vnorené akcie musia mať samostatný význam a minimálnu dotykovú plochu.
- Na vnorenej informačnej obrazovke s inline navigation title SHOULD prvý obsahový nadpis používať `.title2` alebo nižšiu hierarchiu, pokiaľ nejde o zámerný produktový hero. Obsahový nadpis MUST NOT vizuálne súperiť s navigation title.

### 6.8 Hierarchia koreňovej pracovnej obrazovky

- Primárny root SHOULD používateľovi do troch sekúnd vysvetliť, **kde je, čo je najdôležitejší stav a čo môže urobiť ďalej**.
- Root SHOULD používať jednu dominantnú obsahovú prioritu. Viaceré rovnocenné hero bloky alebo CTA nad prvým scrollom SHOULD NOT súperiť o pozornosť.
- Ak root používa veľký title/subtitle pár, MUST používať spoločné `appPage.*` tokeny. Settings gear zostáva pravou krajnou systémovou akciou podľa 6.3.1 a 6.3.2.
- Pozdrav, informačný status, kritické upozornenie a CTA SHOULD NOT byť vrstvené do jedného komponentu, ak nesú odlišný význam.
- Rovnaká kritická informácia SHOULD NOT byť súčasne opakovaná badgeom, nadpisom, stavovým textom a CTA textom bez ďalšej informačnej hodnoty.

### 6.9 Progressive disclosure a vizuálna hustota

- MUST zobrazovať najčastejšie potrebnú informáciu skôr než zriedkavý detail.
- Sekcia SHOULD mať jeden dominantný status a najviac jedno hlavné CTA; sekundárne akcie MAY byť v riadku, `...` menu alebo obrazovke Podrobnosti.
- Podrobné právne, diagnostické, technické alebo administratívne údaje SHOULD byť dostupné bez ich povinného zobrazenia na každom roote.
- Aplikácia MUST NOT skrývať kritickú informáciu iba kvôli vizuálnemu zjednodušeniu. Progressive disclosure znižuje šum, nie dostupnosť dôležitého obsahu.

### 6.10 Search, filtre a segmented controls

- Vyhľadávacie pole s rovnakou rolou MUST používať spoločnú výšku, radius, horizontálny padding, ikonovú rolu a focus/error stav podľa `DESIGN_TOKENS.md`.
- Filtračné chips MUST mať rovnakú sémantiku aktívneho/neaktívneho stavu a minimálnu dotykovú plochu; horizontálny zoznam MAY scrollovať.
- Segmented control SHOULD byť použitý pre malý počet navzájom sa vylučujúcich pohľadov alebo režimov, nie ako náhrada rozsiahleho filtrovacieho systému.
- Filter MUST zachovať čitateľný názov aj pri lokalizácii; text MUST NOT byť zmenšovaný cez `minimumScaleFactor` ako primárne riešenie.

### 6.11 Spodná navigácia a globálne akcie

- Spodná navigácia MUST obsahovať iba hlavné pracovné oblasti produktu.
- Aktívny tab MUST byť jednoznačný ikonou aj textom alebo inou než iba farebnou zmenou.
- Centrálna dominantná akcia, napríklad `+`, MAY byť použitá iba ak je globálna, častá a významovo rovnaká z väčšiny hlavných tabov.
- Produkt MUST NOT pridávať centrálne `+` iba kvôli vizuálnej konzistencii s inou aplikáciou.
- Bottom bar MUST rešpektovať safe area, Dynamic Type a nesmie zakrývať poslednú interaktívnu položku obsahu.

### 6.12 Primary CTA, empty state a context actions

- Primárne CTA s rovnakou rolou MUST používať spoločný button variant, výšku, radius, disabled a loading stav podľa `DESIGN_TOKENS.md`.
- Empty state SHOULD obsahovať ikonu, krátky názov, najviac jednu stručnú vysvetľujúcu vetu a najviac jedno hlavné CTA.
- Kontextové menu SHOULD radiť akcie: hlavná úprava → stavová/obľúbená akcia → archivácia alebo presun → deštruktívna akcia. Produkt MAY poradie upraviť podľa doménovej priority.
- Deštruktívna akcia MUST byť vizuálne oddelená a MUST používať deštruktívnu sémantiku.

### 6.13 Badge, label, obľúbenosť a používateľské označenie

- Badge MUST byť čitateľný na aktuálnom pozadí. Implementácia MUST zvoliť adaptívny foreground/background alebo kontrastný kontajner; pevná farba indikátora MUST NOT zaniknúť na produktovom pozadí.
- Stavová hviezda, bodka alebo iná značka MUST NOT používať farbu ako jediný nositeľ významu.
- Krátke trhové alebo systémové označenie, napríklad `SK`, `CZ`, MAY byť badge.
- Ak používateľ môže mať viac objektov rovnakého typu, značky alebo trhu, produkt SHOULD ponúknuť voliteľné vlastné **Označenie** (napr. „Romanova“, „Firemná“, „Moja“).
- Vlastné označenie MUST byť používateľský text, nie uzavretý zoznam predpokladaných rolí.
- Ak označenie nie je vyplnené, komponent SHOULD uvoľniť jeho priestor namiesto zobrazovania prázdneho placeholdera.

### 6.13.1 Neutral Surface & Text Color Contract

- Základné neutrálne plochy a textové roly MUST byť vizuálne zhodné naprieč aplikáciami rodiny IbaJuraj v rovnakom appearance režime.
- Implementácia SHOULD používať sémantické systémové farby namiesto lokálnych hex hodnôt alebo voľných `.gray`, `.black.opacity(...)` a `.white.opacity(...)` pre štandardné neutrálne roly.
- `appBackground` MUST mapovať na `systemGroupedBackground` v Light Mode a `systemBackground` v Dark Mode. Referenčný výsledok je približne `#F2F2F7` / `#000000`.
- `cardSurface` / `tileSurface` MUST mapovať na `secondarySystemGroupedBackground`. Referenčný výsledok je približne `#FFFFFF` / `#1C1C1E`.
- `elevatedSurface` MAY používať ďalšiu systémovú elevated/secondary surface iba vtedy, keď ide o skutočne odlišnú vizuálnu vrstvu; MUST NOT nahrádzať základnú card/tile surface bez produktového dôvodu.
- Primárny text MUST používať `label`/`primary`; sekundárny text MUST používať `secondaryLabel`/`secondary`; separátory MUST používať sémantický `separator`.
- Produktový accent, success, warning, danger a information MAY zostať špecifické pre aplikáciu. Tieto farby MUST NOT meniť základný neutrál background/card/text kontrakt.
- Brand surfaces v Peňaženke Kariet a obdobné produktové brand plochy MAY používať vlastné farby. Text, badge, favorite indikátor a ostatné affordances na nich MUST adaptovať kontrast podľa aktuálneho surface.
- Light/Dark parity MUST byť súčasťou runtime adopčného gate: porovnávajú sa minimálne root background, card/tile surface, primary text, secondary text, separator a disabled state.
- Aplikácia MUST NOT byť označená ako plne adoptujúca Standard 1.5.1, ak rovnaká neutrálna rola používa medzi aplikáciami odlišný odtieň bez zaznamenanej výnimky.

### 6.14 Responsive layout pre iPhone a iPad

- Layout MUST vychádzať z dostupného kontajnerového priestoru, size classes a safe areas; MUST NOT byť vetvený podľa marketingového názvu zariadenia.
- iPad layout SHOULD používať rozumný `maxWidth` alebo adaptívne stĺpce, aby sa iPhone obsah iba neroztiahol na celú šírku.
- Grid MUST adaptovať počet stĺpcov podľa minimálnej šírky komponentu a Dynamic Type.
- Podporovaný iPad MUST mať runtime audit aspoň v jednej portrait a jednej landscape konfigurácii.
- Dlhý text, klávesnica, sheet a popover MUST zostať použiteľné pri Split View alebo inom zúženom kontajneri, ak ho platforma pre produkt podporuje.

### 6.15 Motion a haptics

- Animácia SHOULD vysvetľovať zmenu stavu alebo priestorový vzťah a SHOULD NOT byť dekoráciou, ktorá spomaľuje bežnú úlohu.
- Bežná mikroanimácia SHOULD používať krátku dĺžku podľa `motion.*` tokenov.
- Haptika SHOULD rozlišovať selection, success a warning/error iba tam, kde poskytuje spätnú väzbu; SHOULD NOT sa spúšťať pri každom scroll alebo pasívnom prechode.
- Reduce Motion MUST byť rešpektovaný. Kritická funkcia MUST NOT závisieť od animácie.

## 7. Obsah a texty

- MUST používať zrozumiteľný jazyk a vysvetliť odborné pojmy.
- MUST pri chybe uviesť, čo sa stalo a čo môže používateľ urobiť.
- MUST lokalizovať všetky používateľské texty; právne citácie môžu mať osobitný režim.
- MUST kontrolovať prirodzenosť prekladu, nielen doslovnú správnosť.
- MUST formátovať čísla, meny, dátumy a jednotky podľa lokality.
- Počty položiek MUST používať lokalizované plurálové pravidlá; pevné spojenie čísla s jediným tvarom podstatného mena nie je postačujúce.
- SHOULD uprednostniť krátke, konkrétne nadpisy pred marketingovými formuláciami.
- Lokalizované App Store texty a screenshoty MUST prejsť kontrolou prirodzeného znenia, gramatiky, terminológie a lokálneho formátovania; automatický alebo doslovný preklad nie je postačujúci release dôkaz.

## 8. Stavový model obrazoviek

Každá dátová obrazovka MUST podľa potreby riešiť:

1. načítavanie,
2. obsah,
3. prázdny stav,
4. chybu,
5. neúplné alebo obmedzené údaje,
6. offline stav,
7. čakajúcu synchronizáciu.

Prázdna obrazovka bez vysvetlenia nie je platný stav.

### 8.1 Spätná väzba, chyby a obnova

- Po uložení, vymazaní, importe, exporte alebo inom významnom výsledku MUST aplikácia jednoznačne oznámiť, čo sa vykonalo.
- Haptická odozva MAY dopĺňať vizuálne alebo hlasové potvrdenie, ale MUST NOT byť jediným nositeľom výsledku.
- Používateľská chyba MUST vysvetliť, čo sa stalo, čo zostalo zachované a aký je ďalší krok; MUST NOT zobrazovať neupravený technický text frameworku alebo služby.
- Opakovateľná operácia SHOULD ponúknuť akciu **Skúsiť znova**.
- Zlyhanie jednej časti SHOULD NOT zablokovať použiteľný zvyšok aplikácie.
- Ak je dostupný posledný overený bezpečný stav, aplikácia SHOULD umožniť jeho použitie namiesto prázdnej alebo nefunkčnej obrazovky.

### 8.2 Async a spracovávajúce stavy

- Asynchrónna operácia SHOULD mať explicitný stav `idle`, `processing` a výsledok `success`, `partial` alebo `failure` podľa významu funkcie.
- Počas spracovania MUST byť zrejmé, že aplikácia pracuje; MUST NOT pôsobiť zamrznuto.
- Ak opakované spustenie môže vytvoriť duplicitu alebo konflikt, príslušná akcia MUST byť počas spracovania zablokovaná alebo idempotentná.
- Po chybe SHOULD byť dostupný konkrétny ďalší krok: skúsiť znova, upraviť údaje, otvoriť Nastavenia alebo pokračovať lokálne.


## 9. Formuláre

### 9.0 Spoločný Form & Editor kontrakt

- Formulár MUST jasne rozlíšiť povinné a voliteľné údaje bez spoliehania sa iba na farbu.
- Ak je `Uložiť` deaktivované, obrazovka SHOULD používateľovi zrozumiteľne ukázať, ktorý povinný údaj chýba alebo je neplatný.
- Inline validačná správa SHOULD byť pri poli alebo skupine, ktorej sa týka; všeobecný alert sa používa pre globálnu chybu.
- Editor SHOULD používať stabilné poradie: náhľad alebo identita → základné údaje → vzhľad/zaradenie → doplnkové údaje → technické/rozšírené možnosti. Produkt MAY nepoužité sekcie vynechať.
- Výber súvisiacej entity (vozidlo, osoba, účet, karta a pod.) SHOULD používať rovnaký picker/list pattern naprieč aplikáciou.
- Bežný edit flow MUST smerovať priamo k editácii a SHOULD NOT vyžadovať zbytočné `Upraviť → detail → Upraviť`.

- MUST jasne označiť povinné údaje a dôvod, prečo sú potrebné.
- MUST zobrazovať validáciu pri konkrétnom poli.
- MUST chrániť rozpracované údaje pred neúmyselnou stratou.
- MUST používať vhodnú klávesnicu, výber dátumu a formát vstupu.
- MUST po uložení jednoznačne potvrdiť výsledok.
- SHOULD meniť polia podľa typu objektu namiesto jedného univerzálneho formulára s nerelevantnými položkami.

- MUST umožniť pohodlné skrytie klávesnice bez nutnosti opustiť obrazovku.
- IbaJuraj aplikácie SHOULD používať spoločný plávajúci ovládací prvok s ikonou klávesnice a šípkou nadol, ak je potrebné explicitné zatvorenie klávesnice; vlastné textové tlačidlo `Hotovo` nad klávesnicou SHOULD NOT byť zavedené bez produktového dôvodu.
- Scrollovateľný obsah SHOULD podporovať prirodzené interaktívne schovanie klávesnice a ukončenie fokusu tam, kde je to bezpečné pre rozpracované údaje.

### 9.1 Zachovanie rozpracovanej práce

- Rozpracované údaje MUST NOT byť stratené náhodným gestom späť, zmenou tabu, krátkym prechodom do backgroundu alebo obnovením view.
- Ak opustenie obrazovky zruší neuložené zmeny, aplikácia MUST používateľa upozorniť a pomenovať následok.
- Zmena tabu SHOULD zachovať platný stav každej hlavnej sekcie, ak produktový workflow nevyžaduje reset.
- Navigačný stav MAY byť obnovený po opätovnom spustení iba vtedy, keď cieľ stále existuje a jeho obnovenie je bezpečné.

## 10. Dáta, migrácie a kompatibilita

- MUST mať verziu dátovej schémy.
- MUST testovať aktualizáciu z verejne dostupnej App Store verzie, nie iba čistú inštaláciu.
- MUST mať migračný plán pre zmenu modelu.
- MUST zakázať tiché odstránenie nerozpoznaných alebo starších údajov.
- SHOULD poskytnúť obnovu alebo bezpečný fallback pri zlyhaní migrácie.
- MUST pri importe validovať typ, veľkosť, schému a dôveryhodnosť súboru.

### 10.1 Životný cyklus používateľských údajov

Pre každý druh uložených údajov MUST byť určené:

- kde sa ukladá,
- či a ako sa synchronizuje,
- či je súčasťou zálohy alebo exportu,
- ako sa vymaže,
- či vymazanie platí iba lokálne alebo na všetkých zariadeniach.

- Synchronizácia, záloha a export MUST byť chápané ako rozdielne funkcie; jedna z nich MUST NOT byť bez vysvetlenia prezentovaná ako náhrada ostatných.
- Deštruktívna operácia MUST pomenovať rozsah, dotknuté zariadenia a možnosť obnovy.
- Obnova MUST validovať celý vstup pred zápisom a MUST NOT uložiť čiastočný neoverený stav.
- Vypnutie synchronizácie alebo odhlásenie MUST používateľovi vysvetliť, ktoré údaje zostanú lokálne a ktoré prestanú byť dostupné.

### 10.2 Dátum, čas a časové pásmo

Ak aplikácia ukladá, zobrazuje alebo vypočítava doménové dátumy a časy:

- Dátový model MUST rozlišovať kalendárny deň od presného časového okamihu.
- Kalendárny termín MUST NOT zmeniť deň iba v dôsledku zmeny časového pásma.
- Formát dátumu a času MUST rešpektovať lokalitu a používateľský kalendár, ak doména výslovne nevyžaduje inak.
- Výpočty termínov MUST zohľadniť zmenu letného a zimného času, ak pracujú s presným časom.
- Hranice stavov **dnes**, **zajtra**, **platné** a **po termíne** MUST byť definované jedným zdrojom pravdy a testované na prechode dňa.

### 10.3 Vzdialený obsah a konfigurácia

Ak aplikácia prijíma vzdialený obsahový alebo konfiguračný balík:

- balík MUST mať stabilnú identitu, verziu schémy, verziu obsahu a údaj o kompatibilite,
- integrita a podľa rizika autenticita balíka MUST byť overená pred použitím,
- nový balík MUST byť aplikovaný atómovo a MUST NOT nahradiť platný stav čiastočným obsahom,
- aplikácia SHOULD zachovať posledný overený kompatibilný balík pre offline alebo obnovovací stav,
- nekompatibilný alebo poškodený balík MUST byť odmietnutý bez straty posledného platného stavu,
- používateľ SHOULD vedieť rozlíšiť aktuálny, zastaraný a neoverený obsah, ak to ovplyvňuje dôveryhodnosť výsledku.

## 11. Synchronizácia a zdieľanie

Ak aplikácia synchronizuje alebo zdieľa údaje, MUST rozlišovať:

- lokálny stav,
- čakajúce zmeny,
- synchronizované,
- konflikt,
- chybu,
- offline stav.

Používateľ SHOULD dostať zrozumiteľný stav, napríklad počet čakajúcich zmien alebo čas poslednej synchronizácie. Konflikty MUST NOT byť riešené tichou stratou údajov.

### 11.1 Spoločné stavy synchronizácie

Ak produkt zobrazuje používateľovi stav synchronizácie, SHOULD používať tieto významové stavy alebo ich produktovo zrozumiteľné ekvivalenty:

- **Synchronizované** – lokálny a vzdialený stav sú potvrdene zhodné,
- **Synchronizuje sa** – prebieha odosielanie alebo sťahovanie,
- **Čaká na synchronizáciu** – lokálna zmena ešte nebola potvrdená vzdialeným úložiskom,
- **Iba lokálne / Offline** – vzdialený zdroj nie je dostupný alebo nie je zapnutý,
- **Konflikt** – existujú dve nezlučiteľné verzie,
- **Chyba synchronizácie** – synchronizácia zlyhala a používateľ má dostať ďalší krok.

- Stav **Synchronizované** MUST NOT byť zobrazený iba preto, že je účet dostupný; musí vychádzať z posledného potvrdeného sync výsledku.
- Synchronizácia MUST zachovať lokálnu integritu pri zlyhaní siete.
- Manuálne `Synchronizovať teraz` MAY dopĺňať automatickú synchronizáciu, ale MUST NOT byť jediným mechanizmom, ak produkt deklaruje automatickú synchronizáciu.

## 12. Upozornenia a systémové oprávnenia

### 12.1 Upozornenia

- Pred systémovou žiadosťou o upozornenia SHOULD aplikácia vysvetliť konkrétny prínos.
- Upozornenie SHOULD viesť priamo na platný súvisiaci obsah alebo zrozumiteľný náhradný stav.
- Po zmene alebo vymazaní zdrojového objektu MUST aplikácia zrušiť alebo preplánovať neaktuálne upozornenia.
- Aplikácia MUST zabrániť neúmyselným duplicitným upozorneniam na tú istú udalosť.
- Citlivý obsah SHOULD NOT byť zobrazovaný v texte upozornenia bez vedomého používateľského nastavenia.
- Ak upozornenie nemožno naplánovať, aplikácia SHOULD používateľovi vysvetliť dôvod a možný ďalší krok.

### 12.2 Systémové oprávnenia

- Oprávnenie MUST byť vyžiadané až v kontexte funkcie, ktorá ho potrebuje.
- Pred prvou systémovou žiadosťou SHOULD aplikácia zrozumiteľne vysvetliť prínos a rozsah oprávnenia.
- Odmietnutie MUST NOT vytvoriť slepú obrazovku; aplikácia SHOULD ponúknuť použiteľnú alternatívu alebo cestu do systémových Nastavení.
- Aplikácia MUST NOT žiadať oprávnenie, ktoré aktuálny workflow nepotrebuje.

## 13. Súkromie a bezpečnosť

- MUST zdokumentovať, aké údaje nová funkcia spracúva, prečo, kde sa ukladajú a ako sa vymažú.
- MUST aktualizovať Privacy Manifest a zásady ochrany súkromia, ak sa zmení spracovanie údajov.
- Každý distribuovaný app, widget a extension target MUST obsahovať alebo zdediť správny Privacy Manifest a deklarovať iba required-reason API dôvody zodpovedajúce skutočnému používaniu.
- Release kontrola MUST porovnať používané required-reason API s obsahom všetkých distribuovaných Privacy Manifestov; prázdny manifest bez potrebných deklarácií nie je splnením pravidla.
- MUST neukladať tajné kľúče, tokeny ani osobné údaje do repozitára alebo logov.
- MUST používať Keychain pre citlivé prihlasovacie údaje a tokeny.
- MUST validovať a podľa potreby kryptograficky overovať vzdialené balíky.
- MUST zobrazovať používateľovi diagnostické údaje pred ich odoslaním.
- MUST zakázať zdieľanie citlivých údajov cez verejnú Telegram skupinu.

- Ak aplikácia ponúka lokálny zámok, biometria, voliteľný PIN aplikácie a automatické uzamknutie SHOULD tvoriť jeden konzistentný bezpečnostný model.
- Bezpečnostné nastavenia lokálneho zámku SHOULD zostať lokálne v zariadení a SHOULD NOT sa synchronizovať ani exportovať spolu s bežnými používateľskými dátami, ak na to nie je výslovný bezpečný návrh.
- Interná navigácia, prepnutie tabu, otvorenie/zatvorenie interného sheetu ani návrat z vnoreného detailu MUST NOT samy osebe spustiť nové biometrické overenie.
- Čas automatického uzamknutia SHOULD byť vyhodnocovaný podľa skutočného životného cyklu aplikácie a odchodu do neaktívneho/background stavu, nie podľa opakovaného `onAppear` jednotlivých obrazoviek.

## 14. Prístupnosť

Release kontrola MUST overiť:

- VoiceOver názvy, hodnoty a poradie,
- Dynamic Type,
- kontrast,
- Reduce Motion,
- minimálne dotykové plochy,
- význam nezávislý iba od farby,
- ovládanie bez presných gest, ak existuje dostupnejšia alternatíva.

### 14.1 Accessibility Quality Gate

- Interaktívna ikonová akcia MUST mať zmysluplný accessibility label; dekoratívna ikona SHOULD byť skrytá pred VoiceOver.
- VoiceOver poradie MUST sledovať vizuálnu a významovú hierarchiu obrazovky.
- Kritický stav MUST byť zrozumiteľný aj bez farby a animácie.
- Pri zväčšenom texte MUST zostať dostupná hlavná akcia a identita objektu; sekundárny layout MAY prejsť z horizontálneho na vertikálny.
- Release audit Level 3+ MUST overiť aspoň jeden najväčší praktický Dynamic Type režim a základný VoiceOver pre primárne flow.

## 15. Vyhľadávanie

Ak aplikácia obsahuje vyhľadávanie:

- MUST tolerovať diakritiku a bežné varianty zápisu, ak to doména umožňuje.
- SHOULD podporovať dôvodné aliasy, skratky a synonymá.
- MUST mať užitočný prázdny výsledok s ďalším krokom.
- SHOULD vysvetliť, prečo výsledok zodpovedá dotazu.
- MUST testovať výkon nad realistickým objemom údajov.

## 16. Spoločné komponenty

Komponent sa môže zaradiť do IbaJuraj Foundation, keď:

1. používa sa najmenej v dvoch aplikáciách,
2. má rovnaký účel,
3. neobsahuje doménovú logiku,
4. je stabilný aspoň počas dvoch buildov,
5. zdieľanie zníži duplicitu bez obmedzenia produktu.

Kandidáti: identita aplikácie, odkazy podpory, dizajnové tokeny, settings riadky, Navigation Tile, Entity Card, Feature Card, stavové bannery, prázdne a chybové stavy a version footer.

Pre 1.3.0 sú odporúčanými kandidátmi `IJTopActionButton`, `IJTopActionCluster`, `IJSettingsSection`, `IJSettingsRow`, `IJAppearanceControl`, `IJSupportLinks`, `IJStandardMetadata` a helper adaptívnej mriežky. Produktové karty a doménové workflow MUST zostať mimo spoločného balíka, pokiaľ nespĺňajú všetkých päť podmienok.

### 16.1 Source hygiene a veľkosť workflow súborov

- Produkčný zdrojový súbor, ktorý už nemá referenciu alebo nie je súčasťou aktívneho targetu, SHOULD byť odstránený alebo explicitne archivovaný mimo produkčného stromu.
- Workflow Swift súbor SHOULD zostať približne pod **430 riadkami**. Prekročenie nie je automatická chyba, ale SHOULD spustiť audit zodpovedností a možnosti rozdelenia.
- Root view SHOULD byť primárne composition/navigation vrstva a SHOULD NOT vlastniť rozsiahlu importnú, OCR, sync alebo doménovú logiku.
- Veľký store/model controller SHOULD byť delený podľa zodpovednosti pomocou služieb alebo focused extensions bez obchádzania enkapsulácie.
- Rozdelenie jedného typu do viacerých Swift súborov MUST rešpektovať Swift access control; stav alebo mutačné API potrebné cross-file extensionom MUST mať zámerne zvolenú internú úroveň, nie náhodne `private`.
- Source-hygiene validator MUST kontrolovať aktuálne cesty a MUST NOT úspešne prejsť iba na základe historických názvov súborov.
- Release balík SHOULD presunúť historické build audity a jednorazové validačné reporty do `Development/`, `ReleaseNotes/` alebo inej neprodukčnej histórie.

## 17. Testovanie a definícia hotovej funkcie

Funkcia je hotová až keď má:

- správny používateľský tok,
- prázdny, chybový a načítavací stav,
- lokalizáciu,
- prístupnosť,
- automatické testy primerané riziku,
- migračný test, ak mení dáta,
- privacy kontrolu,
- aktualizovanú dokumentáciu a changelog.

Historické build testy SHOULD NOT byť trvalo naviazané na konkrétne číslo buildu, ak v skutočnosti testujú funkciu.

### 17.1 Výkon a stabilita

- Dlhá operácia MUST NOT blokovať hlavné používateľské rozhranie bez viditeľného stavu priebehu.
- Scrollovanie realistického množstva údajov SHOULD zostať plynulé na najmenšom podporovanom zariadení.
- Import, synchronizácia, spracovanie príloh a vzdialený obsah SHOULD byť vykonávané mimo hlavného vlákna, ak by mohli spôsobiť viditeľné blokovanie.
- Zrušiteľná dlhá operácia SHOULD ponúknuť bezpečné zrušenie.
- View lifecycle MUST NOT bez dôvodu opakovane spúšťať drahé načítanie, zápis alebo autentifikáciu.
- Release audit MUST overiť pamäť a stabilitu pri realistických prílohách, obrázkoch alebo dátových balíkoch, ak ich produkt používa.

## 18. Release

Pred vydaním MUST byť overené:

- zhoda verzie a buildu vo všetkých metadátach,
- čistý build a testy,
- migrácia z verejnej verzie,
- odkazy podpory a súkromia,
- lokalizácie a App Store texty,
- prístupnosť,
- Privacy Manifest,
- šifrovanie a exportné nastavenia,
- odstránenie `.DS_Store`, `__MACOSX`, tajomstiev a nepotrebných archívov z distribučného ZIP-u.

- pri aplikáciách s vlastnou navigáciou kontrola šípky späť aj systémového swipe-back,
- pri textových vstupoch kontrola schovania klávesnice vrátane podporovaných klávesníc tretích strán,
- pri lokálnom zámku kontrola, že bežná interná navigácia nespúšťa opakovanú biometriu,
- kontrola, že pravé stavové hodnoty v Nastaveniach nie sú orezané ani nevhodne zalomené.
- kontrola kontaktného odkazu od aplikácie po predvyplnený webový formulár vrátane bezpečného fallbacku,
- kontrola zhody runtime verzie štandardu, tagu a úrovne adopcie s `APP_STANDARD_ADOPTION.md`,
- kontrola Privacy Manifestu pre každý distribuovaný app, widget a extension target,
- kontrola, že bežné vnorené Nastavenia nepoužívajú sheet alebo full-screen cover namiesto push navigácie.

### 18.1 Spoločná testovacia matica

Každé vydanie MUST pokryť reprezentatívne kombinácie:

- kompaktný iPhone, štandardný iPhone a veľký iPhone,
- orientáciu na výšku a, ak ju aplikácia podporuje, orientáciu na šírku,
- svetlý a tmavý vzhľad,
- bežnú a accessibility veľkosť Dynamic Type,
- všetky podporované lokalizácie so zameraním na najdlhšie texty,
- online, offline, chybový a obnovovací stav, ak aplikácia používa sieť alebo synchronizáciu,
- čistú inštaláciu a aktualizáciu z aktuálnej verejnej App Store verzie.

Pre layout audit SHOULD matica pokryť dostupnú šírku približne 320, 375 a 430 bodov. Presný model zariadenia nie je normatívny; rozhodujúca je dostupná šírka kontajnera.

Ak aplikácia deklaruje podporu iPadu, Macu alebo inej device family, release matica MUST pokryť aj jej reprezentatívnu veľkosť a vstupné metódy.

Nie je potrebné fyzicky testovať každý model zariadenia, ale zvolená matica MUST pokryť hlavné veľkostné triedy a rizikové kombinácie. Výsledok manuálneho auditu MUST byť zaznamenaný v release dokumentácii.

## 19. Model adopcie

Každá aplikácia MUST evidovať jednu z úrovní:

- **Level 0 – Declared:** existuje `APP_STANDARD_ADOPTION.md` a pripnutá verzia štandardu,
- **Level 1 – Identity:** spoločná identita, runtime verzia, podpora a verejné odkazy,
- **Level 2 – Shared UX:** spoločné Nastavenia, navigačné správanie, tokeny a nové alebo migrované komponenty,
- **Level 3 – Quality Gates:** automatické kontroly metadát, lokalizácie, prístupnosti, integrity a release dokumentácie,
- **Level 4 – Full Adoption:** v spoločnom rozsahu nezostáva nezdokumentovaná výnimka.

Názov úrovne MUST používať presne jednu z uvedených hodnôt. Vlastné názvy, napríklad `Level 2 – Enforced`, MUST NOT byť použité ako stav adopcie.

- Nová obrazovka MUST používať aktuálny prijatý štandard okamžite.
- Existujúca obrazovka MAY byť migrovaná v plánovanom builde, ak je odchýlka evidovaná a neporušuje bezpečnosť alebo integritu údajov.
- Aplikácia MUST v adopčnom súbore uviesť úroveň, posledný audit, aktívne výnimky a zdroj release dôkazov.
- Level 3 a Level 4 MUST mať uložené automatické aj manuálne release dôkazy; samotné vyhľadanie textových literálov v zdrojovom kóde nie je dostatočný dôkaz.

## 20. Živý štandard a návrhy zmien

Štandard sa môže priebežne rozširovať, ale nie nekontrolovane.

1. Audit nájde opakovaný vzor alebo nedostatok.
2. Vytvorí sa návrh v `Proposals/`.
3. Návrh uvedie dôvod, dotknuté aplikácie, migráciu a záväznosť.
4. Po schválení sa aktualizuje štandard, changelog a podľa možnosti automatická kontrola.

Automatický nástroj MUST NOT bez schválenia meniť povinné pravidlá.

## 21. Výnimky

Každá výnimka MUST uviesť:

- pravidlo,
- dotknutú aplikáciu,
- dôvod,
- rozsah,
- podmienky bezpečného použitia,
- dátum revízie alebo podmienku ukončenia.

Výnimka sa eviduje v produktovom súbore `APP_STANDARD_ADOPTION.md` alebo ADR.

## 22. Produktové doplnky

- **Strážca Termínov:** Administrative Detail Framework, Agenda ako autoritatívny systém, Progressive Completion, Action over Information, No Dead Ends.
- **Lex Drive:** Trust before Intelligence, Situation before Law, Answer before Citation, overiteľnosť právneho zdroja, účinnosť právneho stavu a auditovateľnosť.
- **Kalkulačka 2v1:** kalkulačné workflow, hlasový vstup a doménové formátovanie výsledkov zostávajú produktovo špecifické.
- **Peňaženka Kariet:** rýchly prístup ku kartám, pomer strán Wallet Card, prezentácia čiarových/2D kódov a zdieľané peňaženky zostávajú produktovo špecifické. Predvolený domovský variant MAY používať adaptívnu mriežku najviac štyroch pripnutých kariet; pripnuté karty SHOULD NOT byť duplicitne zobrazované medzi poslednými použitými.

Tieto doplnky MUST zostať produktovo špecifické a MUST NOT byť mechanicky prenášané medzi aplikáciami. Spoločné systémové vzory MAY byť do tohto štandardu zaradené až po overení rovnakej potreby vo viacerých produktoch.
