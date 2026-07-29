# .reset instance()

> 62 nodes

## Key Concepts

- **.reset_instance()** (87 connections) — `server/database.py`
- **test_database_error_handling.py** (41 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_database_manager_init_raises_when_instance_exists()** (5 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_initialize_database_config_validation_error()** (5 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_initialize_database_config_runtime_error()** (5 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_initialize_database_none_url()** (5 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_initialize_database_unsupported_url()** (5 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_initialize_database_value_error()** (5 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_initialize_database_type_error()** (5 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_initialize_database_connection_error()** (5 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_initialize_database_os_error()** (5 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_initialize_database_generic_exception()** (5 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_get_database_path_unsupported_raises()** (5 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_get_database_path_none_url_raises()** (5 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_close_handles_attribute_error_during_dispose()** (5 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_initialize_database_skips_if_already_initialized()** (4 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_initialize_database_converts_postgresql_url()** (4 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_initialize_database_keeps_asyncpg_url()** (4 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_initialize_database_uses_nullpool_for_test()** (4 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_initialize_database_uses_pool_config_for_production()** (4 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_initialize_database_uses_module_level_url()** (4 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_get_engine_reinitializes_if_none()** (4 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_get_engine_event_loop_changed()** (4 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_get_engine_no_running_loop()** (4 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_get_session_maker_not_initialized()** (4 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- *... and 37 more nodes in this community*

## Relationships

- [.get instance()](get_instance%28%29.md) (55 shared connections)
- [close db()](close_db%28%29.md) (20 shared connections)
- [. init ()](_init_%28%29.md) (12 shared connections)
- [main()](main%28%29.md) (10 shared connections)
- [Reset database state before each](Reset_database_state_before_each.md) (7 shared connections)
- [test database](test_database.md) (3 shared connections)
- [AttributeError](AttributeError.md) (1 shared connections)

## Source Files

- `server/database.py`
- `server/tests/unit/infrastructure/test_database_error_handling.py`

## Audit Trail

- EXTRACTED: 286 (96%)
- INFERRED: 12 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*