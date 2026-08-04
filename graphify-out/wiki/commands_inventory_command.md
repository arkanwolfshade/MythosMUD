# commands inventory command

> 135 nodes

## Key Concepts

- **test_inventory_helpers.py** (38 connections) — `server/tests/unit/commands/test_inventory_helpers.py`
- **equipment_helpers.py** (29 connections) — `server/commands/equipment_helpers.py`
- **test_equipment_helpers.py** (25 connections) — `server/tests/unit/commands/test_equipment_helpers.py`
- **inventory_item_matching.py** (22 connections) — `server/commands/inventory_item_matching.py`
- **match_room_drop_by_name()** (19 connections) — `server/commands/inventory_item_matching.py`
- **normalize_slot_name()** (19 connections) — `server/commands/inventory_item_matching.py`
- **match_equipped_item_by_name()** (18 connections) — `server/commands/inventory_item_matching.py`
- **match_inventory_item_by_name()** (16 connections) — `server/commands/inventory_item_matching.py`
- **resolve_unequip_slot()** (14 connections) — `server/commands/equipment_helpers.py`
- **resolve_equip_item_index()** (13 connections) — `server/commands/equipment_helpers.py`
- **test_inventory_commands_helpers.py** (13 connections) — `server/tests/unit/commands/test_inventory_commands_helpers.py`
- **handle_wearable_container_on_equip()** (10 connections) — `server/commands/equipment_helpers.py`
- **find_equipped_item_after_equip()** (9 connections) — `server/commands/equipment_helpers.py`
- **_player()** (8 connections) — `server/tests/unit/commands/test_equipment_helpers.py`
- **build_equipped_candidates()** (5 connections) — `server/commands/inventory_item_matching.py`
- **_equip_stack_from_inventory_index()** (4 connections) — `server/commands/equipment_helpers.py`
- **InventoryStack** (4 connections)
- **extract_item_identifier()** (4 connections) — `server/commands/inventory_item_matching.py`
- **build_drop_candidates()** (4 connections) — `server/commands/inventory_item_matching.py`
- **match_exact_drop()** (4 connections) — `server/commands/inventory_item_matching.py`
- **match_prefix_drop()** (4 connections) — `server/commands/inventory_item_matching.py`
- **match_substring_drop()** (4 connections) — `server/commands/inventory_item_matching.py`
- **build_inventory_candidates()** (4 connections) — `server/commands/inventory_item_matching.py`
- **Player** (3 connections)
- **_find_equipped_by_item_id()** (3 connections) — `server/commands/equipment_helpers.py`
- *... and 110 more nodes in this community*

## Relationships

- [container helpers endpoints](container_helpers_endpoints.md) (28 shared connections)
- [inventory commands command](inventory_commands_command.md) (9 shared connections)
- [commands inventory helpers](commands_inventory_helpers.md) (6 shared connections)
- [stats game generator](stats_game_generator.md) (3 shared connections)
- [combat models rationale](combat_models_rationale.md) (2 shared connections)
- [Loot Generation](Loot_Generation.md) (2 shared connections)
- [commands inventory pickup](commands_inventory_pickup.md) (1 shared connections)

## Source Files

- `server/commands/equipment_helpers.py`
- `server/commands/inventory_item_matching.py`
- `server/tests/unit/commands/test_equipment_helpers.py`
- `server/tests/unit/commands/test_inventory_commands_helpers.py`
- `server/tests/unit/commands/test_inventory_helpers.py`

## Audit Trail

- EXTRACTED: 503 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*