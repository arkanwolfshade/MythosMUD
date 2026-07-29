# DropResolved

> 125 nodes

## Key Concepts

- **inventory_command_helpers.py** (48 connections) — `server/commands/inventory_command_helpers.py`
- **inventory_pickup_command.py** (35 connections) — `server/commands/inventory_pickup_command.py`
- **persist_player()** (30 connections) — `server/commands/inventory_command_helpers.py`
- **inventory_get_command.py** (29 connections) — `server/commands/inventory_get_command.py`
- **inventory_commands.py** (28 connections) — `server/commands/inventory_commands.py`
- **inventory_drop_command.py** (25 connections) — `server/commands/inventory_drop_command.py`
- **inventory_put_command.py** (21 connections) — `server/commands/inventory_put_command.py`
- **RoomDropManager** (19 connections) — `server/commands/inventory_command_contracts.py`
- **resolve_state_and_player()** (19 connections) — `server/commands/inventory_command_helpers.py`
- **clone_inventory()** (18 connections) — `server/commands/inventory_command_helpers.py`
- **handle_drop_command()** (15 connections) — `server/commands/inventory_drop_command.py`
- **handle_get_command()** (14 connections) — `server/commands/inventory_get_command.py`
- **build_and_broadcast_inventory_event()** (13 connections) — `server/commands/inventory_command_helpers.py`
- **_handle_get_from_room()** (13 connections) — `server/commands/inventory_get_command.py`
- **_pickup_commit_inventory_after_floor_extract()** (13 connections) — `server/commands/inventory_pickup_command.py`
- **handle_put_command()** (13 connections) — `server/commands/inventory_put_command.py`
- **_drop_resolve_stack_or_error()** (12 connections) — `server/commands/inventory_drop_command.py`
- **_get_from_container_path()** (12 connections) — `server/commands/inventory_get_command.py`
- **test_inventory_commands_persistence_helpers.py** (12 connections) — `server/tests/unit/commands/test_inventory_commands_persistence_helpers.py`
- **Player** (11 connections)
- **add_pickup_to_inventory()** (10 connections) — `server/commands/inventory_command_helpers.py`
- **FloorPickupAfterExtract** (10 connections) — `server/commands/inventory_pickup_command.py`
- **_pickup_resolve_floor_stack_or_error()** (10 connections) — `server/commands/inventory_pickup_command.py`
- **inventory_command_contracts.py** (9 connections) — `server/commands/inventory_command_contracts.py`
- **GetCommandRuntime** (9 connections) — `server/commands/inventory_get_command.py`
- *... and 100 more nodes in this community*

## Relationships

- [AbstractContextManager](AbstractContextManager.md) (23 shared connections)
- [test resolve state no app()](test_resolve_state_no_app%28%29.md) (21 shared connections)
- [Any](Any.md) (21 shared connections)
- [handle pickup command()](handle_pickup_command%28%29.md) (19 shared connections)
- [equipment helpers](equipment_helpers.md) (17 shared connections)
- [. init ()](_init_%28%29.md) (14 shared connections)
- [main()](main%28%29.md) (13 shared connections)
- [container helpers inventory](container_helpers_inventory.md) (13 shared connections)
- [.apply dp change()](apply_dp_change%28%29.md) (8 shared connections)
- [admin summon command](admin_summon_command.md) (4 shared connections)
- [container helpers inventory find](container_helpers_inventory_find.md) (4 shared connections)
- [init](init.md) (3 shared connections)

## Source Files

- `server/commands/inventory_command_coercion.py`
- `server/commands/inventory_command_contracts.py`
- `server/commands/inventory_command_helpers.py`
- `server/commands/inventory_commands.py`
- `server/commands/inventory_drop_command.py`
- `server/commands/inventory_get_command.py`
- `server/commands/inventory_pickup_command.py`
- `server/commands/inventory_put_command.py`
- `server/tests/unit/commands/test_inventory_commands_persistence_helpers.py`

## Audit Trail

- EXTRACTED: 678 (91%)
- INFERRED: 64 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*