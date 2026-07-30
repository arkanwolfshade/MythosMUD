# Test broadcast player mortally wounded

> 8 nodes

## Key Concepts

- **TestNPCSession** (6 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_session_yields_session()** (3 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_session_rollback_on_error()** (3 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_session_inits_db_for_unit_test()** (3 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test NPC session management.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test get_npc_session() yields session.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test get_npc_session() rolls back on error during yield.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test get_npc_session() calls init_npc_db() for unit_test databases.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`

## Relationships

- [test admin commands](test_admin_commands.md) (4 shared connections)
- [.initialize()](initialize%28%29.md) (1 shared connections)

## Source Files

- `server/tests/unit/infrastructure/test_npc_database.py`

## Audit Trail

- EXTRACTED: 18 (95%)
- INFERRED: 1 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*