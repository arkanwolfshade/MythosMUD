# LootAllRequest

> 88 nodes

## Key Concepts

- **LootAllRequest** (58 connections) — `server/api/container_models.py`
- **test_container_helpers_loot.py** (24 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **transfer_all_items_from_container()** (21 connections) — `server/api/container_helpers.py`
- **handle_container_service_error()** (19 connections) — `server/api/container_helpers.py`
- **get_container_and_player_for_loot_all()** (17 connections) — `server/api/container_helpers.py`
- **TestTransferAllItemsFromContainer** (16 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **asyncio** (14 connections)
- **TestGetContainerAndPlayerForLootAll** (10 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **TestHandleContainerServiceErrorEdgeCases** (8 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **TestHandleContainerServiceError** (8 connections) — `server/tests/unit/api/test_container_helpers.py`
- **.test_transfer_all_items_from_container_capacity_error()** (7 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **asyncio** (7 connections)
- **.test_loot_all_items_emit_event_failure()** (6 connections) — `server/tests/unit/api/test_container_endpoints_loot_register.py`
- **.test_transfer_all_items_from_container_empty_items()** (6 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_item_without_quantity()** (6 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_multiple_items()** (6 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_partial_success()** (6 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_result_missing_container()** (6 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_result_missing_inventory()** (6 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_success()** (6 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_transfer_error()** (6 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_updates_from_result()** (6 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **UUID** (6 connections)
- **.test_loot_all_items_all_items_looted()** (5 connections) — `server/tests/unit/api/test_container_endpoints_loot_register.py`
- **.test_loot_all_items_audit_log_error_handled()** (5 connections) — `server/tests/unit/api/test_container_endpoints_loot_register.py`
- *... and 63 more nodes in this community*

## Relationships

- [container_endpoints_basic.py](container_endpoints_basic.py.md) (39 shared connections)
- [ContainerComponent](ContainerComponent.md) (18 shared connections)
- [TransferContainerRequest](TransferContainerRequest.md) (16 shared connections)
- [ContainerService](ContainerService.md) (13 shared connections)
- [ContainerServiceError](ContainerServiceError.md) (13 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (7 shared connections)
- [User](User.md) (6 shared connections)
- [test_containers.py](test_containers.py.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/api/container_helpers.py`
- `server/api/container_models.py`
- `server/tests/unit/api/test_container_endpoints_loot_register.py`
- `server/tests/unit/api/test_container_helpers.py`
- `server/tests/unit/api/test_container_helpers_loot.py`

## Audit Trail

- EXTRACTED: 234 (88%)
- INFERRED: 32 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*