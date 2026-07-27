# Look Item Commands

> 33 nodes · cohesion 0.07

## Key Concepts

- **_handle_item_look()** (17 connections) — `server/commands/look_item.py`
- **_try_lookup_item_implicit()** (15 connections) — `server/commands/look_item.py`
- **_check_item_in_location()** (13 connections) — `server/commands/look_item.py`
- **look_item.py** (12 connections) — `server/commands/look_item.py`
- **_check_equipped_item()** (10 connections) — `server/commands/look_item.py`
- **Any** (8 connections) — `server/commands/look_item.py`
- **test_check_equipped_item_not_found()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_check_item_in_location_no_prototype()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_check_item_in_location_with_location_name()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_handle_item_look_in_inventory()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_handle_item_look_in_room_drops()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_handle_item_look_not_found()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_handle_item_look_player_no_get_inventory()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_handle_item_look_with_instance_number()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_try_lookup_item_implicit_in_equipped()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_try_lookup_item_implicit_in_room_drops()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_try_lookup_item_implicit_not_found()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_try_lookup_item_implicit_player_no_get_equipped_items()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **Item look functionality for MythosMUD.  This module handles looking at items, in** (1 connections) — `server/commands/look_item.py`
- **Check if item found in a location and return formatted result.** (1 connections) — `server/commands/look_item.py`
- **Check if item is equipped and return formatted result.** (1 connections) — `server/commands/look_item.py`
- **Handle looking at a specific item.** (1 connections) — `server/commands/look_item.py`
- **Test checking item in location with location name.** (1 connections) — `server/tests/unit/commands/test_look_item.py`
- **Test checking item in location when prototype not found.** (1 connections) — `server/tests/unit/commands/test_look_item.py`
- **Test checking equipped item when not found.** (1 connections) — `server/tests/unit/commands/test_look_item.py`
- *... and 8 more nodes in this community*

## Relationships

- [[Look Item Command Tests]] (24 shared connections)
- [[Commands Look Item]] (15 shared connections)
- [[Alias Expansion Logic]] (3 shared connections)
- [[NPC Admin API]] (2 shared connections)
- [[Commands Command Look]] (2 shared connections)
- [[Look Player Command]] (2 shared connections)

## Source Files

- `server/commands/look_item.py`
- `server/tests/unit/commands/test_look_item.py`

## Audit Trail

- EXTRACTED: 126 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
