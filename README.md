# IbaJuraj Application Standard 1.7.0

IbaJuraj Application Standard 1.7.0 is the active shared standard for IbaJuraj apps.

It was promoted from RC3 after cross-app adoption and runtime review across Peňaženka Kariet, Strážca Termínov, Lex Drive and Kalkulačka 2v1. No new normative rules were added during final promotion; the final release preserves the validated RC3 rule set.

## Main areas
- whole-app container-driven adaptive layout,
- safe-area-relative viewport utilization,
- native/custom bottom-navigation contracts,
- screen-family inventory and release gates,
- shared Settings/About and live appearance behavior,
- single header ownership and duplicate-heading prevention,
- coherent sheet headers,
- platform system-chrome ownership,
- machine-verifiable `STD-*` conformance.

## Validate this package

```bash
bash Checks/validate-standard.sh
python3 Checks/validate-conformance-catalog.py
python3 -m unittest Checks/test_validate_app_conformance.py
```

## Validate an adopting app

```bash
python3 Checks/validate-app-conformance.py \
  --app-root /path/to/app \
  --standard-root /path/to/standard
```

The app must provide `STANDARD_CONFORMANCE.json` including `screenAudit.families`.

## Release
Final release tag: `standard-v1.7.0`.
