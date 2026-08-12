# test_database_extended.py

> 52 nodes

## Key Concepts

- **test_database_extended.py** (43 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **asyncio** (12 connections)
- **init_db()** (10 connections) — `server/database.py`
- **get_engine()** (7 connections) — `server/database.py`
- **close_db()** (6 connections) — `server/database.py`
- **get_database_url()** (6 connections) — `server/database.py`
- **.get_database_path()** (5 connections) — `server/database.py`
- **test_database_manager_close_dispose_error()** (5 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_close_with_engine()** (5 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_close_without_engine()** (5 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **ensure_database_directory()** (4 connections) — `server/database.py`
- **test_close_db_error()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_close_db_success()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_async_session_http_exception_re_raised()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_async_session_rollback_error()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_async_session_rollback_on_error()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_async_session_success()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_database_url_initializes_database()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_engine_initializes_database()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_session_maker_initializes_database()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_init_db_connection_error()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_init_db_import_error()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_init_db_success()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_ensure_database_directory_postgresql()** (3 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_database_path_postgresql()** (3 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- *... and 27 more nodes in this community*

## Relationships

- [.get_instance](get_instance.md) (29 shared connections)
- [database.py](database.py.md) (11 shared connections)
- [log_and_raise](log_and_raise.md) (3 shared connections)
- [DatabaseManager](DatabaseManager.md) (3 shared connections)
- [bundles/game.py](bundles-game.py.md) (2 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (2 shared connections)

## Source Files

- `server/database.py`
- `server/tests/unit/infrastructure/test_database_extended.py`

## Audit Trail

- EXTRACTED: 192 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*