# Chat Rate Limiter

> 20 nodes

## Key Concepts

- **.create_unequip_command()** (14 connections) — `server/utils/command_factories_inventory.py`
- **test_create_unequip_command_no_args()** (4 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_unequip_command_empty()** (4 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_unequip_command_whitespace()** (4 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_unequip_command()** (3 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_unequip_command_known_slot()** (3 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_unequip_command_unknown_slot()** (3 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_unequip_command_multi_word()** (3 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_unequip_command_all_slots()** (3 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_unequip_command_with_slot()** (3 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **Test create_unequip_command() creates UnequipCommand.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **Test create_unequip_command() raises error with no args.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **Test create_unequip_command() raises error with empty args.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **Test create_unequip_command() raises error with whitespace only.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **Test create_unequip_command() handles known slot.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **Test create_unequip_command() handles unknown slot as search term.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **Test create_unequip_command() handles multi-word search term.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **Test create_unequip_command() handles all known slots.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **Test create_unequip_command() with slot.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **Create unequip command.** (1 connections) — `server/utils/command_factories_inventory.py`

## Relationships

- [Base Command Models](Base_Command_Models.md) (9 shared connections)
- [Room Service Tests](Room_Service_Tests.md) (3 shared connections)
- [Test Refactoring Status](Test_Refactoring_Status.md) (2 shared connections)
- [WebSocket Request Context](WebSocket_Request_Context.md) (1 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_command_factories_inventory.py`
- `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- `server/utils/command_factories_inventory.py`

## Audit Trail

- EXTRACTED: 51 (94%)
- INFERRED: 3 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*