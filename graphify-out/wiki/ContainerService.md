# ContainerService

> 94 nodes

## Key Concepts

- **ContainerService** (79 connections) — `server/services/container_service.py`
- **test_container_service.py** (61 connections) — `server/tests/unit/services/test_container_service.py`
- **transfer_all_items_from_container()** (21 connections) — `server/api/container_helpers.py`
- **asyncio** (18 connections)
- **TestTransferAllItemsFromContainer** (16 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **_container_data()** (16 connections) — `server/tests/unit/services/test_container_service.py`
- **api/conftest.py** (16 connections) — `server/tests/unit/api/conftest.py`
- **MutationDecision** (15 connections) — `server/services/inventory_mutation_guard.py`
- **asyncio** (14 connections)
- **_stack()** (12 connections) — `server/tests/unit/services/test_container_service.py`
- **.test_transfer_all_items_from_container_capacity_error()** (7 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **fixture** (7 connections)
- **.test_transfer_all_items_from_container_empty_items()** (6 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_item_without_quantity()** (6 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_multiple_items()** (6 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_partial_success()** (6 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_result_missing_container()** (6 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_result_missing_inventory()** (6 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_success()** (6 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_transfer_error()** (6 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_updates_from_result()** (6 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **test_transfer_to_container_mutation_guard_suppressed()** (6 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_to_container_player_not_found()** (6 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_to_container_success()** (6 connections) — `server/tests/unit/services/test_container_service.py`
- **test_lock_container_updates_state()** (5 connections) — `server/tests/unit/services/test_container_service.py`
- *... and 69 more nodes in this community*

## Relationships

- [container_endpoints_basic.py](container_endpoints_basic.py.md) (37 shared connections)
- [ContainerComponent](ContainerComponent.md) (27 shared connections)
- [ContainerServiceError](ContainerServiceError.md) (9 shared connections)
- [InventoryService](InventoryService.md) (7 shared connections)
- [ContainerLockState](ContainerLockState.md) (7 shared connections)
- [InventoryMutationGuard](InventoryMutationGuard.md) (6 shared connections)
- [pytest.md](pytest.md.md) (4 shared connections)
- [ValidationError](ValidationError.md) (3 shared connections)
- [GameBundle](GameBundle.md) (2 shared connections)
- [command_service.py](command_service.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [DatabaseError](DatabaseError.md) (2 shared connections)

## Source Files

- `server/api/container_helpers.py`
- `server/services/container_service.py`
- `server/services/inventory_mutation_guard.py`
- `server/tests/unit/api/conftest.py`
- `server/tests/unit/api/test_container_helpers_loot.py`
- `server/tests/unit/services/test_container_service.py`

## Audit Trail

- EXTRACTED: 244 (77%)
- INFERRED: 71 (23%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*