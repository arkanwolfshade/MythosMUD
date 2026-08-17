# reset_database

> 21 nodes

## Key Concepts

- **reset_database()** (16 connections) — `server/database.py`
- **test_reset_database_resets_singleton()** (6 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_reset_database()** (6 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_reset_database_resets_singleton()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **reset_db_state()** (4 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **reset_db_state()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **reset_db()** (4 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_reset_database_resets_module_url()** (3 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_reset_database_resets_module_url()** (3 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **fixture** (1 connections)
- **fixture** (1 connections)
- **fixture** (1 connections)
- **Reset the database connection state (for testing). This resets the…** (1 connections) — `server/database.py`
- **Reset database state before each test.** (1 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **Test reset_database resets singleton.** (1 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **Test reset_database resets module-level _database_url.** (1 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **Reset database state before each test.** (1 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **Test reset_database resets both singleton and module-level URL.** (1 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **Reset database state before each test.** (1 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **Test reset_database resets module-level _database_url.** (1 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **Test reset_database resets DatabaseManager singleton.** (1 connections) — `server/tests/unit/infrastructure/test_database_init.py`

## Relationships

- [DatabaseManager](DatabaseManager.md) (10 shared connections)
- [.reset_instance](reset_instance.md) (7 shared connections)
- [test_database_extended.py](test_database_extended.py.md) (3 shared connections)
- [DatabaseError](DatabaseError.md) (2 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/database.py`
- `server/tests/unit/infrastructure/test_database_error_handling.py`
- `server/tests/unit/infrastructure/test_database_extended.py`
- `server/tests/unit/infrastructure/test_database_init.py`

## Audit Trail

- EXTRACTED: 40 (93%)
- INFERRED: 3 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*