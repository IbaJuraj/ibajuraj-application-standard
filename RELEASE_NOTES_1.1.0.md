# IbaJuraj Application Standard 1.1.0

Spätne kompatibilná minor aktualizácia spoločného autoritatívneho štandardu aplikácií IbaJuraj.

## Hlavné zmeny

- jednotnejšie systémové Nastavenia a pomenovanie spoločných funkcií,
- minimálna navigačná hĺbka,
- pravidlá push vs. modal,
- povinné zachovanie iOS swipe-back pri bežnej vnorenej navigácii,
- spoločný spôsob schovania klávesnice,
- krátke a čitateľné stavové hodnoty v Nastaveniach,
- priamy Kontakt bez zbytočného medzikroku,
- spoločný model biometrie, voliteľného PIN-u a automatického uzamknutia,
- lifecycle pravidlá zabraňujúce opakovanému Face ID pri internej navigácii,
- nové release kontroly pre tieto systémové UX oblasti.

## Kompatibilita

Verzia 1.1.0 nemení produktové doménové modely, počet tabov ani produktovo špecifické workflow. Samotná adopcia 1.1.0 nevyžaduje migráciu používateľských dát.

Aplikácie majú používať konkrétny tag `standard-v1.1.0` a prijatie evidovať v `APP_STANDARD_ADOPTION.md`.
