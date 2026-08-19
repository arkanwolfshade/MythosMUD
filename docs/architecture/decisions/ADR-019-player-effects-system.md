# ADR-019: Player Effects System

**Version 1.0.0** · MythosMUD · 2026-08-19

---

## AI READING INSTRUCTION

Read `[SPEC]` and `[BUG]` blocks for authoritative facts.
Read `[NOTE]` only if additional context is needed.
`[?]` blocks are unverified — treat with lower confidence.

---

## 1. Overview

**[SPEC]**
**Status:** Accepted
**Date:** 2026-08-19
**Provenance:** Authored after implementation. This ADR records a decision already embodied in code; it
was written to close a documentation gap identified by the 2026-08 design/implementation audit. Treat its
description as derived from the implementation, not as a decision that preceded it.

## 2. Context

**[NOTE]**
The effects system was implemented under a plan (`effects_system_adr_and_implementation`) whose
`write-adr-009` todo was never completed. The number ADR-009 was subsequently allocated to
[Instanced Rooms](ADR-009-instanced-rooms.md), leaving the effects system with no ADR while production
code continued to cite "ADR-009" as its authority — a citation that resolves to an unrelated decision.

Mechanism-level description already exists in
[SUBSYSTEM_STATUS_EFFECTS_DESIGN.md](../../subsystems/SUBSYSTEM_STATUS_EFFECTS_DESIGN.md). This ADR
therefore records the *decision* and its contract rather than re-describing the mechanism.

## 3. Decision

**[SPEC]**
Persistent, time-bounded player status effects are stored in PostgreSQL and expired by the game tick.

1. **Storage**: table `player_effects`, one row per active effect, created by
   `server/alembic/versions/2026_02_09_add_player_effects_table.py`. Columns: `player_id` (FK),
   `effect_type` (String 64), `category` (String 64), `duration` (Integer), `applied_at_tick` (Integer),
   `intensity` (Integer, default 1), `source` (String 128, nullable).

2. **Time base is ticks, not wall-clock.** `duration` and `applied_at_tick` are tick counts, so effect
   lifetime is tied to simulation progress rather than real time.

3. **Effect vocabulary**: `StatusEffectType` in `server/models/game.py` — lucidity-driven
   (`HALLUCINATING`, `PARANOID`, `TREMBLING`, `CORRUPTED`, `DELIRIOUS`), spell-driven (`DOMINATED`,
   `CLOUD_MEMORY`, `FEAR`, `EVIL_EYE`, `BLINDED`, `WARDED`, `EXTINGUISH_FIRE`), plus `POISONED`, `BUFF`,
   and `LOGIN_WARDED`.

4. **Expiry is centralised in the tick loop.** `process_player_effects_expiration`
   (`server/app/game_tick_status_effects.py`) calls
   `async_persistence.expire_player_effects_for_tick(tick_count)` once per tick and acts on the returned
   `(player_id, effect_type)` pairs. Individual services do not poll for expiry.

5. **Effects requiring in-memory state clear it on expiry.** `LOGIN_WARDED` is the first such case:
   `_handle_login_warded_expirations` invokes `handle_login_grace_period_expiration` to release grace
   state and trigger a room update. New effects with in-process state follow this pattern.

6. **Relationship ownership**: `Player.player_effects` (`server/models/player.py`) with
   `cascade="all, delete-orphan"` — effects do not outlive their player.

7. **Client contract**: active effects are surfaced to the client for display (HeaderBar); the client
   renders effect state and never computes expiry.

## 4. Alternatives Considered

**[SPEC]**

1. **Wall-clock expiry with per-effect timers** — Rejected: timers drift against simulation state, do
   not survive restart, and multiply asyncio tasks. The pre-existing login grace-period timer
   (`server/realtime/login_grace_period.py`) remains only as a fallback path.
2. **In-memory-only effects** — Rejected: effects must survive reconnect and restart.
3. **Per-effect tables** — Rejected: the effect vocabulary changes far more often than its shape; one
   table with an `effect_type` discriminator keeps migrations proportional to schema change, not content
   change.

## 5. Consequences

**[SPEC]**

- **Positive**: effects survive restart and reconnect; expiry is deterministic against simulation time;
  one place to reason about lifetime; adding an effect type requires no migration.
- **Negative**: expiry granularity is bounded by tick rate; effects needing in-memory state require an
  explicit expiry hook, which is easy to omit for a new effect type.
- **Neutral**: `category` and `intensity` are carried but not yet load-bearing for every effect type.

## 6. Related ADRs

**[SPEC]**

- [ADR-006: PostgreSQL as Primary Datastore](ADR-006-postgresql-primary-datastore.md)
- [ADR-009: Instanced Rooms](ADR-009-instanced-rooms.md) — governs `no_death` rooms, which interact with
  DP and posture. **Code comments previously cited ADR-009 for the effects system; those citations were
  incorrect and now point here.**
- [SUBSYSTEM_STATUS_EFFECTS_DESIGN.md](../../subsystems/SUBSYSTEM_STATUS_EFFECTS_DESIGN.md) — mechanism detail

## 7. Changelog

**[SPEC]**

| Version | Date | Change |
| --- | --- | --- |
| 1.0.0 | 2026-08-19 | Initial ADR; closes the gap left by the unwritten `write-adr-009` todo |
