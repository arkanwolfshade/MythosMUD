# test_inventory_put_command.py

> 32 nodes

## Key Concepts

- **test_inventory_put_command.py** (25 connections) — `server/tests/unit/commands/test_inventory_put_command.py`
- **inventory_put_command.py** (22 connections) — `server/commands/inventory_put_command.py`
- **handle_put_command()** (16 connections) — `server/commands/inventory_put_command.py`
- **_put_resolve_container_id()** (13 connections) — `server/commands/inventory_put_command.py`
- **_put_transfer_finish()** (13 connections) — `server/commands/inventory_put_command.py`
- **asyncio** (12 connections)
- **_put_run_validated()** (10 connections) — `server/commands/inventory_put_command.py`
- **PutCommandRuntime** (7 connections) — `server/commands/inventory_put_command.py`
- **PutValidatedWork** (7 connections) — `server/commands/inventory_put_command.py`
- **test_put_run_validated_container_error()** (7 connections) — `server/tests/unit/commands/test_inventory_put_command.py`
- **test_put_run_validated_success()** (7 connections) — `server/tests/unit/commands/test_inventory_put_command.py`
- **remove_item_from_inventory()** (5 connections) — `server/commands/inventory_command_helpers.py`
- **test_handle_put_command_success()** (5 connections) — `server/tests/unit/commands/test_inventory_put_command.py`
- **test_handle_put_command_validation_error()** (5 connections) — `server/tests/unit/commands/test_inventory_put_command.py`
- **test_put_resolve_container_missing_id()** (5 connections) — `server/tests/unit/commands/test_inventory_put_command.py`
- **test_put_resolve_container_not_found()** (5 connections) — `server/tests/unit/commands/test_inventory_put_command.py`
- **test_put_transfer_finish_error()** (5 connections) — `server/tests/unit/commands/test_inventory_put_command.py`
- **test_put_transfer_finish_not_success()** (5 connections) — `server/tests/unit/commands/test_inventory_put_command.py`
- **test_put_transfer_finish_persist_error()** (5 connections) — `server/tests/unit/commands/test_inventory_put_command.py`
- **test_put_transfer_finish_success()** (5 connections) — `server/tests/unit/commands/test_inventory_put_command.py`
- **test_handle_put_command_no_player()** (4 connections) — `server/tests/unit/commands/test_inventory_put_command.py`
- **test_put_resolve_container_id_room_container()** (4 connections) — `server/tests/unit/commands/test_inventory_put_command.py`
- **CommandResponse** (4 connections)
- **UUID** (3 connections)
- **Player** (2 connections)
- *... and 7 more nodes in this community*

## Relationships

- [pytest.md](pytest.md.md) (16 shared connections)
- [command_result_text](command_result_text.md) (15 shared connections)
- [inventory_command_helpers.py](inventory_command_helpers.py.md) (10 shared connections)
- [test_container_helpers_inventory_ops.py](test_container_helpers_inventory_ops.py.md) (3 shared connections)
- [test_container_helpers_inventory_find.py](test_container_helpers_inventory_find.py.md) (3 shared connections)
- [AliasStorage](AliasStorage.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [alias_storage.py](alias_storage.py.md) (1 shared connections)

## Source Files

- `server/commands/inventory_command_helpers.py`
- `server/commands/inventory_put_command.py`
- `server/tests/unit/commands/test_inventory_put_command.py`

## Audit Trail

- EXTRACTED: 108 (83%)
- INFERRED: 22 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*