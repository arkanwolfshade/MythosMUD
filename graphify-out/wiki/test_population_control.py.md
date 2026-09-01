# test_population_control.py

> 89 nodes

## Key Concepts

- **test_population_control.py** (66 connections) — `server/tests/unit/npc/test_population_control.py`
- **mock_event_bus()** (4 connections) — `server/tests/unit/npc/test_population_control.py`
- **population_controller()** (4 connections) — `server/tests/unit/npc/test_population_control.py`
- **fixture** (4 connections)
- **mock_async_persistence()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **mock_lifecycle_manager()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_check_spawn_requirements_for_room_with_definitions()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_get_zone_configuration_exact_match()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_get_zone_configuration_no_slash()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_get_zone_configuration_zone_fallback()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_handle_npc_entered_room()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_handle_npc_left_room()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_handle_player_entered_room()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_handle_player_left_room()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_population_controller_init()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_population_controller_init_requires_async_persistence()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_check_spawn_requirements_for_room_no_config()** (2 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_cleanup_inactive_npcs_empty()** (2 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_cleanup_inactive_npcs_invalid_spawned_at()** (2 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_cleanup_inactive_npcs_keeps_required()** (2 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_cleanup_inactive_npcs_multiple_removals()** (2 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_cleanup_inactive_npcs_no_spawned_at()** (2 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_cleanup_inactive_npcs_removes_old_npcs()** (2 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_despawn_npc_no_lifecycle_manager()** (2 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_despawn_npc_not_found()** (2 connections) — `server/tests/unit/npc/test_population_control.py`
- *... and 64 more nodes in this community*

## Relationships

- [EventBus](EventBus.md) (9 shared connections)
- [PopulationStats](PopulationStats.md) (7 shared connections)
- [ZoneConfiguration](ZoneConfiguration.md) (6 shared connections)
- [event_types.py](event_types.py.md) (4 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (4 shared connections)
- [NPCSpawnRule](NPCSpawnRule.md) (2 shared connections)
- [NPCDefinition](NPCDefinition.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/tests/unit/npc/test_population_control.py`

## Audit Trail

- EXTRACTED: 123 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*