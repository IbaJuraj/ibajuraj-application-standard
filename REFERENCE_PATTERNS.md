# IbaJuraj Standard 1.3.0 – referenčné vzory

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

## O aplikácii

```text
‹  O aplikácii

┌──────────────────────────────────────┐
│ Verzia                       1.0 (1) │
│ IbaJuraj Application Standard  1.3.0 │
└──────────────────────────────────────┘
┌──────────────────────────────────────┐
│ Ohodnotiť aplikáciu                  │
│ Zdieľať aplikáciu                    │
└──────────────────────────────────────┘
```

Hodnoty sú runtime metadata, nie ručne duplikované reťazce.
