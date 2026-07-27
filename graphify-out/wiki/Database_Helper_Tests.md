# Database Helper Tests

> 71 nodes · cohesion 0.04

## Key Concepts

- **test_database_helpers.py** (46 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **get_async_session()** (12 connections) — `server/database_helpers.py`
- **close_db()** (8 connections) — `server/database_helpers.py`
- **get_engine()** (8 connections) — `server/database_helpers.py`
- **init_db()** (8 connections) — `server/database_helpers.py`
- **ensure_database_directory()** (6 connections) — `server/database_helpers.py`
- **get_database_url()** (5 connections) — `server/database_helpers.py`
- **test_close_db_engine_initialization_failure()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_async_session_rollback_failure()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_engine_raises_validation_error()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_session_maker_raises_validation_error()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_init_db_configure_mappers_failure()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_init_db_connection_verification_failure()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_init_db_raises_on_error()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **Test get_async_session rolls back on exception.** (3 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **reset_db()** (3 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_close_db_raises_runtime_error_on_failure()** (3 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_close_db_success()** (3 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_ensure_database_directory_creates_directory()** (3 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_ensure_database_directory_no_op_for_postgresql()** (3 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_async_session_finally_block_executes()** (3 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_async_session_http_exception_passthrough()** (3 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_async_session_http_exception_propagates()** (3 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_async_session_rollback_on_error()** (3 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_async_session_rollback_success()** (3 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- *... and 46 more nodes in this community*

## Relationships

- [[NPC Admin API]] (28 shared connections)
- [[Lucidity Database Models]] (6 shared connections)
- [[Database Manager Tests]] (5 shared connections)
- [[NPC Database Sessions]] (3 shared connections)

## Source Files

- `server/database.py`
- `server/database_helpers.py`
- `server/npc_database.py`
- `server/tests/unit/infrastructure/test_database_helpers.py`

## Audit Trail

- EXTRACTED: 221 (98%)
- INFERRED: 5 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
