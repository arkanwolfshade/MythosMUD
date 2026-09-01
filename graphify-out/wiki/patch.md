# patch

> 46 nodes

## Key Concepts

- **patch** (20 connections)
- **asyncio** (9 connections)
- **TestNPCDatabaseInitialization** (8 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_close_npc_db_disposes_engine()** (6 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **TestCloseNpcDb** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **TestGetNPCDatabasePath** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **TestInitNpcDb** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **TestNPCSession** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_close_npc_db_handles_closed_loop()** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_close_npc_db_handles_no_engine()** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_engine_recreates_on_loop_change()** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_init_npc_db_raises_on_none_engine()** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_init_npc_db_success()** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_session_inits_db_for_unit_test()** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_session_rollback_on_error()** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_session_yields_session()** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_database_path_raises_for_non_postgresql()** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_database_path_returns_none_for_postgresql()** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_engine_env_fallback()** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_engine_initializes_engine()** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_engine_raises_on_invalid_url()** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_engine_uses_existing_engine()** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_engine_uses_nullpool_for_test()** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **TestEventLoopHandling** (3 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test get_npc_engine() uses NullPool for test databases.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- *... and 21 more nodes in this community*

## Relationships

- [npc_database.py](npc_database.py.md) (25 shared connections)
- [ValidationError](ValidationError.md) (3 shared connections)
- [TestEnsureNPCDatabaseDirectory](TestEnsureNPCDatabaseDirectory.md) (2 shared connections)

## Source Files

- `server/tests/unit/infrastructure/test_npc_database.py`

## Audit Trail

- EXTRACTED: 90 (97%)
- INFERRED: 3 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*