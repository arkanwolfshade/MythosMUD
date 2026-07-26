# _find_item_in_inventory

> 24 nodes · cohesion 0.08

## Key Concepts

- **_find_item_in_inventory()** (18 connections) — `server/commands/look_item.py`
- **test_find_item_in_inventory_empty()** (3 connections) — `server/tests/unit/commands/test_look_item_helpers.py`
- **test_find_item_in_inventory_found()** (3 connections) — `server/tests/unit/commands/test_look_item_helpers.py`
- **test_find_item_in_inventory_instance_number_out_of_range()** (3 connections) — `server/tests/unit/commands/test_look_item_helpers.py`
- **test_find_item_in_inventory_multiple_matches()** (3 connections) — `server/tests/unit/commands/test_look_item_helpers.py`
- **test_find_item_in_inventory_no_match()** (3 connections) — `server/tests/unit/commands/test_look_item_helpers.py`
- **test_find_item_in_inventory_not_found()** (3 connections) — `server/tests/unit/commands/test_look_item_helpers.py`
- **test_find_item_in_inventory_with_instance_number()** (3 connections) — `server/tests/unit/commands/test_look_item_helpers.py`
- **test_find_item_in_inventory_by_item_id()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_find_item_in_inventory_not_found()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_find_item_in_inventory_success()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_find_item_in_inventory_with_name_field()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **Find an item in player inventory by name or prototype_id.      Args:         inv** (1 connections) — `server/commands/look_item.py`
- **Test _find_item_in_inventory() with empty list.** (1 connections) — `server/tests/unit/commands/test_look_item_helpers.py`
- **Test _find_item_in_inventory() with no matching items.** (1 connections) — `server/tests/unit/commands/test_look_item_helpers.py`
- **Test _find_item_in_inventory() with multiple matches (ambiguous).** (1 connections) — `server/tests/unit/commands/test_look_item_helpers.py`
- **Test _find_item_in_inventory() with instance number.** (1 connections) — `server/tests/unit/commands/test_look_item_helpers.py`
- **Test _find_item_in_inventory() with instance number out of range.** (1 connections) — `server/tests/unit/commands/test_look_item_helpers.py`
- **Test _find_item_in_inventory() finds item by name.** (1 connections) — `server/tests/unit/commands/test_look_item_helpers.py`
- **Test _find_item_in_inventory() returns None when item not found.** (1 connections) — `server/tests/unit/commands/test_look_item_helpers.py`
- **Test finding item in inventory by name.** (1 connections) — `server/tests/unit/commands/test_look_item.py`
- **Test finding item in inventory when not found.** (1 connections) — `server/tests/unit/commands/test_look_item.py`
- **Test finding item in inventory by item_id.** (1 connections) — `server/tests/unit/commands/test_look_item.py`
- **Test finding item in inventory using 'name' field.** (1 connections) — `server/tests/unit/commands/test_look_item.py`

## Relationships

- [test_look_item_helpers.py](test_look_item_helpers.py.md) (8 shared connections)
- [test_look_item.py](test_look_item.py.md) (5 shared connections)
- [_find_item_in_equipped](_find_item_in_equipped.md) (4 shared connections)

## Source Files

- `server/commands/look_item.py`
- `server/tests/unit/commands/test_look_item.py`
- `server/tests/unit/commands/test_look_item_helpers.py`

## Audit Trail

- EXTRACTED: 63 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*