# IbaJuraj Standard 1.3.1 – release checklist

## Metadata a zdroj pravdy

- [ ] `STANDARD_VERSION`, `standard.json`, dokumenty a adopčný súbor majú zhodnú verziu.
- [ ] Tag má tvar `standard-v1.3.1` a existuje v autoritatívnom repozitári.
- [ ] Marketingová verzia a build aplikácie sa načítavajú z build nastavení alebo `Bundle`.
- [ ] Runtime verzia, tag a úroveň adopcie pochádzajú z jedného zdroja.
- [ ] Nevydaná verzia nie je prezentovaná ako aktívne prijatá.

## Spoločný UX kontrakt

- [ ] Nastavenia sú vpravo hore na hlavnej úvodnej obrazovke a nie sú samostatným tabom.
- [ ] Vzhľad používa priamy segmented control, ak ho aplikácia podporuje.
- [ ] Kontakt a O aplikácii sú v poslednej sekcii Pomoc a informácie.
- [ ] Bežné vnorené obrazovky používajú push, systémovú šípku a swipe-back.
- [ ] Sheet/full-screen cover zostal iba pre transakčné workflow.
- [ ] Settings riadky používajú spoločné tokeny a responzívne trailing hodnoty.
- [ ] Navigačná plocha chráni inline titulok pred presvitaním alebo prekrývaním posúvaného obsahu.
- [ ] Interné a externé prechody používajú odlišné sémantické indikátory.
- [ ] Informačné riadky a súhrnné skratky používajú zodpovedajúci grouped a adaptívny variant.

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
