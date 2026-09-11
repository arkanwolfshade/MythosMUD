# DatabaseManager

> 134 nodes

## Key Concepts

- **DatabaseManager** (113 connections) — `server/database.py`
- **.get_instance()** (88 connections) — `server/database.py`
- **.reset_instance()** (87 connections) — `server/database.py`
- **test_database_error_handling.py** (41 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_database_init.py** (36 connections) — `server/tests/unit/infrastructure/test_database_init.py`
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
- **test_reset_database_resets_singleton()** (6 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- *... and 109 more nodes in this community*

## Relationships

- [test_database_extended.py](test_database_extended.py.md) (49 shared connections)
- [get_logger](get_logger.md) (26 shared connections)
- [test_database_helpers.py](test_database_helpers.py.md) (23 shared connections)
- [reset_database](reset_database.md) (18 shared connections)
- [test_database.py](test_database.py.md) (12 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (3 shared connections)
- [RoomService](RoomService.md) (3 shared connections)
- [.get_engine](get_engine.md) (2 shared connections)
- [get_session_maker](get_session_maker.md) (2 shared connections)
- [get_async_session](get_async_session.md) (2 shared connections)
- [MemoryMonitor](MemoryMonitor.md) (1 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (1 shared connections)

## Source Files

- `server/database.py`
- `server/services/exploration_service.py`
- `server/tests/unit/infrastructure/test_database_error_handling.py`
- `server/tests/unit/infrastructure/test_database_init.py`

## Audit Trail

- EXTRACTED: 345 (76%)
- INFERRED: 107 (24%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*