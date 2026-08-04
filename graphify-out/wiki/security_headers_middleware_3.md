# security headers middleware

> 6 nodes

## Key Concepts

- **_row_fetchall()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_get_explored_rooms()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_get_explored_rooms_empty()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **SQLAlchemy-style result mock with fetchall() -> rows.** (1 connections) — `server/tests/unit/services/test_exploration_service.py`
- **Test get_explored_rooms() returns list of explored room IDs.** (1 connections) — `server/tests/unit/services/test_exploration_service.py`
- **Test get_explored_rooms() returns empty list when no explored rooms.** (1 connections) — `server/tests/unit/services/test_exploration_service.py`

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