# Návrhy zmien

Tento priečinok obsahuje návrhy na zmenu IbaJuraj Application Standardu.

## Stav návrhu

Každý návrh používa jeden zo stavov:

- `proposed` – čaká na posúdenie,
- `accepted` – schválený, ešte nemusí byť vydaný,
- `rejected` – zamietnutý,
- `superseded` – nahradený novším návrhom,
- `implemented` – zahrnutý do vydanej verzie štandardu.

## Názov súboru

```text
IJAS-0001-strucny-nazov.md
```

Číslo je jedinečné a nemení sa.

## Proces

1. Skopírujte `TEMPLATE.md`.
2. Popíšte opakovaný problém a dotknuté aplikácie.
3. Navrhnite MUST, MUST NOT, SHOULD, SHOULD NOT alebo MAY.
4. Uveďte migráciu, riziká a možnosti automatickej kontroly.
5. Po schválení aktualizujte štandard a changelog.

- `IJAS-0006-shared-settings-support-about-geometry.md` – Accepted; presná family-wide geometria Nastavení, Kontakt a O aplikácii pre 1.4.0.

- `IJAS-0008-family-interaction-density-and-source-hygiene.md` – accepted for Standard 1.5.0.
- `IJAS-0009-neutral-surface-and-text-color-contract.md` – accepted for Standard 1.5.1.
- `IJAS-0010-user-selected-theme-surface-and-accent-contrast.md` – implemented in Standard 1.5.2.
- `IJAS-0012-header-family-alignment-contract.md` – Header Family Alignment Contract (implemented in Standard 1.6.2)
- `IJAS-0013-navigation-surface-clearance-and-pinned-header-eligibility.md` – implemented in Standard 1.6.3.
- `IJAS-0014-verified-ai-generated-assistance-and-feedback.md` – implemented in Standard 1.6.3.
- `IJAS-0015-authoritative-data-traceability-and-safe-relevance.md` – implemented in Standard 1.6.3.
- `IJAS-0016-runtime-regression-and-debug-isolation.md` – implemented in Standard 1.6.3.
