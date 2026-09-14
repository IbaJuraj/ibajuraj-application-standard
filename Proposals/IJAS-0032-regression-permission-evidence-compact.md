# IJAS-0032 — Regression, Permission, Evidence and Compact Surfaces

**Status:** accepted for 1.8.0 RC2.

Adds:
- `STD-TEST-001` — automated regression coverage for material deterministic engines,
- `STD-PERM-001` — disabled feature and permission parity,
- `STD-EVIDENCE-001` — build-scoped runtime evidence and regression traceability,
- `STD-COMPACT-001` — compact-surface content priority and destination integrity.

The proposal explicitly distinguishes a temporarily disabled feature from dead code: source may remain behind a flag, but user-facing entry points and permission prompts must match actual availability.
