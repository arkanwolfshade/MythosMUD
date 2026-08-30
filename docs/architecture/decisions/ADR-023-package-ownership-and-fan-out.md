# ADR-023: Package Ownership (`game/` vs `services/` vs `npc/`) and Fan-Out Watch List

**Version 1.0.0** · MythosMUD · 2026-08-30

---

## AI READING INSTRUCTION

Read `[SPEC]` and `[BUG]` blocks for authoritative facts.
Read `[NOTE]` only if additional context is needed.
`[?]` blocks are unverified — treat with lower confidence.

---

## 1. Overview

**[SPEC]**
**Status:** Accepted
**Date:** 2026-08-30

Written to close the P1 ownership finding of `#757` (2026-08 server/ architecture review):
`server/game/` and `server/services/` both hold business logic, both are full of
`*_service.py` files, and no rule distinguished which new logic goes where. This ADR states
that rule going forward and records a fan-out watch list from the same review's P2 hub-
concentration finding.

## 2. Context

**[NOTE]**
`docs/BOUNDED_CONTEXTS_AND_SERVICE_BOUNDARIES.md` already answers *which bounded context* owns
a piece of behavior (Core, Realtime, Game, Combat, Magic, NPC, Chat, Temporal, Monitoring) —
the container-bundle axis. It does not answer *which directory* a new file goes in; it never
names `server/game/`, `server/services/`, or `server/npc/`. That is a different, orthogonal
axis, and this ADR is scoped to it alone.

Verified inventory at time of writing: `server/game/` ~69 files (chat, movement, magic, party,
quests, player lifecycle); `server/services/` ~121 files (combat, lucidity, container,
inventory, NPC-combat, infrastructure); `server/npc/` ~30 files (NPC lifecycle, spawning,
behaviors, combat integration). The split between `game/` and `services/` reads as historical
accretion, not design — there is no discoverable rule in code, tests, or prior ADRs for why
`chat_service.py` lives in `game/` while `combat_service.py` lives in `services/`.

## 3. Decision

**[SPEC]**

**Forward-binding placement rule, decided here for the first time:**

- **`server/npc/`** — NPC entity lifecycle and behavior: spawning, population control,
  lifecycle state machines, movement/behavior strategy, and the NPC-specific integration shims
  that adapt NPC state into other subsystems (e.g. `npc_combat_schedule.py`). If it is *about
  an NPC as an actor*, it lives here.
- **`server/services/`** — Business logic keyed by a **game mechanic that spans actor types**
  (players and NPCs both participate): combat, lucidity, containers/inventory, death/respawn
  mechanics. A service in this package should not assume its subject is a player.
- **`server/game/`** — Business logic keyed by a **player-facing command or player-only
  concept**: chat, movement, party, skills, stats generation, magic-system orchestration,
  player creation/search. If the only actor that can trigger it is a player, it lives here.

**Grandfathering.** The existing ~190 files are **not** moved to conform to this rule. A mass
move would be a diff on the order of the packages themselves and would churn the exact files
`#757`'s P1 hotspot finding wants held stable (`server/realtime/websocket_room_updates.py` and
its neighbors depend on both packages' current locations). This ADR binds *new* placement
decisions and code review judgment; it does not retroactively judge existing files as
misplaced.

**Fan-out watch list.** `#757`'s P2 hub-concentration finding named five files as fan-out
pressure points via jCodemunch's `get_architecture_metrics`. Verification found no defect in
this — high fan-in on `structured_logging/enhanced_logging_config.py` (471 importers) and
`exceptions.py` (242) is exactly what a logging facade and exception hierarchy should look
like — but the fan-out side is worth a stated baseline rather than silent drift:

| File | Fan-out (2026-08-30) | Review trigger |
| --- | --- | --- |
| `server/commands/command_service.py` | 33 | > 40 |
| `server/realtime/connection_manager.py` | 32 | > 40 |
| `server/services/combat_service.py` | 31 | > 40 |
| `server/dependencies.py` | 30 | > 40 |
| `server/container/bundles/game.py` | 29 | > 40 (composition root; expected to grow with feature count) |

A new import that pushes one of these past its trigger is not blocked — there is no CI guard
on this table, deliberately (see §4) — but should be called out and justified in code review,
the way an unusually large diff is.

## 4. Alternatives Considered

**[SPEC]**

1. **Extend `BOUNDED_CONTEXTS_AND_SERVICE_BOUNDARIES.md` with a directory-axis section** —
   Rejected: buries a forward-binding decision inside a descriptive document; ADRs are this
   project's instrument for decisions, not encyclopedic docs.
2. **Mass-move existing files to conform** — Rejected: diff size and hotspot churn, per §3.
3. **CI-enforce the fan-out thresholds** — Rejected: layer *direction* (ADR-001, enforced via
   `import-linter` per the same `#757` pass) is a binary, low-noise property suited to a guard.
   Fan-out count is a gradient with no natural threshold; machine-enforcing an arbitrary number
   generates friction on legitimate changes without preventing a real defect.
4. **Let `docs/packages/PACKAGE_SERVICES_DESIGN.md` / a future `PACKAGE_GAME_DESIGN.md` settle
   it via their boundary-contract sections** — Rejected as the primary instrument: those docs
   are explicitly reverse-engineered and descriptive (`docs/packages/README.md`'s stated
   posture); they would record the current mess accurately, not decide a rule. Once written,
   such docs should cite this ADR for the *why*, the way `PACKAGE_SERVICES_DESIGN.md` already
   cites `docs/subsystems/` for the behavioral cross-reference.

## 5. Consequences

**[SPEC]**

- **Positive**: new code has a discoverable placement rule; the fan-out table gives review a
  concrete number instead of "does this feel like a lot of imports."
- **Negative**: the rule is silent on ~190 pre-existing files, so `server/game/` and
  `server/services/` will remain mixed for the foreseeable future; a reader browsing either
  package will still see both actor-spanning and player-only logic until enough natural churn
  passes through.
- **Neutral**: the watch-list thresholds are unenforced and can go stale; they are a review aid,
  not a contract. Re-run the methodology in §6 if they no longer look load-bearing.

## 6. Methodology

**[NOTE]**
Fan-out figures are `mcp__jcodemunch__get_architecture_metrics`'s `top_concentrators.fan_out`
list, read verbatim on 2026-08-30 against the indexed `server/` tree (2051 files measured).
Reproduce by re-running that tool against a freshly re-indexed repo; the numbers are expected to
drift with ordinary development and are not a frozen baseline.

## 7. Related ADRs

**[SPEC]**

- [ADR-001](ADR-001-layered-architecture-event-driven.md) — the layer-direction decision this
  ADR's sibling `import-linter` contract enforces; this ADR covers the orthogonal
  package-placement axis within the Service Layer.
- [ADR-002](ADR-002-application-container-dependency-injection.md) — why `container/bundles/`
  fan-out is composition-root behavior, not a violation.

## 8. Related docs

**[SPEC]**

- [`docs/BOUNDED_CONTEXTS_AND_SERVICE_BOUNDARIES.md`](../../BOUNDED_CONTEXTS_AND_SERVICE_BOUNDARIES.md)
  — the bounded-context axis; orthogonal to this ADR's directory-placement axis.
- [`docs/packages/PACKAGE_SERVICES_DESIGN.md`](../../packages/PACKAGE_SERVICES_DESIGN.md) — the
  reverse-engineered catalog of `server/services/`'s current (grandfathered) contents.

## 9. Changelog

**[SPEC]**

| Version | Date | Change |
| --- | --- | --- |
| 1.0.0 | 2026-08-30 | Initial version, closes the P1 ownership and P2 hub-concentration findings of #757 |
