# test_npc_utils.py

> 116 nodes

## Key Concepts

- **test_npc_utils.py** (34 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **despawn_npc_impl()** (20 connections) — `server/npc/lifecycle_despawn.py`
- **test_lifecycle_despawn.py** (19 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **get_zone_key_from_room_id()** (17 connections) — `server/npc/npc_utils.py`
- **lifecycle_despawn.py** (16 connections) — `server/npc/lifecycle_despawn.py`
- **extract_room_id_from_npc()** (15 connections) — `server/npc/npc_utils.py`
- **NPCLifecycleEvent** (13 connections) — `server/npc/lifecycle_types.py`
- **extract_definition_id_from_npc()** (12 connections) — `server/npc/npc_utils.py`
- **extract_npc_metadata()** (12 connections) — `server/npc/npc_utils.py`
- **npc_utils.py** (11 connections) — `server/npc/npc_utils.py`
- **_make_manager()** (10 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **extract_room_id_from_lifecycle_record()** (8 connections) — `server/npc/npc_utils.py`
- **.despawn_npc()** (8 connections) — `server/npc/population_control.py`
- **_resolve_despawn_room_id()** (6 connections) — `server/npc/lifecycle_despawn.py`
- **._get_active_npcs_from_lifecycle_manager()** (6 connections) — `server/npc/population_control.py`
- **_remove_npc_from_room_on_despawn()** (5 connections) — `server/npc/lifecycle_despawn.py`
- **.cleanup_inactive_npcs()** (5 connections) — `server/npc/population_control.py`
- **._get_zone_key_from_room_id()** (5 connections) — `server/npc/population_control.py`
- **._should_remove_inactive_npc()** (5 connections) — `server/npc/population_control.py`
- **test_despawn_exception_sets_error_state()** (5 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **test_despawn_success_with_persistence_and_room()** (5 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **Any** (5 connections)
- **.is_required()** (4 connections) — `server/models/npc.py`
- **_room_id_from_lifecycle_event()** (4 connections) — `server/npc/npc_utils.py`
- **._update_population_stats_for_despawn()** (4 connections) — `server/npc/population_control.py`
- *... and 91 more nodes in this community*

## Relationships

- [event_types.py](event_types.py.md) (34 shared connections)
- [PopulationStats](PopulationStats.md) (2 shared connections)
- [NPCBase](NPCBase.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [NPCLifecycleRecord](NPCLifecycleRecord.md) (1 shared connections)
- [NPCDefinition](NPCDefinition.md) (1 shared connections)
- [ZoneConfiguration](ZoneConfiguration.md) (1 shared connections)

## Source Files

- `server/models/npc.py`
- `server/npc/lifecycle_despawn.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/lifecycle_types.py`
- `server/npc/npc_utils.py`
- `server/npc/population_control.py`
- `server/tests/unit/npc/test_lifecycle_despawn.py`
- `server/tests/unit/npc/test_npc_utils.py`

## Audit Trail

- EXTRACTED: 222 (95%)
- INFERRED: 11 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*