# persistence rationale player

> 19 nodes

## Key Concepts

- **inventory_put_command.py** (21 connections) — `server/commands/inventory_put_command.py`
- **handle_put_command()** (12 connections) — `server/commands/inventory_put_command.py`
- **_put_resolve_container_id()** (9 connections) — `server/commands/inventory_put_command.py`
- **_put_transfer_finish()** (8 connections) — `server/commands/inventory_put_command.py`
- **_put_run_validated()** (7 connections) — `server/commands/inventory_put_command.py`
- **remove_item_from_inventory()** (5 connections) — `server/commands/inventory_command_helpers.py`
- **PutCommandRuntime** (4 connections) — `server/commands/inventory_put_command.py`
- **PutValidatedWork** (4 connections) — `server/commands/inventory_put_command.py`
- **CommandResponse** (4 connections)
- **UUID** (3 connections)
- **test_handle_put_command()** (3 connections) — `server/tests/unit/commands/test_inventory_commands.py`
- **Player** (2 connections)
- **Remove or update item quantity in player inventory after transfer.** (1 connections) — `server/commands/inventory_command_helpers.py`
- **Put command: move inventory items into a container.** (1 connections) — `server/commands/inventory_put_command.py`
- **Services and request scope for put-after-validation.** (1 connections) — `server/commands/inventory_put_command.py`
- **Validated inventory item and command fields for put.** (1 connections) — `server/commands/inventory_put_command.py`
- **Locate a room or wearable container id, or return an error response.** (1 connections) — `server/commands/inventory_put_command.py`
- **Put an item from inventory into a container.** (1 connections) — `server/commands/inventory_put_command.py`
- **Test handle_put_command() puts item in container.** (1 connections) — `server/tests/unit/commands/test_inventory_commands.py`

## Relationships

- [inventory commands command](inventory_commands_command.md) (5 shared connections)
- [commands inventory command](commands_inventory_command.md) (5 shared connections)
- [container inventory helpers](container_inventory_helpers.md) (4 shared connections)
- [commands admin mute](commands_admin_mute.md) (3 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)
- [container find inventory](container_find_inventory.md) (2 shared connections)
- [commands inventory pickup](commands_inventory_pickup.md) (2 shared connections)
- [world models rationale](world_models_rationale.md) (1 shared connections)
- [combat models rationale](combat_models_rationale.md) (1 shared connections)

## Source Files

- `server/commands/inventory_command_helpers.py`
- `server/commands/inventory_put_command.py`
- `server/tests/unit/commands/test_inventory_commands.py`

## Audit Trail

- EXTRACTED: 81 (91%)
- INFERRED: 8 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*