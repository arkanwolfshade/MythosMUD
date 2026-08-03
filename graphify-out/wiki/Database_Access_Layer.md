# Database Access Layer

> 128 nodes

## Key Concepts

- **.get_instance()** (88 connections) — `server/database.py`
- **.reset_instance()** (87 connections) — `server/database.py`
- **test_database_error_handling.py** (41 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_database_init.py** (36 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **get_database_path()** (12 connections) — `server/database.py`
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
- **test_reset_database_resets_singleton()** (5 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_get_database_path_none_url()** (5 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_initialize_database_import_error()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_initialize_database_config_validation_error()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_initialize_database_config_runtime_error()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_initialize_database_none_url()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_initialize_database_unsupported_url()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- *... and 103 more nodes in this community*

## Relationships

- [memory lifespan app](memory_lifespan_app.md) (32 shared connections)
- [command inventory models](command_inventory_models.md) (21 shared connections)
- [manager subject services](manager_subject_services.md) (13 shared connections)
- [conftest mock rationale](conftest_mock_rationale.md) (12 shared connections)
- [Database Config](Database_Config.md) (9 shared connections)
- [holiday services service](holiday_services_service.md) (7 shared connections)
- [combat npc services](combat_npc_services.md) (6 shared connections)
- [commands lucidity recovery](commands_lucidity_recovery.md) (5 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)
- [combat services service](combat_services_service.md) (1 shared connections)
- [look helpers commands](look_helpers_commands.md) (1 shared connections)

## Source Files

- `server/database.py`
- `server/tests/unit/infrastructure/test_database_error_handling.py`
- `server/tests/unit/infrastructure/test_database_extended.py`
- `server/tests/unit/infrastructure/test_database_init.py`

## Audit Trail

- EXTRACTED: 567 (96%)
- INFERRED: 26 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*