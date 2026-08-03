# container helpers endpoints

> 201 nodes

## Key Concepts

- **__init__.py** (47 connections) — `server/services/__init__.py`
- **InventoryMutationGuard** (42 connections) — `server/services/inventory_mutation_guard.py`
- **InventoryStack** (34 connections) — `server/services/inventory_service.py`
- **inventory_service.py** (29 connections) — `server/services/inventory_service.py`
- **InventoryCapacityError** (29 connections) — `server/services/inventory_service.py`
- **inventory_mutation_guard.py** (20 connections) — `server/services/inventory_mutation_guard.py`
- **test_inventory_service.py** (20 connections) — `server/tests/unit/services/test_inventory_service.py`
- **MutationDecision** (18 connections) — `server/services/inventory_mutation_guard.py`
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
- *... and 176 more nodes in this community*

## Relationships

- [commands inventory command](commands_inventory_command.md) (45 shared connections)
- [Exception Containers](Exception_Containers.md) (26 shared connections)
- [commands admin mute](commands_admin_mute.md) (5 shared connections)
- [inventory commands command](inventory_commands_command.md) (5 shared connections)
- [alias storage commands](alias_storage_commands.md) (4 shared connections)
- [command inventory factories](command_inventory_factories.md) (4 shared connections)
- [time service rationale](time_service_rationale.md) (4 shared connections)
- [Loot Generation](Loot_Generation.md) (4 shared connections)
- [Error Conversion](Error_Conversion.md) (3 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (3 shared connections)
- [System Metrics](System_Metrics.md) (3 shared connections)
- [npc shopkeeper rationale](npc_shopkeeper_rationale.md) (3 shared connections)

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

- EXTRACTED: 640 (88%)
- INFERRED: 91 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*