# IbaJuraj Application Standard 1.8.0 RC2

This branch contains the **1.8.0 RC2 release candidate**. The stable public authority remains **1.7.0** until the final 1.8.0 promotion gate is complete.

RC2 is the first fully integrated machine-readable candidate in the 1.8 line:
- 96 exact stable 1.7.0 rule objects,
- 12 formalized commitments from the published RC1 scope,
- 11 new RC2 hardening rules,
- **119 rules total**.

Main new areas: localization-first architecture, Development/Production data continuity, Production backend readiness, async/derived-state integrity, cloud mutation truth/reconciliation, persisted-state recovery, upgrade continuity, deterministic regression coverage, disabled-feature permission parity, build-scoped evidence and compact surfaces.

## Validate this candidate

```bash
bash Checks/validate-standard.sh
python3 Checks/validate-conformance-catalog.py
python3 -m unittest Checks/test_validate_app_conformance.py
```

## Stable authority
Stable release tag: `standard-v1.7.0`.

## Candidate publication
Candidate tag: `standard-v1.8.0-rc2`.
RC2 is a prerelease and must not be treated as `Latest`/stable before cross-app runtime closure.

---

## 1.7.0 baseline
IbaJuraj Application Standard 1.7.0 was promoted from RC3 after cross-app adoption and runtime review across Peňaženka Kariet, Strážca Termínov, Lex Drive and Kalkulačka 2v1. Its validated 96-rule baseline remains the inherited foundation for RC2.
