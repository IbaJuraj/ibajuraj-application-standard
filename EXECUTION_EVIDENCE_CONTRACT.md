# IbaJuraj Standard RC4 — Exact-Build Execution Evidence

This document specifies the **candidate** execution evidence format. It prevents declaring PASS merely because a test name, Markdown section or report path exists. It does not by itself prove a physical runtime event occurred: use trusted native CI logs or signed/human-reviewed runtime reports as the primary artifact.

## Phases

~~~bash
python3 Checks/validate-app-conformance.py --standard-root . --app-root /path/to/app --phase development
python3 Checks/validate-app-conformance.py --standard-root . --app-root /path/to/app --phase release-candidate
python3 Checks/validate-app-conformance.py --standard-root . --app-root /path/to/app --phase post-release
~~~

Without `--phase`, validation conservatively assumes `release-candidate`. The production-release pipeline **MUST** specify that phase explicitly.

## Required declaration

A candidate app's `STANDARD_CONFORMANCE.json` includes these fields *alongside* its existing capabilities, rules and screen families:

~~~json
{
  "standardVersion": "1.9.0",
  "standardCandidate": "RC4",
  "app": {
    "name": "ExampleApp",
    "productId": "example.identifier",
    "version": "1.0.0",
    "build": "123",
    "sourceRevision": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
  },
  "executionEvidence": {
    "file": "Evidence/STANDARD_EXECUTION_RESULTS.json"
  }
}
~~~

`sourceRevision` is an actual Git commit SHA (40 hex chars) or independently reproducible source-tree SHA-256 (64 hex chars), not a label fabricated to satisfy the format. The example is **incomplete** as a conformance manifest and does not constitute evidence.

## Execution result file (illustrative fixture only)

~~~json
{
  "schemaVersion": 1,
  "standardVersion": "1.9.0",
  "standardCandidate": "RC4",
  "phase": "release-candidate",
  "app": {
    "name": "ExampleApp",
    "productId": "example.identifier",
    "version": "1.0.0",
    "build": "123",
    "sourceRevision": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
  },
  "sourceRevision": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
  "results": {
    "STD-BACKUP-001": {
      "status": "pass",
      "mode": "unit",
      "check": "BackupTests/testIntegrity",
      "executedAt": "2026-10-16T15:00:00+02:00",
      "runner": "xcodebuild test / trusted CI run",
      "artifact": "Evidence/logs/BackupTests.log",
      "artifactSha256": "<real lowercase SHA-256 of the exact log>"
    },
    "STD-BACKUP-002": {
      "status": "pass",
      "mode": "runtime",
      "check": "RUNTIME_ACCEPTANCE.md#restore-and-rollback",
      "executedAt": "2026-10-16T16:00:00+02:00",
      "runner": "human-reviewed runtime acceptance",
      "device": "iPad 9",
      "os": "iPadOS version",
      "artifact": "Evidence/logs/RestoreAcceptance.md",
      "artifactSha256": "<real lowercase SHA-256 of the exact report>"
    }
  }
}
~~~

Replace all fictitious identities, placeholders, hashes and "pass" claims with actual executed evidence. `mode` and `check` must exactly match the conformance entry: `test` for unit/UI or `runtimeGate` for runtime. A passed `SCREEN-ROOT` family uses `SCREEN-ROOT` as the result key, mode `ui`, and `check` equal to its first evidence reference.

## Interpretation

- **PASS:** catalog, candidate, phase and exact app version/build/source revision match; recorded executed result is pass with real check ID, timezone-aware timestamp, runner, raw output and SHA256. UI/runtime also require device+OS context.
- **PENDING (exit 2 for release blockers):** applicable rule lacks the report, lacks a result or marks it pending. `test` or `runtimeGate` alone is not enough.
- **FAIL (exit 1):** explicitly failed or malformed result, wrong app/version/build/source revision/phase, invalid artifact path, absent raw output, missing required device/time/runner, or hash mismatch.
- **N/A:** genuinely inapplicable capability or phase.
- **EXCEPTION:** separate reviewed ADR with risk/owner/effective scope. It does not imply a test passed.

A self-declared PASS JSON with a fabricated file is NOT genuine execution. The validator verifies consistency/tampering relative to supplied artifacts; trusted CI and human review must still establish the actual origin. No rule in this document authorizes editing production user data.

## Privacy and security

Do not publish recovery keys, API tokens, wallet secrets, unredacted personal records, private backup archives or credentials in a conformance evidence bundle. Redact any test data and metadata as needed. Keep app-specific cloud identities, encryptions keys and account data separate.
