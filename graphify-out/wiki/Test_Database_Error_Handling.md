# Test Database Error Handling

> 159 nodes

## Key Concepts

- **DatabaseManager** (112 connections) — `server/database.py`
- **.get_instance()** (88 connections) — `server/database.py`
- **.reset_instance()** (87 connections) — `server/database.py`
- **test_database_error_handling.py** (43 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_database_init.py** (37 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **._initialize_database()** (14 connections) — `server/database.py`
- **test_database.py** (8 connections) — `server/tests/unit/infrastructure/test_database.py`
- **test_close_handles_attribute_error_during_dispose()** (7 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **asyncio** (7 connections)
- **.get_session_maker()** (6 connections) — `server/database.py`
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
- *... and 134 more nodes in this community*

## Relationships

- [Test Database Extended](Test_Database_Extended.md) (44 shared connections)
- [Database](Database.md) (26 shared connections)
- [Test Database Helpers](Test_Database_Helpers.md) (25 shared connections)
- [Test Command Factories Inventory](Test_Command_Factories_Inventory.md) (10 shared connections)
- [Error Handling & Exceptions](Error_Handling_&_Exceptions.md) (10 shared connections)
- [Test Websocket Handler Validation Errors](Test_Websocket_Handler_Validation_Errors.md) (3 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (3 shared connections)
- [Application Container Bundles](Application_Container_Bundles.md) (2 shared connections)
- [Wearable Container Service](Wearable_Container_Service.md) (2 shared connections)
- [Rooms](Rooms.md) (1 shared connections)
- [Test Exploration Service](Test_Exploration_Service.md) (1 shared connections)
- [Async Persistence Direct Queries](Async_Persistence_Direct_Queries.md) (1 shared connections)

## Source Files

- `server/database.py`
- `server/tests/unit/infrastructure/test_database.py`
- `server/tests/unit/infrastructure/test_database_error_handling.py`
- `server/tests/unit/infrastructure/test_database_extended.py`
- `server/tests/unit/infrastructure/test_database_init.py`

## Audit Trail

- EXTRACTED: 387 (78%)
- INFERRED: 109 (22%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*