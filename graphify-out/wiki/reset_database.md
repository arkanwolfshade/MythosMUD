# reset_database

> 7 nodes

## Key Concepts

- **reset_database()** (9 connections) — `server/database_helpers.py`
- **test_reset_database()** (5 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **reset_db()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **fixture** (1 connections)
- **Reset database state for testing. This function resets the DatabaseManager…** (1 connections) — `server/database_helpers.py`
- **Reset database state before each test.** (1 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **Test reset_database resets DatabaseManager singleton and module state.** (1 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`

## Relationships

- [DatabaseManager](DatabaseManager.md) (4 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [test_database_helpers.py](test_database_helpers.py.md) (3 shared connections)

## Source Files

- `server/database_helpers.py`
- `server/tests/unit/infrastructure/test_database_helpers.py`

## Audit Trail

- EXTRACTED: 14 (88%)
- INFERRED: 2 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*