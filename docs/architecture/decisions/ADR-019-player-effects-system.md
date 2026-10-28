# ADR-019: Player Effects System

**Version 1.2.1** · MythosMUD · 2026-10-27

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
`player_effects` is the only effects store ([ADR-029](ADR-029-authoritative-player-registry.md) step 3b-i):
spells, scripted content (dialogue `apply_effect`, container `on_put`) and the login ward all write rows. The old
`players.status_effects` column was dropped in step 3b-ii (migration `20261027140000_drop_players_status_effects`).

1. **Storage**: table `player_effects`, one row per active effect (baseline `db/schema.sql`, #811; runtime
   columns from migration `20261027120000_player_effects_runtime_state`). Columns: `player_id` (FK),
   `effect_type` (String 64), `category` (String 64), `remaining_seconds` (Integer, NULL = until removed),
   `payload` (jsonb: the effect's per-type state, such as a drain's `rate` and `elapsed`), `instance_scoped`
   (Boolean: removed when the player's instance is lost), `intensity` (Integer, default 1), `source`
   (String 128, nullable).

2. **Time base is online game seconds.** `remaining_seconds` counts down once per game second for online
   players only, so an effect pauses while its player is offline. (It replaced `duration` /
   `applied_at_tick`, which were tick counts against a counter that restarts at 0 in every process.)

3. **Effect vocabulary**: `StatusEffectType` in `server/models/game.py` — lucidity-driven
   (`HALLUCINATING`, `PARANOID`, `TREMBLING`, `CORRUPTED`, `DELIRIOUS`), spell-driven (`DOMINATED`,
   `CLOUD_MEMORY`, `FEAR`, `EVIL_EYE`, `BLINDED`, `WARDED`, `EXTINGUISH_FIRE`), plus `POISONED`, `BUFF`,
   `LOGIN_WARDED`, and `STUNNED`.

4. **Expiry is centralised in the tick loop.** Once per game second, `process_status_effects`
   (`server/app/game_tick_status_effects.py`) runs each online player's per-second effect actions, then calls
   `async_persistence.advance_player_effects(online_ids)`, which takes a second off every timed effect,
   deletes the ones that ran out, and returns their `(player_id, effect_type)` pairs. Individual services do
   not poll for expiry.

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
- **Negative**: expiry granularity is one game second; effects needing in-memory state require an
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
| 1.1.0 | 2026-09-15 | Correct §3.1: the cited Alembic revision was never wired up and was removed in #811; schema is now in the baseline |
| 1.2.0 | 2026-10-27 | ADR-029 step 3b-i: the only effects store; `remaining_seconds` in online game seconds, `payload`, `instance_scoped` |
| 1.2.1 | 2026-10-27 | ADR-029 step 3b-ii: `players.status_effects` dropped |
