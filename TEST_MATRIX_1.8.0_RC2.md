# IbaJuraj Application Standard 1.8.0 RC2 — Test Matrix

## Standard package
- catalog count/uniqueness = 119
- first 96 inherited rule objects preserve 1.7.0 applicability/verification metadata
- 12 formalized RC1 rules present
- 11 RC2 rules present
- version/candidate/stable-authority parity
- schema/template compatibility
- releaseBlocking semantics for RC2 MUST/MUST NOT rules
- main Standard ↔ catalog rule-ID parity
- package hygiene

## App adoption additions
- stale async completion ordering
- authoritative mutation → coherent derived-state rebuild
- remote failure does not show false success
- access/share interruption → relaunch reconciliation
- corrupted persisted-state recovery
- relationship deletion blocker/cascade/detach semantics
- current production → candidate upgrade data preservation
- automated deterministic-engine regression suite
- disabled feature has no active entry point and no permission prompt
- runtime evidence records exact app version/build/device/OS/date
- compact surface readability/content priority/specific destination

## Evidence rule
Static source inspection cannot close a runtime-only requirement. Runtime evidence is valid only for the exact tested app build and Standard version unless an explicit evidence carry-forward rule is documented and justified.
