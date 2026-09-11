# test_npc_utils.py

> 106 nodes

## Key Concepts

- **test_npc_utils.py** (37 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **get_zone_key_from_room_id()** (17 connections) — `server/npc/npc_utils.py`
- **extract_room_id_from_npc()** (15 connections) — `server/npc/npc_utils.py`
- **npc_utils.py** (14 connections) — `server/npc/npc_utils.py`
- **extract_definition_id_from_npc()** (12 connections) — `server/npc/npc_utils.py`
- **extract_npc_metadata()** (12 connections) — `server/npc/npc_utils.py`
- **spawn_npc_via_population_controller()** (11 connections) — `server/npc/npc_utils.py`
- **extract_room_id_from_lifecycle_record()** (8 connections) — `server/npc/npc_utils.py`
- **.despawn_npc()** (8 connections) — `server/npc/population_control.py`
- **._check_spawn_requirements_for_room()** (7 connections) — `server/npc/population_control.py`
- **_resolve_despawn_room_id()** (6 connections) — `server/npc/lifecycle_despawn.py`
- **._get_active_npcs_from_lifecycle_manager()** (6 connections) — `server/npc/population_control.py`
- **._register_spawned_npc_in_population_stats()** (6 connections) — `server/npc/population_control.py`
- **._spawn_npc()** (6 connections) — `server/npc/population_control.py`
- **Any** (6 connections)
- **.cleanup_inactive_npcs()** (5 connections) — `server/npc/population_control.py`
- **._get_zone_key_from_room_id()** (5 connections) — `server/npc/population_control.py`
- **._should_remove_inactive_npc()** (5 connections) — `server/npc/population_control.py`
- **.is_required()** (4 connections) — `server/models/npc.py`
- **_room_id_from_lifecycle_event()** (4 connections) — `server/npc/npc_utils.py`
- **.get_zone_configuration()** (4 connections) — `server/npc/population_control.py`
- **._update_population_stats_for_despawn()** (4 connections) — `server/npc/population_control.py`
- **_stable_room_id_for_zone()** (3 connections) — `server/npc/npc_utils.py`
- **.get_zone_population_summary()** (3 connections) — `server/npc/population_control.py`
- **test_extract_definition_id_from_npc_from_lifecycle_manager()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- *... and 81 more nodes in this community*

## Relationships

- [event_types.py](event_types.py.md) (22 shared connections)
- [NPCDefinition](NPCDefinition.md) (6 shared connections)
- [test_lifecycle_periodic.py](test_lifecycle_periodic.py.md) (3 shared connections)
- [test_lifecycle_respawn.py](test_lifecycle_respawn.py.md) (3 shared connections)
- [test_population_control.py](test_population_control.py.md) (2 shared connections)
- [NPCBase](NPCBase.md) (2 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (1 shared connections)

## Source Files

- `server/models/npc.py`
- `server/npc/lifecycle_despawn.py`
- `server/npc/npc_utils.py`
- `server/npc/population_control.py`
- `server/tests/unit/npc/test_npc_utils.py`

## Audit Trail

- EXTRACTED: 190 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*