# IJAS-0029 — Async and Derived-State Integrity

**Status:** accepted for 1.8.0 RC2.

Adds:
- `STD-ASYNC-001` — stale async completion cannot overwrite newer state,
- `STD-DERIVED-001` — authoritative mutation precedes one coherent derived-state rebuild.

This generalizes cross-app findings where correct synchronous mutation order was insufficient because older asynchronous completions could still restore stale notifications, widgets, caches or indexes.
