# find_fstring_logging_violations

> 15 nodes

## Key Concepts

- **_get_item_description_from_prototype()** (12 connections) — `server/commands/look_item.py`
- **test_get_item_description_from_prototype_exception_handling()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_get_item_description_from_prototype_fallback()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_get_item_description_from_prototype_fallback_no_prototype()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_get_item_description_from_prototype_no_prototype_id()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_get_item_description_from_prototype_no_registry()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_get_item_description_from_prototype_success()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_get_item_description_from_prototype_with_item_id()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **Test getting item description with fallback name when prototype exists.** (2 connections) — `server/tests/unit/commands/test_look_item.py`
- **Get item description from prototype registry. Returns: Formatted result string…** (1 connections) — `server/commands/look_item.py`
- **Test getting item description from prototype.** (1 connections) — `server/tests/unit/commands/test_look_item.py`
- **Test getting item description when prototype registry is None.** (1 connections) — `server/tests/unit/commands/test_look_item.py`
- **Test getting item description when prototype_id is missing.** (1 connections) — `server/tests/unit/commands/test_look_item.py`
- **Test getting item description using item_id when prototype_id missing.** (1 connections) — `server/tests/unit/commands/test_look_item.py`
- **Test getting item description handles exceptions.** (1 connections) — `server/tests/unit/commands/test_look_item.py`

## Relationships

- [NATS Anti-Patterns and Best Practices Review](NATS_Anti-Patterns_and_Best_Practices_Review.md) (8 shared connections)
- [useStatsRollingActions.ts](useStatsRollingActions.ts.md) (3 shared connections)

## Source Files

- `server/commands/look_item.py`
- `server/tests/unit/commands/test_look_item.py`

## Audit Trail

- EXTRACTED: 26 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*