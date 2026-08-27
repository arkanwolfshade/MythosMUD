# useStatsRollingActions.ts

> 19 nodes

## Key Concepts

- **_find_item_in_inventory()** (18 connections) — `server/commands/look_item.py`
- **_handle_item_look()** (15 connections) — `server/commands/look_item.py`
- **look_item.py** (14 connections) — `server/commands/look_item.py`
- **_check_item_in_location()** (13 connections) — `server/commands/look_item.py`
- **_try_lookup_item_implicit()** (13 connections) — `server/commands/look_item.py`
- **_check_equipped_item()** (10 connections) — `server/commands/look_item.py`
- **Any** (8 connections)
- **test_check_equipped_item_not_found()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_check_item_in_location_not_found()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_find_item_in_inventory_not_found()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **Item look functionality for MythosMUD. This module handles looking at items,…** (1 connections) — `server/commands/look_item.py`
- **Check if item found in a location and return formatted result.** (1 connections) — `server/commands/look_item.py`
- **Check if item is equipped and return formatted result.** (1 connections) — `server/commands/look_item.py`
- **Handle looking at a specific item.** (1 connections) — `server/commands/look_item.py`
- **Try to find and display an item in implicit lookup.** (1 connections) — `server/commands/look_item.py`
- **Find an item in player inventory by name or prototype_id. Args: inventory: List…** (1 connections) — `server/commands/look_item.py`
- **Test finding item in inventory when not found.** (1 connections) — `server/tests/unit/commands/test_look_item.py`
- **Test checking item in location when item not found.** (1 connections) — `server/tests/unit/commands/test_look_item.py`
- **Test checking equipped item when not found.** (1 connections) — `server/tests/unit/commands/test_look_item.py`

## Relationships

- [NATS Anti-Patterns and Best Practices Review](NATS_Anti-Patterns_and_Best_Practices_Review.md) (18 shared connections)
- [ComprehensiveLoggingMiddleware](ComprehensiveLoggingMiddleware.md) (13 shared connections)
- [test_look_item_helpers.py](test_look_item_helpers.py.md) (12 shared connections)
- [Migration Strategy](Migration_Strategy.md) (4 shared connections)
- [find_fstring_logging_violations](find_fstring_logging_violations.md) (3 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (2 shared connections)
- [test_magic_service.py](test_magic_service.py.md) (1 shared connections)

## Source Files

- `server/commands/look_item.py`
- `server/tests/unit/commands/test_look_item.py`

## Audit Trail

- EXTRACTED: 81 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*