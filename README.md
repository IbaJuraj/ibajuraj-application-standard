# IbaJuraj Application Standard 1.8.0 RC1

IbaJuraj Application Standard **1.8.0 RC1** is the current release candidate for the next shared Standard.

The active public authority remains **1.7.0** (`standard-v1.7.0`) until RC1 completes cross-app adoption and is promoted to final 1.8.0.

## What 1.8.0 RC1 adds
- localization-first architecture with stable semantic localization keys,
- locale-aware formatting/pluralization and localized search parity,
- optional in-app language selector contract with Automatic/System mode,
- locale-neutral persisted identifiers and transport metadata,
- independence of runtime languages from App Store storefront availability,
- release-package root hygiene and build-history archiving,
- single-device Xcode ↔ TestFlight/App Store data continuity,
- Development/Production backend identity separation,
- Production backend/schema/config readiness gate,
- real TestFlight/Production backend smoke testing,
- representative real-volume data performance gate.

All **96 rules from 1.7.0 remain preserved**. RC1 adds **12 new stable rule IDs**, for a total of **108 rules**.

## Primary RC1 adoption
1. Peňaženka Kariet
2. Strážca Termínov
3. representative applicability audit in Lex Drive and Kalkulačka 2v1

## Validate this candidate

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

The app must provide `STANDARD_CONFORMANCE.json` including capability flags, rule evidence and `screenAudit.families`.

## Release status
- Active stable: `standard-v1.7.0`
- RC candidate: `standard-v1.8.0-rc1`
- Candidate branch: `standard-1.8.0-rc1`
- Final `standard-v1.8.0` must not be created until the RC promotion gate is complete.
