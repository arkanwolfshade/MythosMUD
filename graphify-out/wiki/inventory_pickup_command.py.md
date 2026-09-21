# inventory_pickup_command.py

> 61 nodes

## Key Concepts

- **inventory_pickup_command.py** (35 connections) — `server/commands/inventory_pickup_command.py`
- **inventory_commands.py** (28 connections) — `server/commands/inventory_commands.py`
- **inventory_drop_command.py** (25 connections) — `server/commands/inventory_drop_command.py`
- **resolve_state_and_player()** (19 connections) — `server/commands/inventory_command_helpers.py`
- **handle_pickup_command()** (17 connections) — `server/commands/inventory_pickup_command.py`
- **RoomDropManager** (16 connections) — `server/commands/inventory_command_contracts.py`
- **handle_drop_command()** (14 connections) — `server/commands/inventory_drop_command.py`
- **_pickup_commit_inventory_after_floor_extract()** (13 connections) — `server/commands/inventory_pickup_command.py`
- **_drop_resolve_stack_or_error()** (12 connections) — `server/commands/inventory_drop_command.py`
- **inventory_command_contracts.py** (11 connections) — `server/commands/inventory_command_contracts.py`
- **complete_pickup_after_floor_extract()** (9 connections) — `server/commands/inventory_pickup_command.py`
- **_pickup_resolve_floor_stack_or_error()** (9 connections) — `server/commands/inventory_pickup_command.py`
- **FloorPickupAfterExtract** (8 connections) — `server/commands/inventory_pickup_command.py`
- **resolve_pickup_item_index()** (8 connections) — `server/commands/inventory_command_helpers.py`
- **FloorPickupEnvironment** (7 connections) — `server/commands/inventory_pickup_command.py`
- **get_room_manager()** (7 connections) — `server/commands/inventory_command_helpers.py`
- **CommandResponse** (7 connections)
- **FloorPickupPayload** (6 connections) — `server/commands/inventory_pickup_command.py`
- **_drop_finish_after_persist()** (6 connections) — `server/commands/inventory_drop_command.py`
- **_drop_parsed_quantity_or_error()** (6 connections) — `server/commands/inventory_drop_command.py`
- **_pickup_broadcast_success()** (6 connections) — `server/commands/inventory_pickup_command.py`
- **CommandResponse** (6 connections)
- **prepare_extracted_stack()** (5 connections) — `server/commands/inventory_command_helpers.py`
- **_drop_quantity_bounds_or_error()** (4 connections) — `server/commands/inventory_drop_command.py`
- **_drop_quantity_or_error()** (4 connections) — `server/commands/inventory_drop_command.py`
- *... and 36 more nodes in this community*

## Relationships

- [inventory_command_helpers.py](inventory_command_helpers.py.md) (29 shared connections)
- [Player](Player.md) (27 shared connections)
- [command_result_text](command_result_text.md) (18 shared connections)
- [get_logger](get_logger.md) (9 shared connections)
- [inventory_equip_command.py](inventory_equip_command.py.md) (5 shared connections)
- [inventory_unequip_command.py](inventory_unequip_command.py.md) (5 shared connections)
- [AliasStorage](AliasStorage.md) (5 shared connections)
- [InventoryService](InventoryService.md) (3 shared connections)
- [command_service.py](command_service.py.md) (2 shared connections)
- [test_inventory_display_helpers.py](test_inventory_display_helpers.py.md) (2 shared connections)
- [models/player.py](models-player.py.md) (2 shared connections)
- [test_inventory_helpers.py](test_inventory_helpers.py.md) (1 shared connections)

## Source Files

- `server/commands/inventory_command_contracts.py`
- `server/commands/inventory_command_helpers.py`
- `server/commands/inventory_commands.py`
- `server/commands/inventory_drop_command.py`
- `server/commands/inventory_pickup_command.py`

## Audit Trail

- EXTRACTED: 207 (90%)
- INFERRED: 22 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*