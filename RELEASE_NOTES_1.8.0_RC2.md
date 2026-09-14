# IbaJuraj Application Standard 1.8.0 RC2

**Candidate date:** 12 September 2026  
**Candidate tag:** `standard-v1.8.0-rc2`  
**Stable authority remains:** `standard-v1.7.0`

## Summary
RC2 is the first fully integrated machine-readable candidate in the 1.8 line.

It preserves the exact 96-rule stable baseline metadata, formalizes the 12 commitments published in RC1 release notes, and adds 11 cross-app hardening rules from Strážca Termínov and Kalkulačka 2v1 audits.

**Total: 119 rules.**

## RC2 additions
- stale async completion protection,
- deterministic derived-state rebuild ordering,
- cloud remote-truth semantics,
- durable access/share reconciliation,
- corrupt persisted-state recovery,
- relationship-aware deletion,
- production→candidate upgrade gate,
- deterministic-engine automated regressions,
- disabled-feature/permission parity,
- exact-build runtime evidence,
- compact-surface priority and destination integrity.

## Important integration note
RC1 release notes claimed 108 rules, while its tagged core machine files remained at stable 1.7.0/96. RC2 closes that gap explicitly; see `RC1_INTEGRATION_GAP_AUDIT.md`.

## Publication model
RC2 is a GitHub prerelease candidate, not the stable/latest authority. Final `standard-v1.8.0` remains gated by cross-app applicability and runtime closure.
