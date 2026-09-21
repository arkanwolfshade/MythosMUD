# test_database_extended.py

> 62 nodes

## Key Concepts

- **test_database_extended.py** (43 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **get_database_path()** (12 connections) — `server/database.py`
- **asyncio** (12 connections)
- **init_db()** (10 connections) — `server/database.py`
- **get_engine()** (9 connections) — `server/database.py`
- **close_db()** (6 connections) — `server/database.py`
- **get_database_url()** (6 connections) — `server/database.py`
- **test_database_manager_close_dispose_error()** (6 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_close_with_engine()** (6 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_close_without_engine()** (6 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_database_path_none_url()** (6 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **.get_database_path()** (5 connections) — `server/database.py`
- **test_get_database_url_initializes_database()** (5 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_engine_initializes_database()** (5 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_session_maker_initializes_database()** (5 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_database_path_module_level_none()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_get_database_path_module_level_postgresql()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_get_database_path_module_level_unsupported()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **ensure_database_directory()** (4 connections) — `server/database.py`
- **test_close_db_error()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_close_db_success()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_async_session_http_exception_re_raised()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_async_session_rollback_error()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_async_session_rollback_on_error()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_async_session_success()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- *... and 37 more nodes in this community*

## Relationships

- [.get_instance](get_instance.md) (33 shared connections)
- [DatabaseManager](DatabaseManager.md) (13 shared connections)
- [DatabaseError](DatabaseError.md) (10 shared connections)
- [get_async_session](get_async_session.md) (5 shared connections)
- [ValidationError](ValidationError.md) (3 shared connections)
- [collect_idle_memory_sample](collect_idle_memory_sample.md) (1 shared connections)
- [connection_manager.py](connection_manager.py.md) (1 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (1 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/database.py`
- `server/tests/unit/infrastructure/test_database_extended.py`
- `server/tests/unit/infrastructure/test_database_init.py`

## Audit Trail

- EXTRACTED: 143 (93%)
- INFERRED: 11 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*