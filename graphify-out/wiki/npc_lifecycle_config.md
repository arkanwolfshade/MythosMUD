# npc lifecycle config

> 58 nodes

## Key Concepts

- **test_lifecycle_periodic.py** (41 connections) — `server/tests/unit/npc/test_lifecycle_periodic.py`
- **check_optional_npc_spawns_impl()** (13 connections) — `server/npc/lifecycle_periodic.py`
- **run_periodic_maintenance_impl()** (11 connections) — `server/npc/lifecycle_periodic.py`
- **NPCMaintenanceConfig** (9 connections) — `server/config/npc_config.py`
- **cleanup_old_records_impl()** (9 connections) — `server/npc/lifecycle_periodic.py`
- **_should_skip_optional_npc()** (9 connections) — `server/npc/lifecycle_periodic.py`
- **_check_spawn_conditions_for_optional_npc()** (9 connections) — `server/npc/lifecycle_periodic.py`
- **_attempt_optional_npc_spawn()** (9 connections) — `server/npc/lifecycle_periodic.py`
- **get_zone_key_for_definition()** (9 connections) — `server/npc/lifecycle_periodic.py`
- **Any** (8 connections)
- **get_spawn_room_for_definition()** (8 connections) — `server/npc/lifecycle_periodic.py`
- **npc_config.py** (5 connections) — `server/config/npc_config.py`
- **_make_record()** (4 connections) — `server/tests/unit/npc/test_lifecycle_periodic.py`
- **.get_config_summary()** (3 connections) — `server/config/npc_config.py`
- **.cleanup_old_records()** (3 connections) — `server/npc/lifecycle_manager.py`
- **.periodic_maintenance()** (3 connections) — `server/npc/lifecycle_manager.py`
- **test_cleanup_old_records_removes_stale_despawned()** (3 connections) — `server/tests/unit/npc/test_lifecycle_periodic.py`
- **test_cleanup_old_records_removes_stale_error()** (3 connections) — `server/tests/unit/npc/test_lifecycle_periodic.py`
- **.get_respawn_delay()** (2 connections) — `server/config/npc_config.py`
- **test_run_periodic_maintenance_respawn_and_cleanup()** (2 connections) — `server/tests/unit/npc/test_lifecycle_periodic.py`
- **test_run_periodic_maintenance_spawn_check_exception()** (2 connections) — `server/tests/unit/npc/test_lifecycle_periodic.py`
- **test_check_optional_npc_spawns_no_population_controller()** (2 connections) — `server/tests/unit/npc/test_lifecycle_periodic.py`
- **test_should_skip_required_npc()** (2 connections) — `server/tests/unit/npc/test_lifecycle_periodic.py`
- **test_should_skip_npc_in_respawn_queue()** (2 connections) — `server/tests/unit/npc/test_lifecycle_periodic.py`
- **test_should_skip_recent_spawn_check()** (2 connections) — `server/tests/unit/npc/test_lifecycle_periodic.py`
- *... and 33 more nodes in this community*

## Relationships

- [models npc rationale](models_npc_rationale.md) (14 shared connections)
- [command parser rationale](command_parser_rationale.md) (8 shared connections)
- [player persistence repository](player_persistence_repository.md) (2 shared connections)
- [npc aggressive mob](npc_aggressive_mob.md) (1 shared connections)

## Source Files

- `server/config/npc_config.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/lifecycle_periodic.py`
- `server/tests/unit/npc/test_lifecycle_periodic.py`

## Audit Trail

- EXTRACTED: 223 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*