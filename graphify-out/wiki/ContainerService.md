# ContainerService

> 85 nodes

## Key Concepts

- **ContainerService** (90 connections) — `server/services/container_service.py`
- **test_container_service.py** (73 connections) — `server/tests/unit/services/test_container_service.py`
- **asyncio** (27 connections)
- **_container_data()** (25 connections) — `server/tests/unit/services/test_container_service.py`
- **_stack()** (21 connections) — `server/tests/unit/services/test_container_service.py`
- **MutationDecision** (17 connections) — `server/services/inventory_mutation_guard.py`
- **_container()** (15 connections) — `server/tests/unit/services/test_container_service.py`
- **_open_from_fixture()** (11 connections) — `server/tests/unit/services/test_container_service.py`
- **_allow_all_mutations()** (8 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_from_container_capacity_exceeded()** (8 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_from_container_item_not_found()** (7 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_from_container_mutation_guard_suppressed()** (7 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_from_container_reraises_unexpected_error()** (7 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_from_container_success()** (7 connections) — `server/tests/unit/services/test_container_service.py`
- **TestExecuteTransfer** (6 connections) — `server/tests/unit/api/test_container_helpers.py`
- **.test_execute_transfer_to_container()** (6 connections) — `server/tests/unit/api/test_container_helpers.py`
- **.test_execute_transfer_to_player()** (6 connections) — `server/tests/unit/api/test_container_helpers.py`
- **test_loot_all_stops_on_capacity_error()** (6 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_to_container_mutation_guard_suppressed()** (6 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_to_container_player_not_found()** (6 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_to_container_success()** (6 connections) — `server/tests/unit/services/test_container_service.py`
- **TestGetPlayerIdFromUser** (5 connections) — `server/tests/unit/api/test_container_helpers.py`
- **test_lock_container_updates_state()** (5 connections) — `server/tests/unit/services/test_container_service.py`
- **test_loot_all_continues_past_other_errors()** (5 connections) — `server/tests/unit/services/test_container_service.py`
- **test_loot_all_player_not_found()** (5 connections) — `server/tests/unit/services/test_container_service.py`
- *... and 60 more nodes in this community*

## Relationships

- [ContainerServiceError](ContainerServiceError.md) (19 shared connections)
- [ContainerComponent](ContainerComponent.md) (17 shared connections)
- [LootAllRequest](LootAllRequest.md) (13 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (12 shared connections)
- [InventoryMutationGuard](InventoryMutationGuard.md) (4 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [test_inventory_mutation_guard.py](test_inventory_mutation_guard.py.md) (3 shared connections)
- [TransferContainerRequest](TransferContainerRequest.md) (3 shared connections)
- [ValidationError](ValidationError.md) (3 shared connections)
- [HolidayService](HolidayService.md) (2 shared connections)
- [api/conftest.py](api-conftest.py.md) (2 shared connections)
- [test_containers.py](test_containers.py.md) (2 shared connections)

## Source Files

- `server/services/container_service.py`
- `server/services/inventory_mutation_guard.py`
- `server/tests/unit/api/test_container_helpers.py`
- `server/tests/unit/services/test_container_service.py`

## Audit Trail

- EXTRACTED: 232 (72%)
- INFERRED: 89 (28%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*