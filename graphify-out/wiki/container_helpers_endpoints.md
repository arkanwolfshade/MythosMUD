# container helpers endpoints

> 197 nodes

## Key Concepts

- **__init__.py** (47 connections) — `server/services/__init__.py`
- **InventoryService** (43 connections) — `server/services/inventory_service.py`
- **InventoryMutationGuard** (42 connections) — `server/services/inventory_mutation_guard.py`
- **InventoryStack** (34 connections) — `server/services/inventory_service.py`
- **inventory_service.py** (29 connections) — `server/services/inventory_service.py`
- **inventory_mutation_guard.py** (20 connections) — `server/services/inventory_mutation_guard.py`
- **test_inventory_service.py** (20 connections) — `server/tests/unit/services/test_inventory_service.py`
- **MutationDecision** (19 connections) — `server/services/inventory_mutation_guard.py`
- **test_inventory_mutation_guard.py** (17 connections) — `server/tests/unit/services/test_inventory_mutation_guard.py`
- **test_inventory_mutation_guard_internal.py** (15 connections) — `server/tests/unit/services/test_inventory_mutation_guard_internal.py`
- **InventoryValidationError** (13 connections) — `server/services/inventory_service.py`
- **InventorySplitError** (13 connections) — `server/services/inventory_service.py`
- **.acquire_async()** (11 connections) — `server/services/inventory_mutation_guard.py`
- **.acquire()** (10 connections) — `server/services/inventory_mutation_guard.py`
- **test_inventory_mutation_guard_error_handling.py** (10 connections) — `server/tests/unit/services/test_inventory_mutation_guard_error_handling.py`
- **test_inventory_mutation_guard_sync.py** (10 connections) — `server/tests/unit/services/test_inventory_mutation_guard_sync.py`
- **Lock** (9 connections)
- **InventoryServiceError** (9 connections) — `server/services/inventory_service.py`
- **._clone_stack()** (9 connections) — `server/services/inventory_service.py`
- **test_inventory_mutation_guard_async.py** (9 connections) — `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- **.add_stack()** (8 connections) — `server/services/inventory_service.py`
- **.split_stack()** (8 connections) — `server/services/inventory_service.py`
- **Any** (7 connections)
- **._validate_and_clone_optional_fields()** (7 connections) — `server/services/inventory_service.py`
- **._clone_with_quantity()** (7 connections) — `server/services/inventory_service.py`
- *... and 172 more nodes in this community*

## Relationships

- [retry nats handler](retry_nats_handler.md) (39 shared connections)
- [Exception Containers](Exception_Containers.md) (35 shared connections)
- [models npc rationale](models_npc_rationale.md) (9 shared connections)
- [inventory commands command](inventory_commands_command.md) (8 shared connections)
- [combat services persistence](combat_services_persistence.md) (6 shared connections)
- [commands inventory command](commands_inventory_command.md) (5 shared connections)
- [commands inventory pickup](commands_inventory_pickup.md) (4 shared connections)
- [holiday service services](holiday_service_services.md) (3 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (3 shared connections)
- [room cache services](room_cache_services.md) (3 shared connections)
- [System Metrics](System_Metrics.md) (3 shared connections)
- [container inventory display](container_inventory_display.md) (3 shared connections)

## Source Files

- `server/container/main.py`
- `server/services/__init__.py`
- `server/services/inventory_mutation_guard.py`
- `server/services/inventory_service.py`
- `server/tests/unit/services/test_inventory_mutation_guard.py`
- `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- `server/tests/unit/services/test_inventory_mutation_guard_error_handling.py`
- `server/tests/unit/services/test_inventory_mutation_guard_internal.py`
- `server/tests/unit/services/test_inventory_mutation_guard_sync.py`
- `server/tests/unit/services/test_inventory_service.py`

## Audit Trail

- EXTRACTED: 654 (89%)
- INFERRED: 84 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*