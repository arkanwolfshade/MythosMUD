# server commands look item

> 27 nodes

## Key Concepts

- **_handle_item_look()** (15 connections) — `server/commands/look_item.py`
- **look_item.py** (14 connections) — `server/commands/look_item.py`
- **_check_item_in_location()** (13 connections) — `server/commands/look_item.py`
- **_try_lookup_item_implicit()** (13 connections) — `server/commands/look_item.py`
- **_check_equipped_item()** (10 connections) — `server/commands/look_item.py`
- **Any** (8 connections)
- **test_check_equipped_item_no_get_equipped_items_method()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_check_equipped_item_not_found()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_check_equipped_item_success()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_check_item_in_location_fallback_name()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_check_item_in_location_no_prototype()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_check_item_in_location_not_found()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_check_item_in_location_success()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_check_item_in_location_with_location_name()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **Item look functionality for MythosMUD. This module handles looking at items,…** (1 connections) — `server/commands/look_item.py`
- **Check if item found in a location and return formatted result.** (1 connections) — `server/commands/look_item.py`
- **Check if item is equipped and return formatted result.** (1 connections) — `server/commands/look_item.py`
- **Handle looking at a specific item.** (1 connections) — `server/commands/look_item.py`
- **Try to find and display an item in implicit lookup.** (1 connections) — `server/commands/look_item.py`
- **Test checking item in location successfully.** (1 connections) — `server/tests/unit/commands/test_look_item.py`
- **Test checking item in location with location name.** (1 connections) — `server/tests/unit/commands/test_look_item.py`
- **Test checking item in location when item not found.** (1 connections) — `server/tests/unit/commands/test_look_item.py`
- **Test checking item in location when prototype not found.** (1 connections) — `server/tests/unit/commands/test_look_item.py`
- **Test checking equipped item successfully.** (1 connections) — `server/tests/unit/commands/test_look_item.py`
- **Test checking equipped item when not found.** (1 connections) — `server/tests/unit/commands/test_look_item.py`
- *... and 2 more nodes in this community*

## Relationships

- [server tests unit commands test](server_tests_unit_commands_test.md) (25 shared connections)
- [server commands look item find](server_commands_look_item_find.md) (13 shared connections)
- [server commands look item get](server_commands_look_item_get.md) (3 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [server commands exploration commands](server_commands_exploration_commands.md) (1 shared connections)

## Source Files

- `server/commands/look_item.py`
- `server/tests/unit/commands/test_look_item.py`

## Audit Trail

- EXTRACTED: 77 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*