# Lock

> 163 nodes

## Key Concepts

- **InventoryService** (43 connections) — `server/services/inventory_service.py`
- **InventoryMutationGuard** (42 connections) — `server/services/inventory_mutation_guard.py`
- **InventoryStack** (34 connections) — `server/services/inventory_service.py`
- **inventory_service.py** (29 connections) — `server/services/inventory_service.py`
- **inventory_mutation_guard.py** (20 connections) — `server/services/inventory_mutation_guard.py`
- **test_inventory_service.py** (20 connections) — `server/tests/unit/services/test_inventory_service.py`
- **MutationDecision** (18 connections) — `server/services/inventory_mutation_guard.py`
- **test_inventory_mutation_guard.py** (17 connections) — `server/tests/unit/services/test_inventory_mutation_guard.py`
- **InventoryValidationError** (13 connections) — `server/services/inventory_service.py`
- **InventorySplitError** (13 connections) — `server/services/inventory_service.py`
- **.acquire_async()** (11 connections) — `server/services/inventory_mutation_guard.py`
- **.acquire()** (10 connections) — `server/services/inventory_mutation_guard.py`
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
- **_AsyncPlayerGuardState** (6 connections) — `server/services/inventory_mutation_guard.py`
- **InventoryStackRequired** (6 connections) — `server/services/inventory_service.py`
- **InnerContainer** (6 connections) — `server/services/inventory_service.py`
- *... and 138 more nodes in this community*

## Relationships

- [test resolve state no app()](test_resolve_state_no_app%28%29.md) (43 shared connections)
- [AbstractContextManager](AbstractContextManager.md) (20 shared connections)
- [Any](Any.md) (8 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (7 shared connections)
- [.shutdown()](shutdown%28%29.md) (4 shared connections)
- [handle pickup command()](handle_pickup_command%28%29.md) (4 shared connections)
- [Test prepare command for processing](Test_prepare_command_for_processing.md) (3 shared connections)
- [test admin commands](test_admin_commands.md) (3 shared connections)
- [DeadLetterMessage](DeadLetterMessage.md) (3 shared connections)
- [BaseCommand](BaseCommand.md) (3 shared connections)
- [container helpers inventory display](container_helpers_inventory_display.md) (3 shared connections)
- [. init ()](_init_%28%29.md) (2 shared connections)

## Source Files

- `server/container/main.py`
- `server/npc/threading.py`
- `server/services/inventory_mutation_guard.py`
- `server/services/inventory_service.py`
- `server/tests/unit/services/test_equipment_service.py`
- `server/tests/unit/services/test_inventory_mutation_guard.py`
- `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- `server/tests/unit/services/test_inventory_mutation_guard_sync.py`
- `server/tests/unit/services/test_inventory_service.py`

## Audit Trail

- EXTRACTED: 535 (86%)
- INFERRED: 87 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*