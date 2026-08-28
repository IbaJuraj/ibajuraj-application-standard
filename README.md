# IbaJuraj Application Standard 1.7.0 RC1

This package is the release candidate for the next shared IbaJuraj app standard.

Current published authority: **1.6.4**.  
Candidate: **1.7.0 RC1**.

## New in 1.7.0
- whole-app adaptive layout,
- common bottom-navigation variants,
- cross-app About/version parity,
- live theme selection,
- machine-verifiable conformance with stable rule IDs.

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

The app must provide `STANDARD_CONFORMANCE.json`.

## Promotion
After real app adoption validates the contracts, remove RC wording, set `standard.json.status` to `active`, set release date and publish tag `standard-v1.7.0`.
