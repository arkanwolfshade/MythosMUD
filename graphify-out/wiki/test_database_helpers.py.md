# test_database_helpers.py

> 63 nodes

## Key Concepts

- **test_database_helpers.py** (46 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **asyncio** (14 connections)
- **get_async_session()** (12 connections) — `server/database_helpers.py`
- **get_session_maker()** (9 connections) — `server/database_helpers.py`
- **init_db()** (8 connections) — `server/database_helpers.py`
- **close_db()** (7 connections) — `server/database_helpers.py`
- **test_close_db_engine_initialization_failure()** (5 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_session_maker_raises_validation_error()** (5 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_close_db_raises_runtime_error_on_failure()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_close_db_success()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_async_session_finally_block_executes()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_async_session_http_exception_passthrough()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_async_session_http_exception_propagates()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_async_session_rollback_failure()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_async_session_rollback_on_error()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_async_session_rollback_success()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_async_session_success()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_session_maker()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_init_db_configure_mappers_failure()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_init_db_connection_verification_failure()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_init_db_raises_on_error()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_init_db_success()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_ensure_database_directory_creates_directory()** (3 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_ensure_database_directory_no_op_for_postgresql()** (3 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_database_path_empty_string_url_raises()** (3 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- *... and 38 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (23 shared connections)
- [.get_instance](get_instance.md) (5 shared connections)
- [get_engine](get_engine.md) (4 shared connections)
- [get_database_url](get_database_url.md) (3 shared connections)
- [reset_db](reset_db.md) (1 shared connections)

## Source Files

- `server/database_helpers.py`
- `server/tests/unit/infrastructure/test_database_helpers.py`

## Audit Trail

- EXTRACTED: 129 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*