# Command Factories Inventory

> 23 nodes · cohesion 0.09

## Key Concepts

- **InventoryCommandFactory** (17 connections) — `server/utils/command_factories_inventory.py`
- **.create_pickup_command()** (6 connections) — `server/utils/command_factories_inventory.py`
- **.create_get_command()** (4 connections) — `server/utils/command_factories_inventory.py`
- **.create_inventory_command()** (4 connections) — `server/utils/command_factories_inventory.py`
- **.create_put_command()** (4 connections) — `server/utils/command_factories_inventory.py`
- **.create_unequip_command()** (4 connections) — `server/utils/command_factories_inventory.py`
- **._parse_index_or_search_term()** (4 connections) — `server/utils/command_factories_inventory.py`
- **._parse_quantity_from_args()** (4 connections) — `server/utils/command_factories_inventory.py`
- **.create_drop_command()** (3 connections) — `server/utils/command_factories_inventory.py`
- **DropCommand** (1 connections) — `server/utils/command_factories_inventory.py`
- **GetCommand** (1 connections) — `server/utils/command_factories_inventory.py`
- **InventoryCommand** (1 connections) — `server/utils/command_factories_inventory.py`
- **PickupCommand** (1 connections) — `server/utils/command_factories_inventory.py`
- **PutCommand** (1 connections) — `server/utils/command_factories_inventory.py`
- **UnequipCommand** (1 connections) — `server/utils/command_factories_inventory.py`
- **Factory class for creating inventory and item management command objects.** (1 connections) — `server/utils/command_factories_inventory.py`
- **Create InventoryCommand from arguments.** (1 connections) — `server/utils/command_factories_inventory.py`
- **Parse quantity from args if present.          Args:             args: Original a** (1 connections) — `server/utils/command_factories_inventory.py`
- **Parse index or search term from selector tokens.          Args:             args** (1 connections) — `server/utils/command_factories_inventory.py`
- **Create pickup command supporting numeric indices or fuzzy names.** (1 connections) — `server/utils/command_factories_inventory.py`
- **Create put command.          Supports: put <item> [in] <container> [quantity]** (1 connections) — `server/utils/command_factories_inventory.py`
- **Create get command.          Supports: get <item> [from] <container> [quantity]** (1 connections) — `server/utils/command_factories_inventory.py`
- **Create unequip command.** (1 connections) — `server/utils/command_factories_inventory.py`

## Relationships

- [[NPC Admin API]] (10 shared connections)
- [[Inventory Command Factories]] (2 shared connections)
- [[Communication Command Classes]] (2 shared connections)
- [[Command Factory Creators]] (2 shared connections)

## Source Files

- `server/utils/command_factories_inventory.py`

## Audit Trail

- EXTRACTED: 62 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
