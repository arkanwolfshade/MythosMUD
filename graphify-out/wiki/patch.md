# patch

> 11 nodes

## Key Concepts

- **patch** (20 connections)
- **TestGetNPCDatabasePath** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_database_path_raises_for_non_postgresql()** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_database_path_returns_none_for_postgresql()** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_session_maker()** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **TestNPCSessionMaker** (3 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test NPC session maker functions.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test get_npc_session_maker() returns session maker.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test get_npc_database_path() function.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test get_npc_database_path() returns None for PostgreSQL.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test get_npc_database_path() raises for non-PostgreSQL URLs.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`

## Relationships

- [get_npc_instance_service](get_npc_instance_service.md) (5 shared connections)
- [asyncio](asyncio.md) (5 shared connections)
- [get_npc_engine](get_npc_engine.md) (5 shared connections)
- [close_npc_db](close_npc_db.md) (3 shared connections)
- [ensure_npc_database_directory](ensure_npc_database_directory.md) (2 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [reset_npc_database](reset_npc_database.md) (1 shared connections)
- [.test_get_npc_engine_recreates_on_loop_change](test_get_npc_engine_recreates_on_loop_change.md) (1 shared connections)

## Source Files

- `server/tests/unit/infrastructure/test_npc_database.py`

## Audit Trail

- EXTRACTED: 33 (97%)
- INFERRED: 1 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*