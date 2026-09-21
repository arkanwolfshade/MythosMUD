# npc_database.py

> 117 nodes

## Key Concepts

- **npc_database.py** (31 connections) — `server/npc_database.py`
- **test_npc_database.py** (26 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **patch** (25 connections)
- **get_npc_session()** (24 connections) — `server/npc_database.py`
- **get_npc_engine()** (14 connections) — `server/npc_database.py`
- **_initialize_npc_database()** (13 connections) — `server/npc_database.py`
- **init_npc_db()** (11 connections) — `server/npc_database.py`
- **get_npc_database_path()** (10 connections) — `server/npc_database.py`
- **get_postgres_connect_args()** (9 connections) — `server/database_config_helpers.py`
- **_build_npc_connect_args()** (9 connections) — `server/npc_database.py`
- **close_npc_db()** (9 connections) — `server/npc_database.py`
- **asyncio** (9 connections)
- **TestNPCDatabaseInitialization** (8 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **get_npc_session_maker()** (8 connections) — `server/npc_database.py`
- **_build_npc_pool_kwargs()** (7 connections) — `server/npc_database.py`
- **TestBuildNpcConnectArgs** (6 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **ensure_npc_database_directory()** (6 connections) — `server/npc_database.py`
- **_resolve_npc_database_url()** (6 connections) — `server/npc_database.py`
- **.test_close_npc_db_disposes_engine()** (6 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **TestCloseNpcDb** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **TestGetNPCDatabasePath** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **TestInitNpcDb** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **TestNPCSession** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **reset_npc_database()** (5 connections) — `server/npc_database.py`
- **.test_close_npc_db_handles_closed_loop()** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- *... and 92 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (10 shared connections)
- [ValidationError](ValidationError.md) (9 shared connections)
- [DatabaseManager](DatabaseManager.md) (5 shared connections)
- [DatabaseError](DatabaseError.md) (5 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (4 shared connections)
- [NPCDefinition](NPCDefinition.md) (4 shared connections)
- [get_config](get_config.md) (3 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (3 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (3 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (3 shared connections)
- [fixtures/integration/__init__.py](fixtures-integration-__init__.py.md) (2 shared connections)
- [test_npc_admin_commands.py](test_npc_admin_commands.py.md) (1 shared connections)

## Source Files

- `server/commands/npc_admin/instance.py`
- `server/container/bundles/core.py`
- `server/database_config_helpers.py`
- `server/npc_database.py`
- `server/tests/unit/infrastructure/test_npc_database.py`

## Audit Trail

- EXTRACTED: 251 (97%)
- INFERRED: 7 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*