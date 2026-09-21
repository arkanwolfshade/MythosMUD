# ContainerService

> 101 nodes

## Key Concepts

- **ContainerService** (90 connections) — `server/services/container_service.py`
- **test_container_service.py** (72 connections) — `server/tests/unit/services/test_container_service.py`
- **asyncio** (27 connections)
- **_container_data()** (25 connections) — `server/tests/unit/services/test_container_service.py`
- **transfer_all_items_from_container()** (21 connections) — `server/api/container_helpers.py`
- **_stack()** (21 connections) — `server/tests/unit/services/test_container_service.py`
- **MutationDecision** (17 connections) — `server/services/inventory_mutation_guard.py`
- **TestTransferAllItemsFromContainer** (16 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **_container()** (15 connections) — `server/tests/unit/services/test_container_service.py`
- **asyncio** (14 connections)
- **_open_from_fixture()** (11 connections) — `server/tests/unit/services/test_container_service.py`
- **_allow_all_mutations()** (8 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_from_container_capacity_exceeded()** (8 connections) — `server/tests/unit/services/test_container_service.py`
- **.test_transfer_all_items_from_container_capacity_error()** (7 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **test_transfer_from_container_item_not_found()** (7 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_from_container_mutation_guard_suppressed()** (7 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_from_container_reraises_unexpected_error()** (7 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_from_container_success()** (7 connections) — `server/tests/unit/services/test_container_service.py`
- **.test_transfer_all_items_from_container_empty_items()** (6 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_item_without_quantity()** (6 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_multiple_items()** (6 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_partial_success()** (6 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_result_missing_container()** (6 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_result_missing_inventory()** (6 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_success()** (6 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- *... and 76 more nodes in this community*

## Relationships

- [LootAllRequest](LootAllRequest.md) (22 shared connections)
- [ContainerComponent](ContainerComponent.md) (20 shared connections)
- [ContainerServiceError](ContainerServiceError.md) (19 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (14 shared connections)
- [server/services/__init__.py](server-services-__init__.py.md) (7 shared connections)
- [InventoryMutationGuard](InventoryMutationGuard.md) (6 shared connections)
- [ValidationError](ValidationError.md) (3 shared connections)
- [item_catalog_repository.py](item_catalog_repository.py.md) (1 shared connections)
- [bundles/game.py](bundles-game.py.md) (1 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (1 shared connections)

## Source Files

- `server/api/container_helpers.py`
- `server/services/container_service.py`
- `server/services/inventory_mutation_guard.py`
- `server/services/inventory_service.py`
- `server/tests/unit/api/test_container_helpers_loot.py`
- `server/tests/unit/services/test_container_service.py`

## Audit Trail

- EXTRACTED: 279 (75%)
- INFERRED: 92 (25%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*