# IbaJuraj Standard 1.5.1 – testovacia matica

Táto matica je spoločný minimálny release dôkaz. Produkt MAY pridať rizikové kombinácie podľa svojich funkcií.

## Povinné prostredia

| Oblasť | Minimálne pokrytie |
|---|---|
| Dostupná šírka | približne 320, 375 a 430 pt |
| Orientácia | portrait; landscape, ak ju aplikácia podporuje |
| Vzhľad | Automaticky, Svetlý, Tmavý |
| Dynamic Type | default, XXL, accessibility XXXL |
| Lokalizácia | všetky podporované jazyky; dôraz na najdlhšie texty |
| Sieť | online, offline, chyba a obnova, ak sa používa sieť |
| Inštalácia | čistá inštalácia a aktualizácia z verejnej verzie |
| Vstup | dotyk, VoiceOver a podporované klávesnice |

## Typografia hlavnej pracovnej obrazovky

- [ ] Hlavný root title používa `.largeTitle.weight(.bold)` bez lokálnej pevnej bodovej veľkosti.
- [ ] Podnadpis používa `.subheadline`, sekundárnu farbu a prirodzené zalomenie.
- [ ] Medzera title/subtitle je 6 pt.
- [ ] Title/subtitle pár je side-by-side typograficky zhodný s referenčnou IbaJuraj aplikáciou.
- [ ] Default, XXL a accessibility XXXL nespôsobujú orezanie alebo použitie `minimumScaleFactor`.

## Navigácia a Nastavenia

- [ ] Gear je vpravo hore na hlavnej úvodnej obrazovke a má accessibility label **Nastavenia**.
- [ ] Gear je pravou krajnou akciou a jedna strana hlavičky nemá viac než dve samostatné akcie.
- [ ] Root Nastavení sa otvorí push navigáciou.
- [ ] Každá bežná vnorená obrazovka podporuje systémovú šípku aj swipe-back.
- [ ] Šípka a gesto vedú na rovnaký cieľ a zachovajú stav aj pozíciu posunu.
- [ ] Neuložené zmeny majú rovnaké bezpečné správanie pri šípke aj geste.
- [ ] Sheet/full-screen cover sa používa iba pre transakčné workflow.
- [ ] Vzhľad je priamo v root Nastavení a zmena sa prejaví bez reštartu.
- [ ] Dlhé trailing hodnoty sa presunú pod názov alebo zalomia bez zmenšenia textu.
- [ ] Posúvaný obsah nepresvitá cez navigačný titulok ani s ním vizuálne nesúperí.
- [ ] Interný push prechod používa chevron; externý odkaz používa `arrow.up.right.square`.
- [ ] Settings row má pri rovnakom obsahu rovnakú základnú výšku naprieč aplikáciami; používa 16/10 pt padding, 36 × 36 pt ikonovú dlaždicu a `minHeight` 56 pt.
- [ ] Padding settings row sa aplikuje pred `frame(minHeight:)`; nevzniká dodatočná výška spôsobená opačným poradím modifierov.
- [ ] Segmented **Vzhľad** má rovnakú výšku a odsadenie vo všetkých aplikáciách, ktoré ho používajú.

## Kontakt a O aplikácii

- [ ] Kontakt obsahuje formulár, sekundárny Telegram a upozornenie na citlivé údaje.
- [ ] Kontaktný odkaz predvyplní správnu aplikáciu a typ podnetu na webe.
- [ ] Neplatné query parametre majú bezpečný fallback a formulár sa nikdy neodošle automaticky.
- [ ] Chyba otvorenia externého odkazu je zrozumiteľná a ponúka alternatívu.
- [ ] Verzia a build na obrazovke O aplikácii zodpovedajú `Bundle`.
- [ ] Verzia, tag a úroveň adopcie štandardu zodpovedajú `APP_STANDARD_ADOPTION.md`.
- [ ] Kontaktné akčné karty používajú rovnakú geometriu: 16 pt padding, 42 × 42 pt ikona, 20 pt radius a 12 pt medzera.
- [ ] About metadata a akčné karty používajú rovnakú geometriu: 18 pt radius, 16 pt padding, 24 pt ikonový stĺpec a 12 pt medzera medzi akciami.
- [ ] Side-by-side screenshot audit Nastavenia / Kontakt / O aplikácii neukazuje rozdiel v základnej hustote rovnakých komponentov.

## Layout a dlaždice

- [ ] Rozloženie nereaguje na názov zariadenia ani `UIScreen.main.bounds`.
- [ ] Navigačná mriežka zachová minimálnu šírku 150 pt alebo prejde na menej stĺpcov.
- [ ] Accessibility text má funkčný jednostĺpcový variant.
- [ ] Rovnaký variant v jednom riadku má rovnakú výslednú výšku.
- [ ] Dvojica súhrnných skratiek je kompaktná, rovnocenná a pri nedostatku priestoru sa adaptívne zloží pod seba.
- [ ] Tri a viac rovnocenných informačných riadkov sú zoskupené do jednej karty s čitateľnými oddeľovačmi.
- [ ] Obsahový nadpis vnoreného informačného detailu nesúperí s navigačným titulkom.
- [ ] Wallet Card zachová produktový pomer strán a Calculator Key minimálnu hit area.
- [ ] Posledný obsah nie je zakrytý tab barom, klávesnicou ani safe area.

## Prístupnosť

- [ ] VoiceOver číta názov, hodnotu, stav a hint kľúčových ovládacích prvkov.
- [ ] Fokus má logické poradie.
- [ ] Žiadny stav nie je komunikovaný iba farbou.
- [ ] Reduce Motion, Increase Contrast a Reduce Transparency nespôsobia stratu funkcie.
- [ ] Každý interaktívny prvok má minimálnu dotykovú plochu 44 × 44 pt.
- [ ] Počty položiek používajú správne plurálové tvary pre 0, 1, 2–4 a 5+ podľa podporovaného jazyka.

## Privacy a distribúcia

- [ ] Každý distribuovaný app, widget a extension target má správny Privacy Manifest.
- [ ] Required-reason API deklarácie zodpovedajú reálnemu používaniu.
- [ ] Citlivé údaje, tokeny ani kľúče nie sú v logoch alebo repozitári.
- [ ] Používateľ vidí diagnostické údaje pred odoslaním.
- [ ] Build a automatické testy prešli bez nevyriešeného release blokátora.

## Záznam výsledku

Výsledok MUST uvádzať dátum, verziu aplikácie, build, testované prostredia, meno auditora, nálezy, výnimky a odkazy na screenshoty alebo logy. Prázdny checklist bez dôkazov nie je platný Level 3 alebo Level 4 audit.


## 1.5.0 – doplňujúce scenáre

- [ ] Root: jedna dominantná priorita je pochopiteľná do približne 3 sekúnd.
- [ ] Root: kritický stav neopakuje rovnakú informáciu vo viacerých konkurenčných vrstvách.
- [ ] Search/filter: rovnaké roly majú konzistentnú geometriu a focus state.
- [ ] Empty state: max. jedno hlavné CTA a žiadny slepý koniec.
- [ ] Context menu: destructive action je oddelená a správne pomenovaná.
- [ ] Badge/favorite: kontrast je čitateľný na svetlom, tmavom aj brand surface.
- [ ] User label: prázdna hodnota nerezeruje riadok; dlhá hodnota bezpečne skracuje/zalamuje podľa variantu.
- [ ] Form: disabled Save má viditeľnú príčinu.
- [ ] Async: processing/success/failure je zrozumiteľný a nedá sa nebezpečne duplikovať operácia.
- [ ] Sync: „Synchronizované“ sa zobrazí iba po potvrdenom výsledku.
- [ ] iPad: portrait + landscape, max-width/adaptive grid, klávesnica/popover podľa funkcie.
- [ ] Reduce Motion + selection/success/warning haptics podľa relevantnosti.
- [ ] VoiceOver order + veľký Dynamic Type pre primárne flow.
- [ ] Source hygiene: audit >430 riadkov, unused files a zastaraných validator paths.
- [ ] Cross-file extension refactor: Xcode build overí access-control mutability a visibility.
## 1.5.1 – Light/Dark Neutral Parity Gate

Pre každú aplikáciu a každý podporovaný appearance režim:

- [ ] Root/background surface používa spoločný `color.appBackground`.
- [ ] Card/tile surface používa spoločný `color.cardSurface`.
- [ ] Primary text má rovnakú sémantickú rolu a vizuálnu intenzitu.
- [ ] Secondary text má rovnakú sémantickú rolu a vizuálnu intenzitu.
- [ ] Separator a disabled states sú sémantické, nie lokálne custom gray.
- [ ] Light Mode screenshot parity bola porovnaná s referenčnou aplikáciou.
- [ ] Dark Mode screenshot parity bola porovnaná s referenčnou aplikáciou.
- [ ] Brand surface výnimky majú čitateľný adaptívny kontrast.
- [ ] Odchýlka má explicitnú `STANDARD_EXCEPTION.md`, ak je produktovo nevyhnutná.

