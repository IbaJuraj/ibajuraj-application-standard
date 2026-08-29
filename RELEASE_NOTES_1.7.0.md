# IbaJuraj Application Standard 1.7.0 – Release Candidate 3

RC3 hardens the 1.7.0 adaptive foundation after whole-app review of real app screens. It retains the RC2 viewport and screen-family contracts and adds explicit single-header ownership, duplicate-heading prevention, coherent sheet-header hierarchy, and platform system-chrome ownership.

Highlights:
- single authoritative header owner per screen,
- no duplicate navigation/page/section heading for the same semantic role,
- coherent sheet title/subtitle/dismissal hierarchy,
- platform-owned system chrome is not visually imitated by the app,
- whole-app container-driven adaptive layout,
- root header anchored to live top safe area with minimal shared extra inset,
- native vs custom bottom navigation,
- custom bottom bar positioned as low as safely possible,
- physical bar position separated from scroll content clearance,
- horizontal max-width/density adaptation,
- no unexplained fixed edge waste,
- screen-family inventory and release gate,
- state geometry stability,
- keyboard + bottom chrome coordination,
- layout performance smoke gate,
- live theme-selection behavior,
- standard About/version presentation,
- stable `STD-*` rule IDs and shared conformance validator.

RC3 is not yet the public authoritative release. The current public authority remains 1.6.4 until promotion and final tag `standard-v1.7.0`.
