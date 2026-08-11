# Rate Limiter Utilities

> 24 nodes

## Key Concepts

- **inventory_drop_command.py** (25 connections) — `server/commands/inventory_drop_command.py`
- **handle_drop_command()** (15 connections) — `server/commands/inventory_drop_command.py`
- **build_and_broadcast_inventory_event()** (13 connections) — `server/commands/inventory_command_helpers.py`
- **_drop_resolve_stack_or_error()** (12 connections) — `server/commands/inventory_drop_command.py`
- **get_room_manager()** (7 connections) — `server/commands/inventory_command_helpers.py`
- **CommandResponse** (7 connections)
- **_drop_parsed_quantity_or_error()** (6 connections) — `server/commands/inventory_drop_command.py`
- **_drop_finish_after_persist()** (6 connections) — `server/commands/inventory_drop_command.py`
- **_drop_quantity_or_error()** (4 connections) — `server/commands/inventory_drop_command.py`
- **_inventory_rows_after_drop()** (4 connections) — `server/commands/inventory_drop_command.py`
- **_drop_slot_index_or_error()** (4 connections) — `server/commands/inventory_drop_command.py`
- **_drop_quantity_bounds_or_error()** (4 connections) — `server/commands/inventory_drop_command.py`
- **Player** (3 connections)
- **test_handle_drop_command()** (3 connections) — `server/tests/unit/commands/test_inventory_commands.py`
- **Build and broadcast an inventory-related event to the room.** (1 connections) — `server/commands/inventory_command_helpers.py`
- **Get room manager from connection manager, returning (room_manager, error).** (1 connections) — `server/commands/inventory_command_helpers.py`
- **_DropResolved** (1 connections)
- **Drop command: move an inventory stack to the room floor.** (1 connections) — `server/commands/inventory_drop_command.py`
- **Apply partial or full removal of one inventory slot (1-based index).** (1 connections) — `server/commands/inventory_drop_command.py`
- **Resolve 1-based inventory slot from command data or return a usage / range error** (1 connections) — `server/commands/inventory_drop_command.py`
- **Return an error response if drop quantity is out of range for the stack.** (1 connections) — `server/commands/inventory_drop_command.py`
- **Parse quantity from command + stack; return error dict or a validated int (may s** (1 connections) — `server/commands/inventory_drop_command.py`
- **Drop an inventory stack into the current room.** (1 connections) — `server/commands/inventory_drop_command.py`
- **Test handle_drop_command() drops item.** (1 connections) — `server/tests/unit/commands/test_inventory_commands.py`

## Relationships

- [Spell Effect Protocols](Spell_Effect_Protocols.md) (15 shared connections)
- [Container Sync Remediation](Container_Sync_Remediation.md) (8 shared connections)
- [Container Open Events](Container_Open_Events.md) (4 shared connections)
- [Investigations Sessions Xx](Investigations_Sessions_Xx.md) (4 shared connections)
- [WebSocket Auth Integration](WebSocket_Auth_Integration.md) (3 shared connections)
- [Admin NPC Schemas](Admin_NPC_Schemas.md) (3 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (2 shared connections)
- [Pylint Unique Findings](Pylint_Unique_Findings.md) (1 shared connections)
- [Container Component Capacity](Container_Component_Capacity.md) (1 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (1 shared connections)
- [Zone Config Loader](Zone_Config_Loader.md) (1 shared connections)

## Source Files

- `server/commands/inventory_command_helpers.py`
- `server/commands/inventory_drop_command.py`
- `server/tests/unit/commands/test_inventory_commands.py`

## Audit Trail

- EXTRACTED: 113 (92%)
- INFERRED: 10 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*