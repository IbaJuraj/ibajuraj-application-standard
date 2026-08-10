# IbaJuraj Standard 1.3.0 – testovacia matica

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

## Kontakt a O aplikácii

- [ ] Kontakt obsahuje formulár, sekundárny Telegram a upozornenie na citlivé údaje.
- [ ] Kontaktný odkaz predvyplní správnu aplikáciu a typ podnetu na webe.
- [ ] Neplatné query parametre majú bezpečný fallback a formulár sa nikdy neodošle automaticky.
- [ ] Chyba otvorenia externého odkazu je zrozumiteľná a ponúka alternatívu.
- [ ] Verzia a build na obrazovke O aplikácii zodpovedajú `Bundle`.
- [ ] Verzia, tag a úroveň adopcie štandardu zodpovedajú `APP_STANDARD_ADOPTION.md`.

## Layout a dlaždice

- [ ] Rozloženie nereaguje na názov zariadenia ani `UIScreen.main.bounds`.
- [ ] Navigačná mriežka zachová minimálnu šírku 150 pt alebo prejde na menej stĺpcov.
- [ ] Accessibility text má funkčný jednostĺpcový variant.
- [ ] Rovnaký variant v jednom riadku má rovnakú výslednú výšku.
- [ ] Wallet Card zachová produktový pomer strán a Calculator Key minimálnu hit area.
- [ ] Posledný obsah nie je zakrytý tab barom, klávesnicou ani safe area.

## Prístupnosť

- [ ] VoiceOver číta názov, hodnotu, stav a hint kľúčových ovládacích prvkov.
- [ ] Fokus má logické poradie.
- [ ] Žiadny stav nie je komunikovaný iba farbou.
- [ ] Reduce Motion, Increase Contrast a Reduce Transparency nespôsobia stratu funkcie.
- [ ] Každý interaktívny prvok má minimálnu dotykovú plochu 44 × 44 pt.

## Privacy a distribúcia

- [ ] Každý distribuovaný app, widget a extension target má správny Privacy Manifest.
- [ ] Required-reason API deklarácie zodpovedajú reálnemu používaniu.
- [ ] Citlivé údaje, tokeny ani kľúče nie sú v logoch alebo repozitári.
- [ ] Používateľ vidí diagnostické údaje pred odoslaním.
- [ ] Build a automatické testy prešli bez nevyriešeného release blokátora.

## Záznam výsledku

Výsledok MUST uvádzať dátum, verziu aplikácie, build, testované prostredia, meno auditora, nálezy, výnimky a odkazy na screenshoty alebo logy. Prázdny checklist bez dôkazov nie je platný Level 3 alebo Level 4 audit.
