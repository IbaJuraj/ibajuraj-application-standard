# IbaJuraj Application Standard 1.7.0 – Release Checklist

## Standard package
- [ ] `STANDARD_VERSION` = `1.7.0`
- [ ] `standard.json` version = `1.7.0`
- [ ] `CONFORMANCE_CATALOG.json` valid
- [ ] all catalog rule IDs unique
- [ ] every MUST/MUST NOT rule in 1.7.0 delta has a catalog entry
- [ ] `Checks/validate-standard.sh` PASS
- [ ] `Checks/validate-conformance-catalog.py` PASS
- [ ] ZIP integrity PASS
- [ ] SHA-256 generated

## App adoption
- [ ] `APP_STANDARD_ADOPTION.md` updated
- [ ] `STANDARD_CONFORMANCE.json` present
- [ ] all capability flags accurate
- [ ] applicable MUST rules have evidence/test/runtime gate or ADR exception
- [ ] localization parity PASS
- [ ] About contract PASS
- [ ] live appearance PASS if custom themes exist
- [ ] whole-app adaptive matrix PASS
- [ ] bottom navigation contract PASS if applicable
- [ ] privacy/debug/release hygiene PASS
- [ ] native Xcode build/test PASS
- [ ] physical/runtime acceptance PASS

## Promotion RC → active
- [ ] at least one reference app adopted RC without requiring semantic contract redesign
- [ ] remaining ambiguities resolved
- [ ] `standard.json.status` changed to `active`
- [ ] RC wording removed from main document/README
- [ ] tag prepared: `standard-v1.7.0`
