# server database helpers close db

> 74 nodes

## Key Concepts

- **test_database_helpers.py** (48 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **get_database_path()** (17 connections) — `server/database_helpers.py`
- **asyncio** (14 connections)
- **get_async_session()** (12 connections) — `server/database_helpers.py`
- **get_session_maker()** (10 connections) — `server/database_helpers.py`
- **get_engine()** (9 connections) — `server/database_helpers.py`
- **close_db()** (8 connections) — `server/database_helpers.py`
- **init_db()** (8 connections) — `server/database_helpers.py`
- **ensure_database_directory()** (6 connections) — `server/database_helpers.py`
- **test_get_engine_raises_validation_error()** (6 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_session_maker_raises_validation_error()** (6 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_close_db_engine_initialization_failure()** (5 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
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
- **test_get_async_session_success()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_database_path_empty_string_url_raises()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_database_path_unsupported_url_raises()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- *... and 49 more nodes in this community*

## Relationships

- [server database databasemanager](server_database_databasemanager.md) (13 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (12 shared connections)
- [server exceptions rationale 179](server_exceptions_rationale_179.md) (7 shared connections)
- [server database databasemanager reset instance](server_database_databasemanager_reset_instance.md) (4 shared connections)
- [server database helpers get database](server_database_helpers_get_database.md) (3 shared connections)
- [server database helpers rationale 26](server_database_helpers_rationale_26.md) (3 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (1 shared connections)

## Source Files

- `server/database_helpers.py`
- `server/tests/unit/infrastructure/test_database_helpers.py`

## Audit Trail

- EXTRACTED: 148 (91%)
- INFERRED: 14 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*