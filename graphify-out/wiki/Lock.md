# Lock

> 151 nodes

## Key Concepts

- **__init__.py** (47 connections) — `server/services/__init__.py`
- **InventoryService** (43 connections) — `server/services/inventory_service.py`
- **InventoryMutationGuard** (42 connections) — `server/services/inventory_mutation_guard.py`
- **InventoryStack** (34 connections) — `server/services/inventory_service.py`
- **inventory_service.py** (29 connections) — `server/services/inventory_service.py`
- **InventoryCapacityError** (29 connections) — `server/services/inventory_service.py`
- **inventory_mutation_guard.py** (20 connections) — `server/services/inventory_mutation_guard.py`
- **test_inventory_service.py** (20 connections) — `server/tests/unit/services/test_inventory_service.py`
- **MutationDecision** (18 connections) — `server/services/inventory_mutation_guard.py`
- **test_inventory_mutation_guard.py** (17 connections) — `server/tests/unit/services/test_inventory_mutation_guard.py`
- **InventoryValidationError** (13 connections) — `server/services/inventory_service.py`
- **InventorySplitError** (13 connections) — `server/services/inventory_service.py`
- **.acquire_async()** (11 connections) — `server/services/inventory_mutation_guard.py`
- **.acquire()** (10 connections) — `server/services/inventory_mutation_guard.py`
- **Lock** (9 connections)
- **InventoryServiceError** (9 connections) — `server/services/inventory_service.py`
- **._clone_stack()** (9 connections) — `server/services/inventory_service.py`
- **test_inventory_mutation_guard_async.py** (9 connections) — `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- **.add_stack()** (8 connections) — `server/services/inventory_service.py`
- **.split_stack()** (8 connections) — `server/services/inventory_service.py`
- **Any** (7 connections)
- **._validate_and_clone_optional_fields()** (7 connections) — `server/services/inventory_service.py`
- **._clone_with_quantity()** (7 connections) — `server/services/inventory_service.py`
- **_AsyncPlayerGuardState** (6 connections) — `server/services/inventory_mutation_guard.py`
- **InventoryStackRequired** (6 connections) — `server/services/inventory_service.py`
- *... and 126 more nodes in this community*

## Relationships

- [AbstractContextManager](AbstractContextManager.md) (32 shared connections)
- [.validate message()](validate_message%28%29.md) (24 shared connections)
- [test resolve state no app()](test_resolve_state_no_app%28%29.md) (20 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (11 shared connections)
- [Any](Any.md) (10 shared connections)
- [DeadLetterMessage](DeadLetterMessage.md) (5 shared connections)
- [UUID](UUID.md) (4 shared connections)
- [.shutdown()](shutdown%28%29.md) (4 shared connections)
- [handle pickup command()](handle_pickup_command%28%29.md) (4 shared connections)
- [Test prepare command for processing](Test_prepare_command_for_processing.md) (3 shared connections)
- [test admin commands](test_admin_commands.md) (3 shared connections)
- [test room subscription manager npcs](test_room_subscription_manager_npcs.md) (3 shared connections)

## Source Files

- `server/container/main.py`
- `server/npc/threading.py`
- `server/services/__init__.py`
- `server/services/inventory_mutation_guard.py`
- `server/services/inventory_service.py`
- `server/tests/unit/services/test_inventory_mutation_guard.py`
- `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- `server/tests/unit/services/test_inventory_service.py`

## Audit Trail

- EXTRACTED: 562 (84%)
- INFERRED: 104 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*