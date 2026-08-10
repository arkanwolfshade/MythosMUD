# Spell Registry Costs

> 121 nodes

## Key Concepts

- **.get_instance()** (88 connections) — `server/database.py`
- **.reset_instance()** (87 connections) — `server/database.py`
- **test_database_error_handling.py** (41 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_database_init.py** (36 connections) — `server/tests/unit/infrastructure/test_database_init.py`
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
- **test_initialize_database_import_error()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_initialize_database_config_validation_error()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_initialize_database_config_runtime_error()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_initialize_database_none_url()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_initialize_database_unsupported_url()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_initialize_database_value_error()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_initialize_database_type_error()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_initialize_database_connection_error()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- *... and 96 more nodes in this community*

## Relationships

- [Holiday Persistence Models](Holiday_Persistence_Models.md) (39 shared connections)
- [Room Service Tests](Room_Service_Tests.md) (18 shared connections)
- [Container Loot Helpers](Container_Loot_Helpers.md) (13 shared connections)
- [Combat Services Messaging](Combat_Services_Messaging.md) (13 shared connections)
- [Rate Limiter Utilities](Rate_Limiter_Utilities.md) (12 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (9 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (6 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (1 shared connections)

## Source Files

- `server/database.py`
- `server/services/exploration_service.py`
- `server/tests/unit/infrastructure/test_database_error_handling.py`
- `server/tests/unit/infrastructure/test_database_init.py`

## Audit Trail

- EXTRACTED: 539 (96%)
- INFERRED: 24 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*