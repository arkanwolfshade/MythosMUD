# NATS Anti-Patterns and Best Practices Review

> 34 nodes

## Key Concepts

- **test_look_item.py** (56 connections) — `server/tests/unit/commands/test_look_item.py`
- **fixture** (4 connections)
- **mock_prototype_registry()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **sample_equipped_item()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **sample_inventory_item()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **sample_room_drop()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_check_equipped_item_no_get_equipped_items_method()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_check_equipped_item_success()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_check_item_in_location_fallback_name()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_check_item_in_location_no_prototype()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_check_item_in_location_success()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_check_item_in_location_with_location_name()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_find_item_in_equipped_by_prototype_id()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_find_item_in_equipped_not_found()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_find_item_in_equipped_success()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_find_item_in_inventory_by_item_id()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_find_item_in_inventory_success()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_find_item_in_inventory_with_name_field()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **Test finding item in inventory by name.** (2 connections) — `server/tests/unit/commands/test_look_item.py`
- **Unit tests for item look functionality. Tests the helper functions for looking…** (1 connections) — `server/tests/unit/commands/test_look_item.py`
- **Test finding item in equipped items by name.** (1 connections) — `server/tests/unit/commands/test_look_item.py`
- **Test finding item in equipped items when not found.** (1 connections) — `server/tests/unit/commands/test_look_item.py`
- **Test checking item in location successfully.** (1 connections) — `server/tests/unit/commands/test_look_item.py`
- **Test checking item in location with location name.** (1 connections) — `server/tests/unit/commands/test_look_item.py`
- **Test checking item in location when prototype not found.** (1 connections) — `server/tests/unit/commands/test_look_item.py`
- *... and 9 more nodes in this community*

## Relationships

- [useStatsRollingActions.ts](useStatsRollingActions.ts.md) (18 shared connections)
- [test_look_item_helpers.py](test_look_item_helpers.py.md) (12 shared connections)
- [Migration Strategy](Migration_Strategy.md) (8 shared connections)
- [find_fstring_logging_violations](find_fstring_logging_violations.md) (8 shared connections)
- [ComprehensiveLoggingMiddleware](ComprehensiveLoggingMiddleware.md) (4 shared connections)
- [ContainerComponent](ContainerComponent.md) (1 shared connections)

## Source Files

- `server/tests/unit/commands/test_look_item.py`

## Audit Trail

- EXTRACTED: 88 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*