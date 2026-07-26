# InventoryMutationGuard

> 171 nodes · cohesion 0.02

## Key Concepts

- **InventoryMutationGuard** (42 connections) — `server/services/inventory_mutation_guard.py`
- **InventoryStack** (34 connections) — `server/services/inventory_service.py`
- **inventory_mutation_guard.py** (20 connections) — `server/services/inventory_mutation_guard.py`
- **MutationDecision** (18 connections) — `server/services/inventory_mutation_guard.py`
- **test_inventory_mutation_guard.py** (17 connections) — `server/tests/unit/services/test_inventory_mutation_guard.py`
- **test_inventory_mutation_guard_internal.py** (15 connections) — `server/tests/unit/services/test_inventory_mutation_guard_internal.py`
- **InventorySplitError** (13 connections) — `server/services/inventory_service.py`
- **InventoryValidationError** (13 connections) — `server/services/inventory_service.py`
- **.acquire_async()** (11 connections) — `server/services/inventory_mutation_guard.py`
- **.acquire()** (10 connections) — `server/services/inventory_mutation_guard.py`
- **test_inventory_mutation_guard_error_handling.py** (10 connections) — `server/tests/unit/services/test_inventory_mutation_guard_error_handling.py`
- **test_inventory_mutation_guard_sync.py** (10 connections) — `server/tests/unit/services/test_inventory_mutation_guard_sync.py`
- **Lock** (9 connections)
- **._clone_stack()** (9 connections) — `server/services/inventory_service.py`
- **InventoryServiceError** (9 connections) — `server/services/inventory_service.py`
- **test_inventory_mutation_guard_async.py** (9 connections) — `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- **.add_stack()** (8 connections) — `server/services/inventory_service.py`
- **.split_stack()** (8 connections) — `server/services/inventory_service.py`
- **._clone_with_quantity()** (7 connections) — `server/services/inventory_service.py`
- **._validate_and_clone_optional_fields()** (7 connections) — `server/services/inventory_service.py`
- **Any** (7 connections)
- **_AsyncPlayerGuardState** (6 connections) — `server/services/inventory_mutation_guard.py`
- **InnerContainer** (6 connections) — `server/services/inventory_service.py`
- **InventoryStackRequired** (6 connections) — `server/services/inventory_service.py`
- **.get_lock()** (5 connections) — `server/services/inventory_mutation_guard.py`
- *... and 146 more nodes in this community*

## Relationships

- [__init__.py](__init__.py.md) (49 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (14 shared connections)
- [get_logger](get_logger.md) (7 shared connections)
- [lifespan.py](lifespan.py.md) (6 shared connections)
- [ContainerService](ContainerService.md) (3 shared connections)
- [NPCThreadManager](NPCThreadManager.md) (2 shared connections)
- [container_helpers_inventory_display.py](container_helpers_inventory_display.py.md) (2 shared connections)
- [ContainerComponent](ContainerComponent.md) (2 shared connections)
- [inventory_command_helpers.py](inventory_command_helpers.py.md) (2 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)
- [MetricsCollector](MetricsCollector.md) (1 shared connections)
- [.__init__](__init__.md) (1 shared connections)

## Source Files

- `server/services/inventory_mutation_guard.py`
- `server/services/inventory_service.py`
- `server/tests/unit/services/test_inventory_mutation_guard.py`
- `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- `server/tests/unit/services/test_inventory_mutation_guard_error_handling.py`
- `server/tests/unit/services/test_inventory_mutation_guard_internal.py`
- `server/tests/unit/services/test_inventory_mutation_guard_sync.py`
- `server/tests/unit/services/test_inventory_service.py`

## Audit Trail

- EXTRACTED: 491 (87%)
- INFERRED: 71 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*