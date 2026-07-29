# .get instance()

> 53 nodes

## Key Concepts

- **.get_instance()** (88 connections) — `server/database.py`
- **test_database_init.py** (36 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_initialize_database_import_error()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_initialize_database_config_validation_error()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_initialize_database_config_runtime_error()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_initialize_database_none_url()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_initialize_database_unsupported_url()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_initialize_database_value_error()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_initialize_database_type_error()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_initialize_database_connection_error()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_initialize_database_os_error()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_initialize_database_generic_exception()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_get_database_path_unsupported_raises()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_get_database_path_none_url_raises()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_initialize_database_skip_if_already_initialized()** (4 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_initialize_database_uses_module_level_url()** (4 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_initialize_database_converts_postgresql_url()** (4 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_initialize_database_keeps_asyncpg_url()** (4 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_initialize_database_uses_nullpool_for_test()** (4 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_initialize_database_uses_pool_config_for_production()** (4 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_initialize_database_sets_creation_loop_id()** (4 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_initialize_database_sets_creation_loop_id_none()** (4 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_get_engine_reinitializes_if_none()** (4 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_get_engine_handles_no_running_loop()** (4 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_get_database_path_postgresql_returns_none()** (4 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- *... and 28 more nodes in this community*

## Relationships

- [.reset instance()](reset_instance%28%29.md) (55 shared connections)
- [close db()](close_db%28%29.md) (20 shared connections)
- [. init ()](_init_%28%29.md) (15 shared connections)
- [main()](main%28%29.md) (9 shared connections)
- [Reset database state before each](Reset_database_state_before_each.md) (6 shared connections)
- [test database](test_database.md) (4 shared connections)
- [.initialize()](initialize%28%29.md) (1 shared connections)
- [.get explored rooms()](get_explored_rooms%28%29.md) (1 shared connections)

## Source Files

- `server/database.py`
- `server/tests/unit/infrastructure/test_database_init.py`

## Audit Trail

- EXTRACTED: 251 (95%)
- INFERRED: 12 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*