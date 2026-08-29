# IbaJuraj Application Standard 1.7.0 RC2 – Release Checklist

## Standard package
- [ ] `STANDARD_VERSION` = `1.7.0`
- [ ] `standard.json` version = `1.7.0`, candidate = `RC2`
- [ ] `CONFORMANCE_CATALOG.json` valid
- [ ] all catalog rule IDs unique
- [ ] every MUST/MUST NOT rule in RC2 delta has a catalog entry
- [ ] validator supports `allCapabilities` and screen-family gate
- [ ] validator unit tests PASS
- [ ] `Checks/validate-standard.sh` PASS
- [ ] `Checks/validate-conformance-catalog.py` PASS
- [ ] ZIP integrity PASS
- [ ] SHA-256 generated

## App adoption
- [ ] `APP_STANDARD_ADOPTION.md` updated
- [ ] `STANDARD_CONFORMANCE.json` present
- [ ] all capability flags accurate
- [ ] `screenAudit.families` covers every applicable family
- [ ] each family lists concrete screens
- [ ] applicable MUST rules have evidence/test/runtime gate or ADR exception
- [ ] localization parity PASS
- [ ] About contract PASS
- [ ] live appearance PASS if custom themes exist
- [ ] whole-app adaptive + viewport matrix PASS
- [ ] root-header top anchors use shared family token
- [ ] no unexplained edge waste
- [ ] bottom navigation contract PASS if applicable
- [ ] custom bar position separate from content clearance
- [ ] keyboard/bottom chrome coordination PASS if applicable
- [ ] state geometry stability PASS
- [ ] layout performance/lag smoke test PASS
- [ ] privacy/debug/release hygiene PASS
- [ ] native Xcode build/test PASS
- [ ] physical/runtime acceptance PASS

## Promotion RC → active
- [ ] all four target apps have completed RC2 adoption/audit or documented approved exceptions
- [ ] remaining contract ambiguities resolved
- [ ] `standard.json.status` changed to `active`
- [ ] `candidate` removed/null
- [ ] RC wording removed from main document/README
- [ ] final tag prepared: `standard-v1.7.0`
