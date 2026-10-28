# test_event_publisher.py

> 112 nodes · cohesion 0.04

## Key Concepts

- **test_container_persistence_async_helpers.py** (47 connections) — `server/tests/unit/persistence/test_container_persistence_async_helpers.py`
- **container_persistence_async.py** (37 connections) — `server/persistence/container_persistence_async.py`
- **container_query_helpers_async.py** (25 connections) — `server/persistence/container_query_helpers_async.py`
- **container_repository.py** (25 connections) — `server/persistence/repositories/container_repository.py`
- **test_container_query_helpers_async.py** (22 connections) — `server/tests/unit/persistence/test_container_query_helpers_async.py`
- **create_container_async()** (15 connections) — `server/persistence/container_persistence_async.py`
- **get_container_async()** (15 connections) — `server/persistence/container_persistence_async.py`
- **update_container_async()** (15 connections) — `server/persistence/container_persistence_async.py`
- **_build_container_data_from_row_async()** (15 connections) — `server/persistence/container_query_helpers_async.py`
- **get_bank_container_async()** (14 connections) — `server/persistence/container_query_helpers_async.py`
- **get_decayed_containers_async()** (14 connections) — `server/persistence/container_query_helpers_async.py`
- **asyncio** (14 connections)
- **_finalize_container_creation()** (13 connections) — `server/persistence/container_persistence_async.py`
- **get_containers_by_entity_id_async()** (13 connections) — `server/persistence/container_query_helpers_async.py`
- **fetch_container_items_async()** (12 connections) — `server/persistence/container_persistence_async.py`
- **_populate_container_items_async()** (12 connections) — `server/persistence/container_persistence_async.py`
- **Any** (12 connections)
- **get_containers_by_room_id_async()** (12 connections) — `server/persistence/container_query_helpers_async.py`
- **_build_item_dict()** (11 connections) — `server/persistence/container_persistence_async.py`
- **_container_data_from_row()** (11 connections) — `server/persistence/container_persistence_async.py`
- **delete_container_async()** (10 connections) — `server/persistence/container_persistence_async.py`
- **asyncio** (10 connections)
- **_call_create_container_procedure()** (9 connections) — `server/persistence/container_persistence_async.py`
- **AsyncSession** (9 connections)
- **_validate_container_create_params()** (9 connections) — `server/persistence/container_persistence_async.py`
- *... and 87 more nodes in this community*

## Relationships

- [.profession_to_dict](profession_to_dict.md) (38 shared connections)
- [endpoints.py](endpoints.py.md) (25 shared connections)
- [LoggingPatternLinter](LoggingPatternLinter.md) (10 shared connections)
- [Room](Room.md) (6 shared connections)
- [AttributeError](AttributeError.md) (6 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (5 shared connections)
- [command_result_text](command_result_text.md) (2 shared connections)
- [item_prototype.schema.json](item_prototype.schema.json.md) (2 shared connections)
- [combat_taunt.py](combat_taunt.py.md) (1 shared connections)
- [✅ Phase 2 Async Persistence Migration - COMPLETE](✅_Phase_2_Async_Persistence_Migration_-_COMPLETE.md) (1 shared connections)

## Source Files

- `server/persistence/container_helpers.py`
- `server/persistence/container_persistence_async.py`
- `server/persistence/container_query_helpers_async.py`
- `server/persistence/repositories/container_repository.py`
- `server/tests/unit/persistence/test_container_persistence_async_helpers.py`
- `server/tests/unit/persistence/test_container_query_helpers_async.py`

## Audit Trail

- EXTRACTED: 351 (96%)
- INFERRED: 16 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*