# aggro_threat.py

> 150 nodes · cohesion 0.02

## Key Concepts

- **test_population_control.py** (65 connections) — `server/tests/unit/npc/test_population_control.py`
- **PopulationStats** (40 connections) — `server/npc/population_stats.py`
- **test_population_stats.py** (23 connections) — `server/tests/unit/npc/test_population_stats.py`
- **population_stats.py** (7 connections) — `server/npc/population_stats.py`
- **population_controller()** (5 connections) — `server/tests/unit/npc/test_population_control.py`
- **mock_event_bus()** (4 connections) — `server/tests/unit/npc/test_population_control.py`
- **fixture** (4 connections)
- **test_should_spawn_npc()** (4 connections) — `server/tests/unit/npc/test_population_control.py`
- **.to_dict()** (3 connections) — `server/npc/population_stats.py`
- **.get_population_stats()** (3 connections) — `server/npc/spawning_service.py`
- **mock_async_persistence()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **mock_lifecycle_manager()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_check_spawn_requirements_for_room_with_definitions()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_clear_population_stats()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_despawn_npc_success()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_get_population_stats_existing()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_get_zone_configuration_exact_match()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_get_zone_configuration_no_slash()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_get_zone_configuration_zone_fallback()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_get_zone_population_summary_with_stats()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_handle_npc_entered_room()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_handle_npc_left_room()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_handle_player_entered_room()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_handle_player_left_room()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_population_controller_init()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- *... and 125 more nodes in this community*

## Relationships

- [CombatInstance](CombatInstance.md) (14 shared connections)
- [test_message_category_invariants.py](test_message_category_invariants.py.md) (7 shared connections)
- [RoomLoader](RoomLoader.md) (5 shared connections)
- [BaseEvent](BaseEvent.md) (5 shared connections)
- [test_container_persistence_async_helpers.py](test_container_persistence_async_helpers.py.md) (2 shared connections)
- [get_username_from_user](get_username_from_user.md) (2 shared connections)
- [ADR-023: Package Ownership (`game/` vs `services/` vs `npc/`) and Fan-Out Watch List](ADR-023-_Package_Ownership_`game-`_vs_`services-`_vs_`npc-`_and_Fan-Out_Watch_List.md) (2 shared connections)
- [ErrorType](ErrorType.md) (2 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (1 shared connections)
- [test_rescue_service.py](test_rescue_service.py.md) (1 shared connections)

## Source Files

- `server/npc/population_stats.py`
- `server/npc/spawning_service.py`
- `server/tests/unit/npc/test_population_control.py`
- `server/tests/unit/npc/test_population_stats.py`

## Audit Trail

- EXTRACTED: 216 (98%)
- INFERRED: 5 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*