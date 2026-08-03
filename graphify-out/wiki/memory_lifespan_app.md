# memory lifespan app

> 60 nodes

## Key Concepts

- **test_database_extended.py** (43 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **.initialize()** (12 connections) — `server/container/bundles/core.py`
- **init_db()** (11 connections) — `server/database.py`
- **close_db()** (9 connections) — `server/database.py`
- **get_engine()** (8 connections) — `server/database.py`
- **test_get_engine_initializes_database()** (5 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_get_database_path_unsupported()** (5 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **ensure_database_directory()** (4 connections) — `server/database.py`
- **test_get_session_maker_initializes_database()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_get_engine_initializes()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_get_engine_reinitializes_if_none()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_get_session_maker_initializes()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_get_database_url_initializes()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_get_database_path_postgresql()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_close_with_engine()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_close_without_engine()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_close_dispose_error()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_database_path_unsupported()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_get_engine_event_loop_check()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_get_engine_no_running_loop()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **.close()** (3 connections) — `server/database.py`
- **test_get_async_session_success()** (3 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_async_session_rollback_error()** (3 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_init_db_success()** (3 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_init_db_import_error()** (3 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- *... and 35 more nodes in this community*

## Relationships

- [Database Access Layer](Database_Access_Layer.md) (32 shared connections)
- [combat npc services](combat_npc_services.md) (12 shared connections)
- [commands lucidity recovery](commands_lucidity_recovery.md) (5 shared connections)
- [Error Conversion](Error_Conversion.md) (3 shared connections)
- [conftest mock rationale](conftest_mock_rationale.md) (3 shared connections)
- [command inventory models](command_inventory_models.md) (3 shared connections)
- [Database Config](Database_Config.md) (2 shared connections)
- [follow service game](follow_service_game.md) (1 shared connections)
- [schemas player rationale](schemas_player_rationale.md) (1 shared connections)
- [NPC Combat](NPC_Combat.md) (1 shared connections)
- [models npc rationale](models_npc_rationale.md) (1 shared connections)
- [main rationale failure()](main_rationale_failure%28%29.md) (1 shared connections)

## Source Files

- `server/container/bundles/core.py`
- `server/database.py`
- `server/tests/unit/infrastructure/test_database_extended.py`

## Audit Trail

- EXTRACTED: 202 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*