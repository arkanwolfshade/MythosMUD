# Test resolve connection manager from

> 8 nodes

## Key Concepts

- **TestCloseNpcDb** (6 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_close_npc_db_disposes_engine()** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_close_npc_db_handles_closed_loop()** (3 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_close_npc_db_handles_no_engine()** (3 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test close_npc_db() function.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test close_npc_db() disposes engine.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test close_npc_db() handles closed event loop.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test close_npc_db() handles case when engine is None.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`

## Relationships

- [test admin commands](test_admin_commands.md) (4 shared connections)
- [.initialize()](initialize%28%29.md) (1 shared connections)
- [get item description from prototype()](get_item_description_from_prototype%28%29.md) (1 shared connections)

## Source Files

- `server/tests/unit/infrastructure/test_npc_database.py`

## Audit Trail

- EXTRACTED: 19 (95%)
- INFERRED: 1 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*