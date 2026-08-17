# IbaJuraj Application Standard 1.6.0

**Status:** Final  
**Date:** 2026-08-17

## Scope

1. **About metadata** – app version and build remain user-visible; Standard is user-visible only as `Verzia X.Y.Z`. Internal adoption level, tag and runtime/audit state stay in technical metadata.
2. **Compact detail summaries** – `Na prvý pohľad`/summary sections must be proportionate to their information value and must not unnecessarily delay the primary next action.
3. **Settings entry on every primary root** – a user must not switch primary tabs only to reach system Settings; the shared `gearshape.fill` entry remains the rightmost system header action.
4. **State and CTA clarity** – the same domain state uses consistent user-facing terminology across root/list/detail, technical signed values are translated into natural wording, and a unique critical object should deep-open directly when appropriate.
5. **Primary-root header alignment** – primary roots share one vertical title/header baseline and consistent trailing Settings geometry.
6. **Floating-action safety** – overlay/FAB actions must not obscure content, trailing controls, tab bars or required touch targets.

## Compatibility

Backward-compatible MINOR update. No domain-data migration is required.

## Final normative package

For the final 1.6.0 release, `IBAJURAJ_APPLICATION_STANDARD.md` and `STANDARD_1.6.0_FINAL_AMENDMENT.md` together form the normative Standard. The final amendment contains the last RC2/RC3 runtime decisions and prevails if it conflicts with the base 1.6.0 text.

## Release gate

Final RC3 runtime verification passed on **Strážca Termínov v1.55 Build 78**. The 1.6.0 content is approved for the final `standard-v1.6.0` release.
