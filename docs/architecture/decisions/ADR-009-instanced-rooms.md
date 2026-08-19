# ADR-009: Instanced Rooms for Tutorial and Future Content

**Version 1.0.0** · MythosMUD · 2026-07-30

---

## AI READING INSTRUCTION

Read `[SPEC]` and `[BUG]` blocks for authoritative facts.
Read `[NOTE]` only if additional context is needed.
`[?]` blocks are unverified — treat with lower confidence.

---

## 1. Overview

**[SPEC]**
**Status:** Accepted
**Date:** 2026-02-17
**Provenance:** Recorded by the 2026-08 design/implementation audit. This ADR set was authored after the
systems it describes: the structural architecture documents it draws on predate it by months, and
`DOCUMENTATION_AUDIT.md` records that the design documentation was reverse-engineered with code treated as
the source of truth. Read it as a description of a decision already in force, not a record made at decision
time.

## 2. Context

**[NOTE]**
MythosMUD needs per-player instanced spaces for the new-character tutorial so that new
players do not see other players during the initial onboarding. Instanced rooms must
persist in memory until the player exits, support a fixed exit to the shared world
(Main Foyer), and handle reconnection (place player at instance start after disconnect).
Combat and death should be disabled in tutorial instances.

## 3. Decision

**[NOTE]**

1. **Room templates**: Use existing room schema with `attributes.is_instanced`,
   `instance_template_id`, `instance_exit_room_id`, `no_combat`, and `no_death`.

2. **InstanceManager**: In-memory service that clones room templates, remaps room IDs
   (`instance_{uuid}_{template_stable_id}`), and remaps exits (within-instance vs fixed
   exit). InstanceStore holds active instances keyed by `instance_id`.

3. **Room lookup**: `get_room_by_id` checks InstanceManager first, then cache (instance-first).

4. **Player state**: `players.tutorial_instance_id` (nullable) tracks active tutorial
   instance. Cleared on exit; used on reconnect to ensure instance exists and place at
   first room.

5. **Tutorial exit**: When player moves to the configured exit room (Main Foyer),
   clear `tutorial_instance_id`, destroy instance, persist player.

6. **Combat/death guards**: Rooms with `no_combat` block player-initiated combat;
   rooms with `no_death` cap damage so player DP never goes below 0.

## 4. Alternatives Considered

**[NOTE]**

- **Separate tutorial world**: Rejected; reusing room definitions and world loader keeps
  complexity lower.
- **Database-backed instances**: Rejected; in-memory instances suffice for session-scoped
  tutorial; persistence only for `tutorial_instance_id` on player.
- **Block combat at death handler**: Rejected; capping damage at 0 in no_death rooms
  keeps combat flow intact without special death-path logic.

## 5. Consequences

**[SPEC]**

- **Positive**: Tutorial is isolated; reconnect behavior is predictable; room attributes
  support future instanced zones (dungeons, group content).
- **Negative**: Instances are lost on server restart; players with `tutorial_instance_id`
  set are placed at instance start on reconnect (instance recreated if missing).
- **Neutral**: InstanceManager is optional dependency; systems without it behave as before.

## 6. Changelog

**[SPEC]**

| Version | Date | Change |
| --- | --- | --- |
| 1.0.0 | 2026-07-30 | Initial HADS structural conversion |
