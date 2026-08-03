# conftest mock rationale

> 16 nodes

## Key Concepts

- **reset_database()** (16 connections) — `server/database.py`
- **test_reset_database()** (5 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_reset_database_resets_singleton()** (4 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **reset_db_state()** (3 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_reset_database_resets_module_url()** (3 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **reset_db_state()** (3 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **reset_db()** (3 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_reset_database_resets_module_url()** (3 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **Reset the database connection state (for testing).      This resets the Database** (1 connections) — `server/database.py`
- **Reset database state before each test.** (1 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **Test reset_database resets module-level _database_url.** (1 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **Reset database state before each test.** (1 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **Test reset_database resets both singleton and module-level URL.** (1 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **Reset database state before each test.** (1 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **Test reset_database resets module-level _database_url.** (1 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **Test reset_database resets DatabaseManager singleton.** (1 connections) — `server/tests/unit/infrastructure/test_database_init.py`

## Relationships

- [Database Access Layer](Database_Access_Layer.md) (12 shared connections)
- [memory lifespan app](memory_lifespan_app.md) (3 shared connections)
- [combat npc services](combat_npc_services.md) (1 shared connections)
- [manager subject services](manager_subject_services.md) (1 shared connections)
- [game models enums](game_models_enums.md) (1 shared connections)

## Source Files

- `server/database.py`
- `server/tests/unit/infrastructure/test_database_error_handling.py`
- `server/tests/unit/infrastructure/test_database_extended.py`
- `server/tests/unit/infrastructure/test_database_init.py`

## Audit Trail

- EXTRACTED: 48 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*