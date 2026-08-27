# Uvicorn ASGI Server Best Practices

> 27 nodes

## Key Concepts

- **_find_container_wearable()** (23 connections) — `server/commands/look_container.py`
- **_select_match()** (5 connections) — `server/commands/look_container.py`
- **test_find_container_wearable_instance_number_out_of_range()** (4 connections) — `server/tests/unit/commands/test_look_container.py`
- **test_find_container_wearable_with_instance_number()** (4 connections) — `server/tests/unit/commands/test_look_container.py`
- **test_find_container_wearable_empty()** (3 connections) — `server/tests/unit/commands/test_look_container_helpers.py`
- **test_find_container_wearable_found()** (3 connections) — `server/tests/unit/commands/test_look_container_helpers.py`
- **test_find_container_wearable_instance_number_out_of_range()** (3 connections) — `server/tests/unit/commands/test_look_container_helpers.py`
- **test_find_container_wearable_multiple_matches()** (3 connections) — `server/tests/unit/commands/test_look_container_helpers.py`
- **test_find_container_wearable_no_match()** (3 connections) — `server/tests/unit/commands/test_look_container_helpers.py`
- **test_find_container_wearable_not_found()** (3 connections) — `server/tests/unit/commands/test_look_container_helpers.py`
- **test_find_container_wearable_with_instance_number()** (3 connections) — `server/tests/unit/commands/test_look_container_helpers.py`
- **test_find_container_wearable_not_found()** (3 connections) — `server/tests/unit/commands/test_look_container.py`
- **test_find_container_wearable_with_inner_container()** (3 connections) — `server/tests/unit/commands/test_look_container.py`
- **_wearable_matches_target()** (2 connections) — `server/commands/look_container.py`
- **Test finding wearable container with instance number.** (2 connections) — `server/tests/unit/commands/test_look_container.py`
- **_T** (1 connections)
- **Find a wearable container in equipped items by name or prototype_id. Args:…** (1 connections) — `server/commands/look_container.py`
- **Pick a single match by instance number, or the sole match when unambiguous.** (1 connections) — `server/commands/look_container.py`
- **Test _find_container_wearable() with empty dict.** (1 connections) — `server/tests/unit/commands/test_look_container_helpers.py`
- **Test _find_container_wearable() with no matching containers.** (1 connections) — `server/tests/unit/commands/test_look_container_helpers.py`
- **Test _find_container_wearable() with multiple matches (ambiguous).** (1 connections) — `server/tests/unit/commands/test_look_container_helpers.py`
- **Test _find_container_wearable() with instance number.** (1 connections) — `server/tests/unit/commands/test_look_container_helpers.py`
- **Test _find_container_wearable() with instance number out of range.** (1 connections) — `server/tests/unit/commands/test_look_container_helpers.py`
- **Test _find_container_wearable() finds wearable container.** (1 connections) — `server/tests/unit/commands/test_look_container_helpers.py`
- **Test _find_container_wearable() returns None when container not found.** (1 connections) — `server/tests/unit/commands/test_look_container_helpers.py`
- *... and 2 more nodes in this community*

## Relationships

- [errorHandler.ts](errorHandler.ts.md) (10 shared connections)
- [talk_command.py](talk_command.py.md) (9 shared connections)
- [ClientLogger](ClientLogger.md) (6 shared connections)

## Source Files

- `server/commands/look_container.py`
- `server/tests/unit/commands/test_look_container.py`
- `server/tests/unit/commands/test_look_container_helpers.py`

## Audit Trail

- EXTRACTED: 52 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*