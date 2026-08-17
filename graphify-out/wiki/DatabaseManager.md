# DatabaseManager

> 75 nodes

## Key Concepts

- **DatabaseManager** (113 connections) — `server/database.py`
- **.get_instance()** (88 connections) — `server/database.py`
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
- *... and 50 more nodes in this community*

## Relationships

- [.reset_instance](reset_instance.md) (80 shared connections)
- [test_database_extended.py](test_database_extended.py.md) (28 shared connections)
- [DatabaseError](DatabaseError.md) (13 shared connections)
- [test_database_helpers.py](test_database_helpers.py.md) (13 shared connections)
- [reset_database](reset_database.md) (13 shared connections)
- [get_logger](get_logger.md) (12 shared connections)
- [test_database.py](test_database.py.md) (9 shared connections)
- [get_database_path](get_database_path.md) (7 shared connections)
- [get_database_url](get_database_url.md) (4 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (1 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (1 shared connections)

## Source Files

- `server/database.py`
- `server/tests/unit/infrastructure/test_database_error_handling.py`

## Audit Trail

- EXTRACTED: 222 (68%)
- INFERRED: 106 (32%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*