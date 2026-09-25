# IJAS-0035 — Release Candidate Quality Gate & Intelligent Self-Audit

**Status:** accepted  
**Target:** IbaJuraj Application Standard 1.9.0 RC2  
**Date:** 2026-09-25

## Problem

A complete whole-app audit after every small development build would slow iteration without proportional benefit. The strict gate is most valuable when a build is explicitly nominated for App Store or other production distribution. The final audit should combine deterministic checks with semantic/visual review, while AI must remain explainable and non-autonomous.

## Decision

Introduce a shared Release Candidate Quality Gate and reference architecture called **IbaJuraj Release Inspector / Quality Engine**. The implementation may be shared or app-specific; the observable release behavior and evidence are normative.

## New rules

### STD-RELEASE-006 — Release Candidate Quality Gate cadence — MUST
A complete whole-app release audit is mandatory for a build explicitly nominated for App Store/store/production submission. Ordinary development builds require Build/Test plus targeted regression of changed or high-risk areas. Any material change after a completed RC gate invalidates that exact-build release evidence and requires a new RC gate.

### STD-DIAG-001 — Internal Full App Check — MUST
Every adopting app must provide an internal/developer-only Full App Check callable on the exact RC build. It runs non-destructive deterministic checks over applicable internal state and services, including initialization, persisted-data integrity, migrations, navigation/destinations, localization integrity, calculations/business rules, sync/API/deep links and cache/configuration where applicable. Write-path tests use isolated/synthetic fixtures or a reversible test context.

### STD-DIAG-002 — Structured diagnostic findings and severity — MUST
Diagnostics emit stable finding IDs with component, expected/observed state, evidence, explanation and severity: BLOCKER / ERROR / WARNING / INFO. BLOCKER and ERROR are release-blocking unless covered by an explicit Standard exception/ADR. WARNING requires review; INFO is non-blocking. Known exceptions remain explicit and traceable.

### STD-RELEASE-007 — Release diff and risk-based coverage — MUST
Before the RC gate, compare the candidate with the last production/App Store baseline. Identify changed source/data model/schema/migrations/configuration/dependencies/UI/localization/feature flags as applicable, map likely blast radius and expand test depth for high-risk areas.

### STD-TEST-002 — Critical user journeys and resilience scenarios — MUST
The RC gate exercises representative end-to-end user journeys, not only isolated screens. As applicable, include lifecycle restart/persistence and failure scenarios such as offline state, timeout, denied permission, interrupted import/write, corrupt input, sync failure/conflict and upgrade from older persisted data.

### STD-UI-001 — Release visual/runtime matrix — MUST
Changed and high-risk user-facing surfaces are checked across representative device/viewport classes and applicable appearance, Dynamic Type and supported localization states. Screenshot/image-diff automation may assist, but ambiguous visual findings require human review.

### STD-AI-003 — AI release review is advisory, explainable and non-autonomous — MUST
When AI is used in the RC audit, each finding includes a reason, supporting evidence/context and confidence indication. AI may prioritize, explain and suggest fixes, but must not silently mutate production data/content/code and must not be the sole basis for final release PASS/FAIL. An AI-only blocking finding requires deterministic corroboration or explicit human confirmation.

### STD-AI-004 — AI release review uses data minimization — MUST
AI release-review inputs use synthetic, anonymized or minimized data by default. Secrets, credentials, authentication tokens and equivalent sensitive material must never be sent. Logs, screenshots and imported datasets are sanitized before AI analysis when they may contain private user information.

### STD-EVIDENCE-002 — RC Evidence Bundle and release baseline — MUST
Each RC gate produces an exportable evidence bundle tied to the exact app version/build and Standard candidate. It records check summary, findings, exceptions, release diff/risk scope, runtime/UI evidence and AI-review summary when used. The build actually released to production/App Store becomes the next comparison baseline.

### STD-POSTRELEASE-001 — Production feedback loop — MUST when supported
If an app has post-release monitoring capability, privacy-respecting crash/error/performance signals are reviewed after release and meaningful regressions feed the next release baseline and test scope.

## Release Inspector modes
- Development Check — Build/Test plus targeted checks; no mandatory whole-app deep audit after every small build.
- Full App Check — internal in-app diagnostic sweep.
- Release Check — complete RC gate combining deterministic checks, app-specific checks, user journeys, visual/runtime matrix, release diff, evidence and optional AI review.
- Post-Release Monitoring — production feedback where supported.

## PASS semantics
A Release Check is eligible for PASS only when required deterministic/runtime gates pass, no unresolved BLOCKER or ERROR remains without a valid exception, WARNING findings are reviewed, AI is not treated as autonomous proof, and the exact-build Evidence Bundle is complete.
