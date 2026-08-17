# patch

> 21 nodes

## Key Concepts

- **patch** (20 connections)
- **TestNPCDatabaseInitialization** (8 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **ensure_npc_database_directory()** (6 connections) — `server/npc_database.py`
- **TestEnsureNPCDatabaseDirectory** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_ensure_npc_database_directory_creates_directory()** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_ensure_npc_database_directory_no_op_for_postgresql()** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_engine_env_fallback()** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_engine_initializes_engine()** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_engine_raises_on_invalid_url()** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_engine_uses_existing_engine()** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_engine_uses_nullpool_for_test()** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Ensure NPC database directory exists. DEPRECATED: PostgreSQL does not use file…** (1 connections) — `server/npc_database.py`
- **Test get_npc_engine() uses NullPool for test databases.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test ensure_npc_database_directory() function.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test ensure_npc_database_directory() is no-op for PostgreSQL.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test ensure_npc_database_directory() creates directory if needed.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test NPC database initialization.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test get_npc_engine() initializes engine when None.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test get_npc_engine() returns existing engine if already initialized.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test get_npc_engine() raises ValidationError for non-PostgreSQL URL.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test get_npc_engine() uses environment fallback when config fails.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`

## Relationships

- [npc_database.py](npc_database.py.md) (11 shared connections)
- [asyncio](asyncio.md) (9 shared connections)
- [get_npc_database_path](get_npc_database_path.md) (3 shared connections)
- [ValidationError](ValidationError.md) (1 shared connections)

## Source Files

- `server/npc_database.py`
- `server/tests/unit/infrastructure/test_npc_database.py`

## Audit Trail

- EXTRACTED: 49 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*