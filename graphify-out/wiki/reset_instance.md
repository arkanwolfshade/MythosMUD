# .reset_instance

> 75 nodes

## Key Concepts

- **.reset_instance()** (87 connections) — `server/database.py`
- **test_database_error_handling.py** (41 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **asyncio** (7 connections)
- **test_close_handles_attribute_error_during_dispose()** (6 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_close_handles_closed_event_loop()** (5 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_close_handles_dispose_timeout()** (5 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_close_handles_generic_exception_during_dispose()** (5 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_close_handles_no_running_loop()** (5 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_close_handles_none_engine()** (5 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_close_handles_runtime_error_during_dispose()** (5 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_reset_database_resets_singleton()** (5 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_get_database_path_none_url_raises()** (4 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_get_database_path_postgresql_returns_none()** (4 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_get_database_path_unsupported_raises()** (4 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_get_database_url_not_initialized()** (4 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_get_engine_event_loop_changed()** (4 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_get_engine_no_running_loop()** (4 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_get_engine_reinitializes_if_none()** (4 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_get_session_maker_not_initialized()** (4 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_initialize_database_config_runtime_error()** (4 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_initialize_database_config_validation_error()** (4 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_initialize_database_connection_error()** (4 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_initialize_database_converts_postgresql_url()** (4 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_initialize_database_generic_exception()** (4 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_initialize_database_keeps_asyncpg_url()** (4 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- *... and 50 more nodes in this community*

## Relationships

- [.get_instance](get_instance.md) (62 shared connections)
- [DatabaseManager](DatabaseManager.md) (7 shared connections)
- [get_async_session](get_async_session.md) (7 shared connections)
- [reset_database](reset_database.md) (6 shared connections)
- [test_database_helpers.py](test_database_helpers.py.md) (6 shared connections)
- [get_database_path](get_database_path.md) (4 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (3 shared connections)
- [DatabaseError](DatabaseError.md) (3 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (1 shared connections)
- [AttributeError](AttributeError.md) (1 shared connections)
- [get_session_maker](get_session_maker.md) (1 shared connections)

## Source Files

- `server/database.py`
- `server/tests/unit/infrastructure/test_database_error_handling.py`
- `server/tests/unit/infrastructure/test_database_extended.py`

## Audit Trail

- EXTRACTED: 210 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*