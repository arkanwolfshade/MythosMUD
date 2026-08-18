# server commands inventory command helpers

> 91 nodes

## Key Concepts

- **command_result_text()** (41 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **test_inventory_put_command.py** (25 connections) — `server/tests/unit/commands/test_inventory_put_command.py`
- **inventory_put_command.py** (22 connections) — `server/commands/inventory_put_command.py`
- **test_inventory_commands.py** (21 connections) — `server/tests/unit/commands/test_inventory_commands.py`
- **PickupTestWiring** (19 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **test_inventory_commands_pickup.py** (18 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **handle_put_command()** (16 connections) — `server/commands/inventory_put_command.py`
- **asyncio** (14 connections)
- **_put_resolve_container_id()** (13 connections) — `server/commands/inventory_put_command.py`
- **_put_transfer_finish()** (13 connections) — `server/commands/inventory_put_command.py`
- **asyncio** (12 connections)
- **_put_run_validated()** (10 connections) — `server/commands/inventory_put_command.py`
- **inventory_commands_test_support.py** (10 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **test_handle_pickup_command()** (8 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **test_handle_pickup_command_inventory_capacity_error()** (8 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **PutCommandRuntime** (7 connections) — `server/commands/inventory_put_command.py`
- **PutValidatedWork** (7 connections) — `server/commands/inventory_put_command.py`
- **test_handle_pickup_command_persist_failure_restores_drop_and_inventory()** (7 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **test_put_run_validated_container_error()** (7 connections) — `server/tests/unit/commands/test_inventory_put_command.py`
- **test_put_run_validated_success()** (7 connections) — `server/tests/unit/commands/test_inventory_put_command.py`
- **asyncio** (7 connections)
- **sample_floor_item_stack()** (6 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **_pickup_with_persist_patch()** (6 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **test_handle_pickup_command_invalid_index()** (6 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- **test_handle_pickup_command_no_room_manager()** (6 connections) — `server/tests/unit/commands/test_inventory_commands_pickup.py`
- *... and 66 more nodes in this community*

## Relationships

- [dropresolved](dropresolved.md) (23 shared connections)
- [server commands equipment helpers normalize](server_commands_equipment_helpers_normalize.md) (15 shared connections)
- [server async persistence](server_async_persistence.md) (15 shared connections)
- [server commands inventory get command](server_commands_inventory_get_command.md) (8 shared connections)
- [object](object.md) (4 shared connections)
- [abstractcontextmanager](abstractcontextmanager.md) (4 shared connections)
- [server commands alias commands](server_commands_alias_commands.md) (3 shared connections)
- [claude rules pytest](claude_rules_pytest.md) (3 shared connections)
- [server alias storage aliasstorage](server_alias_storage_aliasstorage.md) (2 shared connections)
- [server commands container helpers inventory](server_commands_container_helpers_inventory.md) (2 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [aliaspayload](aliaspayload.md) (1 shared connections)

## Source Files

- `server/commands/inventory_command_helpers.py`
- `server/commands/inventory_put_command.py`
- `server/tests/unit/commands/inventory_commands_test_support.py`
- `server/tests/unit/commands/test_inventory_commands.py`
- `server/tests/unit/commands/test_inventory_commands_pickup.py`
- `server/tests/unit/commands/test_inventory_put_command.py`

## Audit Trail

- EXTRACTED: 245 (86%)
- INFERRED: 41 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*