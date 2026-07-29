# look item

> 29 nodes

## Key Concepts

- **_find_item_in_inventory()** (18 connections) — `server/commands/look_item.py`
- **_handle_item_look()** (17 connections) — `server/commands/look_item.py`
- **_try_lookup_item_implicit()** (15 connections) — `server/commands/look_item.py`
- **look_item.py** (14 connections) — `server/commands/look_item.py`
- **_check_item_in_location()** (13 connections) — `server/commands/look_item.py`
- **_check_equipped_item()** (10 connections) — `server/commands/look_item.py`
- **Any** (8 connections)
- **test_find_item_in_inventory_not_found()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_check_item_in_location_with_location_name()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_handle_item_look_in_equipped()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_try_lookup_item_implicit_in_room_drops()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_try_lookup_item_implicit_not_found()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_check_item_in_location_fallback_name()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_handle_item_look_with_instance_number()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_handle_item_look_player_no_get_inventory()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **Item look functionality for MythosMUD.  This module handles looking at items, in** (1 connections) — `server/commands/look_item.py`
- **Find an item in player inventory by name or prototype_id.      Args:         inv** (1 connections) — `server/commands/look_item.py`
- **Check if item found in a location and return formatted result.** (1 connections) — `server/commands/look_item.py`
- **Check if item is equipped and return formatted result.** (1 connections) — `server/commands/look_item.py`
- **Handle looking at a specific item.** (1 connections) — `server/commands/look_item.py`
- **Try to find and display an item in implicit lookup.** (1 connections) — `server/commands/look_item.py`
- **Test finding item in inventory when not found.** (1 connections) — `server/tests/unit/commands/test_look_item.py`
- **Test checking item in location with location name.** (1 connections) — `server/tests/unit/commands/test_look_item.py`
- **Test handling item look when item is equipped.** (1 connections) — `server/tests/unit/commands/test_look_item.py`
- **Test trying implicit lookup when item is in room drops.** (1 connections) — `server/tests/unit/commands/test_look_item.py`
- *... and 4 more nodes in this community*

## Relationships

- [test look item](test_look_item.md) (29 shared connections)
- [test find item in equipped](test_find_item_in_equipped.md) (13 shared connections)
- [look command](look_command.md) (5 shared connections)
- [test find item in room](test_find_item_in_room.md) (4 shared connections)
- [get item description from prototype()](get_item_description_from_prototype%28%29.md) (3 shared connections)
- [main()](main%28%29.md) (2 shared connections)
- [Test trying implicit lookup when](Test_trying_implicit_lookup_when.md) (1 shared connections)

## Source Files

- `server/commands/look_item.py`
- `server/tests/unit/commands/test_look_item.py`

## Audit Trail

- EXTRACTED: 133 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*