# schemas players profession

> 12 nodes

## Key Concepts

- **TestNPCDatabaseInitialization** (8 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_engine_raises_on_invalid_url()** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_engine_initializes_engine()** (3 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_engine_uses_existing_engine()** (3 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_engine_env_fallback()** (3 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_engine_uses_nullpool_for_test()** (3 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test NPC database initialization.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test get_npc_engine() initializes engine when None.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test get_npc_engine() returns existing engine if already initialized.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test get_npc_engine() raises ValidationError for non-PostgreSQL URL.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test get_npc_engine() uses environment fallback when config fails.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test get_npc_engine() uses NullPool for test databases.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`

## Relationships

- [player effects endpoints](player_effects_endpoints.md) (6 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (2 shared connections)

## Source Files

- `server/tests/unit/infrastructure/test_npc_database.py`

## Audit Trail

- EXTRACTED: 28 (93%)
- INFERRED: 2 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*