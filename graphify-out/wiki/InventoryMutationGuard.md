# InventoryMutationGuard

> 166 nodes

## Key Concepts

- **InventoryMutationGuard** (40 connections) — `server/services/inventory_mutation_guard.py`
- **InventoryStack** (34 connections) — `server/services/inventory_service.py`
- **inventory_mutation_guard.py** (21 connections) — `server/services/inventory_mutation_guard.py`
- **MutationDecision** (19 connections) — `server/services/inventory_mutation_guard.py`
- **test_inventory_mutation_guard.py** (17 connections) — `server/tests/unit/services/test_inventory_mutation_guard.py`
- **test_inventory_mutation_guard_internal.py** (15 connections) — `server/tests/unit/services/test_inventory_mutation_guard_internal.py`
- **InventoryValidationError** (10 connections) — `server/services/inventory_service.py`
- **test_inventory_mutation_guard_async.py** (10 connections) — `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- **test_inventory_mutation_guard_error_handling.py** (10 connections) — `server/tests/unit/services/test_inventory_mutation_guard_error_handling.py`
- **test_inventory_mutation_guard_sync.py** (10 connections) — `server/tests/unit/services/test_inventory_mutation_guard_sync.py`
- **InventoryServiceError** (9 connections) — `server/services/inventory_service.py`
- **InventorySplitError** (9 connections) — `server/services/inventory_service.py`
- **._clone_stack()** (9 connections) — `server/services/inventory_service.py`
- **.acquire()** (8 connections) — `server/services/inventory_mutation_guard.py`
- **.acquire_async()** (8 connections) — `server/services/inventory_mutation_guard.py`
- **.add_stack()** (8 connections) — `server/services/inventory_service.py`
- **.split_stack()** (8 connections) — `server/services/inventory_service.py`
- **._clone_with_quantity()** (7 connections) — `server/services/inventory_service.py`
- **Any** (7 connections)
- **_AsyncPlayerGuardState** (6 connections) — `server/services/inventory_mutation_guard.py`
- **InventoryStackRequired** (6 connections) — `server/services/inventory_service.py`
- **._validate_and_clone_optional_fields()** (6 connections) — `server/services/inventory_service.py`
- **asyncio** (6 connections)
- **asyncio** (6 connections)
- **_PlayerGuardState** (5 connections) — `server/services/inventory_mutation_guard.py`
- *... and 141 more nodes in this community*

## Relationships

- [server/services/__init__.py](server-services-__init__.py.md) (38 shared connections)
- [ContainerService](ContainerService.md) (17 shared connections)
- [MonitoringDashboard](MonitoringDashboard.md) (4 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [connection_manager.py](connection_manager.py.md) (3 shared connections)
- [MetricsCollector](MetricsCollector.md) (2 shared connections)
- [ContainerTransferToMixin](ContainerTransferToMixin.md) (2 shared connections)
- [inventory_equip_command.py](inventory_equip_command.py.md) (2 shared connections)
- [LootAllRequest](LootAllRequest.md) (1 shared connections)
- [container_helpers_inventory_display.py](container_helpers_inventory_display.py.md) (1 shared connections)
- [ContainerComponent](ContainerComponent.md) (1 shared connections)
- [inventory_command_helpers.py](inventory_command_helpers.py.md) (1 shared connections)

## Source Files

- `server/services/inventory_mutation_guard.py`
- `server/services/inventory_service.py`
- `server/tests/unit/services/test_inventory_mutation_guard.py`
- `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- `server/tests/unit/services/test_inventory_mutation_guard_error_handling.py`
- `server/tests/unit/services/test_inventory_mutation_guard_internal.py`
- `server/tests/unit/services/test_inventory_mutation_guard_sync.py`

## Audit Trail

- EXTRACTED: 289 (91%)
- INFERRED: 30 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*