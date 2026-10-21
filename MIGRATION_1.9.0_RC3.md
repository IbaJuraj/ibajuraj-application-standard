# Migration to IbaJuraj Application Standard 1.9.0 RC3

**Stable authority remains:** 1.8.0  
**Candidate:** 1.9.0 RC3  
**Candidate rule count:** 134

## From RC2

RC3 preserves all RC2 Release Candidate Quality Gate contracts. Existing Release Inspector behavior remains valid unless AI is used.

For apps without AI capabilities, no new AI conformance work is required beyond updating the Standard candidate pin.

For apps with AI/generative assistance:

1. update `standardCandidate` to `RC3`,
2. declare relevant capabilities:
   - `hasOnDeviceAI`,
   - `hasCloudAI`,
   - `hasAITools`,
   - `hasAdaptiveAI`,
   - `hasAIPersonalization`,
3. add machine-readable `ai.features[]` entries with stable ID, `riskProfile` and `execution`,
4. review `STD-AI-001` through `STD-AI-006`,
5. if adaptive/personalized learning exists, also review `STD-AI-007`.

## Provider/runtime

Supplemental AI must fail gracefully. Local-model unavailability, offline state, timeout, rate limit, quota/billing and provider failure must not break the deterministic workflow.

On-device AI is preferred where it provides sufficient quality and meaningful privacy/availability/latency/cost benefit. Cloud AI may remain appropriate where required by the product.

## Security/privacy

- Keep AI/provider credentials in Keychain or equivalent secure storage.
- Use least-privilege scopes.
- Never send secrets/tokens to the model.
- Sanitize/minimize private inputs before cloud analysis.
- Treat imported/external content as data, not instructions.

## Evaluation

Material model/provider/prompt/tool-policy changes require targeted regression. Structured outputs must be validated before they influence deterministic state. Maintain rollback to the last known-good AI configuration.

## Adaptive AI

Learning memory remains separate from authoritative source-of-truth data. Candidate learned patterns require provenance, validation and appropriate human confirmation before they can affect financial, safety, legal/authoritative or Release Inspector behavior. Users must be able to reset stored AI personalization without deleting primary app data.

## TradeBook pilot

TradeBook should pilot:
- Release Inspector deterministic authority,
- local on-device advisory AI,
- optional cloud fallback,
- safe provider errors,
- machine-readable AI profile metadata,
- controlled candidate-pattern learning.
