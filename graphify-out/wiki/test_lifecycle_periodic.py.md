# test_lifecycle_periodic.py

> 64 nodes

## Key Concepts

- **test_lifecycle_periodic.py** (42 connections) — `server/tests/unit/npc/test_lifecycle_periodic.py`
- **lifecycle_periodic.py** (21 connections) — `server/npc/lifecycle_periodic.py`
- **check_optional_npc_spawns_impl()** (13 connections) — `server/npc/lifecycle_periodic.py`
- **_attempt_optional_npc_spawn()** (11 connections) — `server/npc/lifecycle_periodic.py`
- **run_periodic_maintenance_impl()** (11 connections) — `server/npc/lifecycle_periodic.py`
- **NPCMaintenanceConfig** (10 connections) — `server/config/npc_config.py`
- **cleanup_old_records_impl()** (10 connections) — `server/npc/lifecycle_periodic.py`
- **_check_spawn_conditions_for_optional_npc()** (9 connections) — `server/npc/lifecycle_periodic.py`
- **get_zone_key_for_definition()** (9 connections) — `server/npc/lifecycle_periodic.py`
- **_should_skip_optional_npc()** (9 connections) — `server/npc/lifecycle_periodic.py`
- **get_spawn_room_for_definition()** (8 connections) — `server/npc/lifecycle_periodic.py`
- **Any** (8 connections)
- **npc_config.py** (5 connections) — `server/config/npc_config.py`
- **_make_record()** (4 connections) — `server/tests/unit/npc/test_lifecycle_periodic.py`
- **test_cleanup_old_records_removes_stale_despawned()** (4 connections) — `server/tests/unit/npc/test_lifecycle_periodic.py`
- **test_cleanup_old_records_removes_stale_error()** (4 connections) — `server/tests/unit/npc/test_lifecycle_periodic.py`
- **.get_config_summary()** (3 connections) — `server/config/npc_config.py`
- **.should_run_maintenance()** (3 connections) — `server/config/npc_config.py`
- **.cleanup_old_records()** (3 connections) — `server/npc/lifecycle_manager.py`
- **.periodic_maintenance()** (3 connections) — `server/npc/lifecycle_manager.py`
- **test_attempt_optional_npc_spawn_success_routes_through_population_controller()** (3 connections) — `server/tests/unit/npc/test_lifecycle_periodic.py`
- **test_should_not_skip_when_interval_elapsed()** (3 connections) — `server/tests/unit/npc/test_lifecycle_periodic.py`
- **.get_respawn_delay()** (2 connections) — `server/config/npc_config.py`
- **test_attempt_optional_npc_spawn_no_controller()** (2 connections) — `server/tests/unit/npc/test_lifecycle_periodic.py`
- **test_attempt_optional_npc_spawn_no_zone_config()** (2 connections) — `server/tests/unit/npc/test_lifecycle_periodic.py`
- *... and 39 more nodes in this community*

## Relationships

- [NPCLifecycleManager](NPCLifecycleManager.md) (13 shared connections)
- [NPCDefinition](NPCDefinition.md) (4 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (3 shared connections)
- [test_lifecycle_respawn.py](test_lifecycle_respawn.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [connection_manager.py](connection_manager.py.md) (2 shared connections)
- [test_npc_utils.py](test_npc_utils.py.md) (1 shared connections)

## Source Files

- `server/config/npc_config.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/lifecycle_periodic.py`
- `server/tests/unit/npc/test_lifecycle_periodic.py`

## Audit Trail

- EXTRACTED: 139 (97%)
- INFERRED: 5 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*