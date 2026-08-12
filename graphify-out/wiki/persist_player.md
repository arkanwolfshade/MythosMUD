# persist_player

> 57 nodes

## Key Concepts

- **persist_player()** (30 connections) — `server/commands/inventory_command_helpers.py`
- **inventory_drop_command.py** (25 connections) — `server/commands/inventory_drop_command.py`
- **inventory_put_command.py** (21 connections) — `server/commands/inventory_put_command.py`
- **resolve_state_and_player()** (19 connections) — `server/commands/inventory_command_helpers.py`
- **clone_inventory()** (18 connections) — `server/commands/inventory_command_helpers.py`
- **handle_drop_command()** (15 connections) — `server/commands/inventory_drop_command.py`
- **handle_put_command()** (13 connections) — `server/commands/inventory_put_command.py`
- **_drop_resolve_stack_or_error()** (11 connections) — `server/commands/inventory_drop_command.py`
- **Player** (11 connections)
- **_put_resolve_container_id()** (9 connections) — `server/commands/inventory_put_command.py`
- **_put_transfer_finish()** (8 connections) — `server/commands/inventory_put_command.py`
- **get_room_manager()** (7 connections) — `server/commands/inventory_command_helpers.py`
- **_sync_collect_quests_after_inventory_save()** (7 connections) — `server/commands/inventory_command_helpers.py`
- **_put_run_validated()** (7 connections) — `server/commands/inventory_put_command.py`
- **CommandResponse** (7 connections)
- **_drop_finish_after_persist()** (6 connections) — `server/commands/inventory_drop_command.py`
- **_drop_parsed_quantity_or_error()** (6 connections) — `server/commands/inventory_drop_command.py`
- **_player_uuid_for_quest_sync()** (5 connections) — `server/commands/inventory_command_helpers.py`
- **remove_item_from_inventory()** (5 connections) — `server/commands/inventory_command_helpers.py`
- **test_persist_player_error()** (5 connections) — `server/tests/unit/commands/test_inventory_commands_persistence_helpers.py`
- **PutCommandRuntime** (4 connections) — `server/commands/inventory_put_command.py`
- **PutValidatedWork** (4 connections) — `server/commands/inventory_put_command.py`
- **_drop_quantity_bounds_or_error()** (4 connections) — `server/commands/inventory_drop_command.py`
- **_drop_quantity_or_error()** (4 connections) — `server/commands/inventory_drop_command.py`
- **_drop_slot_index_or_error()** (4 connections) — `server/commands/inventory_drop_command.py`
- *... and 32 more nodes in this community*

## Relationships

- [inventory_pickup_command.py](inventory_pickup_command.py.md) (18 shared connections)
- [inventory_commands.py](inventory_commands.py.md) (14 shared connections)
- [inventory_command_helpers.py](inventory_command_helpers.py.md) (14 shared connections)
- [test_inventory_helpers_extended.py](test_inventory_helpers_extended.py.md) (9 shared connections)
- [Player](Player.md) (9 shared connections)
- [AliasStorage](AliasStorage.md) (7 shared connections)
- [inventory_equip_command.py](inventory_equip_command.py.md) (6 shared connections)
- [test_inventory_commands_more_helpers.py](test_inventory_commands_more_helpers.py.md) (6 shared connections)
- [test_container_helpers_inventory_ops.py](test_container_helpers_inventory_ops.py.md) (5 shared connections)
- [ContainerServiceError](ContainerServiceError.md) (4 shared connections)
- [coerce_int](coerce_int.md) (4 shared connections)
- [get_logger](get_logger.md) (4 shared connections)

## Source Files

- `server/commands/communication_commands_support.py`
- `server/commands/inventory_command_helpers.py`
- `server/commands/inventory_drop_command.py`
- `server/commands/inventory_put_command.py`
- `server/tests/unit/commands/test_inventory_commands_persistence_helpers.py`

## Audit Trail

- EXTRACTED: 192 (92%)
- INFERRED: 17 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*