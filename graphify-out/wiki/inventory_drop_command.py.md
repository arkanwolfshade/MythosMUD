# inventory_drop_command.py

> 21 nodes · cohesion 0.16

## Key Concepts

- **inventory_drop_command.py** (25 connections) — `server/commands/inventory_drop_command.py`
- **handle_drop_command()** (15 connections) — `server/commands/inventory_drop_command.py`
- **_drop_resolve_stack_or_error()** (12 connections) — `server/commands/inventory_drop_command.py`
- **get_room_manager()** (7 connections) — `server/commands/inventory_command_helpers.py`
- **CommandResponse** (7 connections)
- **_drop_finish_after_persist()** (6 connections) — `server/commands/inventory_drop_command.py`
- **_drop_parsed_quantity_or_error()** (6 connections) — `server/commands/inventory_drop_command.py`
- **_drop_quantity_bounds_or_error()** (4 connections) — `server/commands/inventory_drop_command.py`
- **_drop_quantity_or_error()** (4 connections) — `server/commands/inventory_drop_command.py`
- **_drop_slot_index_or_error()** (4 connections) — `server/commands/inventory_drop_command.py`
- **_inventory_rows_after_drop()** (4 connections) — `server/commands/inventory_drop_command.py`
- **Player** (3 connections)
- **test_handle_drop_command()** (3 connections) — `server/tests/unit/commands/test_inventory_commands.py`
- **_DropResolved** (1 connections)
- **Drop command: move an inventory stack to the room floor.** (1 connections) — `server/commands/inventory_drop_command.py`
- **Drop an inventory stack into the current room.** (1 connections) — `server/commands/inventory_drop_command.py`
- **Apply partial or full removal of one inventory slot (1-based index).** (1 connections) — `server/commands/inventory_drop_command.py`
- **Resolve 1-based inventory slot from command data or return a usage / range error** (1 connections) — `server/commands/inventory_drop_command.py`
- **Return an error response if drop quantity is out of range for the stack.** (1 connections) — `server/commands/inventory_drop_command.py`
- **Parse quantity from command + stack; return error dict or a validated int (may s** (1 connections) — `server/commands/inventory_drop_command.py`
- **Test handle_drop_command() drops item.** (1 connections) — `server/tests/unit/commands/test_inventory_commands.py`

## Relationships

- [inventory_command_helpers.py](inventory_command_helpers.py.md) (11 shared connections)
- [inventory_pickup_command.py](inventory_pickup_command.py.md) (6 shared connections)
- [AliasStorage](AliasStorage.md) (6 shared connections)
- [coerce_int](coerce_int.md) (5 shared connections)
- [test_inventory_commands.py](test_inventory_commands.py.md) (3 shared connections)
- [Player](Player.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)

## Source Files

- `server/commands/inventory_command_helpers.py`
- `server/commands/inventory_drop_command.py`
- `server/tests/unit/commands/test_inventory_commands.py`

## Audit Trail

- EXTRACTED: 98 (91%)
- INFERRED: 10 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*