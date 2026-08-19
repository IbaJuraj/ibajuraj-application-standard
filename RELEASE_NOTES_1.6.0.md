# IbaJuraj Application Standard 1.6.0

**Status:** Final  
**Date:** 2026-08-17

## Scope

1. **About metadata** – app version and build remain user-visible; Standard is user-visible only as `Verzia X.Y.Z`. Internal adoption level, tag and runtime/audit state stay in technical metadata.
2. **Compact detail summaries** – `Na prvý pohľad`/summary sections must be proportionate to their information value and must not unnecessarily delay the primary next action.
3. **Settings entry on every primary root** – a user must not switch primary tabs only to reach system Settings; the shared `gearshape.fill` entry remains the rightmost system header action.
4. **State and CTA clarity** – the same domain state uses consistent user-facing terminology across root/list/detail, technical signed values are translated into natural wording, and a unique critical object should deep-open directly when appropriate.

## Compatibility

Backward-compatible MINOR update. No domain-data migration is required.

## Release gate

RC3 runtime verification passed on Strážca Termínov v1.55 Build 78. The 1.6.0 content is approved for the final `standard-v1.6.0` release.

## Final RC3 alignment
- Primary roots now MUST share one root-title vertical baseline and common header top inset.
- The trailing Settings action follows the same root header geometry so tab switches do not visibly shift title/action position.
