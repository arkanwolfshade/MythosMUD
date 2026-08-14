# population_control.py

> 91 nodes

## Key Concepts

- **population_control.py** (42 connections) — `server/npc/population_control.py`
- **test_npc_utils.py** (34 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **get_zone_key_from_room_id()** (17 connections) — `server/npc/npc_utils.py`
- **extract_room_id_from_npc()** (15 connections) — `server/npc/npc_utils.py`
- **extract_definition_id_from_npc()** (12 connections) — `server/npc/npc_utils.py`
- **extract_npc_metadata()** (12 connections) — `server/npc/npc_utils.py`
- **npc_utils.py** (11 connections) — `server/npc/npc_utils.py`
- **extract_room_id_from_lifecycle_record()** (8 connections) — `server/npc/npc_utils.py`
- **.despawn_npc()** (8 connections) — `server/npc/population_control.py`
- **._get_active_npcs_from_lifecycle_manager()** (6 connections) — `server/npc/population_control.py`
- **.cleanup_inactive_npcs()** (5 connections) — `server/npc/population_control.py`
- **._get_zone_key_from_room_id()** (5 connections) — `server/npc/population_control.py`
- **._should_remove_inactive_npc()** (5 connections) — `server/npc/population_control.py`
- **Any** (5 connections)
- **.is_required()** (4 connections) — `server/models/npc.py`
- **_room_id_from_lifecycle_event()** (4 connections) — `server/npc/npc_utils.py`
- **._update_population_stats_for_despawn()** (4 connections) — `server/npc/population_control.py`
- **_stable_room_id_for_zone()** (3 connections) — `server/npc/npc_utils.py`
- **.get_zone_population_summary()** (3 connections) — `server/npc/population_control.py`
- **test_extract_definition_id_from_npc_from_lifecycle_manager()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_extract_definition_id_from_npc_has_definition_id()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_extract_definition_id_from_npc_lifecycle_manager_no_definition()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_extract_definition_id_from_npc_lifecycle_manager_no_record()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_extract_definition_id_from_npc_no_manager()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_extract_definition_id_from_npc_non_int()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- *... and 66 more nodes in this community*

## Relationships

- [EventBus](EventBus.md) (12 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (12 shared connections)
- [lifecycle_manager.py](lifecycle_manager.py.md) (8 shared connections)
- [event_types.py](event_types.py.md) (7 shared connections)
- [ZoneConfiguration](ZoneConfiguration.md) (5 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [connection_manager.py](connection_manager.py.md) (1 shared connections)
- [NPCSpawnRule](NPCSpawnRule.md) (1 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (1 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (1 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (1 shared connections)
- [zone_config_loader.py](zone_config_loader.py.md) (1 shared connections)

## Source Files

- `server/models/npc.py`
- `server/npc/npc_utils.py`
- `server/npc/population_control.py`
- `server/tests/unit/npc/test_npc_utils.py`

## Audit Trail

- EXTRACTED: 189 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*