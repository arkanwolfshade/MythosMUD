# get_npc_engine

> 15 nodes

## Key Concepts

- **get_npc_engine()** (14 connections) — `server/npc_database.py`
- **TestNPCDatabaseInitialization** (8 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_engine_env_fallback()** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_engine_initializes_engine()** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_engine_raises_on_invalid_url()** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_engine_uses_existing_engine()** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_engine_uses_nullpool_for_test()** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **AsyncEngine** (1 connections)
- **Get the NPC database engine, initializing if necessary. Returns: AsyncEngine |…** (1 connections) — `server/npc_database.py`
- **Test get_npc_engine() uses NullPool for test databases.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test NPC database initialization.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test get_npc_engine() initializes engine when None.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test get_npc_engine() returns existing engine if already initialized.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test get_npc_engine() raises ValidationError for non-PostgreSQL URL.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test get_npc_engine() uses environment fallback when config fails.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`

## Relationships

- [get_npc_instance_service](get_npc_instance_service.md) (5 shared connections)
- [patch](patch.md) (5 shared connections)
- [close_npc_db](close_npc_db.md) (2 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [.test_get_npc_engine_recreates_on_loop_change](test_get_npc_engine_recreates_on_loop_change.md) (1 shared connections)

## Source Files

- `server/npc_database.py`
- `server/tests/unit/infrastructure/test_npc_database.py`

## Audit Trail

- EXTRACTED: 31 (97%)
- INFERRED: 1 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*