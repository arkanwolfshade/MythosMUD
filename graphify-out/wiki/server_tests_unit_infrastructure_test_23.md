# server tests unit infrastructure test

> 10 nodes

## Key Concepts

- **test_database.py** (8 connections) — `server/tests/unit/infrastructure/test_database.py`
- **test_database_manager_initial_state()** (5 connections) — `server/tests/unit/infrastructure/test_database.py`
- **test_database_manager_reset_instance()** (5 connections) — `server/tests/unit/infrastructure/test_database.py`
- **test_database_manager_singleton()** (5 connections) — `server/tests/unit/infrastructure/test_database.py`
- **test_database_manager_direct_init_raises()** (4 connections) — `server/tests/unit/infrastructure/test_database.py`
- **Unit tests for database initialization.** (1 connections) — `server/tests/unit/infrastructure/test_database.py`
- **Test that DatabaseManager is a singleton.** (1 connections) — `server/tests/unit/infrastructure/test_database.py`
- **Test resetting the singleton instance.** (1 connections) — `server/tests/unit/infrastructure/test_database.py`
- **Test that direct initialization raises RuntimeError when instance exists.** (1 connections) — `server/tests/unit/infrastructure/test_database.py`
- **Test initial state of database manager.** (1 connections) — `server/tests/unit/infrastructure/test_database.py`

## Relationships

- [server database databasemanager](server_database_databasemanager.md) (8 shared connections)
- [server database databasemanager get instance](server_database_databasemanager_get_instance.md) (4 shared connections)
- [claude rules pytest](claude_rules_pytest.md) (1 shared connections)
- [claude rules sqlalchemy](claude_rules_sqlalchemy.md) (1 shared connections)

## Source Files

- `server/tests/unit/infrastructure/test_database.py`

## Audit Trail

- EXTRACTED: 20 (87%)
- INFERRED: 3 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*