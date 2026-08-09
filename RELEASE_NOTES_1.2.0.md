# IbaJuraj Application Standard 1.2.0

Spätne kompatibilná minor aktualizácia spoločného autoritatívneho štandardu aplikácií IbaJuraj.

## Hlavné zmeny

- jednotný vstup do Nastavení cez `gearshape.fill` vpravo hore; systémové Nastavenia už nepatria do spodnej pracovnej navigácie,
- spoločný grouped-card vizuál Nastavení, ikonové dlaždice, section headers, chevrony, stavové hodnoty a priamy segmented prepínač Vzhľadu,
- adaptívne rozloženie podľa dostupného priestoru, orientácie, lokalizácie a Dynamic Type,
- spoločné sémantické varianty navigačných dlaždíc, entitných kariet, vernostných kariet, feature kariet a zoznamových riadkov,
- minimálne namiesto pevne uzamknutých rozmerov a adaptívny počet stĺpcov,
- spoločná hierarchia informácií, dizajnové tokeny a pravidlá vizuálnej hustoty,
- spätná väzba po akcii, zrozumiteľné chyby, obnova a ochrana rozpracovaných údajov,
- pravidlá životného cyklu údajov, dátumov a časových pásiem, upozornení a systémových oprávnení,
- výkonové a stabilitné očakávania,
- úrovne adopcie a rozšírená release testovacia matica,
- opravená release infraštruktúra, GitHub workflow, SHA-256 integrita a automatická validácia.

## Kompatibilita

Verzia 1.2.0 nemení produktové doménové modely ani hlavné produktové workflow a nevyžaduje migráciu používateľských dát. Môže však znížiť počet spodných tabov odstránením systémových Nastavení a presunúť ich pod spoločné tlačidlo vpravo hore.

Nové obrazovky používajú pravidlá 1.2.0 okamžite. Existujúce obrazovky sa auditujú v najbližšom plánovanom builde a dočasné odchýlky sa evidujú v `APP_STANDARD_ADOPTION.md`.

Aplikácie majú používať konkrétny tag `standard-v1.2.0`.
