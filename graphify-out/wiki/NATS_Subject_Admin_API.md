# NATS Subject Admin API

> 20 nodes

## Key Concepts

- **.create_put_command()** (14 connections) — `server/utils/command_factories_inventory.py`
- **test_create_put_command_no_args()** (4 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_put_command_only_item()** (4 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_put_command_quantity_zero()** (4 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_put_command_quantity_negative()** (4 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_put_command_with_in_keyword()** (3 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_put_command_multi_word_container()** (3 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_put_command_multi_word_container_no_quantity()** (3 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_put_command()** (3 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **test_create_put_command_with_in()** (3 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **Test create_put_command() raises error with no args.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **Test create_put_command() raises error with only item.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **Test create_put_command() handles 'in' keyword.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **Test create_put_command() raises error when quantity is zero.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **Test create_put_command() raises error when quantity is negative.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **Test create_put_command() handles multi-word container.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **Test create_put_command() handles multi-word container without quantity.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **Test create_put_command() creates PutCommand.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **Test create_put_command() handles optional 'in' keyword.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **Create put command.          Supports: put <item> [in] <container> [quantity]** (1 connections) — `server/utils/command_factories_inventory.py`

## Relationships

- [Base Command Models](Base_Command_Models.md) (8 shared connections)
- [Room Service Tests](Room_Service_Tests.md) (4 shared connections)
- [Test Refactoring Status](Test_Refactoring_Status.md) (3 shared connections)
- [Admin Summon Command](Admin_Summon_Command.md) (1 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_command_factories_inventory.py`
- `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- `server/utils/command_factories_inventory.py`

## Audit Trail

- EXTRACTED: 51 (93%)
- INFERRED: 4 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*