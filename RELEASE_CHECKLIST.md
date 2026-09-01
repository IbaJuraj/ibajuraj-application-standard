# IbaJuraj Application Standard 1.7.0 – Final Release Checklist

## Standard package
- [x] `STANDARD_VERSION` = `1.7.0`
- [x] `standard.json` version = `1.7.0`
- [x] `standard.json.status` = `active`
- [x] release date = `2026-09-02`
- [x] candidate marker cleared
- [x] `CONFORMANCE_CATALOG.json` contains the final 96-rule set
- [x] all catalog rule IDs unique
- [x] validator supports `allCapabilities` and screen-family gate
- [x] source hygiene gate retained
- [x] final release notes and 1.6.4 → 1.7.0 audit present

## Cross-app promotion gate
- [x] Peňaženka Kariet reviewed against RC3 contracts
- [x] Strážca Termínov reviewed against RC3 contracts
- [x] Lex Drive reviewed against RC3 contracts
- [x] Kalkulačka 2v1 reviewed against RC3 contracts
- [x] final cross-app runtime review completed by the product owner
- [x] no observed Standard-related malfunction/regression requiring RC4
- [x] remaining contract ambiguities resolved for 1.7.0
- [x] RC wording removed from the active main document and README

Application-specific `STANDARD_CONFORMANCE.json`, Xcode, runtime, localization, accessibility and screen-family evidence remain owned by each adopting app. A static Standard-repository PASS does not replace those app-level runtime gates.

## Final repository validation
- [x] `bash Checks/validate-standard.sh` PASS on the final promotion head
- [x] `python3 -m unittest Checks/test_validate_app_conformance.py` PASS on the final promotion head
- [x] GitHub Actions `Validate IbaJuraj Standard` PASS on the final promotion head
- [x] post-merge GitHub Actions validation PASS on final `main`

Evidence:
- final promotion head: `3078997e3aa590cf65a9deecd49de141ff00393c`
- final PR validation: workflow run `33566068474` — SUCCESS
- final merge commit: `14c7bc08f5de17d3234f55201ad81021a1ca8fa4`
- post-merge validation: workflow run `33566091242` — SUCCESS

Detailed evidence is recorded in `FINAL_RELEASE_AUDIT_1.7.0.md`.

## Publication
- [x] final tag name prepared: `standard-v1.7.0`
- [x] final release PR #7 merged into `main`
- [ ] tag `standard-v1.7.0` created from final `main`
- [ ] GitHub Release `IbaJuraj Application Standard 1.7.0` published
- [ ] `/standard/` verified against the final release

Draft PR #6 was closed without merge after the GitHub connector could not perform the Draft → Ready transition. It had no comments or reviews. Final non-draft PR #7 used the identical validated head and was merged successfully.

The merge is intentionally completed before tag publication. Tag/release publication is the next step.
