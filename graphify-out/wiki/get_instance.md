# .get_instance

> 101 nodes

## Key Concepts

- **.get_instance()** (88 connections) — `server/database.py`
- **.reset_instance()** (87 connections) — `server/database.py`
- **test_database_error_handling.py** (41 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_database_manager_init_raises_when_instance_exists()** (5 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_reset_database_resets_singleton()** (5 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_database_manager_close_dispose_error()** (5 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_close_with_engine()** (5 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_close_without_engine()** (5 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **reset_db_state()** (4 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_get_database_path_none_url_raises()** (4 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_get_database_path_postgresql_returns_none()** (4 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_get_database_path_unsupported_raises()** (4 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_get_database_url_not_initialized()** (4 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_get_engine_event_loop_changed()** (4 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_get_engine_no_running_loop()** (4 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_get_engine_reinitializes_if_none()** (4 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_get_session_maker_not_initialized()** (4 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_initialize_database_config_runtime_error()** (4 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_initialize_database_config_validation_error()** (4 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_initialize_database_connection_error()** (4 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_initialize_database_converts_postgresql_url()** (4 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_initialize_database_generic_exception()** (4 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_initialize_database_keeps_asyncpg_url()** (4 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_initialize_database_none_url()** (4 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_initialize_database_os_error()** (4 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- *... and 76 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (48 shared connections)
- [test_database_init.py](test_database_init.py.md) (45 shared connections)
- [asyncio](asyncio.md) (21 shared connections)
- [test_database_helpers.py](test_database_helpers.py.md) (5 shared connections)
- [get_database_url](get_database_url.md) (3 shared connections)
- [get_engine](get_engine.md) (3 shared connections)
- [._get_room_uuid_by_stable_id](_get_room_uuid_by_stable_id.md) (1 shared connections)

## Source Files

- `server/database.py`
- `server/tests/unit/infrastructure/test_database.py`
- `server/tests/unit/infrastructure/test_database_error_handling.py`
- `server/tests/unit/infrastructure/test_database_extended.py`
- `server/tests/unit/infrastructure/test_database_helpers.py`
- `server/tests/unit/infrastructure/test_database_init.py`

## Audit Trail

- EXTRACTED: 293 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*