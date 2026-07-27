# Services Exploration Service

> 16 nodes · cohesion 0.13

## Key Concepts

- **ExplorationService** (37 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_mark_room_as_explored_sync_no_loop()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_exploration_service_init()** (3 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_get_explored_rooms_async_fetchall()** (3 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_get_room_uuid_by_stable_id_database_error()** (3 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_is_room_explored_database_error()** (3 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_is_room_explored_database_error_in_query()** (3 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_is_room_explored_generic_exception()** (3 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_mark_room_as_explored_sync_with_loop()** (3 connections) — `server/tests/unit/services/test_exploration_service.py`
- **Test is_room_explored() raises DatabaseError on database failure.** (2 connections) — `server/tests/unit/services/test_exploration_service.py`
- **Test mark_room_as_explored_sync() schedules task when loop is running.** (1 connections) — `server/tests/unit/services/test_exploration_service.py`
- **Test mark_room_as_explored_sync() handles no running loop gracefully.** (1 connections) — `server/tests/unit/services/test_exploration_service.py`
- **Test _get_room_uuid_by_stable_id() raises DatabaseError on SQLAlchemyError.** (1 connections) — `server/tests/unit/services/test_exploration_service.py`
- **Test get_explored_rooms() handles async fetchall() result.** (1 connections) — `server/tests/unit/services/test_exploration_service.py`
- **Test is_room_explored() raises generic exception.** (1 connections) — `server/tests/unit/services/test_exploration_service.py`
- **Test ExplorationService initialization.** (1 connections) — `server/tests/unit/services/test_exploration_service.py`

## Relationships

- [[Services Exploration Service]] (36 shared connections)
- [[NPC Admin API]] (1 shared connections)
- [[Database Manager Tests]] (1 shared connections)

## Source Files

- `server/tests/unit/services/test_exploration_service.py`

## Audit Trail

- EXTRACTED: 67 (96%)
- INFERRED: 3 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
