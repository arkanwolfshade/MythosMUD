# AnyIO vs Asyncio Guide

> 21 nodes

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
- **test_handle_put_command_no_target()** (4 connections) — `server/tests/unit/commands/test_inventory_commands.py`
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
- **Test handle_put_command() handles missing target.** (1 connections) — `server/tests/unit/commands/test_inventory_commands.py`

## Relationships

- [Container Sync Remediation](Container_Sync_Remediation.md) (5 shared connections)
- [Container Inventory Ops](Container_Inventory_Ops.md) (4 shared connections)
- [Async Task Registry](Async_Task_Registry.md) (3 shared connections)
- [Player Schema Converter](Player_Schema_Converter.md) (3 shared connections)
- [Container Component Capacity](Container_Component_Capacity.md) (2 shared connections)
- [Zone Config Loader](Zone_Config_Loader.md) (2 shared connections)
- [Client Event Store](Client_Event_Store.md) (2 shared connections)
- [Container Inventory Finders](Container_Inventory_Finders.md) (2 shared connections)
- [NATS Connection State Machine](NATS_Connection_State_Machine.md) (2 shared connections)
- [Container Open Events](Container_Open_Events.md) (1 shared connections)
- [Admin NPC Schemas](Admin_NPC_Schemas.md) (1 shared connections)

## Source Files

- `server/commands/inventory_command_helpers.py`
- `server/commands/inventory_put_command.py`
- `server/tests/unit/commands/test_inventory_commands.py`

## Audit Trail

- EXTRACTED: 85 (89%)
- INFERRED: 10 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*