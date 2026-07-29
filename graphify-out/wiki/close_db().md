# close db()

> 59 nodes

## Key Concepts

- **test_database_extended.py** (43 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **init_db()** (11 connections) — `server/database.py`
- **close_db()** (9 connections) — `server/database.py`
- **get_engine()** (8 connections) — `server/database.py`
- **get_database_url()** (6 connections) — `server/database.py`
- **test_get_engine_initializes_database()** (5 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_get_database_path_unsupported()** (5 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_session_maker_initializes_database()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_database_url_initializes_database()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_get_engine_initializes()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_get_engine_reinitializes_if_none()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_get_session_maker_initializes()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_get_database_url_initializes()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_get_database_path_postgresql()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_close_with_engine()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_close_without_engine()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_close_dispose_error()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_get_engine_event_loop_check()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_get_engine_no_running_loop()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **.close()** (3 connections) — `server/database.py`
- **test_get_async_session_success()** (3 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_async_session_http_exception_re_raised()** (3 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_async_session_rollback_on_error()** (3 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_async_session_rollback_error()** (3 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_init_db_success()** (3 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- *... and 34 more nodes in this community*

## Relationships

- [main()](main%28%29.md) (19 shared connections)
- [.get instance()](get_instance%28%29.md) (15 shared connections)
- [.reset instance()](reset_instance%28%29.md) (14 shared connections)
- [. init ()](_init_%28%29.md) (7 shared connections)
- [Reset database state before each](Reset_database_state_before_each.md) (3 shared connections)
- [.initialize()](initialize%28%29.md) (2 shared connections)
- [ensure database directory()](ensure_database_directory%28%29.md) (2 shared connections)

## Source Files

- `server/database.py`
- `server/tests/unit/infrastructure/test_database_extended.py`

## Audit Trail

- EXTRACTED: 195 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*