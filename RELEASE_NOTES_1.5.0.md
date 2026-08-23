# IbaJuraj Application Standard 1.5.0

**Release date:** 13. 8. 2026
**Tag:** `standard-v1.5.0`
**Compatibility:** backward-compatible MINOR release

## Hlavná myšlienka

**Jedna rodina aplikácií, nie jedna šablóna aplikácie.** Verzia 1.5.0 zjednocuje ovládanie, geometriu, význam stavov a kvalitu základných komponentov, ale zachováva identitu Lex Drive, Strážcu Termínov, Peňaženky Kariet, Kalkulačky 2v1 a budúcich produktov.

## Nové spoločné oblasti

- root screen hierarchy a jedna dominantná priorita,
- progressive disclosure a content-density pravidlá,
- search/filter/segmented controls,
- bottom navigation a globálne CTA,
- primary CTA, empty states a context actions,
- adaptívne badge/label kontrasty a používateľské označenia,
- Form & Editor kontrakt,
- async a sync states,
- iPad/responsive layout,
- motion/haptics a Reduce Motion,
- Accessibility Quality Gate,
- source hygiene a ~430-line workflow review threshold.

## Dôležité kompatibilitné pravidlo

1.5.0 nevyžaduje, aby aplikácie vyzerali identicky. Spoločné MUST/SHOULD pravidlá sa týkajú rovnakých sémantických rolí. Produktová farba, doménový obsah, počet tabov a špecifické hero komponenty ostávajú produktové rozhodnutia.

## Migrácia

Žiadna dátová migrácia nie je potrebná iba kvôli štandardu 1.5.0. Aplikácie majú vykonať UX, accessibility, responsive a source-hygiene audit podľa `MIGRATION.md`.

## Release gate

Pred Level 3/4 adopciou musí byť uložený manuálny runtime dôkaz vrátane relevantných iPhone/iPad konfigurácií, Dynamic Type, VoiceOver, async/sync stavov a refaktorovaných cross-file Swift extensionov.
