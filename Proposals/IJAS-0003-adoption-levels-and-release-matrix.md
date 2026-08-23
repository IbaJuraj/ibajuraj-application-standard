# IJAS-0003 – Úrovne adopcie a release testovacia matica

**Stav:** implemented
**Navrhovateľ:** IbaJuraj
**Dátum:** 2026-08-09
**Dotknuté aplikácie:** všetky aplikácie IbaJuraj
**Navrhovaná verzia štandardu:** 1.2.0

## Problém

Samotné číslo prijatého štandardu nehovorí, ktoré spoločné komponenty a quality gates aplikácia reálne používa. Release audit zároveň potrebuje reprezentatívne pokrytie displejov, lokalizácií, prístupnosti a sieťových stavov.

## Dôkazy a príklady

Jednotlivé aplikácie prijímajú spoločné Nastavenia, tokeny, bezpečnosť a kontroly postupne. Natívny Xcode a fyzický runtime audit nemusia byť dokončené v rovnakom okamihu ako statická adopcia.

## Navrhované pravidlo

Každá aplikácia MUST evidovať úroveň adopcie Level 0 až Level 4 a každé vydanie MUST zdokumentovať reprezentatívnu testovaciu maticu.

**Záväznosť:** MUST

## Rozsah

Úrovne opisujú iba spoločný rozsah IbaJuraj Standardu. Nenahrádzajú produktové testy ani App Store release rozhodnutie.

## Migrácia

Existujúci `APP_STANDARD_ADOPTION.md` sa rozšíri o úroveň adopcie, foundation verziu, produktový štandard a release dôkazy.

## Kompatibilita a riziká

Zmena nevyžaduje dátovú migráciu. Rizikom je deklarovanie vyššej úrovne bez dôkazov; preto je súčasťou šablóny odkaz na testy a manuálny audit.

## Automatická kontrola

Validátor overí prítomnosť verzie, tagu a úrovne v adopčnej šablóne. Produktové CI môže kontrolovať konkrétny adopčný súbor.

## Rozhodnutie

**Výsledok:** implemented
**Odôvodnenie:** Úrovne umožnia pravdivo odlíšiť deklaráciu, spoločné UX a plnú adopciu.
**Schválená verzia:** 1.2.0
