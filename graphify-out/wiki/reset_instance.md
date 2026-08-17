# .reset_instance

> 52 nodes

## Key Concepts

- **.reset_instance()** (87 connections) — `server/database.py`
- **test_database_init.py** (37 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_initialize_database_connection_error()** (6 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_initialize_database_generic_exception()** (6 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_initialize_database_os_error()** (6 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_get_database_path_module_level_unsupported()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
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
- *... and 27 more nodes in this community*

## Relationships

- [DatabaseManager](DatabaseManager.md) (80 shared connections)
- [test_database_extended.py](test_database_extended.py.md) (13 shared connections)
- [reset_database](reset_database.md) (8 shared connections)
- [get_database_path](get_database_path.md) (8 shared connections)
- [DatabaseError](DatabaseError.md) (5 shared connections)
- [test_database_helpers.py](test_database_helpers.py.md) (4 shared connections)
- [test_database.py](test_database.py.md) (3 shared connections)
- [get_database_url](get_database_url.md) (2 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/database.py`
- `server/tests/unit/infrastructure/test_database_init.py`

## Audit Trail

- EXTRACTED: 172 (86%)
- INFERRED: 27 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*