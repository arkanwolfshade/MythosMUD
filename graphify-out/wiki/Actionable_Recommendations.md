# Actionable Recommendations

> 23 nodes · cohesion 0.13

## Key Concepts

- **_find_item_in_inventory()** (18 connections) — `server/commands/look_item.py`
- **_handle_item_look()** (17 connections) — `server/commands/look_item.py`
- **_try_lookup_item_implicit()** (15 connections) — `server/commands/look_item.py`
- **look_item.py** (14 connections) — `server/commands/look_item.py`
- **_check_item_in_location()** (13 connections) — `server/commands/look_item.py`
- **_check_equipped_item()** (10 connections) — `server/commands/look_item.py`
- **Any** (8 connections)
- **test_find_item_in_inventory_found()** (3 connections) — `server/tests/unit/commands/test_look_item_helpers.py`
- **test_find_item_in_inventory_instance_number_out_of_range()** (3 connections) — `server/tests/unit/commands/test_look_item_helpers.py`
- **test_find_item_in_inventory_multiple_matches()** (3 connections) — `server/tests/unit/commands/test_look_item_helpers.py`
- **test_find_item_in_inventory_no_match()** (3 connections) — `server/tests/unit/commands/test_look_item_helpers.py`
- **test_find_item_in_inventory_with_instance_number()** (3 connections) — `server/tests/unit/commands/test_look_item_helpers.py`
- **Item look functionality for MythosMUD. This module handles looking at items,…** (1 connections) — `server/commands/look_item.py`
- **Check if item found in a location and return formatted result.** (1 connections) — `server/commands/look_item.py`
- **Check if item is equipped and return formatted result.** (1 connections) — `server/commands/look_item.py`
- **Handle looking at a specific item.** (1 connections) — `server/commands/look_item.py`
- **Try to find and display an item in implicit lookup.** (1 connections) — `server/commands/look_item.py`
- **Find an item in player inventory by name or prototype_id. Args: inventory: List…** (1 connections) — `server/commands/look_item.py`
- **Test _find_item_in_inventory() with no matching items.** (1 connections) — `server/tests/unit/commands/test_look_item_helpers.py`
- **Test _find_item_in_inventory() with multiple matches (ambiguous).** (1 connections) — `server/tests/unit/commands/test_look_item_helpers.py`
- **Test _find_item_in_inventory() with instance number.** (1 connections) — `server/tests/unit/commands/test_look_item_helpers.py`
- **Test _find_item_in_inventory() with instance number out of range.** (1 connections) — `server/tests/unit/commands/test_look_item_helpers.py`
- **Test _find_item_in_inventory() finds item by name.** (1 connections) — `server/tests/unit/commands/test_look_item_helpers.py`

## Relationships

- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) (18 shared connections)
- [lucidity.py](lucidity.py.md) (13 shared connections)
- [compilerOptions](compilerOptions.md) (12 shared connections)
- [_RecordingRoom](_RecordingRoom.md) (5 shared connections)
- [resolve_npc_attack_damage](resolve_npc_attack_damage.md) (4 shared connections)
- [Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Malleus Monstrorum - Cthulhu Mythos Bestiary  (2026-08-12)](Graph_Report_-_C-_Users_arkan_Proton_Drive_arkanwolfshade_My_files_Chaosium_Malleus_Monstrorum_-_Cthulhu_Mythos_Bestiary__2026-08-12.md) (3 shared connections)
- [Room](Room.md) (2 shared connections)

## Source Files

- `server/commands/look_item.py`
- `server/tests/unit/commands/test_look_item_helpers.py`

## Audit Trail

- EXTRACTED: 89 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*