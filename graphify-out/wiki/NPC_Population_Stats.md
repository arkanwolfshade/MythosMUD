# NPC Population Stats

> 148 nodes

## Key Concepts

- **test_population_control.py** (65 connections) — `server/tests/unit/npc/test_population_control.py`
- **PopulationStats** (40 connections) — `server/npc/population_stats.py`
- **test_population_stats.py** (23 connections) — `server/tests/unit/npc/test_population_stats.py`
- **mock_event_bus()** (4 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_should_spawn_npc()** (4 connections) — `server/tests/unit/npc/test_population_control.py`
- **fixture** (4 connections)
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
- **test_population_controller_init_requires_async_persistence()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_add_npc_multiple_same_room()** (3 connections) — `server/tests/unit/npc/test_population_stats.py`
- *... and 123 more nodes in this community*

## Relationships

- [NPC Behavior Engine](NPC_Behavior_Engine.md) (11 shared connections)
- [Community 40](Community_40.md) (8 shared connections)
- [NPC Definition JSON](NPC_Definition_JSON.md) (8 shared connections)
- [Game Event Types](Game_Event_Types.md) (5 shared connections)
- [NPC Room Lifecycle](NPC_Room_Lifecycle.md) (4 shared connections)
- [Distributed Event Bus (NATS)](Distributed_Event_Bus_NATS.md) (3 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (1 shared connections)

## Source Files

- `server/npc/population_stats.py`
- `server/npc/spawning_service.py`
- `server/tests/unit/npc/test_population_control.py`
- `server/tests/unit/npc/test_population_stats.py`

## Audit Trail

- EXTRACTED: 212 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*