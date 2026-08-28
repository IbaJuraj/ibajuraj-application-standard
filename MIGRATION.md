# Migration – IbaJuraj Application Standard 1.6.4 → 1.7.0

1. Keep all 1.6.4 requirements unless explicitly superseded.
2. Update local Standard snapshot/pin to 1.7.0 RC during adoption work.
3. Add `STANDARD_CONFORMANCE.json` from template.
4. Declare capabilities: appearance, custom themes, bottom-navigation mode, iPad, sync, generated assistance.
5. Add evidence for every applicable MUST/MUST NOT rule.
6. Align Settings → O aplikácii with the shared row and About cards.
7. Add common accessibility/test IDs for shared system surfaces.
8. Audit appearance selection for immediate same-screen update.
9. Replace device-name/`UIScreen` layout foundations with container-driven geometry where possible.
10. Run small/regular/large + Dynamic Type + localization matrix.
11. Declare native/custom/none bottom navigation and apply corresponding contract.
12. Add unit/UI tests or explicit runtime gates where static evidence is insufficient.
13. Run common validator and generate release conformance report.
14. Do not claim Level 4 while a release-blocking runtime gate is pending.

No domain data migration is required solely because of Standard 1.7.0.
