# IbaJuraj Application Standard 1.7.0 RC2

This package is Release Candidate 2 for the next shared IbaJuraj app standard.

Current published authority: **1.6.4**.  
Candidate: **1.7.0 RC2**.

RC2 supersedes RC1 for further app adoption. It keeps the RC1 adaptive/navigation/conformance foundation and adds explicit viewport-edge utilization, screen-family inventory/audit, keyboard/chrome coordination, state stability and layout-performance gates.

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

## Promotion
After RC2 adoption validates the contracts, remove RC wording, set `standard.json.status` to `active`, clear the candidate marker, set release date and publish tag `standard-v1.7.0`.
