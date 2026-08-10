# Holiday Persistence Models

> 78 nodes

## Key Concepts

- **test_database_extended.py** (43 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **.initialize()** (12 connections) — `server/container/bundles/core.py`
- **get_database_path()** (12 connections) — `server/database.py`
- **init_db()** (11 connections) — `server/database.py`
- **close_db()** (9 connections) — `server/database.py`
- **get_engine()** (8 connections) — `server/database.py`
- **get_database_url()** (6 connections) — `server/database.py`
- **test_get_engine_initializes_database()** (5 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_get_database_path_unsupported()** (5 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_database_path_none_url()** (5 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_database_path_module_level_none()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_get_database_path_module_level_unsupported()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **.close()** (4 connections) — `server/database.py`
- **ensure_database_directory()** (4 connections) — `server/database.py`
- **test_get_session_maker_initializes_database()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_database_url_initializes_database()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_get_engine_initializes()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_get_engine_reinitializes_if_none()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_get_session_maker_initializes()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_get_database_url_initializes()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_get_database_path_postgresql()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_close_with_engine()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_close_without_engine()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_close_dispose_error()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_database_path_unsupported()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- *... and 53 more nodes in this community*

## Relationships

- [Spell Registry Costs](Spell_Registry_Costs.md) (39 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (19 shared connections)
- [Room Service Tests](Room_Service_Tests.md) (7 shared connections)
- [Rate Limiter Utilities](Rate_Limiter_Utilities.md) (4 shared connections)
- [Combat Services Messaging](Combat_Services_Messaging.md) (3 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (2 shared connections)
- [Player Respawn Events](Player_Respawn_Events.md) (1 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (1 shared connections)
- [Archive Frd Random](Archive_Frd_Random.md) (1 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (1 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (1 shared connections)
- [Realtime Errors Error](Realtime_Errors_Error.md) (1 shared connections)

## Source Files

- `server/container/bundles/core.py`
- `server/database.py`
- `server/tests/unit/infrastructure/test_database_extended.py`
- `server/tests/unit/infrastructure/test_database_init.py`

## Audit Trail

- EXTRACTED: 256 (98%)
- INFERRED: 6 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*