# test_database_helpers.py

> 81 nodes

## Key Concepts

- **test_database_helpers.py** (46 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **get_database_path()** (17 connections) — `server/database_helpers.py`
- **asyncio** (14 connections)
- **get_async_session()** (12 connections) — `server/database_helpers.py`
- **get_session_maker()** (10 connections) — `server/database_helpers.py`
- **get_engine()** (9 connections) — `server/database_helpers.py`
- **close_db()** (8 connections) — `server/database_helpers.py`
- **init_db()** (8 connections) — `server/database_helpers.py`
- **get_database_url()** (7 connections) — `server/database_helpers.py`
- **ensure_database_directory()** (6 connections) — `server/database_helpers.py`
- **test_get_engine_raises_validation_error()** (6 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_session_maker_raises_validation_error()** (6 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_close_db_engine_initialization_failure()** (5 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_database_url()** (5 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_database_url_returns_none()** (5 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_engine()** (5 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_session_maker()** (5 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_close_db_raises_runtime_error_on_failure()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_close_db_success()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_async_session_finally_block_executes()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_async_session_http_exception_passthrough()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_async_session_http_exception_propagates()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_async_session_rollback_failure()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_async_session_rollback_on_error()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_async_session_rollback_success()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- *... and 56 more nodes in this community*

## Relationships

- [DatabaseManager](DatabaseManager.md) (23 shared connections)
- [get_logger](get_logger.md) (20 shared connections)
- [reset_database](reset_database.md) (3 shared connections)

## Source Files

- `server/database_helpers.py`
- `server/tests/unit/infrastructure/test_database_helpers.py`

## Audit Trail

- EXTRACTED: 158 (92%)
- INFERRED: 14 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*