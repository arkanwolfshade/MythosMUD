# lifespan_protocols.py

> 48 nodes

## Key Concepts

- **LootAllRequest** (58 connections) — `server/api/container_models.py`
- **ContainerService** (34 connections) — `server/services/container_service.py`
- **test_container_helpers_loot.py** (24 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **transfer_all_items_from_container()** (21 connections) — `server/api/container_helpers.py`
- **get_container_and_player_for_loot_all()** (17 connections) — `server/api/container_helpers.py`
- **TestTransferAllItemsFromContainer** (16 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **asyncio** (14 connections)
- **TestGetContainerAndPlayerForLootAll** (10 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_capacity_error()** (7 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_empty_items()** (6 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_item_without_quantity()** (6 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_multiple_items()** (6 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_partial_success()** (6 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_result_missing_container()** (6 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_result_missing_inventory()** (6 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_success()** (6 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_transfer_error()** (6 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_updates_from_result()** (6 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_get_container_and_player_for_loot_all_container_not_found()** (5 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_get_container_and_player_for_loot_all_player_no_inventory()** (5 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_get_container_and_player_for_loot_all_player_not_found()** (5 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_get_container_and_player_for_loot_all_success()** (5 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **mock_persistence()** (3 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **mock_request()** (3 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **mock_user()** (3 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- *... and 23 more nodes in this community*

## Relationships

- [ValidationError](ValidationError.md) (42 shared connections)
- [ChatService](ChatService.md) (15 shared connections)
- [asyncio](asyncio.md) (8 shared connections)
- [ContainerComponent](ContainerComponent.md) (7 shared connections)
- [P7 · Rulings — complete](P7_·_Rulings_—_complete.md) (3 shared connections)
- [NPCSpawningService](NPCSpawningService.md) (3 shared connections)
- [NATSServicePoolMixin](NATSServicePoolMixin.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [.disconnect](disconnect.md) (2 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (2 shared connections)
- [Performance Profiler Subagent](Performance_Profiler_Subagent.md) (1 shared connections)
- [Test File Migration Mapping](Test_File_Migration_Mapping.md) (1 shared connections)

## Source Files

- `server/api/container_helpers.py`
- `server/api/container_models.py`
- `server/services/container_service.py`
- `server/tests/unit/api/test_container_helpers_loot.py`

## Audit Trail

- EXTRACTED: 177 (87%)
- INFERRED: 26 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*