# lifecycle_periodic.py

> 23 nodes · cohesion 0.14

## Key Concepts

- **lifecycle_periodic.py** (18 connections) — `server/npc/lifecycle_periodic.py`
- **check_optional_npc_spawns_impl()** (8 connections) — `server/npc/lifecycle_periodic.py`
- **Any** (8 connections)
- **run_periodic_maintenance_impl()** (7 connections) — `server/npc/lifecycle_periodic.py`
- **cleanup_old_records_impl()** (6 connections) — `server/npc/lifecycle_periodic.py`
- **_attempt_optional_npc_spawn()** (5 connections) — `server/npc/lifecycle_periodic.py`
- **get_spawn_room_for_definition()** (5 connections) — `server/npc/lifecycle_periodic.py`
- **get_zone_key_for_definition()** (5 connections) — `server/npc/lifecycle_periodic.py`
- **_check_spawn_conditions_for_optional_npc()** (4 connections) — `server/npc/lifecycle_periodic.py`
- **_should_skip_optional_npc()** (4 connections) — `server/npc/lifecycle_periodic.py`
- **.cleanup_old_records()** (3 connections) — `server/npc/lifecycle_manager.py`
- **.periodic_maintenance()** (3 connections) — `server/npc/lifecycle_manager.py`
- **Clean up old lifecycle records (delegates to lifecycle_periodic).** (1 connections) — `server/npc/lifecycle_manager.py`
- **Perform periodic maintenance (delegates to lifecycle_periodic).** (1 connections) — `server/npc/lifecycle_manager.py`
- **Periodic maintenance and optional NPC spawn checks for lifecycle.  Extracted fro** (1 connections) — `server/npc/lifecycle_periodic.py`
- **Return (should_skip, last_check_time).** (1 connections) — `server/npc/lifecycle_periodic.py`
- **Return (can_spawn, current_count).** (1 connections) — `server/npc/lifecycle_periodic.py`
- **Attempt to spawn an optional NPC. Returns npc_id if spawned, else None.** (1 connections) — `server/npc/lifecycle_periodic.py`
- **Get zone key for an NPC definition (e.g. from sub_zone_id / room_id).** (1 connections) — `server/npc/lifecycle_periodic.py`
- **Get spawn room ID for an NPC definition.** (1 connections) — `server/npc/lifecycle_periodic.py`
- **Clean up old lifecycle records. Returns number of records removed.** (1 connections) — `server/npc/lifecycle_periodic.py`
- **Run respawn queue, optional NPC spawn checks, and cleanup. Returns results dict.** (1 connections) — `server/npc/lifecycle_periodic.py`
- **Check if optional NPCs should spawn; return spawned_count and checks_performed.** (1 connections) — `server/npc/lifecycle_periodic.py`

## Relationships

- [get_logger](get_logger.md) (13 shared connections)
- [NPCMaintenanceConfig](NPCMaintenanceConfig.md) (2 shared connections)

## Source Files

- `server/npc/lifecycle_manager.py`
- `server/npc/lifecycle_periodic.py`

## Audit Trail

- EXTRACTED: 87 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*