# IbaJuraj Standard 1.5.1 – referenčné vzory

Referenčné vzory vysvetľujú spoločnú informačnú hierarchiu. Nie sú pixelovým screenshot testom a nemenia produktovú identitu aplikácie.

## Hlavná obrazovka

```text
┌──────────────────────────────────────┐
│ Názov alebo logo       [akcia] [⚙︎] │
│ Krátky produktový popis              │
│                                      │
│ Primárny produktový obsah            │
└──────────────────────────────────────┘
```

- Hlavný názov používa `appPage.title` = `.largeTitle.weight(.bold)`.
- Priamy podnadpis používa `appPage.subtitle` = `.subheadline` so sekundárnou farbou; medzera medzi nimi je 6 pt.
- Gear je vpravo hore a je pravou krajnou akciou.
- Vedľa gearu je najviac jedna samostatná sekundárna akcia.
- Produkt MAY používať ľavý alebo stredový názov, ak zostane chránený pred kolíziou.

## Root Nastavení

```text
‹  Nastavenia

APLIKÁCIA
┌──────────────────────────────────────┐
│ Vzhľad                               │
│ [Automaticky] [Svetlý] [Tmavý]       │
├──────────────────────────────────────┤
│ Produktové nastavenie       hodnota ›│
└──────────────────────────────────────┘

ÚDAJE A ZABEZPEČENIE
┌──────────────────────────────────────┐
│ Záloha                             › │
│ Export údajov                      › │
└──────────────────────────────────────┘

POMOC A INFORMÁCIE
┌──────────────────────────────────────┐
│ Kontakt                            › │
│ O aplikácii              1.0 (1)   › │
└──────────────────────────────────────┘
```

- Root MAY použiť veľký titulok; vnorené stránky SHOULD používať inline titulok.
- Hodnota sa pri nedostatku priestoru presunie pod názov.
- Settings row používa 16 pt horizontálny + 10 pt vertikálny padding, 36 × 36 pt ikonovú dlaždicu a minimálnu výslednú výšku 56 pt; padding sa aplikuje pred `minHeight`.
- Karta Vzhľad používa 16 pt horizontálny padding, 10 pt horný/spodný padding okolo header/segmentu a segmented control s minimálnou 44 pt dotykovou výškou.
- Rovnaký komponent MUST mať v rôznych IbaJuraj aplikáciách rovnakú základnú geometriu; rozdielny obsah smie výšku zväčšiť iba prirodzeným zalomením.

## Kontakt

```text
‹  Kontakt

Ako vám môžeme pomôcť?
Krátke vysvetlenie podľa aplikácie.

┌──────────────────────────────────────┐
│ Otvoriť kontaktný formulár          ↗│
└──────────────────────────────────────┘
┌──────────────────────────────────────┐
│ Telegram komunita                   ↗│
└──────────────────────────────────────┘

ČO MÔŽETE POSLAŤ
• otázku alebo návrh,
• technický problém,
• produktovo relevantnú nepresnosť.

Neposielajte heslá, doklady ani citlivé údaje.
```

- Akčné karty používajú 16 pt vnútorný padding, 42 × 42 pt ikonový box s radiusom 12 pt, card radius 20 pt a 12 pt medzeru medzi hlavnými akciami.
- Celý obsah používa 16 pt page inset a 18 pt vertikálnu hustotu medzi hlavnými blokmi.

## O aplikácii

```text
‹  O aplikácii

┌──────────────────────────────────────┐
│ Verzia                       1.0 (1) │
│ IbaJuraj Application Standard  1.4.0 │
└──────────────────────────────────────┘
┌──────────────────────────────────────┐
│ Ohodnotiť aplikáciu                  │
│ Zdieľať aplikáciu                    │
└──────────────────────────────────────┘
```

Hodnoty sú runtime metadata, nie ručne duplikované reťazce.

- Metadata a akčné karty používajú 18 pt radius a 16 pt padding; ikonový stĺpec má 24 pt.
- Medzera medzi samostatnými About akciami je 12 pt, hlavný screen spacing 18 pt a page inset 20 pt.
- Produkt MAY pridať vlastné About položky, ale nesmie meniť geometriu spoločného variantu.

## Súhrnné skratky

```text
┌──────────────────┐ ┌──────────────────┐
│ História         │ │ Obľúbené         │
│ 30 položiek      │ │ 1 položka        │
└──────────────────┘ └──────────────────┘
```

- Dve rovnocenné skratky SHOULD zostať vedľa seba, ak má každá aspoň minimálnu šírku.
- Pri väčšom texte alebo nedostatku priestoru sa MUST adaptívne zložiť pod seba.
- Počet MUST používať lokalizované plurálové pravidlá.

## Informačná skupina a odkazy

```text
┌──────────────────────────────────────┐
│ Informácia A                         │
├──────────────────────────────────────┤
│ Informácia B                         │
├──────────────────────────────────────┤
│ Interný detail                     › │
│ Externý zdroj                      ↗ │
└──────────────────────────────────────┘
```

- Tri a viac rovnocenných vysvetľujúcich riadkov SHOULD tvoriť jednu grouped kartu.
- Interný push prechod používa chevron; externý odkaz používa `arrow.up.right.square`.
- Navigačný surface MUST zabrániť presvitaniu posúvaného obsahu cez inline titulok.


## 1.5.0 – Root / Search / Empty / Editor / Badge patterns

### Root
1. app title + krátky subtitle + systémová akcia,
2. jedna dominantná úloha alebo stav,
3. sekundárne skratky/sekcie,
4. detail cez push alebo context action.

### Search + filtre
1. jeden search field,
2. segmented view switch iba pre malé množstvo režimov,
3. horizontálne chips pre kategórie/stavy,
4. výsledky s jasným count/statusom iba ak pomáha rozhodnutiu.

### Empty state
Ikona → krátky title → jedna veta → jedno CTA.

### Editor
Náhľad/identita → základné údaje → zaradenie/vzhľad → voliteľné údaje → technické možnosti. Disabled Save má mať vysvetliteľnú príčinu.

### Badge / user label
Market badge (`SK`, `CZ`) môže dopĺňať identitu, ale nenahrádza používateľské Označenie (`Romanova`, `Firemná`, `Moja`). Badge aj favorite indicator musia adaptovať kontrast na surface.
## 1.5.1 – Neutral surface pattern

Referenčná hierarchia neutrálnej obrazovky:

1. root background = `color.appBackground`,
2. grouped card/tile = `color.cardSurface`,
3. hlavný text = `color.textPrimary`,
4. pomocný text = `color.textSecondary`,
5. divider = `color.separator`,
6. product accent iba pre význam/akciu, nie ako náhrada neutrálnej vrstvy.

Light a Dark variant tej istej obrazovky musia meniť iba appearance mapovanie sémantických rolí, nie lokálnu logiku farieb.

