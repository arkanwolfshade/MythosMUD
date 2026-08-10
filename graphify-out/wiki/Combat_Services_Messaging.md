# Combat Services Messaging

> 16 nodes

## Key Concepts

- **reset_database()** (16 connections) — `server/database.py`
- **test_reset_database_resets_singleton()** (5 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_reset_database()** (5 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **reset_db_state()** (3 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_reset_database_resets_module_url()** (3 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **reset_db_state()** (3 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **reset_db()** (3 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_reset_database_resets_module_url()** (3 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **Reset the database connection state (for testing).      This resets the Database** (1 connections) — `server/database.py`
- **Reset database state before each test.** (1 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **Test reset_database resets singleton.** (1 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **Test reset_database resets module-level _database_url.** (1 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **Reset database state before each test.** (1 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **Test reset_database resets both singleton and module-level URL.** (1 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **Reset database state before each test.** (1 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **Test reset_database resets module-level _database_url.** (1 connections) — `server/tests/unit/infrastructure/test_database_init.py`

## Relationships

- [Spell Registry Costs](Spell_Registry_Costs.md) (13 shared connections)
- [Holiday Persistence Models](Holiday_Persistence_Models.md) (3 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (1 shared connections)
- [Container Loot Helpers](Container_Loot_Helpers.md) (1 shared connections)
- [NATS Subject Manager](NATS_Subject_Manager.md) (1 shared connections)

## Source Files

- `server/database.py`
- `server/tests/unit/infrastructure/test_database_error_handling.py`
- `server/tests/unit/infrastructure/test_database_extended.py`
- `server/tests/unit/infrastructure/test_database_init.py`

## Audit Trail

- EXTRACTED: 49 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*