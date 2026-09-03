# Test Database Extended

> 67 nodes

## Key Concepts

- **test_database_extended.py** (44 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **.initialize()** (12 connections) — `server/container/bundles/core.py`
- **get_database_path()** (12 connections) — `server/database.py`
- **asyncio** (12 connections)
- **init_db()** (10 connections) — `server/database.py`
- **get_engine()** (9 connections) — `server/database.py`
- **close_db()** (7 connections) — `server/database.py`
- **get_database_url()** (6 connections) — `server/database.py`
- **test_database_manager_close_dispose_error()** (6 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_close_with_engine()** (6 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_close_without_engine()** (6 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_database_path_none_url()** (6 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_database_url_initializes_database()** (5 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_engine_initializes_database()** (5 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_session_maker_initializes_database()** (5 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_database_path_module_level_none()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_get_database_path_module_level_postgresql()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_get_database_path_module_level_unsupported()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **.get_database_path()** (4 connections) — `server/database.py`
- **ensure_database_directory()** (4 connections) — `server/database.py`
- **reset_db_state()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_close_db_error()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_close_db_success()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_async_session_http_exception_re_raised()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_async_session_rollback_error()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- *... and 42 more nodes in this community*

## Relationships

- [Test Database Error Handling](Test_Database_Error_Handling.md) (44 shared connections)
- [Database](Database.md) (10 shared connections)
- [Async Persistence Direct Queries](Async_Persistence_Direct_Queries.md) (5 shared connections)
- [Application Container Bundles](Application_Container_Bundles.md) (4 shared connections)
- [Test Command Factories Inventory](Test_Command_Factories_Inventory.md) (3 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (2 shared connections)
- [Wearable Container Service](Wearable_Container_Service.md) (2 shared connections)
- [Test Config Init](Test_Config_Init.md) (1 shared connections)
- [Test Npc Database](Test_Npc_Database.md) (1 shared connections)
- [Task Registry](Task_Registry.md) (1 shared connections)
- [Tracked Task Manager](Tracked_Task_Manager.md) (1 shared connections)
- [Test Distributed Event Bus](Test_Distributed_Event_Bus.md) (1 shared connections)

## Source Files

- `server/container/bundles/core.py`
- `server/database.py`
- `server/tests/unit/infrastructure/test_database_extended.py`
- `server/tests/unit/infrastructure/test_database_init.py`

## Audit Trail

- EXTRACTED: 157 (93%)
- INFERRED: 12 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*