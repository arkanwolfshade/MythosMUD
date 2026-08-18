# server commands inventory get command

> 32 nodes

## Key Concepts

- **inventory_get_command.py** (30 connections) — `server/commands/inventory_get_command.py`
- **test_inventory_get_command.py** (26 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **handle_get_command()** (16 connections) — `server/commands/inventory_get_command.py`
- **_handle_get_from_room()** (16 connections) — `server/commands/inventory_get_command.py`
- **_get_from_container_path()** (15 connections) — `server/commands/inventory_get_command.py`
- **_get_transfer_out_of_container()** (11 connections) — `server/commands/inventory_get_command.py`
- **asyncio** (10 connections)
- **GetCommandRuntime** (8 connections) — `server/commands/inventory_get_command.py`
- **GetItemSpec** (8 connections) — `server/commands/inventory_get_command.py`
- **_get_route_after_validation()** (7 connections) — `server/commands/inventory_get_command.py`
- **test_get_from_container_path_item_not_in_container()** (6 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **test_get_from_container_path_missing_container()** (6 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **test_handle_get_command_uses_pickup_wiring()** (5 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **CommandResponse** (5 connections)
- **_container_transfer_messages()** (4 connections) — `server/commands/inventory_get_command.py`
- **test_get_transfer_out_of_container_error()** (4 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **test_get_transfer_out_of_container_not_success()** (4 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **test_get_transfer_out_of_container_success()** (4 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **test_handle_get_from_room_index_error()** (4 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **test_handle_get_from_room_invalid_quantity()** (4 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **test_handle_get_from_room_unresolved_index()** (4 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **test_handle_get_command_player_not_found()** (3 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **test_container_transfer_messages()** (2 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **Player** (2 connections)
- **UUID** (2 connections)
- *... and 7 more nodes in this community*

## Relationships

- [dropresolved](dropresolved.md) (20 shared connections)
- [server async persistence](server_async_persistence.md) (12 shared connections)
- [server commands inventory command helpers](server_commands_inventory_command_helpers.md) (8 shared connections)
- [object](object.md) (6 shared connections)
- [server commands container helpers inventory](server_commands_container_helpers_inventory.md) (2 shared connections)
- [server alias storage aliasstorage](server_alias_storage_aliasstorage.md) (2 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [server models player player apply](server_models_player_player_apply.md) (1 shared connections)
- [aliaspayload](aliaspayload.md) (1 shared connections)
- [claude rules pytest](claude_rules_pytest.md) (1 shared connections)

## Source Files

- `server/commands/inventory_get_command.py`
- `server/tests/unit/commands/test_inventory_get_command.py`

## Audit Trail

- EXTRACTED: 109 (81%)
- INFERRED: 25 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*