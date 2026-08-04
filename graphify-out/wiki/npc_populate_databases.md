# npc populate databases

> 6 nodes

## Key Concepts

- **_row_scalar_one()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_is_room_explored_true()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_is_room_explored_false()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **SQLAlchemy-style result mock with scalar_one() -> value.** (1 connections) — `server/tests/unit/services/test_exploration_service.py`
- **Test is_room_explored() returns True when room is explored.** (1 connections) — `server/tests/unit/services/test_exploration_service.py`
- **Test is_room_explored() returns False when room is not explored.** (1 connections) — `server/tests/unit/services/test_exploration_service.py`

## Relationships

- [Loot Generation](Loot_Generation.md) (3 shared connections)
- [maps handle ascii](maps_handle_ascii.md) (2 shared connections)

## Source Files

- `server/tests/unit/services/test_exploration_service.py`

## Audit Trail

- EXTRACTED: 15 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*