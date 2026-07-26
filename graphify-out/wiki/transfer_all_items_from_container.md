# transfer_all_items_from_container

> 26 nodes · cohesion 0.10

## Key Concepts

- **transfer_all_items_from_container()** (21 connections) — `server/api/container_helpers.py`
- **TestTransferAllItemsFromContainer** (20 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_capacity_error()** (6 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_empty_items()** (5 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_item_without_quantity()** (5 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_multiple_items()** (5 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_partial_success()** (5 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_result_missing_container()** (5 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_result_missing_inventory()** (5 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_success()** (5 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_transfer_error()** (5 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_updates_from_result()** (5 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **ContainerComponent** (2 connections)
- **InventoryStack** (2 connections)
- **Transfer all items from container to player, returning updated container and inv** (1 connections) — `server/api/container_helpers.py`
- **Test transfer_all_items_from_container function.** (1 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **Test transfer_all_items_from_container transfers all items.** (1 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **Test transfer_all_items_from_container stops on capacity error.** (1 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **Test transfer_all_items_from_container continues on transfer error.** (1 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **Test transfer_all_items_from_container handles multiple items.** (1 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **Test transfer_all_items_from_container handles items without quantity field.** (1 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **Test transfer_all_items_from_container handles partial success with some items f** (1 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **Test transfer_all_items_from_container handles empty items list.** (1 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **Test transfer_all_items_from_container updates container_data and inventory from** (1 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **Test transfer_all_items_from_container handles result without container key.** (1 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- *... and 1 more nodes in this community*

## Relationships

- [ContainerComponent](ContainerComponent.md) (16 shared connections)
- [ContainerService](ContainerService.md) (12 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (11 shared connections)
- [User](User.md) (1 shared connections)

## Source Files

- `server/api/container_helpers.py`
- `server/tests/unit/api/test_container_helpers_loot.py`

## Audit Trail

- EXTRACTED: 100 (93%)
- INFERRED: 8 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*