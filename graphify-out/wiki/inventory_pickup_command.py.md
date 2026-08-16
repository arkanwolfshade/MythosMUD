# inventory_pickup_command.py

> 90 nodes

## Key Concepts

- **inventory_pickup_command.py** (35 connections) — `server/commands/inventory_pickup_command.py`
- **inventory_get_command.py** (30 connections) — `server/commands/inventory_get_command.py`
- **inventory_commands.py** (28 connections) — `server/commands/inventory_commands.py`
- **test_inventory_get_command.py** (26 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **inventory_drop_command.py** (25 connections) — `server/commands/inventory_drop_command.py`
- **resolve_state_and_player()** (19 connections) — `server/commands/inventory_command_helpers.py`
- **RoomDropManager** (16 connections) — `server/commands/inventory_command_contracts.py`
- **handle_get_command()** (16 connections) — `server/commands/inventory_get_command.py`
- **_handle_get_from_room()** (16 connections) — `server/commands/inventory_get_command.py`
- **_get_from_container_path()** (15 connections) — `server/commands/inventory_get_command.py`
- **handle_drop_command()** (14 connections) — `server/commands/inventory_drop_command.py`
- **build_and_broadcast_inventory_event()** (13 connections) — `server/commands/inventory_command_helpers.py`
- **_drop_resolve_stack_or_error()** (12 connections) — `server/commands/inventory_drop_command.py`
- **_get_transfer_out_of_container()** (11 connections) — `server/commands/inventory_get_command.py`
- **inventory_command_contracts.py** (11 connections) — `server/commands/inventory_command_contracts.py`
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
- *... and 65 more nodes in this community*

## Relationships

- [inventory_command_helpers.py](inventory_command_helpers.py.md) (31 shared connections)
- [command_result_text](command_result_text.md) (29 shared connections)
- [Player](Player.md) (16 shared connections)
- [coerce_int](coerce_int.md) (8 shared connections)
- [get_logger](get_logger.md) (8 shared connections)
- [server/services/__init__.py](server-services-__init__.py.md) (7 shared connections)
- [inventory_equip_command.py](inventory_equip_command.py.md) (6 shared connections)
- [AliasStorage](AliasStorage.md) (6 shared connections)
- [test_container_helpers_inventory_ops.py](test_container_helpers_inventory_ops.py.md) (5 shared connections)
- [test_container_helpers_inventory_find.py](test_container_helpers_inventory_find.py.md) (4 shared connections)
- [alias_storage.py](alias_storage.py.md) (4 shared connections)
- [test_inventory_equip_command.py](test_inventory_equip_command.py.md) (2 shared connections)

## Source Files

- `server/commands/inventory_command_coercion.py`
- `server/commands/inventory_command_contracts.py`
- `server/commands/inventory_command_helpers.py`
- `server/commands/inventory_commands.py`
- `server/commands/inventory_drop_command.py`
- `server/commands/inventory_get_command.py`
- `server/commands/inventory_pickup_command.py`
- `server/tests/unit/commands/test_inventory_get_command.py`

## Audit Trail

- EXTRACTED: 294 (87%)
- INFERRED: 43 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*