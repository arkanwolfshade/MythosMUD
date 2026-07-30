# Any

> 118 nodes

## Key Concepts

- **inventory_command_helpers.py** (48 connections) — `server/commands/inventory_command_helpers.py`
- **inventory_pickup_command.py** (35 connections) — `server/commands/inventory_pickup_command.py`
- **persist_player()** (30 connections) — `server/commands/inventory_command_helpers.py`
- **inventory_get_command.py** (29 connections) — `server/commands/inventory_get_command.py`
- **inventory_drop_command.py** (25 connections) — `server/commands/inventory_drop_command.py`
- **RoomDropManager** (19 connections) — `server/commands/inventory_command_contracts.py`
- **clone_inventory()** (18 connections) — `server/commands/inventory_command_helpers.py`
- **handle_drop_command()** (15 connections) — `server/commands/inventory_drop_command.py`
- **handle_get_command()** (14 connections) — `server/commands/inventory_get_command.py`
- **build_and_broadcast_inventory_event()** (13 connections) — `server/commands/inventory_command_helpers.py`
- **_handle_get_from_room()** (13 connections) — `server/commands/inventory_get_command.py`
- **_pickup_commit_inventory_after_floor_extract()** (13 connections) — `server/commands/inventory_pickup_command.py`
- **_drop_resolve_stack_or_error()** (12 connections) — `server/commands/inventory_drop_command.py`
- **_get_from_container_path()** (12 connections) — `server/commands/inventory_get_command.py`
- **test_inventory_commands_persistence_helpers.py** (12 connections) — `server/tests/unit/commands/test_inventory_commands_persistence_helpers.py`
- **Player** (11 connections)
- **add_pickup_to_inventory()** (10 connections) — `server/commands/inventory_command_helpers.py`
- **FloorPickupAfterExtract** (10 connections) — `server/commands/inventory_pickup_command.py`
- **_pickup_resolve_floor_stack_or_error()** (10 connections) — `server/commands/inventory_pickup_command.py`
- **GetCommandRuntime** (9 connections) — `server/commands/inventory_get_command.py`
- **GetItemSpec** (9 connections) — `server/commands/inventory_get_command.py`
- **FloorPickupEnvironment** (9 connections) — `server/commands/inventory_pickup_command.py`
- **FloorPickupPayload** (9 connections) — `server/commands/inventory_pickup_command.py`
- **complete_pickup_after_floor_extract()** (9 connections) — `server/commands/inventory_pickup_command.py`
- **resolve_pickup_item_index()** (8 connections) — `server/commands/inventory_command_helpers.py`
- *... and 93 more nodes in this community*

## Relationships

- [test resolve state no app()](test_resolve_state_no_app%28%29.md) (34 shared connections)
- [DropResolved](DropResolved.md) (21 shared connections)
- [handle pickup command()](handle_pickup_command%28%29.md) (13 shared connections)
- [. init ()](_init_%28%29.md) (11 shared connections)
- [clean command input()](clean_command_input%28%29.md) (8 shared connections)
- [Lock](Lock.md) (8 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (8 shared connections)
- [container helpers inventory](container_helpers_inventory.md) (8 shared connections)
- [maps](maps.md) (5 shared connections)
- [test format metadata empty()](test_format_metadata_empty%28%29.md) (5 shared connections)
- [lifespan](lifespan.md) (5 shared connections)
- [test magic commands](test_magic_commands.md) (5 shared connections)

## Source Files

- `server/commands/inventory_command_coercion.py`
- `server/commands/inventory_command_contracts.py`
- `server/commands/inventory_command_helpers.py`
- `server/commands/inventory_drop_command.py`
- `server/commands/inventory_get_command.py`
- `server/commands/inventory_pickup_command.py`
- `server/tests/unit/commands/test_inventory_commands.py`
- `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- `server/tests/unit/commands/test_inventory_commands_persistence_helpers.py`
- `server/tests/unit/commands/test_inventory_helpers_extended.py`

## Audit Trail

- EXTRACTED: 570 (91%)
- INFERRED: 57 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*