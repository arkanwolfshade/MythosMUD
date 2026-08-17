# LootAllRequest

> 41 nodes

## Key Concepts

- **LootAllRequest** (58 connections) — `server/api/container_models.py`
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
- **ContainerComponent** (2 connections)
- **InventoryStack** (2 connections)
- **Get container and player data for loot_all operation.** (1 connections) — `server/api/container_helpers.py`
- **Transfer all items from container to player, returning updated container and…** (1 connections) — `server/api/container_helpers.py`
- **Request model for looting all items from a container.** (1 connections) — `server/api/container_models.py`
- *... and 16 more nodes in this community*

## Relationships

- [loot_all_items](loot_all_items.md) (22 shared connections)
- [get_logger](get_logger.md) (19 shared connections)
- [ContainerService](ContainerService.md) (12 shared connections)
- [emit_loot_all_event](emit_loot_all_event.md) (8 shared connections)
- [ContainerComponent](ContainerComponent.md) (5 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (3 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (2 shared connections)
- [TransferContainerRequest](TransferContainerRequest.md) (1 shared connections)
- [register_loot_endpoints](register_loot_endpoints.md) (1 shared connections)
- [User](User.md) (1 shared connections)

## Source Files

- `server/api/container_helpers.py`
- `server/api/container_models.py`
- `server/tests/unit/api/test_container_helpers_loot.py`

## Audit Trail

- EXTRACTED: 139 (89%)
- INFERRED: 18 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*