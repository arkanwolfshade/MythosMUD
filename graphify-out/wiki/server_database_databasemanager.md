# server database databasemanager

> 69 nodes

## Key Concepts

- **DatabaseManager** (113 connections) — `server/database.py`
- **.get_instance()** (88 connections) — `server/database.py`
- **test_database_init.py** (37 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_database.py** (8 connections) — `server/tests/unit/infrastructure/test_database.py`
- **test_initialize_database_connection_error()** (6 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_initialize_database_generic_exception()** (6 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_initialize_database_os_error()** (6 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_get_database_path_none_url_raises()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_get_database_path_postgresql_returns_none()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_get_database_path_unsupported_raises()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_get_engine_handles_no_running_loop()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_get_engine_reinitializes_if_none()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_initialize_database_config_runtime_error()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_initialize_database_config_validation_error()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_initialize_database_converts_postgresql_url()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_initialize_database_import_error()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_initialize_database_keeps_asyncpg_url()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_initialize_database_none_url()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_initialize_database_sets_creation_loop_id()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_initialize_database_sets_creation_loop_id_none()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_initialize_database_skip_if_already_initialized()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_initialize_database_type_error()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_initialize_database_unsupported_url()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_initialize_database_uses_module_level_url()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_initialize_database_uses_nullpool_for_test()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- *... and 44 more nodes in this community*

## Relationships

- [server database databasemanager reset instance](server_database_databasemanager_reset_instance.md) (90 shared connections)
- [server database close db](server_database_close_db.md) (28 shared connections)
- [server database helpers close db](server_database_helpers_close_db.md) (13 shared connections)
- [server database databasemanager get database](server_database_databasemanager_get_database.md) (12 shared connections)
- [server database helpers rationale 26](server_database_helpers_rationale_26.md) (11 shared connections)
- [e2e tests load tests get](e2e_tests_load_tests_get.md) (6 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (5 shared connections)
- [server database helpers get database](server_database_helpers_get_database.md) (4 shared connections)
- [scripts populate test npc databases](scripts_populate_test_npc_databases.md) (4 shared connections)
- [server container bundles chat](server_container_bundles_chat.md) (3 shared connections)
- [characterinfo](characterinfo.md) (2 shared connections)
- [maprooms](maprooms.md) (1 shared connections)

## Source Files

- `server/database.py`
- `server/tests/unit/infrastructure/test_database.py`
- `server/tests/unit/infrastructure/test_database_init.py`

## Audit Trail

- EXTRACTED: 209 (68%)
- INFERRED: 97 (32%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*