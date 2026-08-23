# IJAS-0006 – Spoločná geometria Nastavení, Kontakt a O aplikácii

**Stav:** Accepted
**Cieľová verzia:** 1.4.0
**Dátum:** 13. augusta 2026

## Problém

Aplikácie používali rovnaké názvy, grouped-card štýl a ikonový jazyk, ale lokálne implementácie sa líšili vo výške riadkov, poradí SwiftUI modifierov, segmented controle Vzhľad a spacingu obrazoviek Kontakt/O aplikácii. V runtime porovnaní preto jedna aplikácia pôsobila kompaktnejšie než druhá.

## Rozhodnutie

Rovnaké sémantické komponenty sa zjednocujú pomocou presných spoločných tokenov. Produkt smie meniť obsah a počet položiek, nie základnú geometriu rovnakého variantu.

Referenčné hodnoty boli overené na runtime implementácii Lex Drive a následne prenesené do Strážcu Termínov, Kalkulačky 2v1 a Peňaženky Kariet. Štandard ich kodifikuje ako family-wide kontrakt, nie ako závislosť od jednej aplikácie.

## Kompatibilita

Zmena je spätne kompatibilná a nezasahuje do používateľských dát. Vyžaduje iba vizuálny/component audit, preto patrí do MINOR verzie.
