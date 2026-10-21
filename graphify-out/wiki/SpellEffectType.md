# SpellEffectType

> 65 nodes · cohesion 0.06

## Key Concepts

- **test_lifecycle_periodic.py** (42 connections) — `server/tests/unit/npc/test_lifecycle_periodic.py`
- **NPCLifecycleState** (24 connections) — `server/npc/lifecycle_types.py`
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
- **.cleanup_old_records()** (3 connections) — `server/npc/lifecycle_manager.py`
- **.periodic_maintenance()** (3 connections) — `server/npc/lifecycle_manager.py`
- **test_attempt_optional_npc_spawn_success_routes_through_population_controller()** (3 connections) — `server/tests/unit/npc/test_lifecycle_periodic.py`
- **test_should_not_skip_when_interval_elapsed()** (3 connections) — `server/tests/unit/npc/test_lifecycle_periodic.py`
- **.get_respawn_delay()** (2 connections) — `server/config/npc_config.py`
- **StrEnum** (2 connections)
- **test_attempt_optional_npc_spawn_no_controller()** (2 connections) — `server/tests/unit/npc/test_lifecycle_periodic.py`
- *... and 40 more nodes in this community*

## Relationships

- [ADR-023: Package Ownership (`game/` vs `services/` vs `npc/`) and Fan-Out Watch List](ADR-023-_Package_Ownership_`game-`_vs_`services-`_vs_`npc-`_and_Fan-Out_Watch_List.md) (10 shared connections)
- [CombatInstance](CombatInstance.md) (9 shared connections)
- [SpellLearningService](SpellLearningService.md) (6 shared connections)
- [CombatService](CombatService.md) (3 shared connections)
- [ErrorType](ErrorType.md) (3 shared connections)
- [test_rescue_service.py](test_rescue_service.py.md) (3 shared connections)
- [Room](Room.md) (2 shared connections)
- [test_container_persistence_async_helpers.py](test_container_persistence_async_helpers.py.md) (2 shared connections)

## Source Files

- `server/config/npc_config.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/lifecycle_periodic.py`
- `server/npc/lifecycle_types.py`
- `server/tests/unit/npc/test_lifecycle_periodic.py`

## Audit Trail

- EXTRACTED: 148 (92%)
- INFERRED: 13 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*