# NATS Connection State Machine

> 17 nodes

## Key Concepts

- **test_inventory_commands.py** (20 connections) — `server/tests/unit/commands/test_inventory_commands.py`
- **handle_inventory_command()** (14 connections) — `server/commands/inventory_commands.py`
- **test_handle_inventory_command_no_persistence()** (4 connections) — `server/tests/unit/commands/test_inventory_commands.py`
- **test_handle_unequip_command_no_target()** (4 connections) — `server/tests/unit/commands/test_inventory_commands.py`
- **test_handle_get_command_no_target()** (4 connections) — `server/tests/unit/commands/test_inventory_commands.py`
- **test_handle_inventory_command()** (3 connections) — `server/tests/unit/commands/test_inventory_commands.py`
- **test_handle_unequip_command()** (3 connections) — `server/tests/unit/commands/test_inventory_commands.py`
- **test_handle_get_command()** (3 connections) — `server/tests/unit/commands/test_inventory_commands.py`
- **CommandResponse** (1 connections)
- **Display the player's inventory and equipped items, including container contents.** (1 connections) — `server/commands/inventory_commands.py`
- **Unit tests for inventory command handlers (except pickup; see test_inventory_com** (1 connections) — `server/tests/unit/commands/test_inventory_commands.py`
- **Test handle_inventory_command() displays inventory.** (1 connections) — `server/tests/unit/commands/test_inventory_commands.py`
- **Test handle_inventory_command() handles missing persistence.** (1 connections) — `server/tests/unit/commands/test_inventory_commands.py`
- **Test handle_unequip_command() unequips item.** (1 connections) — `server/tests/unit/commands/test_inventory_commands.py`
- **Test handle_unequip_command() handles missing target.** (1 connections) — `server/tests/unit/commands/test_inventory_commands.py`
- **Test handle_get_command() gets item from container.** (1 connections) — `server/tests/unit/commands/test_inventory_commands.py`
- **Test handle_get_command() handles missing target.** (1 connections) — `server/tests/unit/commands/test_inventory_commands.py`

## Relationships

- [Admin NPC Schemas](Admin_NPC_Schemas.md) (9 shared connections)
- [Container Sync Remediation](Container_Sync_Remediation.md) (7 shared connections)
- [Container Open Events](Container_Open_Events.md) (3 shared connections)
- [Container Component Capacity](Container_Component_Capacity.md) (3 shared connections)
- [AnyIO vs Asyncio Guide](AnyIO_vs_Asyncio_Guide.md) (2 shared connections)
- [Player Schema Converter](Player_Schema_Converter.md) (1 shared connections)
- [Async Task Registry](Async_Task_Registry.md) (1 shared connections)
- [Container Inventory Ops](Container_Inventory_Ops.md) (1 shared connections)
- [Admin Command Models](Admin_Command_Models.md) (1 shared connections)

## Source Files

- `server/commands/inventory_commands.py`
- `server/tests/unit/commands/test_inventory_commands.py`

## Audit Trail

- EXTRACTED: 57 (89%)
- INFERRED: 7 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*