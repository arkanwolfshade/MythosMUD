# Test Inventory Commands

> 93 nodes

## Key Concepts

- **command_result_text()** (41 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **test_inventory_put_command.py** (25 connections) — `server/tests/unit/commands/test_inventory_put_command.py`
- **inventory_put_command.py** (22 connections) — `server/commands/inventory_put_command.py`
- **test_inventory_commands.py** (21 connections) — `server/tests/unit/commands/test_inventory_commands.py`
- **PickupTestWiring** (19 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **test_inventory_commands_pickup.py** (18 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **handle_pickup_command()** (17 connections) — `server/commands/inventory_pickup_command.py`
- **handle_put_command()** (16 connections) — `server/commands/inventory_put_command.py`
- **asyncio** (14 connections)
- **_put_resolve_container_id()** (13 connections) — `server/commands/inventory_put_command.py`
- **_put_transfer_finish()** (13 connections) — `server/commands/inventory_put_command.py`
- **asyncio** (12 connections)
- **_put_run_validated()** (10 connections) — `server/commands/inventory_put_command.py`
- **inventory_commands_test_support.py** (10 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **test_handle_pickup_command()** (8 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **test_handle_pickup_command_inventory_capacity_error()** (8 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **PutCommandRuntime** (7 connections) — `server/commands/inventory_put_command.py`
- **PutValidatedWork** (7 connections) — `server/commands/inventory_put_command.py`
- **test_handle_pickup_command_persist_failure_restores_drop_and_inventory()** (7 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **test_put_run_validated_container_error()** (7 connections) — `server/tests/unit/commands/test_inventory_put_command.py`
- **test_put_run_validated_success()** (7 connections) — `server/tests/unit/commands/test_inventory_put_command.py`
- **asyncio** (7 connections)
- **sample_floor_item_stack()** (6 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **_pickup_with_persist_patch()** (6 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **test_handle_pickup_command_invalid_index()** (6 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- *... and 68 more nodes in this community*

## Relationships

- [Equipment & Inventory Helpers](Equipment_&_Inventory_Helpers.md) (34 shared connections)
- [Inventory Drop Command](Inventory_Drop_Command.md) (17 shared connections)
- [Player Model & Migrations](Player_Model_&_Migrations.md) (15 shared connections)
- [Test Container Helpers Inventory Ops](Test_Container_Helpers_Inventory_Ops.md) (4 shared connections)
- [Test Npc Admin Commands](Test_Npc_Admin_Commands.md) (3 shared connections)
- [Test Position Commands](Test_Position_Commands.md) (3 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (3 shared connections)
- [Test Container Helpers Inventory Find](Test_Container_Helpers_Inventory_Find.md) (2 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (2 shared connections)
- [Alias Storage](Alias_Storage.md) (1 shared connections)

## Source Files

- `server/commands/inventory_pickup_command.py`
- `server/commands/inventory_put_command.py`
- `server/tests/unit/commands/inventory_commands_test_support.py`
- `server/tests/unit/commands/test_inventory_commands.py`
- `server/tests/unit/commands/test_inventory_commands_pickup.py`
- `server/tests/unit/commands/test_inventory_put_command.py`

## Audit Trail

- EXTRACTED: 254 (86%)
- INFERRED: 42 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*