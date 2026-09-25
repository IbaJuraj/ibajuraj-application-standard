# IbaJuraj Application Standard 1.9.0 RC3

**Candidate date:** 25 September 2026  
**Stable authority remains:** 1.8.0 (`standard-v1.8.0`)  
**Proposed candidate tag:** `standard-v1.9.0-rc3`

RC3 preserves the 131-rule RC2 candidate and adds three machine-readable AI rules for **134 rules total**.

## Central change

AI governance is consolidated into **seven coherent contracts** rather than many overlapping rules.

- `STD-AI-001` — grounded & verified AI assistance.
- `STD-AI-002` — user transparency, fallback & feedback.
- `STD-AI-003` — advisory, explainable, read-only-by-default AI.
- `STD-AI-004` — privacy, minimization & secret handling.
- `STD-AI-005` — provider/runtime & graceful fallback.
- `STD-AI-006` — untrusted input/output, evaluation & rollback.
- `STD-AI-007` — controlled adaptation, learning memory & human reset.

## On-device and cloud

The Standard is provider-neutral. Apple Foundation Models / Core AI are reference on-device implementations for Apple platforms, not mandatory technologies.

On-device is preferred when quality is sufficient and it materially improves privacy, availability, latency or cost. Supplemental cloud AI remains optional and must fail safely.

## Release Inspector

Deterministic Release Inspector remains the authority for PASS/FAIL. AI may explain, prioritize and suggest fixes, but cannot independently convert a deterministic failure into PASS.

## Controlled self-learning

Adaptive AI may improve from confirmed signals, but learned memory is separate from authoritative data, changes are versioned/reversible and material learned rules require validation/human confirmation before activation.

## Pilot

TradeBook is the first intended RC3 pilot.
