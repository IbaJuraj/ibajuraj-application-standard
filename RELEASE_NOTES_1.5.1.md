# IbaJuraj Application Standard 1.5.1

**Release date:** 13. 8. 2026  
**Tag:** `standard-v1.5.1`  
**Type:** backward-compatible patch

## Hlavná zmena

Standard 1.5.1 zavádza povinný **Neutral Surface & Text Color Contract**. Cieľom je, aby rovnaké neutrálne UI roly mali v Kalkulačke 2v1, Lex Drive, Strážcovi Termínov, Peňaženke Kariet a budúcich aplikáciách rovnaký vizuálny výsledok v Light aj Dark Mode.

## Povinné semantic roly

- App background: Light približne `#F2F2F7`, Dark `#000000`.
- Card/tile surface: Light `#FFFFFF`, Dark približne `#1C1C1E`.
- Primary text: systémový `label` / `primary`.
- Secondary text: systémový `secondaryLabel` / `secondary`.
- Separator a disabled states: systémové semantic roly.

Implementácie SHOULD preferovať systémové semantic colors pred lokálnymi hex/gray/opacity hodnotami.

## Produktové a brand farby

Produktové accent/status farby zostávajú povolené. Brandové dlaždice, napríklad v Peňaženke Kariet, môžu používať vlastný surface, ale texty, badge a favorite indikátory musia adaptovať kontrast.

## Runtime gate

Plná adopcia Standardu 1.5.1 vyžaduje Light/Dark screenshot parity audit minimálne pre root background, card/tile surface, primary text, secondary text, separators a disabled states.

## Migrácia

Žiadna dátová migrácia nie je potrebná. Aplikácie majú pri adopčnom builde upraviť iba neutrálne vizuálne tokeny a zaznamenať produktovo nevyhnutné výnimky.
