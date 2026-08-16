# test_lifecycle_periodic.py

> 52 nodes

## Key Concepts

- **test_lifecycle_periodic.py** (41 connections) — `server/tests/unit/npc/test_lifecycle_periodic.py`
- **NPCLifecycleState** (24 connections) — `server/npc/lifecycle_types.py`
- **lifecycle_periodic.py** (19 connections) — `server/npc/lifecycle_periodic.py`
- **check_optional_npc_spawns_impl()** (13 connections) — `server/npc/lifecycle_periodic.py`
- **run_periodic_maintenance_impl()** (11 connections) — `server/npc/lifecycle_periodic.py`
- **cleanup_old_records_impl()** (10 connections) — `server/npc/lifecycle_periodic.py`
- **_attempt_optional_npc_spawn()** (9 connections) — `server/npc/lifecycle_periodic.py`
- **_check_spawn_conditions_for_optional_npc()** (9 connections) — `server/npc/lifecycle_periodic.py`
- **get_zone_key_for_definition()** (9 connections) — `server/npc/lifecycle_periodic.py`
- **_should_skip_optional_npc()** (9 connections) — `server/npc/lifecycle_periodic.py`
- **get_spawn_room_for_definition()** (8 connections) — `server/npc/lifecycle_periodic.py`
- **Any** (8 connections)
- **_make_record()** (4 connections) — `server/tests/unit/npc/test_lifecycle_periodic.py`
- **test_cleanup_old_records_removes_stale_despawned()** (4 connections) — `server/tests/unit/npc/test_lifecycle_periodic.py`
- **test_cleanup_old_records_removes_stale_error()** (4 connections) — `server/tests/unit/npc/test_lifecycle_periodic.py`
- **.periodic_maintenance()** (3 connections) — `server/npc/lifecycle_manager.py`
- **test_should_not_skip_when_interval_elapsed()** (3 connections) — `server/tests/unit/npc/test_lifecycle_periodic.py`
- **test_attempt_optional_npc_spawn_no_controller()** (2 connections) — `server/tests/unit/npc/test_lifecycle_periodic.py`
- **test_attempt_optional_npc_spawn_no_zone_config()** (2 connections) — `server/tests/unit/npc/test_lifecycle_periodic.py`
- **test_attempt_optional_npc_spawn_probability_miss()** (2 connections) — `server/tests/unit/npc/test_lifecycle_periodic.py`
- **test_check_optional_npc_spawns_no_population_controller()** (2 connections) — `server/tests/unit/npc/test_lifecycle_periodic.py`
- **test_check_optional_npc_spawns_probability_miss()** (2 connections) — `server/tests/unit/npc/test_lifecycle_periodic.py`
- **test_check_optional_npc_spawns_skips_missing_zone_key()** (2 connections) — `server/tests/unit/npc/test_lifecycle_periodic.py`
- **test_check_optional_npc_spawns_successful_spawn()** (2 connections) — `server/tests/unit/npc/test_lifecycle_periodic.py`
- **test_check_spawn_conditions_can_spawn()** (2 connections) — `server/tests/unit/npc/test_lifecycle_periodic.py`
- *... and 27 more nodes in this community*

## Relationships

- [NPCDied](NPCDied.md) (9 shared connections)
- [get_logger](get_logger.md) (9 shared connections)
- [despawn_npc_impl](despawn_npc_impl.md) (6 shared connections)
- [NPCMaintenanceConfig](NPCMaintenanceConfig.md) (5 shared connections)
- [NPCDefinition](NPCDefinition.md) (3 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (2 shared connections)
- [.add_event](add_event.md) (1 shared connections)
- [.cleanup_old_records](cleanup_old_records.md) (1 shared connections)

## Source Files

- `server/npc/lifecycle_manager.py`
- `server/npc/lifecycle_periodic.py`
- `server/npc/lifecycle_types.py`
- `server/tests/unit/npc/test_lifecycle_periodic.py`

## Audit Trail

- EXTRACTED: 128 (91%)
- INFERRED: 13 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*