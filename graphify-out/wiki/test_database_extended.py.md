# test_database_extended.py

> 63 nodes

## Key Concepts

- **test_database_extended.py** (44 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **get_database_path()** (12 connections) — `server/database.py`
- **asyncio** (12 connections)
- **init_db()** (10 connections) — `server/database.py`
- **get_engine()** (7 connections) — `server/database.py`
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
- **.get_engine()** (4 connections) — `server/database.py`
- **_dispose_engine_safely()** (4 connections) — `server/database.py`
- **ensure_database_directory()** (4 connections) — `server/database.py`
- **test_close_db_error()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_close_db_success()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_async_session_http_exception_re_raised()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_async_session_rollback_error()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_async_session_rollback_on_error()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_async_session_success()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_database_path_unsupported()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- *... and 38 more nodes in this community*

## Relationships

- [DatabaseManager](DatabaseManager.md) (41 shared connections)
- [get_session_maker](get_session_maker.md) (15 shared connections)
- [ValidationError](ValidationError.md) (4 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (2 shared connections)
- [log_and_raise](log_and_raise.md) (1 shared connections)
- [database_config_helpers.py](database_config_helpers.py.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [DatabaseError](DatabaseError.md) (1 shared connections)

## Source Files

- `server/database.py`
- `server/tests/unit/infrastructure/test_database_extended.py`

## Audit Trail

- EXTRACTED: 143 (94%)
- INFERRED: 9 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*