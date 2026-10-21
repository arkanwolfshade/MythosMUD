# E2E Test Suite AI Execution Improvements - Summary

> 12 nodes · cohesion 0.41

## Key Concepts

- **test_combat_guard.py** (15 connections) — `server/tests/unit/models/test_combat_guard.py`
- **_fight()** (11 connections) — `server/tests/unit/models/test_combat_guard.py`
- **_player()** (10 connections) — `server/tests/unit/models/test_combat_guard.py`
- **test_a_protector_covers_one_ally_and_the_latest_wins()** (3 connections) — `server/tests/unit/models/test_combat_guard.py`
- **test_an_ally_has_one_protector_and_the_latest_wins()** (3 connections) — `server/tests/unit/models/test_combat_guard.py`
- **test_cover_ends_when_the_ally_leaves_the_fight()** (3 connections) — `server/tests/unit/models/test_combat_guard.py`
- **test_cover_ends_when_the_protector_drops_to_zero_dp()** (3 connections) — `server/tests/unit/models/test_combat_guard.py`
- **test_cover_ends_when_the_protector_leaves_the_fight()** (3 connections) — `server/tests/unit/models/test_combat_guard.py`
- **test_cover_holds_through_its_last_round_then_lapses()** (3 connections) — `server/tests/unit/models/test_combat_guard.py`
- **test_no_guard_by_default()** (3 connections) — `server/tests/unit/models/test_combat_guard.py`
- **test_set_guard_covers_the_ally_and_marks_the_protector()** (3 connections) — `server/tests/unit/models/test_combat_guard.py`
- **#991: Protect cover is checked on read, so it lapses on its own and needs no…** (1 connections) — `server/tests/unit/models/test_combat_guard.py`

## Relationships

- [DatabaseManager](DatabaseManager.md) (3 shared connections)
- [test_player_combat_service.py](test_player_combat_service.py.md) (2 shared connections)
- [InventorySchemaValidationError](InventorySchemaValidationError.md) (2 shared connections)

## Source Files

- `server/tests/unit/models/test_combat_guard.py`

## Audit Trail

- EXTRACTED: 34 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*