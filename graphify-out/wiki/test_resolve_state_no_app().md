# test resolve state no app()

> 20 nodes

## Key Concepts

- **equipment_helpers.py** (28 connections) — `server/commands/equipment_helpers.py`
- **normalize_equipped_items()** (8 connections) — `server/commands/equipment_helpers.py`
- **resolve_unequip_slot()** (8 connections) — `server/commands/equipment_helpers.py`
- **resolve_equip_item_index()** (7 connections) — `server/commands/equipment_helpers.py`
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
- **Resolve item index from command data for equip command.** (1 connections) — `server/commands/equipment_helpers.py`
- **Normalize slot names and slot_type in equipped items.** (1 connections) — `server/commands/equipment_helpers.py`
- **Find the equipped slot and item after equipping.** (1 connections) — `server/commands/equipment_helpers.py`
- **Handle wearable container creation when equipping a container item.** (1 connections) — `server/commands/equipment_helpers.py`
- **Resolve slot from command data for unequip command.** (1 connections) — `server/commands/equipment_helpers.py`

## Relationships

- [Any](Any.md) (21 shared connections)
- [Update player's connection list to](Update_player%27s_connection_list_to.md) (4 shared connections)
- [Test check grace period block](Test_check_grace_period_block.md) (2 shared connections)
- [Test process alias expansion function.](Test_process_alias_expansion_function.md) (2 shared connections)
- [Lock](Lock.md) (2 shared connections)
- [world](world.md) (2 shared connections)
- [chat pose helpers](chat_pose_helpers.md) (1 shared connections)
- [main()](main%28%29.md) (1 shared connections)
- [. init ()](_init_%28%29.md) (1 shared connections)

## Source Files

- `server/commands/equipment_helpers.py`

## Audit Trail

- EXTRACTED: 92 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*