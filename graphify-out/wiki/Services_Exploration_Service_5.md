# Services Exploration Service

> 8 nodes · cohesion 0.25

## Key Concepts

- **_async_session_maker_mock()** (5 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_get_room_uuid_by_stable_id_no_session()** (5 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_mark_room_as_explored_commits_session()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_mark_room_as_explored_no_session()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **Test _get_room_uuid_by_stable_id() creates session when none provided.** (1 connections) — `server/tests/unit/services/test_exploration_service.py`
- **Async context manager returned by get_session_maker() -> maker() in tests.** (1 connections) — `server/tests/unit/services/test_exploration_service.py`
- **Test mark_room_as_explored() commits session when creating new session.** (1 connections) — `server/tests/unit/services/test_exploration_service.py`
- **Test mark_room_as_explored() creates new session when none provided.** (1 connections) — `server/tests/unit/services/test_exploration_service.py`

## Relationships

- [[Services Exploration Service]] (8 shared connections)

## Source Files

- `server/tests/unit/services/test_exploration_service.py`

## Audit Trail

- EXTRACTED: 22 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
