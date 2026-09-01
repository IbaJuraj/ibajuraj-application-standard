# Migration – IbaJuraj Application Standard 1.6.4 → 1.7.0

1. Keep all 1.6.4 requirements unless explicitly superseded.
2. Update the local Standard snapshot/pin to final 1.7.0 (`standard-v1.7.0`).
3. Add/update `STANDARD_CONFORMANCE.json` from the 1.7.0 template.
4. Declare capabilities including search/details/forms/sheets/fullscreen/onboarding/state surfaces and bottom-navigation mode.
5. Add `screenAudit.families` with concrete screen names for every applicable family.
6. Add evidence for every applicable MUST/MUST NOT rule.
7. Align Settings → O aplikácii with the shared row and About cards.
8. Add common accessibility/test IDs for shared system surfaces and root/nested chrome.
9. Audit appearance selection for immediate same-screen update.
10. Replace device-name/`UIScreen` layout foundations with container-driven geometry where possible.
11. Audit top/root anchors, bottom chrome placement, horizontal bounds and unexplained edge waste.
12. For custom bottom navigation, separate physical bar position from scroll content clearance.
13. Run small/regular/large + Dynamic Type + localization + system-overlay matrix.
14. Audit keyboard/form coordination and prevent double bottom reserve.
15. Audit empty/loading/populated/error geometry stability.
16. Run layout performance smoke test for scrolling, tab switching and live theme changes.
17. Audit single header ownership, duplicate page/section headings, sheet header hierarchy and platform system-chrome ownership.
18. Add unit/UI tests or explicit runtime gates where static evidence is insufficient.
19. Run common validator and generate release conformance report.
20. Do not claim Level 4 while a release-blocking rule or screen family is pending.

No domain data migration is required solely because of Standard 1.7.0.
