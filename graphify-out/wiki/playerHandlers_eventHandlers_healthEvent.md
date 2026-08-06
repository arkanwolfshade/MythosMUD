# playerHandlers eventHandlers healthEvent

> 24 nodes

## Key Concepts

- **_row_scalar_one_or_none()** (10 connections) — `server/tests/unit/services/test_exploration_service.py`
- **_async_session_maker_mock()** (5 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_get_room_uuid_by_stable_id_no_session()** (5 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_mark_room_as_explored_no_session()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_get_room_uuid_by_stable_id_with_session()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_get_room_uuid_by_stable_id_not_found()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_get_room_uuid_by_stable_id_string_uuid()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_get_room_uuid_by_stable_id_asyncpg_like_uuid_object()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_mark_explored_in_session_new_record()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_mark_explored_in_session_existing_record()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_get_room_uuid_by_stable_id_asyncpg_uuid()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_mark_room_as_explored_commits_session()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **SQLAlchemy-style result mock with scalar_one_or_none() -> value.** (1 connections) — `server/tests/unit/services/test_exploration_service.py`
- **Async context manager returned by get_session_maker() -> maker() in tests.** (1 connections) — `server/tests/unit/services/test_exploration_service.py`
- **Test mark_room_as_explored() creates new session when none provided.** (1 connections) — `server/tests/unit/services/test_exploration_service.py`
- **Test _get_room_uuid_by_stable_id() with provided session.** (1 connections) — `server/tests/unit/services/test_exploration_service.py`
- **Test _get_room_uuid_by_stable_id() creates session when none provided.** (1 connections) — `server/tests/unit/services/test_exploration_service.py`
- **Test _get_room_uuid_by_stable_id() returns None when room not found.** (1 connections) — `server/tests/unit/services/test_exploration_service.py`
- **Test _get_room_uuid_by_stable_id() handles string UUID from database.** (1 connections) — `server/tests/unit/services/test_exploration_service.py`
- **DB drivers may return non-stdlib UUID; conversion via str() must yield stdlib UU** (1 connections) — `server/tests/unit/services/test_exploration_service.py`
- **Test _mark_explored_in_session() inserts new exploration record.** (1 connections) — `server/tests/unit/services/test_exploration_service.py`
- **Test _mark_explored_in_session() returns True for existing record.** (1 connections) — `server/tests/unit/services/test_exploration_service.py`
- **Test _get_room_uuid_by_stable_id() handles asyncpg UUID objects.** (1 connections) — `server/tests/unit/services/test_exploration_service.py`
- **Test mark_room_as_explored() commits session when creating new session.** (1 connections) — `server/tests/unit/services/test_exploration_service.py`

## Relationships

- [corpse lifecycle service](corpse_lifecycle_service.md) (12 shared connections)
- [maps handle ascii](maps_handle_ascii.md) (10 shared connections)

## Source Files

- `server/tests/unit/services/test_exploration_service.py`

## Audit Trail

- EXTRACTED: 68 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*