# server database databasemanager get instance

> 51 nodes

## Key Concepts

- **.get_instance()** (88 connections) — `server/database.py`
- **test_database_init.py** (37 connections) — `server/tests/unit/infrastructure/test_database_init.py`
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
- **test_initialize_database_uses_pool_config_for_production()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_initialize_database_value_error()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- *... and 26 more nodes in this community*

## Relationships

- [server database databasemanager](server_database_databasemanager.md) (81 shared connections)
- [server database close db](server_database_close_db.md) (14 shared connections)
- [claude rules sqlalchemy](claude_rules_sqlalchemy.md) (8 shared connections)
- [server database databasemanager get database](server_database_databasemanager_get_database.md) (6 shared connections)
- [server database helpers rationale 26](server_database_helpers_rationale_26.md) (6 shared connections)
- [server tests unit infrastructure test](server_tests_unit_infrastructure_test.md) (4 shared connections)
- [server database helpers close db](server_database_helpers_close_db.md) (3 shared connections)
- [server app lifespan startup legacy](server_app_lifespan_startup_legacy.md) (1 shared connections)
- [server database helpers get database](server_database_helpers_get_database.md) (1 shared connections)
- [server services exploration service explorationservice](server_services_exploration_service_explorationservice.md) (1 shared connections)
- [claude rules pytest](claude_rules_pytest.md) (1 shared connections)

## Source Files

- `server/database.py`
- `server/tests/unit/infrastructure/test_database_init.py`

## Audit Trail

- EXTRACTED: 173 (86%)
- INFERRED: 27 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*