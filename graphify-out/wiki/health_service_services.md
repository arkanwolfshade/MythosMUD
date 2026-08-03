# health service services

> 25 nodes

## Key Concepts

- **_find_item_in_equipped()** (17 connections) — `server/commands/look_item.py`
- **_handle_item_look()** (17 connections) — `server/commands/look_item.py`
- **_try_lookup_item_implicit()** (15 connections) — `server/commands/look_item.py`
- **look_item.py** (14 connections) — `server/commands/look_item.py`
- **_check_item_in_location()** (13 connections) — `server/commands/look_item.py`
- **_get_item_description_from_prototype()** (12 connections) — `server/commands/look_item.py`
- **_check_equipped_item()** (10 connections) — `server/commands/look_item.py`
- **Any** (8 connections)
- **test_get_item_description_from_prototype_fallback_no_prototype()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_check_item_in_location_not_found()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_handle_item_look_not_found()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_handle_item_look_look_in_skips_equipped()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_find_item_in_equipped_by_prototype_id()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **Item look functionality for MythosMUD.  This module handles looking at items, in** (1 connections) — `server/commands/look_item.py`
- **Find an item in equipped items by name or prototype_id.      Args:         equip** (1 connections) — `server/commands/look_item.py`
- **Get item description from prototype registry.      Returns:         Formatted re** (1 connections) — `server/commands/look_item.py`
- **Check if item found in a location and return formatted result.** (1 connections) — `server/commands/look_item.py`
- **Check if item is equipped and return formatted result.** (1 connections) — `server/commands/look_item.py`
- **Handle looking at a specific item.** (1 connections) — `server/commands/look_item.py`
- **Try to find and display an item in implicit lookup.** (1 connections) — `server/commands/look_item.py`
- **Test getting item description with fallback name when prototype doesn't exist.** (1 connections) — `server/tests/unit/commands/test_look_item.py`
- **Test checking item in location when item not found.** (1 connections) — `server/tests/unit/commands/test_look_item.py`
- **Test handling item look when item not found.** (1 connections) — `server/tests/unit/commands/test_look_item.py`
- **Test handling item look with look_in flag skips equipped items.** (1 connections) — `server/tests/unit/commands/test_look_item.py`
- **Test finding item in equipped by prototype_id.** (1 connections) — `server/tests/unit/commands/test_look_item.py`

## Relationships

- [Item Lookup](Item_Lookup.md) (27 shared connections)
- [connection realtime statistics](connection_realtime_statistics.md) (9 shared connections)
- [look command commands](look_command_commands.md) (5 shared connections)
- [movement monitor game](movement_monitor_game.md) (4 shared connections)
- [combat npc service](combat_npc_service.md) (4 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)
- [admin services auth](admin_services_auth.md) (1 shared connections)
- [liability types call](liability_types_call.md) (1 shared connections)
- [lucidity services npc](lucidity_services_npc.md) (1 shared connections)
- [tsconfig app DOM](tsconfig_app_DOM.md) (1 shared connections)
- [game level service](game_level_service.md) (1 shared connections)
- [tsconfig build DOM](tsconfig_build_DOM.md) (1 shared connections)

## Source Files

- `server/commands/look_item.py`
- `server/tests/unit/commands/test_look_item.py`

## Audit Trail

- EXTRACTED: 133 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*