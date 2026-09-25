# IbaJuraj Application Standard 1.9.0 RC3 — Test Matrix

## Base RC gate
RC2 cadence remains: small development builds use Build/Test + targeted regression; nominated production RCs run the full Release Candidate Quality Gate.

## Grounding
- verified facts use deterministic/authoritative sources,
- low-confidence or insufficient evidence uses clarification/fallback,
- stale AI result is invalidated or marked stale after source/baseline change,
- time-sensitive external data records source identity, publication/event time when known, retrieval time, affected subject/asset and freshness/staleness,
- conflicting external sources remain explicit until a deterministic or human-reviewed rule resolves the conflict.

## Transparency
- generated explanation is distinguishable from authoritative basis where material,
- supplemental AI failure leaves deterministic workflow usable,
- feedback/context is not silently transmitted,
- developer/mock controls do not appear in normal production UI.

## Read-only / actions
- AI cannot silently write production data,
- material action requires an explicit authorized step,
- market/watch/buy candidates and opportunity scores do not execute trades and are not transaction authorization,
- action-capable tools use allowlists and least privilege,
- Release Inspector PASS/FAIL remains deterministic.

## Privacy / secrets
- model inputs contain no API keys, credentials or auth tokens,
- cloud payload is minimized/sanitized,
- credentials reside in Keychain/equivalent secure storage,
- provider scopes are least-privilege.

## Provider/runtime
Test applicable:
- on-device model supported and ready,
- on-device model supported but temporarily not ready,
- on-device model unavailable/unsupported,
- declared-ready model that fails first execution or warm-up/probe,
- offline,
- timeout,
- rate limit,
- quota exhausted,
- billing unavailable,
- provider/model unavailable,
- retry/fallback,
- retry/refresh does not falsely claim it can force-download or activate a platform-managed model,
- deterministic non-generative fallback is clearly distinguished from model AI,
- provenance captures provider/model/execution/runtimeKind/fallbackKind/time/prompt-contract version without secrets.

## Untrusted input/output
- prompt-like text in CSV/import/web/user content cannot override system/tool policy,
- malformed structured output is rejected,
- semantically invalid output is rejected,
- tool call outside allowlist is rejected.

## Regression / rollback
- representative success/boundary/low-confidence/failure evals PASS,
- model change triggers regression,
- provider change triggers regression,
- prompt-contract change triggers regression,
- material tool-policy change triggers regression,
- rollback to last known-good AI configuration works.

## Adaptive AI
Where supported:
- learning source/provenance is visible to diagnostics,
- unconfirmed AI guess does not become learned fact,
- lifecycle distinguishes candidate → confirmed → active/usable → revoked/reset (or equivalent),
- saving a candidate alone does not activate it or change authoritative data/rules,
- candidate learned rule requires validation/human confirmation when material,
- reset removes AI memory/personalization but preserves primary user data,
- adaptation is versioned and reversible.

## Machine-readable metadata
Validate:
- unique stable AI feature IDs,
- risk profile in `advisory | derived | action-capable | adaptive`,
- execution in `on-device | cloud | hybrid`,
- runtimeKind in `model | deterministic`,
- fallbackKind in `none | model | deterministic`,
- capability flags match declared profiles/execution.
