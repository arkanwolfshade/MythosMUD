# _find_item_in_equipped

> 25 nodes

## Key Concepts

- **_find_item_in_equipped()** (17 connections) — `server/commands/look_item.py`
- **_handle_item_look()** (17 connections) — `server/commands/look_item.py`
- **_try_lookup_item_implicit()** (15 connections) — `server/commands/look_item.py`
- **look_item.py** (14 connections) — `server/commands/look_item.py`
- **_check_item_in_location()** (13 connections) — `server/commands/look_item.py`
- **_check_equipped_item()** (10 connections) — `server/commands/look_item.py`
- **Any** (8 connections)
- **test_check_equipped_item_no_get_equipped_items_method()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_check_equipped_item_success()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_check_item_in_location_fallback_name()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_check_item_in_location_no_prototype()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_check_item_in_location_success()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_find_item_in_equipped_by_prototype_id()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **Item look functionality for MythosMUD. This module handles looking at items,…** (1 connections) — `server/commands/look_item.py`
- **Find an item in equipped items by name or prototype_id. Args: equipped:…** (1 connections) — `server/commands/look_item.py`
- **Check if item found in a location and return formatted result.** (1 connections) — `server/commands/look_item.py`
- **Check if item is equipped and return formatted result.** (1 connections) — `server/commands/look_item.py`
- **Handle looking at a specific item.** (1 connections) — `server/commands/look_item.py`
- **Try to find and display an item in implicit lookup.** (1 connections) — `server/commands/look_item.py`
- **Test checking item in location successfully.** (1 connections) — `server/tests/unit/commands/test_look_item.py`
- **Test checking item in location when prototype not found.** (1 connections) — `server/tests/unit/commands/test_look_item.py`
- **Test checking equipped item successfully.** (1 connections) — `server/tests/unit/commands/test_look_item.py`
- **Test finding item in equipped by prototype_id.** (1 connections) — `server/tests/unit/commands/test_look_item.py`
- **Test checking item in location uses fallback when no prototype.** (1 connections) — `server/tests/unit/commands/test_look_item.py`
- **Test checking equipped item when player has no get_equipped_items method.** (1 connections) — `server/tests/unit/commands/test_look_item.py`

## Relationships

- [test_look_item.py](test_look_item.py.md) (20 shared connections)
- [test_look_item_helpers.py](test_look_item_helpers.py.md) (13 shared connections)
- [asyncio](asyncio.md) (12 shared connections)
- [look_command.py](look_command.py.md) (5 shared connections)
- [_find_item_in_inventory](_find_item_in_inventory.md) (4 shared connections)
- [get_logger](get_logger.md) (2 shared connections)

## Source Files

- `server/commands/look_item.py`
- `server/tests/unit/commands/test_look_item.py`

## Audit Trail

- EXTRACTED: 124 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*