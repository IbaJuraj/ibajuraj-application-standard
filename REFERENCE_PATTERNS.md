# IbaJuraj Standard 1.6.3 – referenčné vzory

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



## Outcome-first / practical-first detail

```text
[Názov výsledku]
[hlavný stav / následok]
[čo to znamená pre používateľa]
[čo treba urobiť alebo čo nasleduje]

[Právny/technický základ ▾]
[Proces a zdroje ▾]
```

- Používateľský výsledok a praktický význam sú pred sekundárnym právnym, diagnostickým alebo procesným detailom.
- `danger`, `warning`, `success` a `information` vyjadrujú význam, nie iba veľkosť čísla.

## Dlhý katalóg so sekčným kontextom

Pinned header je vhodný iba vtedy, keď používateľ pri dlhom scrollovaní reálne stráca informáciu o aktuálnej skupine. Featured/úvodná sekcia zostáva bežne nepripnutá.

```text
[collapsing title / kompaktný navigation title]
[voliteľný pinned názov aktuálnej katalógovej skupiny]
[položka]
[položka]
[položka]
--- ďalšia skupina prirodzene nahradí pinned header ---
```

- Pinned header zostáva pod safe area/navigation surface, má vlastný semantic background a neprekrýva obsah.
- Prvý riadok skupiny nesmie byť odrezaný pod pinned headerom.
- Pinned header nesúperí s navigation title/header family.
- Rovnaký detail otvorený z katalógu, vyhľadávania alebo quick linku používa rovnaký Back + swipe-back kontrakt.
## Header family alignment

Použite jeden spoločný header pattern pre obrazovky, ktoré majú rovnakú vizuálnu identitu, aj keď niektoré obsahujú Back akciu.

```text
[leading slot / Back]   [title + subtitle anchor]   [trailing Settings/action]
                         ↑ rovnaká baseline          ↑ rovnaká centerline
```

- Home alebo iný určený root môže byť referenčnou geometriou.
- Back akcia obsadí leading slot; nesmie posúvať title ani trailing action smerom nadol.
- Nepoužívajte per-screen `padding(.top)` alebo `offset(y:)` na vizuálne dorovnávanie rovnakej header family.
- Runtime parity kontrola porovná referenčný root s aspoň jednou vnorenou obrazovkou rovnakej rodiny v Light/Dark a pri podporovanom Dynamic Type.
## Floating bottom navigation clearance

```text
[posledný obsah]
        ↕ 16–24 pt vizuálna rezerva
┌──────────────────────────────────────┐
│        floating bottom tab bar       │
└──────────────────────────────────────┘
[safe area]
```

- Celkový inset je dynamický: reálna výška tab baru + safe area + kompaktná content clearance.
- Peer root taby používajú rovnaký clearance princíp; posledný obsah je celý viditeľný bez veľkej prázdnej plochy.

## Rotating content pattern – MAY

```text
spustenie/relácia A → [téma 1] [téma 2] [téma 3] [téma 4]
ďalší definovaný cyklus → [téma 5] [téma 6] [téma 1] [téma 7]
```

- Sada je počas relácie stabilná.
- Bez duplicít v jednej sade.
- Rotácia je deterministická alebo kontrolovaná.
- Dôležité položky sa nestratia dlhodobo mimo zobrazovaných sád.

## Verified AI / generated answer

```text
[otázka používateľa]
        ↓
[retrieval / resolver nad autoritatívnymi dátami]
        ↓
[overené podklady + identita/verzia]
        ↓
[AI zrozumiteľné vysvetlenie]
        ↓
[zdrojový detail / pokračovanie / feedback]

Ak podklady nestačia:
[doplňujúca otázka] alebo [bezpečný fallback] alebo [nahlásiť chýbajúcu odpoveď]
```

- AI vysvetlenie nenahrádza autoritatívny zdroj pravdy.
- Pri nízkej istote sa nesmie zobraziť nesúvisiaci „najbližší“ výsledok ako definitívna odpoveď.
- Feedback môže predvyplniť otázku a diagnostický kontext, ale používateľ musí obsah pred odoslaním vidieť a nič sa neodosiela automaticky.
