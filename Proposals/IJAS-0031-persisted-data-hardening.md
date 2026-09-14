# IJAS-0031 — Persisted Data Hardening

**Status:** accepted for 1.8.0 RC2.

Adds:
- `STD-DATA-006` — corrupt persisted state fails safely without destructive empty overwrite,
- `STD-DATA-007` — destructive deletion is relationship-aware,
- `STD-DATA-008` — persisted-data apps have a production-to-candidate upgrade-path gate.

The proposal generalizes data-safety findings from real app audits and complements the RC1 continuity contract.
