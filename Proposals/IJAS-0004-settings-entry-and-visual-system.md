# IJAS-0004 – Spoločný vstup a vizuálny systém Nastavení

**Stav:** implemented
**Navrhovateľ:** IbaJuraj
**Dátum:** 2026-08-09
**Dotknuté aplikácie:** Strážca Termínov, Lex Drive, Peňaženka Kariet, Kalkulačka 2v1
**Navrhovaná verzia štandardu:** 1.2.0

## Problém

Nastavenia používajú medzi aplikáciami rozdielny vstup, navigačný model a vizuálny systém. Kalkulačka používa modal a veľké kapsuly, Lex Drive mieša systémové Nastavenia s obrazovkou Moje a Strážca s Peňaženkou používajú pre Nastavenia pracovný spodný tab.

## Dôkazy a príklady

Strážca Termínov a Peňaženka Kariet už poskytujú overený grouped-card základ, ikonové dlaždice a priamy výber Vzhľadu. Lex Drive má správne umiestnenú ikonu vpravo hore. Spoločná potreba je potvrdená vo všetkých štyroch aplikáciách.

## Navrhované pravidlo

Nastavenia MUST byť dostupné cez `gearshape.fill` vpravo hore na hlavnej obrazovke. Spodná navigácia MUST obsahovať iba hlavné pracovné časti. Nastavenia MUST používať samostatnú push obrazovku a spoločný grouped-card vizuálny systém. Výber Vzhľadu MUST byť priamy segmented control.

**Záväznosť:** MUST

## Rozsah

Spoločný štandard vlastní vstup, navigačné správanie, geometrické tokeny, row komponenty, chevrony, status hodnoty a základnú sekčnú architektúru. Produkt vlastní konkrétne položky a môže vynechať nerelevantné sekcie.

## Migrácia

- Kalkulačka presunie ikonu vpravo, odstráni modal **Zavrieť** a prijme grouped-card obrazovku.
- Lex Drive oddelí systémové Nastavenia od Moje; história, obľúbené a právny kontext zostanú produktové.
- Strážca odstráni Nastavenia zo spodného tabu a pridá ikonu vpravo hore.
- Peňaženka odstráni Nastavenia zo spodnej navigácie a pridá ikonu vpravo hore.

## Kompatibilita a riziká

Zmena nemení používateľské dáta ani doménové modely. Mení vstupný bod a môže znížiť počet spodných tabov. Rizikom je strata návykov existujúcich používateľov; spoločná poloha vpravo hore je však stabilný a ľahko rozpoznateľný cieľ.

## Automatická kontrola

Statická kontrola môže overiť symbol, absenciu settings tabu a používanie spoločných tokenov. Runtime audit overí polohu, pressed state, push navigáciu, swipe-back, Dynamic Type a segmented Vzhľad.

## Rozhodnutie

**Výsledok:** implemented
**Odôvodnenie:** Rovnaký systémový problém a spoločné riešenie sa potvrdili vo všetkých aplikáciách IbaJuraj.
**Schválená verzia:** 1.2.0
