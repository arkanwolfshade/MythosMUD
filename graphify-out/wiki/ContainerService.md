# ContainerService

> 59 nodes

## Key Concepts

- **ContainerService** (79 connections) — `server/services/container_service.py`
- **test_container_service.py** (61 connections) — `server/tests/unit/services/test_container_service.py`
- **asyncio** (18 connections)
- **_container()** (16 connections) — `server/tests/unit/services/test_container_service.py`
- **_container_data()** (16 connections) — `server/tests/unit/services/test_container_service.py`
- **MutationDecision** (15 connections) — `server/services/inventory_mutation_guard.py`
- **_stack()** (12 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_to_container_mutation_guard_suppressed()** (6 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_to_container_player_not_found()** (6 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_to_container_success()** (6 connections) — `server/tests/unit/services/test_container_service.py`
- **test_lock_container_updates_state()** (5 connections) — `server/tests/unit/services/test_container_service.py`
- **test_open_container_player_not_found()** (5 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_to_container_capacity_exceeded()** (5 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_to_container_non_dict_container_data()** (5 connections) — `server/tests/unit/services/test_container_service.py`
- **test_can_unlock_container_admin()** (4 connections) — `server/tests/unit/services/test_container_service.py`
- **test_can_unlock_container_locked_without_key()** (4 connections) — `server/tests/unit/services/test_container_service.py`
- **test_can_unlock_container_with_key()** (4 connections) — `server/tests/unit/services/test_container_service.py`
- **test_close_container_logs_audit_when_data_available()** (4 connections) — `server/tests/unit/services/test_container_service.py`
- **test_open_container_already_open()** (4 connections) — `server/tests/unit/services/test_container_service.py`
- **test_open_container_audit_failure_still_succeeds()** (4 connections) — `server/tests/unit/services/test_container_service.py`
- **test_open_container_locked_without_key()** (4 connections) — `server/tests/unit/services/test_container_service.py`
- **test_open_container_sealed_non_admin()** (4 connections) — `server/tests/unit/services/test_container_service.py`
- **test_open_container_success()** (4 connections) — `server/tests/unit/services/test_container_service.py`
- **test_remove_item_from_container_partial_quantity()** (4 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_to_container_not_found()** (4 connections) — `server/tests/unit/services/test_container_service.py`
- *... and 34 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (20 shared connections)
- [ContainerComponent](ContainerComponent.md) (17 shared connections)
- [LootAllRequest](LootAllRequest.md) (12 shared connections)
- [TransferContainerRequest](TransferContainerRequest.md) (3 shared connections)
- [InventoryMutationGuard](InventoryMutationGuard.md) (3 shared connections)
- [test_inventory_mutation_guard.py](test_inventory_mutation_guard.py.md) (3 shared connections)
- [ValidationError](ValidationError.md) (3 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (2 shared connections)
- [InventoryService](InventoryService.md) (2 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (1 shared connections)
- [bundles/game.py](bundles-game.py.md) (1 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (1 shared connections)

## Source Files

- `server/services/container_service.py`
- `server/services/inventory_mutation_guard.py`
- `server/tests/unit/services/test_container_service.py`

## Audit Trail

- EXTRACTED: 151 (66%)
- INFERRED: 77 (34%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*