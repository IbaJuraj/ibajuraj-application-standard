# Návrhy zmien

Tento priečinok obsahuje návrhy na zmenu IbaJuraj Application Standardu.

## Stav návrhu
- `proposed` – čaká na posúdenie,
- `accepted` – schválený, ešte nemusí byť vydaný ako finálny aktívny Standard,
- `rejected` – zamietnutý,
- `superseded` – nahradený novším návrhom,
- `implemented` – zahrnutý do vydanej aktívnej verzie Standardu.

## Proces
1. Skopírujte `TEMPLATE.md`.
2. Popíšte opakovaný problém a dotknuté aplikácie.
3. Navrhnite MUST, MUST NOT, SHOULD, SHOULD NOT alebo MAY.
4. Uveďte migráciu, riziká a možnosti automatickej kontroly.
5. Po schválení aktualizujte Standard, conformance catalog a changelog.
6. Pri RC môže byť návrh `accepted`; na `implemented` sa zmení až po finálnej publikácii príslušnej aktívnej verzie.

## Aktuálne 1.8.0 RC1
- `IJAS-0025-localization-first-architecture-and-territory-independence.md` – **accepted for Standard 1.8.0 RC1**; localization-first architektúra, locale-aware formatting/pluralization, in-app language selector contract, locale-neutral persistence identity, localized search parity a oddelenie runtime jazykov od App Store území.
- `IJAS-0026-release-package-root-hygiene-and-build-history-archive.md` – **accepted for Standard 1.8.0 RC1**; čistota release rootu a archivácia supersedovaných build/runtime dokumentov bez straty historického dôkazu.
- `IJAS-0027-single-device-development-release-data-continuity.md` – **accepted for Standard 1.8.0 RC1**; stabilná lokálna identita a bezpečné striedanie Xcode ↔ TestFlight/App Store pri oddelených Development/Production backend väzbách.
- `IJAS-0028-production-backend-environment-readiness.md` – **accepted for Standard 1.8.0 RC1**; Production schema/config/permissions readiness, reálny TestFlight smoke a rozlíšenie server-side vs binary fixu.

## Staršie rozhodnutia
- `IJAS-0006-shared-settings-support-about-geometry.md` – accepted; family-wide geometria Nastavení, Kontakt a O aplikácii pre 1.4.0.
- `IJAS-0008-family-interaction-density-and-source-hygiene.md` – accepted for Standard 1.5.0.
- `IJAS-0009-neutral-surface-and-text-color-contract.md` – accepted for Standard 1.5.1.
- `IJAS-0010-user-selected-theme-surface-and-accent-contrast.md` – implemented in Standard 1.5.2.
- `IJAS-0012-header-family-alignment-contract.md` – implemented in Standard 1.6.2.
- `IJAS-0013-navigation-surface-clearance-and-pinned-header-eligibility.md` – implemented in Standard 1.6.3.
- `IJAS-0014-verified-ai-generated-assistance-and-feedback.md` – implemented in Standard 1.6.3.
- `IJAS-0015-authoritative-data-traceability-and-safe-relevance.md` – implemented in Standard 1.6.3.
- `IJAS-0016-runtime-regression-and-debug-isolation.md` – implemented in Standard 1.6.3.
