# IbaJuraj Application Standard 1.3.1

## Zameranie vydania

Patch 1.3.1 uzatvára vizuálne a navigačné zistenia z finálneho auditu Lex Drive. Zachováva architektúru 1.3.0 a dopĺňa presné pravidlá pre čitateľné vnorené obrazovky a kompaktné informačné rozhrania.

## Hlavné zmeny

- navigačný surface musí chrániť titulok pred presvitajúcim alebo prekrývajúcim sa posúvaným obsahom,
- interný prechod používa chevron a externý odkaz symbol `arrow.up.right.square`,
- tri a viac rovnocenných informačných riadkov sa zoskupujú do jednej karty s oddeľovačmi,
- dvojica rovnocenných súhrnných skratiek používa kompaktný adaptívny variant,
- vnorený obsahový nadpis používa `.title2` alebo nižšiu úroveň, ak nejde o zámerný hero obsah,
- počty položiek sa lokalizujú podľa plurálových pravidiel podporovaného jazyka.

## Kompatibilita

Verzia 1.3.1 je spätne kompatibilná patch aktualizácia. Nevyžaduje migráciu používateľských dát. Aplikácie vykonajú UX audit podľa `MIGRATION.md`, aktualizujú adopčné metadata a uložia release dôkazy.

## Autoritatívny tag

Aplikácie majú po publikovaní používať konkrétny tag `standard-v1.3.1` a presnú lokálnu kópiu vydania.
