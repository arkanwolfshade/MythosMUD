# inventory_put_command.py

> 17 nodes

## Key Concepts

- **inventory_put_command.py** (21 connections) — `server/commands/inventory_put_command.py`
- **handle_put_command()** (13 connections) — `server/commands/inventory_put_command.py`
- **_put_resolve_container_id()** (9 connections) — `server/commands/inventory_put_command.py`
- **_put_transfer_finish()** (8 connections) — `server/commands/inventory_put_command.py`
- **_put_run_validated()** (7 connections) — `server/commands/inventory_put_command.py`
- **remove_item_from_inventory()** (5 connections) — `server/commands/inventory_command_helpers.py`
- **PutCommandRuntime** (4 connections) — `server/commands/inventory_put_command.py`
- **PutValidatedWork** (4 connections) — `server/commands/inventory_put_command.py`
- **CommandResponse** (4 connections)
- **UUID** (3 connections)
- **Player** (2 connections)
- **Remove or update item quantity in player inventory after transfer.** (1 connections) — `server/commands/inventory_command_helpers.py`
- **Put command: move inventory items into a container.** (1 connections) — `server/commands/inventory_put_command.py`
- **Put an item from inventory into a container.** (1 connections) — `server/commands/inventory_put_command.py`
- **Services and request scope for put-after-validation.** (1 connections) — `server/commands/inventory_put_command.py`
- **Validated inventory item and command fields for put.** (1 connections) — `server/commands/inventory_put_command.py`
- **Locate a room or wearable container id, or return an error response.** (1 connections) — `server/commands/inventory_put_command.py`

## Relationships

- [inventory_command_helpers.py](inventory_command_helpers.py.md) (10 shared connections)
- [AliasStorage](AliasStorage.md) (4 shared connections)
- [test_container_helpers_inventory_ops.py](test_container_helpers_inventory_ops.py.md) (4 shared connections)
- [test_inventory_commands.py](test_inventory_commands.py.md) (2 shared connections)
- [test_container_helpers_inventory_find.py](test_container_helpers_inventory_find.py.md) (2 shared connections)
- [log_and_raise](log_and_raise.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)

## Source Files

- `server/commands/inventory_command_helpers.py`
- `server/commands/inventory_put_command.py`

## Audit Trail

- EXTRACTED: 48 (86%)
- INFERRED: 8 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*