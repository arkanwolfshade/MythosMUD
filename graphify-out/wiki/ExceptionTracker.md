# ExceptionTracker

> 113 nodes · cohesion 0.03

## Key Concepts

- **npc_database.py** (31 connections) — `server/npc_database.py`
- **test_npc_database.py** (26 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **patch** (25 connections)
- **get_npc_session()** (24 connections) — `server/npc_database.py`
- **get_npc_engine()** (14 connections) — `server/npc_database.py`
- **_initialize_npc_database()** (13 connections) — `server/npc_database.py`
- **init_npc_db()** (11 connections) — `server/npc_database.py`
- **get_npc_database_path()** (10 connections) — `server/npc_database.py`
- **_build_npc_connect_args()** (9 connections) — `server/npc_database.py`
- **close_npc_db()** (9 connections) — `server/npc_database.py`
- **asyncio** (9 connections)
- **get_npc_session_maker()** (8 connections) — `server/npc_database.py`
- **TestNPCDatabaseInitialization** (8 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **_build_npc_pool_kwargs()** (7 connections) — `server/npc_database.py`
- **ensure_npc_database_directory()** (6 connections) — `server/npc_database.py`
- **_resolve_npc_database_url()** (6 connections) — `server/npc_database.py`
- **TestBuildNpcConnectArgs** (6 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_close_npc_db_disposes_engine()** (6 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_session_rollback_on_error()** (6 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **reset_npc_database()** (5 connections) — `server/npc_database.py`
- **TestCloseNpcDb** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_close_npc_db_handles_closed_loop()** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_close_npc_db_handles_no_engine()** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_engine_recreates_on_loop_change()** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **TestGetNPCDatabasePath** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- *... and 88 more nodes in this community*

## Relationships

- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (9 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (6 shared connections)
- [endpoints.py](endpoints.py.md) (5 shared connections)
- [command_parser.py](command_parser.py.md) (4 shared connections)
- [combat_taunt.py](combat_taunt.py.md) (3 shared connections)
- [test_player_combat_service.py](test_player_combat_service.py.md) (3 shared connections)
- [PlayerNameExtractor](PlayerNameExtractor.md) (3 shared connections)
- [rescue_commands.py](rescue_commands.py.md) (3 shared connections)
- [AttributeError](AttributeError.md) (3 shared connections)
- [Test Suite Quality Audit - Executive Summary](Test_Suite_Quality_Audit_-_Executive_Summary.md) (3 shared connections)
- [CombatInstance](CombatInstance.md) (3 shared connections)
- [test_combat_persistence_handler_persistence.py](test_combat_persistence_handler_persistence.py.md) (3 shared connections)

## Source Files

- `server/commands/npc_admin/instance.py`
- `server/npc_database.py`
- `server/tests/unit/infrastructure/test_npc_database.py`

## Audit Trail

- EXTRACTED: 241 (97%)
- INFERRED: 8 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*