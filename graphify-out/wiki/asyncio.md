# asyncio

> 27 nodes

## Key Concepts

- **asyncio** (9 connections)
- **.test_close_npc_db_disposes_engine()** (6 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **TestCloseNpcDb** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
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
- **TestEventLoopHandling** (3 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test NPC session management.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test get_npc_session() yields session.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test get_npc_session() rolls back on error during yield.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test get_npc_session() calls init_npc_db() for unit_test databases.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test init_npc_db() function.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test init_npc_db() successfully initializes database.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test init_npc_db() raises ValidationError when engine is None.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test close_npc_db() function.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test close_npc_db() disposes engine.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test close_npc_db() handles closed event loop.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test close_npc_db() handles case when engine is None.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- *... and 2 more nodes in this community*

## Relationships

- [npc_database.py](npc_database.py.md) (14 shared connections)
- [patch](patch.md) (9 shared connections)
- [ValidationError](ValidationError.md) (1 shared connections)

## Source Files

- `server/tests/unit/infrastructure/test_npc_database.py`

## Audit Trail

- EXTRACTED: 54 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*