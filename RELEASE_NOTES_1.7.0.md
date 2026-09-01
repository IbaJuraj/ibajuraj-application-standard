# IbaJuraj Application Standard 1.7.0

IbaJuraj Application Standard 1.7.0 is the active shared standard for IbaJuraj apps. It was promoted from RC3 on 2 September 2026 after cross-app adoption and runtime review across Peňaženka Kariet, Strážca Termínov, Lex Drive and Kalkulačka 2v1.

The final release does not add new normative rules beyond RC3. It freezes the validated 96-rule conformance set and promotes it to the public authority under tag `standard-v1.7.0`.

Highlights:
- whole-app container-driven adaptive layout,
- safe-area-relative top, bottom and horizontal viewport utilization,
- native and custom bottom-navigation contracts,
- custom bottom bar positioned as low as safely possible,
- physical bar position separated from scroll content clearance,
- adaptive density and no unexplained fixed edge waste,
- screen-family inventory and release gate,
- state geometry stability,
- keyboard + bottom chrome coordination,
- layout performance smoke gate,
- live theme-selection behavior,
- standard About/version presentation,
- single authoritative header owner per screen,
- no duplicate navigation/page/section heading for the same semantic role,
- coherent sheet title/subtitle/dismissal hierarchy,
- platform-owned system chrome is not visually imitated by the app,
- stable `STD-*` rule IDs and shared conformance validator.

## Compatibility
1.7.0 is a backward-compatible MINOR expansion over 1.6.4. Product-specific domain models remain under application ownership. Applications adopt 1.7.0 through their own conformance declaration, automated checks and runtime evidence.

## Release decision
The RC3 contracts completed cross-app review without an observed Standard-related malfunction requiring RC4. The final tag is `standard-v1.7.0`.
