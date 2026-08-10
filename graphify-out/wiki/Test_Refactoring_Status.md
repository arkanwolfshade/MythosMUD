# Test Refactoring Status

> 24 nodes

## Key Concepts

- **test_command_factories_inventory_helpers.py** (22 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **.create_inventory_command()** (6 connections) — `server/utils/command_factories_inventory.py`
- **test_create_inventory_command_with_args()** (4 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **test_create_pickup_command_invalid_quantity()** (4 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **test_create_pickup_command_invalid_index()** (4 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **test_create_inventory_command()** (3 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **test_create_pickup_command_with_index()** (3 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **test_create_pickup_command_with_quantity()** (3 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **test_create_put_command_with_quantity()** (3 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **test_create_equip_command_with_slot()** (3 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **test_create_equip_command_with_name_and_slot()** (3 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **test_create_unequip_command_with_name()** (3 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **Unit tests for inventory command factory helper functions.  Tests the helper fun** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **Test create_inventory_command() creates InventoryCommand.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **Test create_inventory_command() raises error with args.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **Test create_pickup_command() with numeric index.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **Test create_pickup_command() with quantity.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **Test create_pickup_command() raises error for invalid quantity.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **Test create_pickup_command() raises error for invalid index.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **Test create_put_command() with quantity.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **Test create_equip_command() with slot.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **Test create_equip_command() with item name and inferred slot.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **Test create_unequip_command() with item name.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **Create InventoryCommand from arguments.** (1 connections) — `server/utils/command_factories_inventory.py`

## Relationships

- [Base Command Models](Base_Command_Models.md) (8 shared connections)
- [Room Service Tests](Room_Service_Tests.md) (4 shared connections)
- [NATS Subject Admin API](NATS_Subject_Admin_API.md) (3 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (2 shared connections)
- [Calendar NPC Schedule](Calendar_NPC_Schedule.md) (2 shared connections)
- [Architecture Review Plan](Architecture_Review_Plan.md) (2 shared connections)
- [Chat Rate Limiter](Chat_Rate_Limiter.md) (2 shared connections)
- [Admin Summon Command](Admin_Summon_Command.md) (1 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- `server/utils/command_factories_inventory.py`

## Audit Trail

- EXTRACTED: 70 (96%)
- INFERRED: 3 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*