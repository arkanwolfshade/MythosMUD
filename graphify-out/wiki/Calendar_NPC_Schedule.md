# Calendar NPC Schedule

> 13 nodes

## Key Concepts

- **.create_drop_command()** (9 connections) — `server/utils/command_factories_inventory.py`
- **test_create_drop_command_no_args()** (4 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_drop_command_invalid_index()** (4 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_drop_command_invalid_quantity()** (4 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_drop_command_invalid_index()** (4 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **test_create_drop_command()** (3 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_drop_command_with_quantity()** (3 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **Test create_drop_command() creates DropCommand.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **Test create_drop_command() raises error with no args.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **Test create_drop_command() raises error when index is not integer.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **Test create_drop_command() raises error when quantity is not integer.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **Test create_drop_command() with quantity.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **Test create_drop_command() raises error for invalid index.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`

## Relationships

- [Base Command Models](Base_Command_Models.md) (5 shared connections)
- [Room Service Tests](Room_Service_Tests.md) (4 shared connections)
- [Test Refactoring Status](Test_Refactoring_Status.md) (2 shared connections)
- [Cursor Skills Critique](Cursor_Skills_Critique.md) (1 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_command_factories_inventory.py`
- `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- `server/utils/command_factories_inventory.py`

## Audit Trail

- EXTRACTED: 33 (89%)
- INFERRED: 4 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*