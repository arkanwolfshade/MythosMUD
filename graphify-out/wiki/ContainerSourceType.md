# ContainerSourceType

> 62 nodes

## Key Concepts

- **ContainerSourceType** (89 connections) — `server/models/container.py`
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
- *... and 37 more nodes in this community*

## Relationships

- [ContainerComponent](ContainerComponent.md) (33 shared connections)
- [pytest.md](pytest.md.md) (21 shared connections)
- [get_logger](get_logger.md) (16 shared connections)
- [ContainerLockState](ContainerLockState.md) (16 shared connections)
- [test_corpse_lifecycle_service.py](test_corpse_lifecycle_service.py.md) (11 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (11 shared connections)
- [container_events.py](container_events.py.md) (5 shared connections)
- [InventoryService](InventoryService.md) (5 shared connections)
- [inventory_command_helpers.py](inventory_command_helpers.py.md) (4 shared connections)
- [InventoryMutationGuard](InventoryMutationGuard.md) (3 shared connections)
- [test_inventory_mutation_guard.py](test_inventory_mutation_guard.py.md) (3 shared connections)
- [test_wearable_container_service.py](test_wearable_container_service.py.md) (2 shared connections)

## Source Files

- `server/models/container.py`
- `server/services/container_service.py`
- `server/services/inventory_mutation_guard.py`
- `server/tests/unit/services/test_container_service.py`

## Audit Trail

- EXTRACTED: 169 (55%)
- INFERRED: 140 (45%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*