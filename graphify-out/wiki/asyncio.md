# asyncio

> 15 nodes

## Key Concepts

- **asyncio** (9 connections)
- **TestInitNpcDb** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **TestNPCSession** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_init_npc_db_raises_on_none_engine()** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_init_npc_db_success()** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_session_inits_db_for_unit_test()** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_session_rollback_on_error()** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_session_yields_session()** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test NPC session management.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test get_npc_session() yields session.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test get_npc_session() rolls back on error during yield.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test get_npc_session() calls init_npc_db() for unit_test databases.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test init_npc_db() function.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test init_npc_db() successfully initializes database.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test init_npc_db() raises ValidationError when engine is None.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`

## Relationships

- [get_npc_instance_service](get_npc_instance_service.md) (7 shared connections)
- [patch](patch.md) (5 shared connections)
- [close_npc_db](close_npc_db.md) (3 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [.test_get_npc_engine_recreates_on_loop_change](test_get_npc_engine_recreates_on_loop_change.md) (1 shared connections)

## Source Files

- `server/tests/unit/infrastructure/test_npc_database.py`

## Audit Trail

- EXTRACTED: 33 (97%)
- INFERRED: 1 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*