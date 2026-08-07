# corpse lifecycle service

> 28 nodes

## Key Concepts

- **test_exploration_service.py** (45 connections) — `server/tests/unit/services/test_exploration_service.py`
- **_row_scalar_one()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **_row_fetchall()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_mark_room_as_explored_database_error()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_get_explored_rooms()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_get_explored_rooms_empty()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_get_explored_rooms_database_error()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_is_room_explored_true()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_is_room_explored_false()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_is_room_explored_database_error()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_mark_room_as_explored_sync_with_error_handler()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_get_room_uuid_by_stable_id_database_error()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_is_room_explored_database_error_in_query()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **mock_database_manager()** (2 connections) — `server/tests/unit/services/test_exploration_service.py`
- **Unit tests for exploration service.  Tests the ExplorationService class.** (1 connections) — `server/tests/unit/services/test_exploration_service.py`
- **SQLAlchemy-style result mock with scalar_one() -> value.** (1 connections) — `server/tests/unit/services/test_exploration_service.py`
- **SQLAlchemy-style result mock with fetchall() -> rows.** (1 connections) — `server/tests/unit/services/test_exploration_service.py`
- **Create a mock database manager.** (1 connections) — `server/tests/unit/services/test_exploration_service.py`
- **Test mark_room_as_explored() raises DatabaseError on database failure.** (1 connections) — `server/tests/unit/services/test_exploration_service.py`
- **Test get_explored_rooms() returns list of explored room IDs.** (1 connections) — `server/tests/unit/services/test_exploration_service.py`
- **Test get_explored_rooms() returns empty list when no explored rooms.** (1 connections) — `server/tests/unit/services/test_exploration_service.py`
- **Test get_explored_rooms() raises DatabaseError on database failure.** (1 connections) — `server/tests/unit/services/test_exploration_service.py`
- **Test is_room_explored() returns True when room is explored.** (1 connections) — `server/tests/unit/services/test_exploration_service.py`
- **Test is_room_explored() returns False when room is not explored.** (1 connections) — `server/tests/unit/services/test_exploration_service.py`
- **Test is_room_explored() raises DatabaseError on database failure.** (1 connections) — `server/tests/unit/services/test_exploration_service.py`
- *... and 3 more nodes in this community*

## Relationships

- [maps handle ascii](maps_handle_ascii.md) (27 shared connections)
- [playerHandlers eventHandlers healthEvent](playerHandlers_eventHandlers_healthEvent.md) (12 shared connections)
- [endpoints auth rationale](endpoints_auth_rationale.md) (7 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_exploration_service.py`

## Audit Trail

- EXTRACTED: 104 (95%)
- INFERRED: 5 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*