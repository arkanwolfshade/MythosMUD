# server database close db

> 57 nodes

## Key Concepts

- **test_database_extended.py** (44 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **asyncio** (12 connections)
- **init_db()** (10 connections) — `server/database.py`
- **get_engine()** (7 connections) — `server/database.py`
- **close_db()** (6 connections) — `server/database.py`
- **test_database_manager_close_dispose_error()** (6 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_close_with_engine()** (6 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_close_without_engine()** (6 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_get_database_path_unsupported()** (6 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_get_database_path_postgresql()** (5 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_get_database_url_initializes()** (5 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_get_engine_event_loop_check()** (5 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_get_engine_initializes()** (5 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_get_engine_no_running_loop()** (5 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_get_engine_reinitializes_if_none()** (5 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_get_session_maker_initializes()** (5 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_engine_initializes_database()** (5 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_session_maker_initializes_database()** (5 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **ensure_database_directory()** (4 connections) — `server/database.py`
- **test_close_db_error()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_close_db_success()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_async_session_http_exception_re_raised()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_async_session_rollback_error()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_async_session_rollback_on_error()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_async_session_success()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- *... and 32 more nodes in this community*

## Relationships

- [server database databasemanager](server_database_databasemanager.md) (28 shared connections)
- [server database databasemanager reset instance](server_database_databasemanager_reset_instance.md) (13 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (6 shared connections)
- [server database databasemanager get database](server_database_databasemanager_get_database.md) (6 shared connections)
- [scripts add flavor text column](scripts_add_flavor_text_column.md) (5 shared connections)
- [e2e tests load tests get](e2e_tests_load_tests_get.md) (3 shared connections)
- [server database helpers rationale 26](server_database_helpers_rationale_26.md) (3 shared connections)
- [server container bundles chat](server_container_bundles_chat.md) (2 shared connections)
- [server exceptions rationale 179](server_exceptions_rationale_179.md) (2 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/database.py`
- `server/tests/unit/infrastructure/test_database_extended.py`

## Audit Trail

- EXTRACTED: 130 (90%)
- INFERRED: 14 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*