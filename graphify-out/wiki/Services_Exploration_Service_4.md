# Services Exploration Service

> 15 nodes · cohesion 0.13

## Key Concepts

- **_row_scalar_one_or_none()** (10 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_get_room_uuid_by_stable_id_asyncpg_like_uuid_object()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_get_room_uuid_by_stable_id_asyncpg_uuid()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_get_room_uuid_by_stable_id_not_found()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_get_room_uuid_by_stable_id_string_uuid()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_get_room_uuid_by_stable_id_with_session()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_mark_explored_in_session_existing_record()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_mark_explored_in_session_new_record()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **Test _get_room_uuid_by_stable_id() with provided session.** (1 connections) — `server/tests/unit/services/test_exploration_service.py`
- **Test _get_room_uuid_by_stable_id() returns None when room not found.** (1 connections) — `server/tests/unit/services/test_exploration_service.py`
- **Test _get_room_uuid_by_stable_id() handles string UUID from database.** (1 connections) — `server/tests/unit/services/test_exploration_service.py`
- **DB drivers may return non-stdlib UUID; conversion via str() must yield stdlib UU** (1 connections) — `server/tests/unit/services/test_exploration_service.py`
- **Test _mark_explored_in_session() inserts new exploration record.** (1 connections) — `server/tests/unit/services/test_exploration_service.py`
- **Test _mark_explored_in_session() returns True for existing record.** (1 connections) — `server/tests/unit/services/test_exploration_service.py`
- **Test _get_room_uuid_by_stable_id() handles asyncpg UUID objects.** (1 connections) — `server/tests/unit/services/test_exploration_service.py`

## Relationships

- [[Services Exploration Service]] (17 shared connections)

## Source Files

- `server/tests/unit/services/test_exploration_service.py`

## Audit Trail

- EXTRACTED: 45 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
