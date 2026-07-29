# test database

> 10 nodes

## Key Concepts

- **test_database.py** (7 connections) — `server/tests/unit/infrastructure/test_database.py`
- **test_database_manager_singleton()** (4 connections) — `server/tests/unit/infrastructure/test_database.py`
- **test_database_manager_reset_instance()** (4 connections) — `server/tests/unit/infrastructure/test_database.py`
- **test_database_manager_direct_init_raises()** (4 connections) — `server/tests/unit/infrastructure/test_database.py`
- **test_database_manager_initial_state()** (4 connections) — `server/tests/unit/infrastructure/test_database.py`
- **Unit tests for database initialization.** (1 connections) — `server/tests/unit/infrastructure/test_database.py`
- **Test that DatabaseManager is a singleton.** (1 connections) — `server/tests/unit/infrastructure/test_database.py`
- **Test resetting the singleton instance.** (1 connections) — `server/tests/unit/infrastructure/test_database.py`
- **Test that direct initialization raises RuntimeError when instance exists.** (1 connections) — `server/tests/unit/infrastructure/test_database.py`
- **Test initial state of database manager.** (1 connections) — `server/tests/unit/infrastructure/test_database.py`

## Relationships

- [.get instance()](get_instance%28%29.md) (4 shared connections)
- [main()](main%28%29.md) (3 shared connections)
- [.reset instance()](reset_instance%28%29.md) (3 shared connections)

## Source Files

- `server/tests/unit/infrastructure/test_database.py`

## Audit Trail

- EXTRACTED: 28 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*