# ADR-021: ui-v2 Client Transition and Legacy Retirement

**Version 1.0.0** · MythosMUD · 2026-08-19

---

## AI READING INSTRUCTION

Read `[SPEC]` and `[BUG]` blocks for authoritative facts.
Read `[NOTE]` only if additional context is needed.
`[?]` blocks are unverified — treat with lower confidence.

---

## 1. Overview

**[SPEC]**
**Status:** Accepted (transition) · **Open** (retirement — see §6)
**Date:** 2026-08-19
**Provenance:** Recorded by the 2026-08 design/implementation audit. The transition itself already
happened; this ADR documents it after the fact because no ADR covered it. The retirement half is a
genuinely open decision, not a description.

## 2. Context

**[NOTE]**
The shipped client is `client/src/components/ui-v2/` — roughly 95 production modules built around
`GameClientV2Container` and a `PanelSystem`. A substantial earlier surface remains alongside it in
`client/src/components/`, including a `panels/` tree of roughly 26 production modules plus several
`*PanelTest.tsx` demo components.

The audit found no ADR, design doc, or migration note recording that this transition occurred. A
contributor reading the component tree encounters two plausible client architectures with nothing
indicating which is live. That ambiguity is the cost being addressed here.

Related: ADR-008 records React/TypeScript/Vite as the client stack; it predates ui-v2 and does not
describe component architecture.

## 3. Decision

**[SPEC]**
`ui-v2` is the client architecture. All new client work targets
`client/src/components/ui-v2/`.

- The live entry point is `GameClientV2Container`; panel composition goes through `PanelSystem`.
- The pre-existing component surface under `client/src/components/` is **legacy**: it is not the
  target for new work and should not gain new features.
- Legacy modules are removed only after their absence of live consumers has been demonstrated, not
  assumed — see §6.

## 4. Alternatives Considered

**[SPEC]**

1. **Leave the transition unrecorded** — Rejected: this is the status quo the audit flagged, and it costs
   every new contributor the same rediscovery.
2. **Delete the legacy tree immediately** — Rejected as premature: the audit did not establish which
   legacy modules still have live importers. Deletion without that evidence risks removing something
   reachable.
3. **Fold this into ADR-008** — Rejected: ADR-008 records a technology choice (React, TypeScript, Vite);
   component architecture and a retirement plan are a separate decision with a different lifetime.

## 5. Consequences

**[SPEC]**

- **Positive**: a contributor can tell which client architecture is live without tracing imports; new
  work has an unambiguous target.
- **Negative**: two component trees continue to coexist until retirement completes, with the maintenance
  and bundle cost that implies.
- **Neutral**: no change to the technology stack recorded in ADR-008.

## 6. Open — retirement plan

**[?]**
This section records what has **not** been decided. It is deliberately marked `[?]`: the facts below
need establishing before a retirement plan can be written.

1. **Which legacy modules still have live importers?** An import-graph pass over
   `client/src/components/` is required. The audit noted that the `CommandPanelTest.*` group appeared to
   have no external importers, but this was not independently verified and must not be treated as
   settled.
2. **Do any legacy modules carry behaviour ui-v2 lacks?** Retirement must not silently drop a capability.
3. **What is the removal sequence?** Proposed shape: demonstrate no live importers → remove in a single
   reviewable commit per cluster → confirm the bundle shrinks.

Until this section is resolved, the legacy tree stays.

## 7. Related ADRs

**[SPEC]**

- [ADR-008: React 18+ with TypeScript for Client](ADR-008-react-typescript-client.md)
- [ADR-011: XState for Frontend Connection State Machine](ADR-011-xstate-frontend-fsm.md)
- [CLIENT_LAYOUT_BASELINE.md](../../CLIENT_LAYOUT_BASELINE.md) · [CLIENT_TYPOGRAPHY_LAYOUT_SPEC.md](../../CLIENT_TYPOGRAPHY_LAYOUT_SPEC.md)

## 8. Changelog

**[SPEC]**

| Version | Date | Change |
| --- | --- | --- |
| 1.0.0 | 2026-08-19 | Initial ADR; records the ui-v2 transition and opens the retirement question |
