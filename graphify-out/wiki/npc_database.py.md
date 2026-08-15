# npc_database.py

> 120 nodes

## Key Concepts

- **npc_database.py** (27 connections) — `server/npc_database.py`
- **get_npc_session()** (24 connections) — `server/npc_database.py`
- **instance.py** (23 connections) — `server/commands/npc_admin/instance.py`
- **test_npc_database.py** (22 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **patch** (20 connections)
- **get_npc_engine()** (14 connections) — `server/npc_database.py`
- **init_npc_db()** (11 connections) — `server/npc_database.py`
- **_initialize_npc_database()** (11 connections) — `server/npc_database.py`
- **get_npc_database_path()** (10 connections) — `server/npc_database.py`
- **asyncio** (9 connections)
- **TestNPCDatabaseInitialization** (8 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **get_npc_session_maker()** (8 connections) — `server/npc_database.py`
- **Any** (8 connections)
- **ensure_npc_database_directory()** (6 connections) — `server/npc_database.py`
- **.test_close_npc_db_disposes_engine()** (6 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **TestCloseNpcDb** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **TestGetNPCDatabasePath** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **TestInitNpcDb** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **TestNPCSession** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **_parse_npc_spawn_args()** (5 connections) — `server/commands/npc_admin/instance.py`
- **reset_npc_database()** (5 connections) — `server/npc_database.py`
- **.test_close_npc_db_handles_closed_loop()** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_close_npc_db_handles_no_engine()** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_engine_recreates_on_loop_change()** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_init_npc_db_raises_on_none_engine()** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- *... and 95 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (24 shared connections)
- [test_npc_admin_commands.py](test_npc_admin_commands.py.md) (10 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (9 shared connections)
- [ValidationError](ValidationError.md) (8 shared connections)
- [DatabaseError](DatabaseError.md) (7 shared connections)
- [npc_definitions_api.py](npc_definitions_api.py.md) (3 shared connections)
- [migrate_combat_data.py](migrate_combat_data.py.md) (3 shared connections)
- [get_config](get_config.md) (2 shared connections)
- [session_factory](session_factory.md) (2 shared connections)
- [lifespan.py](lifespan.py.md) (1 shared connections)
- [NPCStartupService](NPCStartupService.md) (1 shared connections)
- [AliasStorage](AliasStorage.md) (1 shared connections)

## Source Files

- `server/commands/npc_admin/instance.py`
- `server/npc_database.py`
- `server/services/npc_instance_service.py`
- `server/tests/unit/infrastructure/test_npc_database.py`

## Audit Trail

- EXTRACTED: 257 (98%)
- INFERRED: 6 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*