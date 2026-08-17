# server database databasemanager reset instance

> 67 nodes

## Key Concepts

- **.reset_instance()** (87 connections) — `server/database.py`
- **test_database_error_handling.py** (43 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_close_handles_attribute_error_during_dispose()** (7 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **asyncio** (7 connections)
- **test_close_handles_closed_event_loop()** (6 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_close_handles_dispose_timeout()** (6 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_close_handles_generic_exception_during_dispose()** (6 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_close_handles_no_running_loop()** (6 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_close_handles_none_engine()** (6 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_close_handles_runtime_error_during_dispose()** (6 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_get_database_path_none_url_raises()** (6 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_get_database_path_unsupported_raises()** (6 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_initialize_database_config_runtime_error()** (6 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_initialize_database_config_validation_error()** (6 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_initialize_database_connection_error()** (6 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_initialize_database_generic_exception()** (6 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_initialize_database_none_url()** (6 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_initialize_database_os_error()** (6 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_initialize_database_type_error()** (6 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_initialize_database_unsupported_url()** (6 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_initialize_database_value_error()** (6 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_database_manager_init_raises_when_instance_exists()** (5 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_get_database_path_postgresql_returns_none()** (5 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_get_database_url_not_initialized()** (5 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_get_engine_event_loop_changed()** (5 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- *... and 42 more nodes in this community*

## Relationships

- [server database databasemanager](server_database_databasemanager.md) (90 shared connections)
- [server database close db](server_database_close_db.md) (13 shared connections)
- [server exceptions rationale 179](server_exceptions_rationale_179.md) (9 shared connections)
- [server database helpers rationale 26](server_database_helpers_rationale_26.md) (8 shared connections)
- [server database databasemanager get database](server_database_databasemanager_get_database.md) (5 shared connections)
- [server database helpers close db](server_database_helpers_close_db.md) (4 shared connections)
- [scripts populate test npc databases](scripts_populate_test_npc_databases.md) (4 shared connections)
- [server database helpers get database](server_database_helpers_get_database.md) (2 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [attributeerror](attributeerror.md) (1 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (1 shared connections)

## Source Files

- `server/database.py`
- `server/tests/unit/infrastructure/test_database_error_handling.py`

## Audit Trail

- EXTRACTED: 199 (82%)
- INFERRED: 43 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*