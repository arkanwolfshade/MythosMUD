# Server Infrastructure (7)

> 49 nodes

## Key Concepts

- **npc_database.py** (27 connections) — `server/npc_database.py`
- **get_npc_session()** (24 connections) — `server/npc_database.py`
- **test_npc_database.py** (22 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **get_npc_engine()** (14 connections) — `server/npc_database.py`
- **_initialize_npc_database()** (12 connections) — `server/npc_database.py`
- **init_npc_db()** (11 connections) — `server/npc_database.py`
- **get_npc_database_path()** (11 connections) — `server/npc_database.py`
- **get_postgres_connect_args()** (9 connections) — `server/database_config_helpers.py`
- **get_npc_session_maker()** (9 connections) — `server/npc_database.py`
- **close_npc_db()** (9 connections) — `server/npc_database.py`
- **ensure_npc_database_directory()** (6 connections) — `server/npc_database.py`
- **TestCloseNpcDb** (6 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **reset_npc_database()** (5 connections) — `server/npc_database.py`
- **TestNPCSessionMaker** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_close_npc_db_disposes_engine()** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **TestResetNPCDatabase** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **TestEventLoopHandling** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **async_sessionmaker** (3 connections)
- **AsyncSession** (3 connections)
- **reset_state()** (3 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_session_maker()** (3 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_close_npc_db_handles_closed_loop()** (3 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_close_npc_db_handles_no_engine()** (3 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_reset_npc_database_resets_state()** (3 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_engine_recreates_on_loop_change()** (3 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- *... and 24 more nodes in this community*

## Relationships

- [Server Utils](Server_Utils.md) (13 shared connections)
- [Server Admin](Server_Admin.md) (7 shared connections)
- [Server Npc](Server_Npc.md) (7 shared connections)
- [Server Infrastructure (19)](Server_Infrastructure_%2819%29.md) (6 shared connections)
- [Server App (2)](Server_App_%282%29.md) (5 shared connections)
- [Server Api](Server_Api.md) (4 shared connections)
- [Server Infrastructure (24)](Server_Infrastructure_%2824%29.md) (4 shared connections)
- [Server Services (42)](Server_Services_%2842%29.md) (3 shared connections)
- [Server App](Server_App.md) (3 shared connections)
- [Server Commands (45)](Server_Commands_%2845%29.md) (3 shared connections)
- [Server Scripts (3)](Server_Scripts_%283%29.md) (3 shared connections)
- [Server Infrastructure (26)](Server_Infrastructure_%2826%29.md) (3 shared connections)

## Source Files

- `server/database_config_helpers.py`
- `server/npc_database.py`
- `server/tests/unit/infrastructure/test_npc_database.py`

## Audit Trail

- EXTRACTED: 218 (94%)
- INFERRED: 13 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*