# ContainerService

> 76 nodes

## Key Concepts

- **ContainerService** (79 connections) — `server/services/container_service.py`
- **test_container_service.py** (61 connections) — `server/tests/unit/services/test_container_service.py`
- **asyncio** (18 connections)
- **TestTransferAllItemsFromContainer** (16 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **_container_data()** (16 connections) — `server/tests/unit/services/test_container_service.py`
- **MutationDecision** (15 connections) — `server/services/inventory_mutation_guard.py`
- **asyncio** (14 connections)
- **_stack()** (12 connections) — `server/tests/unit/services/test_container_service.py`
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
- **test_transfer_to_container_mutation_guard_suppressed()** (6 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_to_container_player_not_found()** (6 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_to_container_success()** (6 connections) — `server/tests/unit/services/test_container_service.py`
- **.test_get_container_and_player_for_loot_all_container_not_found()** (5 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **test_lock_container_updates_state()** (5 connections) — `server/tests/unit/services/test_container_service.py`
- **test_open_container_player_not_found()** (5 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_to_container_capacity_exceeded()** (5 connections) — `server/tests/unit/services/test_container_service.py`
- *... and 51 more nodes in this community*

## Relationships

- [LootAllRequest](LootAllRequest.md) (35 shared connections)
- [ContainerComponent](ContainerComponent.md) (33 shared connections)
- [ContainerServiceError](ContainerServiceError.md) (9 shared connections)
- [server/services/__init__.py](server-services-__init__.py.md) (7 shared connections)
- [TestExecuteTransfer](TestExecuteTransfer.md) (3 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (3 shared connections)
- [InventoryMutationGuard](InventoryMutationGuard.md) (3 shared connections)
- [test_inventory_mutation_guard.py](test_inventory_mutation_guard.py.md) (3 shared connections)
- [ValidationError](ValidationError.md) (3 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (2 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (2 shared connections)
- [SkillService](SkillService.md) (1 shared connections)

## Source Files

- `server/services/container_service.py`
- `server/services/inventory_mutation_guard.py`
- `server/tests/unit/api/test_container_helpers_loot.py`
- `server/tests/unit/services/test_container_service.py`

## Audit Trail

- EXTRACTED: 203 (73%)
- INFERRED: 74 (27%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*