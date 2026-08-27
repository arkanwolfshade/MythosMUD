# mock_connection_manager

> 113 nodes

## Key Concepts

- **npc_database.py** (29 connections) — `server/npc_database.py`
- **database_config_helpers.py** (24 connections) — `server/database_config_helpers.py`
- **test_npc_database.py** (23 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **patch** (20 connections)
- **get_npc_session()** (18 connections) — `server/npc_database.py`
- **get_npc_engine()** (14 connections) — `server/npc_database.py`
- **init_npc_db()** (11 connections) — `server/npc_database.py`
- **_initialize_npc_database()** (11 connections) — `server/npc_database.py`
- **get_npc_database_path()** (10 connections) — `server/npc_database.py`
- **test_database_config_helpers_asyncpg_settings.py** (10 connections) — `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- **get_asyncpg_server_settings_for_database_url()** (9 connections) — `server/database_config_helpers.py`
- **get_postgres_connect_args()** (9 connections) — `server/database_config_helpers.py`
- **close_npc_db()** (9 connections) — `server/npc_database.py`
- **asyncio** (9 connections)
- **TestNPCDatabaseInitialization** (8 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **get_npc_session_maker()** (8 connections) — `server/npc_database.py`
- **ensure_npc_database_directory()** (6 connections) — `server/npc_database.py`
- **.test_close_npc_db_disposes_engine()** (6 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **TestCloseNpcDb** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **TestGetNPCDatabasePath** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **TestInitNpcDb** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **TestNPCSession** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **reset_npc_database()** (5 connections) — `server/npc_database.py`
- **.test_close_npc_db_handles_closed_loop()** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_close_npc_db_handles_no_engine()** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- *... and 88 more nodes in this community*

## Relationships

- [generate_invites_db.py](generate_invites_db.py.md) (23 shared connections)
- [inventory_command_helpers.py](inventory_command_helpers.py.md) (12 shared connections)
- [NPCDefinition](NPCDefinition.md) (7 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [designTokens.ts](designTokens.ts.md) (3 shared connections)
- [test_logging_utilities.py](test_logging_utilities.py.md) (3 shared connections)
- [test_look_room.py](test_look_room.py.md) (3 shared connections)
- [Communities (19 total, 4 thin omitted)](Communities_19_total,_4_thin_omitted.md) (3 shared connections)
- [ContainerComponent](ContainerComponent.md) (3 shared connections)
- [test_combat_cleanup_handler.py](test_combat_cleanup_handler.py.md) (1 shared connections)
- [RoomLoader](RoomLoader.md) (1 shared connections)
- [test_quest_service.py](test_quest_service.py.md) (1 shared connections)

## Source Files

- `server/container/bundles/core.py`
- `server/database_config_helpers.py`
- `server/npc_database.py`
- `server/tests/unit/infrastructure/test_npc_database.py`
- `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`

## Audit Trail

- EXTRACTED: 253 (98%)
- INFERRED: 6 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*