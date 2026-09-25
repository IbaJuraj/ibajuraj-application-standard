# IJAS-0036 — AI Runtime, Provider Safety & Controlled Adaptation

**Status:** accepted  
**Target:** IbaJuraj Application Standard 1.9.0 RC3  
**Date:** 2026-09-25

## Problem

The existing Standard already contains verified AI assistance and RC2 AI release-review safeguards, but it does not fully define provider/runtime selection, on-device versus cloud behavior, AI credential handling, untrusted prompt/input boundaries, structured-output validation, model/prompt regression, rollback or controlled self-learning.

Adding a separate rule for every detail would create overlapping contracts and make applicability difficult to maintain.

## Decision

Keep the existing identities `STD-AI-001` through `STD-AI-004`, clarify their scopes, and add only three new rules:

- `STD-AI-005` — Provider, runtime & graceful fallback.
- `STD-AI-006` — Untrusted input/output, evaluation & rollback.
- `STD-AI-007` — Controlled adaptation, learning memory & human reset.

The AI family therefore contains seven coherent contracts.

## Consolidated contract model

### STD-AI-001 — Grounded & verified AI assistance
Verified facts remain grounded in authoritative/deterministic sources. AI may interpret, select, summarize and explain, but does not silently replace authoritative logic. AI results are bound to source/version/snapshot identity and stale results are invalidated or marked stale.

### STD-AI-002 — User transparency, fallback & feedback
Users can distinguish generated assistance from authoritative basis where material. Supplemental AI failure does not break deterministic workflows. Feedback/context is not silently transmitted and developer/mock controls do not leak into normal production UI.

### STD-AI-003 — Advisory, explainable and read-only-by-default AI
AI is read-only by default. Material findings explain their reason/context and uncertainty. Writes, destructive actions and other material actions require a separate authorized step. AI is never the sole Release Inspector PASS/FAIL authority.

### STD-AI-004 — Privacy, data minimization & secret handling
Minimize and sanitize AI inputs. Secrets, credentials and tokens are not model inputs. Provider credentials use Keychain/equivalent secure storage and least-privilege scopes.

### STD-AI-005 — Provider, runtime & graceful fallback
Model on-device/cloud/hybrid execution, capability detection, provider/model provenance, offline/timeout/rate-limit/quota/billing failure and safe fallback. On-device is preferred when it provides sufficient quality and meaningful privacy/availability/latency/cost benefit.

### STD-AI-006 — Untrusted input/output, evaluation & rollback
External/imported content is data, not authority over system instructions or tool policy. Structured output is schema/invariant validated. Tool calls use allowlists and least privilege. Material model/provider/prompt/tool-policy changes require regression and rollback capability.

### STD-AI-007 — Controlled adaptation, learning memory & human reset
Adaptive/personalized learning is separated from authoritative source-of-truth data. Learning provenance is traceable; unconfirmed model guesses cannot become learned facts. Material candidate rules require validation/human confirmation. Adaptation is versioned, reversible and resettable.

## Machine-readable AI metadata

Each declared AI feature should carry:

- stable feature ID,
- `riskProfile`: `advisory`, `derived`, `action-capable` or `adaptive`,
- `execution`: `on-device`, `cloud` or `hybrid`,
- optional personalization/tool metadata.

Capabilities remain the applicability mechanism; risk profiles refine test scope and evidence.

## Apple platforms

Apple Foundation Models / Core AI are reference on-device implementations. The Standard intentionally does not require a specific vendor or framework.

## Pilot

TradeBook is the first intended RC3 pilot:
- deterministic Release Inspector remains authoritative,
- local AI may provide advisory analysis,
- cloud AI remains optional when supplemental,
- future learning produces candidate patterns rather than silently changing financial or safety rules.
