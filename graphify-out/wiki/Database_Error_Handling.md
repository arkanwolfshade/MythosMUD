# Database Error Handling

> 59 nodes · cohesion 0.04

## Key Concepts

- **test_database_error_handling.py** (41 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **Test _initialize_database handles ValueError from create_async_engine.** (4 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **reset_db_state()** (3 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_close_handles_attribute_error_during_dispose()** (3 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_close_handles_runtime_error_during_dispose()** (3 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_database_manager_init_raises_when_instance_exists()** (3 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_get_engine_no_running_loop()** (3 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_reset_database_resets_module_url()** (3 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_reset_database_resets_singleton()** (3 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **Test close handles RuntimeError during dispose.** (2 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_close_handles_closed_event_loop()** (2 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_close_handles_dispose_timeout()** (2 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_close_handles_generic_exception_during_dispose()** (2 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_close_handles_none_engine()** (2 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_get_database_path_none_url_raises()** (2 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_get_database_path_unsupported_raises()** (2 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_get_database_url_not_initialized()** (2 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_get_engine_reinitializes_if_none()** (2 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_get_session_maker_not_initialized()** (2 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_initialize_database_config_validation_error()** (2 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_initialize_database_connection_error()** (2 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_initialize_database_converts_postgresql_url()** (2 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_initialize_database_generic_exception()** (2 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_initialize_database_keeps_asyncpg_url()** (2 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_initialize_database_none_url()** (2 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- *... and 34 more nodes in this community*

## Relationships

- [[NPC Admin API]] (11 shared connections)
- [[Database Manager Tests]] (4 shared connections)
- [[NPC Database Sessions]] (2 shared connections)
- [[Services Service Room]] (1 shared connections)

## Source Files

- `server/tests/unit/infrastructure/test_database_error_handling.py`
- `server/tests/unit/infrastructure/test_database_init.py`

## Audit Trail

- EXTRACTED: 139 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
