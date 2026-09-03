# Inventory Drop Command

> 75 nodes

## Key Concepts

- **inventory_get_command.py** (30 connections) — `server/commands/inventory_get_command.py`
- **test_inventory_get_command.py** (26 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **inventory_drop_command.py** (25 connections) — `server/commands/inventory_drop_command.py`
- **RoomDropManager** (16 connections) — `server/commands/inventory_command_contracts.py`
- **handle_get_command()** (16 connections) — `server/commands/inventory_get_command.py`
- **_handle_get_from_room()** (16 connections) — `server/commands/inventory_get_command.py`
- **_get_from_container_path()** (15 connections) — `server/commands/inventory_get_command.py`
- **handle_drop_command()** (14 connections) — `server/commands/inventory_drop_command.py`
- **_drop_resolve_stack_or_error()** (12 connections) — `server/commands/inventory_drop_command.py`
- **_get_transfer_out_of_container()** (11 connections) — `server/commands/inventory_get_command.py`
- **asyncio** (10 connections)
- **complete_pickup_after_floor_extract()** (9 connections) — `server/commands/inventory_pickup_command.py`
- **_pickup_resolve_floor_stack_or_error()** (9 connections) — `server/commands/inventory_pickup_command.py`
- **GetCommandRuntime** (8 connections) — `server/commands/inventory_get_command.py`
- **GetItemSpec** (8 connections) — `server/commands/inventory_get_command.py`
- **FloorPickupAfterExtract** (8 connections) — `server/commands/inventory_pickup_command.py`
- **resolve_pickup_item_index()** (8 connections) — `server/commands/inventory_command_helpers.py`
- **FloorPickupEnvironment** (7 connections) — `server/commands/inventory_pickup_command.py`
- **get_room_manager()** (7 connections) — `server/commands/inventory_command_helpers.py`
- **_get_route_after_validation()** (7 connections) — `server/commands/inventory_get_command.py`
- **CommandResponse** (7 connections)
- **FloorPickupPayload** (6 connections) — `server/commands/inventory_pickup_command.py`
- **_drop_finish_after_persist()** (6 connections) — `server/commands/inventory_drop_command.py`
- **_drop_parsed_quantity_or_error()** (6 connections) — `server/commands/inventory_drop_command.py`
- **test_get_from_container_path_item_not_in_container()** (6 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- *... and 50 more nodes in this community*

## Relationships

- [Equipment & Inventory Helpers](Equipment_&_Inventory_Helpers.md) (41 shared connections)
- [Test Inventory Commands](Test_Inventory_Commands.md) (17 shared connections)
- [Player Model & Migrations](Player_Model_&_Migrations.md) (14 shared connections)
- [Test Inventory Command Coercion](Test_Inventory_Command_Coercion.md) (8 shared connections)
- [Test Container Helpers Inventory Ops](Test_Container_Helpers_Inventory_Ops.md) (6 shared connections)
- [Test Npc Admin Commands](Test_Npc_Admin_Commands.md) (4 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (4 shared connections)
- [Test Container Helpers Inventory Find](Test_Container_Helpers_Inventory_Find.md) (2 shared connections)
- [Alias Storage](Alias_Storage.md) (2 shared connections)
- [Test Inventory Helpers](Test_Inventory_Helpers.md) (1 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)

## Source Files

- `server/commands/inventory_command_coercion.py`
- `server/commands/inventory_command_contracts.py`
- `server/commands/inventory_command_helpers.py`
- `server/commands/inventory_drop_command.py`
- `server/commands/inventory_get_command.py`
- `server/commands/inventory_pickup_command.py`
- `server/tests/unit/commands/test_inventory_get_command.py`

## Audit Trail

- EXTRACTED: 216 (84%)
- INFERRED: 40 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*