# test_population_control.py

> 146 nodes

## Key Concepts

- **test_population_control.py** (65 connections) — `server/tests/unit/npc/test_population_control.py`
- **PopulationStats** (42 connections) — `server/npc/population_stats.py`
- **test_population_stats.py** (23 connections) — `server/tests/unit/npc/test_population_stats.py`
- **.get_population_stats()** (4 connections) — `server/npc/population_control.py`
- **population_controller()** (4 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_should_spawn_npc()** (4 connections) — `server/tests/unit/npc/test_population_control.py`
- **fixture** (4 connections)
- **.to_dict()** (3 connections) — `server/npc/population_stats.py`
- **.get_population_stats()** (3 connections) — `server/npc/spawning_service.py`
- **mock_async_persistence()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **mock_event_bus()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **mock_lifecycle_manager()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_clear_population_stats()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_despawn_npc_success()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_get_population_stats_existing()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_get_zone_population_summary_with_stats()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_handle_npc_entered_room()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_handle_npc_left_room()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_handle_player_entered_room()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_handle_player_left_room()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_population_controller_init()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_population_controller_init_requires_async_persistence()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_add_npc_multiple_same_room()** (3 connections) — `server/tests/unit/npc/test_population_stats.py`
- **test_add_npc_multiple_same_type()** (3 connections) — `server/tests/unit/npc/test_population_stats.py`
- **test_add_npc_optional()** (3 connections) — `server/tests/unit/npc/test_population_stats.py`
- *... and 121 more nodes in this community*

## Relationships

- [get_npc_instance_service](get_npc_instance_service.md) (15 shared connections)
- [EventBus](EventBus.md) (14 shared connections)
- [ZoneConfiguration](ZoneConfiguration.md) (6 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (2 shared connections)
- [test_npc_utils.py](test_npc_utils.py.md) (1 shared connections)
- [_PopulationLifecycleManager](_PopulationLifecycleManager.md) (1 shared connections)
- [zone_config_loader.py](zone_config_loader.py.md) (1 shared connections)
- [time.py](time.py.md) (1 shared connections)

## Source Files

- `server/npc/population_control.py`
- `server/npc/population_stats.py`
- `server/npc/spawning_service.py`
- `server/tests/unit/npc/test_population_control.py`
- `server/tests/unit/npc/test_population_stats.py`

## Audit Trail

- EXTRACTED: 209 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*