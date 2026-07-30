# get item description from prototype()

> 19 nodes

## Key Concepts

- **get_npc_engine()** (14 connections) — `server/npc_database.py`
- **TestNPCDatabaseInitialization** (8 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_engine_raises_on_invalid_url()** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **TestEventLoopHandling** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_engine_initializes_engine()** (3 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_engine_uses_existing_engine()** (3 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_engine_env_fallback()** (3 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_engine_uses_nullpool_for_test()** (3 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_engine_recreates_on_loop_change()** (3 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **AsyncEngine** (2 connections)
- **Get the NPC database engine, initializing if necessary.      Returns:         As** (1 connections) — `server/npc_database.py`
- **Test NPC database initialization.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test get_npc_engine() initializes engine when None.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test get_npc_engine() returns existing engine if already initialized.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test get_npc_engine() raises ValidationError for non-PostgreSQL URL.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test get_npc_engine() uses environment fallback when config fails.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test get_npc_engine() uses NullPool for test databases.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test event loop change detection and handling.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test get_npc_engine() recreates engine when event loop changes.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`

## Relationships

- [test admin commands](test_admin_commands.md) (7 shared connections)
- [.initialize()](initialize%28%29.md) (4 shared connections)
- [Test resolve connection manager from](Test_resolve_connection_manager_from.md) (1 shared connections)

## Source Files

- `server/npc_database.py`
- `server/tests/unit/infrastructure/test_npc_database.py`

## Audit Trail

- EXTRACTED: 52 (93%)
- INFERRED: 4 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*