# Player Schema Models

> 18 nodes · cohesion 0.19

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
- **test_handle_put_command()** (3 connections) — `server/tests/unit/commands/test_inventory_commands.py`
- **Player** (2 connections)
- **Put command: move inventory items into a container.** (1 connections) — `server/commands/inventory_put_command.py`
- **Put an item from inventory into a container.** (1 connections) — `server/commands/inventory_put_command.py`
- **Services and request scope for put-after-validation.** (1 connections) — `server/commands/inventory_put_command.py`
- **Validated inventory item and command fields for put.** (1 connections) — `server/commands/inventory_put_command.py`
- **Locate a room or wearable container id, or return an error response.** (1 connections) — `server/commands/inventory_put_command.py`
- **Test handle_put_command() puts item in container.** (1 connections) — `server/tests/unit/commands/test_inventory_commands.py`

## Relationships

- [Rest Command Flow](Rest_Command_Flow.md) (7 shared connections)
- [Admin Set Lucidity Command](Admin_Set_Lucidity_Command.md) (6 shared connections)
- [Container Inventory Ops](Container_Inventory_Ops.md) (4 shared connections)
- [Event Bus Serialization](Event_Bus_Serialization.md) (2 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (2 shared connections)
- [Combat Messaging Integration](Combat_Messaging_Integration.md) (2 shared connections)
- [Container Inventory Finders](Container_Inventory_Finders.md) (2 shared connections)
- [Admin Summon Command](Admin_Summon_Command.md) (1 shared connections)

## Source Files

- `server/commands/inventory_command_helpers.py`
- `server/commands/inventory_put_command.py`
- `server/tests/unit/commands/test_inventory_commands.py`

## Audit Trail

- EXTRACTED: 80 (90%)
- INFERRED: 9 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*