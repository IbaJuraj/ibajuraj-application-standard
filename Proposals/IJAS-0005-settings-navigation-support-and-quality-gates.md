# IJAS-0005 – Navigácia Nastavení, podpora a quality gates 1.3

**Stav:** implemented  
**Navrhovateľ:** IbaJuraj  
**Dátum:** 2026-08-10  
**Dotknuté aplikácie:** Kalkulačka 2v1, Lex Drive, Strážca Termínov, Peňaženka Kariet  
**Navrhovaná verzia štandardu:** 1.3.0

## Problém

Po prijatí 1.2.0 zostali medzi aplikáciami rozdiely v hlavičke, navigácii vnorených Nastavení, dlhých trailing hodnotách, obrazovke Kontakt, runtime metadátach, privacy manifestoch a reálnej kvalite adopčných dôkazov.

## Dôkazy a príklady

Kalkulačka zaviedla vhodný kompaktný header variant, ale deklarovala ešte nevydanú verziu. Lex Drive poskytol vhodný priamy Vzhľad a kompaktný Kontakt. Strážca používal pre bežné settings ciele prevažne sheet/full-screen cover. Peňaženka rozhodovala o variante layoutu cez `UIScreen`. Statické validátory pritom všetky aplikácie označili ako vyhovujúce.

## Navrhované pravidlo

Standard zavádza spoločný header action kontrakt, priamy Vzhľad, push navigáciu so šípkou aj swipe-back, kompaktný Kontakt, runtime metadata z jedného zdroja, responzívne texty, privacy gate každého distribuovaného targetu a merateľné release dôkazy.

**Záväznosť:** MUST pre bezpečnosť, navigačnú konzistenciu a pravdivé metadata; SHOULD pre odporúčaný vizuálny variant a poradie voliteľných sekcií.

## Rozsah

Spoločný štandard vlastní systémové roly a ich správanie. Produkt vlastní doménové nastavenia, obsah sekcie **Čo môžete poslať**, produktové karty a workflow.

## Migrácia

Migrácia nevyžaduje zmenu používateľských dát. Aplikácie auditujú hlavičku, settings prezentácie, spätnú navigáciu, kontaktný deep-link, runtime metadata, layout logiku, adopčný názov a privacy manifesty podľa `MIGRATION.md`.

## Kompatibilita a riziká

Pôvodný 48 pt settings entry z 1.2.0 zostáva platný. Preferovaný 42 pt vizuál je zavedený ako rozsah 42–48 pt, aby minor aktualizácia nebola breaking change. Rizikom je falošná zhoda pri textových validátoroch; preto 1.3 vyžaduje runtime dôkazy.

## Automatická kontrola

Kontrola overí metadata a presný enum adopcie, SHA-256 integritu, povinné dokumenty a release evidenciu. Produktové testy majú doplniť kontrolu zakázaného `UIScreen` layoutu, modal settings destinácií, privacy manifestov a kontaktného URL toku. Manuálna matica overí gestá, Dynamic Type a VoiceOver.

## Rozhodnutie

**Výsledok:** implemented  
**Odôvodnenie:** Potreba a spoločné riešenie boli potvrdené vo všetkých štyroch aplikáciách.  
**Schválená verzia:** 1.3.0
