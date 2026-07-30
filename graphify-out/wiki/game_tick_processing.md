# game tick processing

> 26 nodes

## Key Concepts

- **_find_item_in_room_drops()** (23 connections) — `server/commands/look_item.py`
- **test_find_item_in_room_drops_success()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_find_item_in_room_drops_by_prototype_id()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_find_item_in_room_drops_not_found()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_find_item_in_room_drops_multiple_matches()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_find_item_in_room_drops_with_instance_number()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_find_item_in_room_drops_instance_number_out_of_range()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_find_item_in_room_drops_by_item_id()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_find_item_in_room_drops_found()** (3 connections) — `server/tests/unit/commands/test_look_item_helpers.py`
- **test_find_item_in_room_drops_not_found()** (3 connections) — `server/tests/unit/commands/test_look_item_helpers.py`
- **test_find_item_in_room_drops_instance_number()** (3 connections) — `server/tests/unit/commands/test_look_item_helpers.py`
- **test_find_item_in_room_drops_multiple_matches()** (3 connections) — `server/tests/unit/commands/test_look_item_helpers.py`
- **test_find_item_in_room_drops_with_instance_number()** (3 connections) — `server/tests/unit/commands/test_look_item_helpers.py`
- **Find an item in room drops by name or prototype_id.      Args:         room_drop** (1 connections) — `server/commands/look_item.py`
- **Test finding item in room drops by name.** (1 connections) — `server/tests/unit/commands/test_look_item.py`
- **Test finding item in room drops by prototype_id.** (1 connections) — `server/tests/unit/commands/test_look_item.py`
- **Test finding item in room drops when not found.** (1 connections) — `server/tests/unit/commands/test_look_item.py`
- **Test finding item in room drops with multiple matches.** (1 connections) — `server/tests/unit/commands/test_look_item.py`
- **Test finding item in room drops with instance number.** (1 connections) — `server/tests/unit/commands/test_look_item.py`
- **Test finding item in room drops with invalid instance number.** (1 connections) — `server/tests/unit/commands/test_look_item.py`
- **Test finding item in room drops by item_id.** (1 connections) — `server/tests/unit/commands/test_look_item.py`
- **Test _find_item_in_room_drops() finds item by name.** (1 connections) — `server/tests/unit/commands/test_look_item_helpers.py`
- **Test _find_item_in_room_drops() returns None when item not found.** (1 connections) — `server/tests/unit/commands/test_look_item_helpers.py`
- **Test _find_item_in_room_drops() with instance number.** (1 connections) — `server/tests/unit/commands/test_look_item_helpers.py`
- **Test _find_item_in_room_drops() with multiple matches (ambiguous).** (1 connections) — `server/tests/unit/commands/test_look_item_helpers.py`
- *... and 1 more nodes in this community*

## Relationships

- [Any](Any.md) (10 shared connections)
- [test look item](test_look_item.md) (8 shared connections)
- [DeathInterstitial](DeathInterstitial.md) (4 shared connections)

## Source Files

- `server/commands/look_item.py`
- `server/tests/unit/commands/test_look_item.py`
- `server/tests/unit/commands/test_look_item_helpers.py`

## Audit Trail

- EXTRACTED: 72 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*