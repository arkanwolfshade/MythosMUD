# argon2 auth rationale

> 16 nodes

## Key Concepts

- **equipment_helpers.py** (28 connections) — `server/commands/equipment_helpers.py`
- **resolve_unequip_slot()** (8 connections) — `server/commands/equipment_helpers.py`
- **handle_wearable_container_on_equip()** (7 connections) — `server/commands/equipment_helpers.py`
- **find_equipped_item_after_equip()** (6 connections) — `server/commands/equipment_helpers.py`
- **_equip_stack_from_inventory_index()** (4 connections) — `server/commands/equipment_helpers.py`
- **InventoryStack** (4 connections)
- **Player** (3 connections)
- **_find_equipped_by_item_id()** (3 connections) — `server/commands/equipment_helpers.py`
- **_try_resolve_unequip_by_search()** (3 connections) — `server/commands/equipment_helpers.py`
- **_unequip_usage_missing_slot()** (2 connections) — `server/commands/equipment_helpers.py`
- **_try_resolve_unequip_slot_key()** (2 connections) — `server/commands/equipment_helpers.py`
- **Equipment-related helper functions for inventory commands.** (1 connections) — `server/commands/equipment_helpers.py`
- **Deep-copy inventory stack at index and normalize slot_type.** (1 connections) — `server/commands/equipment_helpers.py`
- **Find the equipped slot and item after equipping.** (1 connections) — `server/commands/equipment_helpers.py`
- **Handle wearable container creation when equipping a container item.** (1 connections) — `server/commands/equipment_helpers.py`
- **Resolve slot from command data for unequip command.** (1 connections) — `server/commands/equipment_helpers.py`

## Relationships

- [Inventory Equip](Inventory_Equip.md) (10 shared connections)
- [commands inventory command](commands_inventory_command.md) (9 shared connections)
- [commands inventory helpers](commands_inventory_helpers.md) (7 shared connections)
- [container helpers endpoints](container_helpers_endpoints.md) (2 shared connections)
- [NATS Messaging](NATS_Messaging.md) (2 shared connections)
- [inventory commands command](inventory_commands_command.md) (1 shared connections)
- [world models rationale](world_models_rationale.md) (1 shared connections)
- [Async Query Helpers](Async_Query_Helpers.md) (1 shared connections)

## Source Files

- `server/commands/equipment_helpers.py`

## Audit Trail

- EXTRACTED: 75 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*