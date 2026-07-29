# Reset database state before each

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

- [.reset instance()](reset_instance%28%29.md) (7 shared connections)
- [.get instance()](get_instance%28%29.md) (6 shared connections)
- [main()](main%28%29.md) (3 shared connections)
- [close db()](close_db%28%29.md) (3 shared connections)

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