# inventory_pickup_command.py

> 75 nodes

## Key Concepts

- **inventory_pickup_command.py** (35 connections) — `server/commands/inventory_pickup_command.py`
- **inventory_get_command.py** (29 connections) — `server/commands/inventory_get_command.py`
- **inventory_commands.py** (28 connections) — `server/commands/inventory_commands.py`
- **inventory_put_command.py** (21 connections) — `server/commands/inventory_put_command.py`
- **resolve_state_and_player()** (19 connections) — `server/commands/inventory_command_helpers.py`
- **handle_pickup_command()** (18 connections) — `server/commands/inventory_pickup_command.py`
- **RoomDropManager** (16 connections) — `server/commands/inventory_command_contracts.py`
- **handle_get_command()** (14 connections) — `server/commands/inventory_get_command.py`
- **_pickup_commit_inventory_after_floor_extract()** (13 connections) — `server/commands/inventory_pickup_command.py`
- **handle_put_command()** (13 connections) — `server/commands/inventory_put_command.py`
- **_get_from_container_path()** (12 connections) — `server/commands/inventory_get_command.py`
- **_handle_get_from_room()** (11 connections) — `server/commands/inventory_get_command.py`
- **FloorPickupAfterExtract** (10 connections) — `server/commands/inventory_pickup_command.py`
- **GetCommandRuntime** (9 connections) — `server/commands/inventory_get_command.py`
- **GetItemSpec** (9 connections) — `server/commands/inventory_get_command.py`
- **FloorPickupEnvironment** (9 connections) — `server/commands/inventory_pickup_command.py`
- **FloorPickupPayload** (9 connections) — `server/commands/inventory_pickup_command.py`
- **complete_pickup_after_floor_extract()** (9 connections) — `server/commands/inventory_pickup_command.py`
- **_put_resolve_container_id()** (9 connections) — `server/commands/inventory_put_command.py`
- **inventory_command_contracts.py** (9 connections) — `server/commands/inventory_command_contracts.py`
- **resolve_pickup_item_index()** (8 connections) — `server/commands/inventory_command_helpers.py`
- **_pickup_resolve_floor_stack_or_error()** (8 connections) — `server/commands/inventory_pickup_command.py`
- **_put_transfer_finish()** (8 connections) — `server/commands/inventory_put_command.py`
- **_get_route_after_validation()** (7 connections) — `server/commands/inventory_get_command.py`
- **_get_transfer_out_of_container()** (7 connections) — `server/commands/inventory_get_command.py`
- *... and 50 more nodes in this community*

## Relationships

- [inventory_command_helpers.py](inventory_command_helpers.py.md) (24 shared connections)
- [AliasStorage](AliasStorage.md) (13 shared connections)
- [test_inventory_commands.py](test_inventory_commands.py.md) (13 shared connections)
- [inventory_drop_command.py](inventory_drop_command.py.md) (12 shared connections)
- [get_logger](get_logger.md) (12 shared connections)
- [server/services/__init__.py](server-services-__init__.py.md) (8 shared connections)
- [test_container_helpers_inventory_ops.py](test_container_helpers_inventory_ops.py.md) (8 shared connections)
- [test_container_helpers_inventory_find.py](test_container_helpers_inventory_find.py.md) (7 shared connections)
- [inventory_equip_command.py](inventory_equip_command.py.md) (6 shared connections)
- [Player](Player.md) (6 shared connections)
- [coerce_int](coerce_int.md) (4 shared connections)
- [format_metadata](format_metadata.md) (2 shared connections)

## Source Files

- `server/commands/inventory_command_coercion.py`
- `server/commands/inventory_command_contracts.py`
- `server/commands/inventory_command_helpers.py`
- `server/commands/inventory_commands.py`
- `server/commands/inventory_get_command.py`
- `server/commands/inventory_pickup_command.py`
- `server/commands/inventory_put_command.py`

## Audit Trail

- EXTRACTED: 394 (89%)
- INFERRED: 51 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*