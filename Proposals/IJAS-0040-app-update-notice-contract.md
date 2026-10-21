# IJAS-0040 — Non-blocking App Update Notice
**Status:** accepted for candidate 1.9.0 RC4; **Rule:** `STD-UPDATE-001`.

**Problem:** Strážca's service records last check before HTTP success and drops dismissed update without version persistence. Blind reuse can suppress retries or spam the same version.

**Contract:** Correct app provider/storefront/link; separate successful fetch from attempts, bounded retry, version-scoped snooze, localized UI without startup blocking. Private app without version provider is N/A.

**Applies to:** `hasAppUpdateNotice`. **Evidence:** deterministic provider-mock tests and real store link/locale runtime.
