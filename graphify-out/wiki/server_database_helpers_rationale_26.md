# server database helpers rationale 26

> 26 nodes

## Key Concepts

- **reset_database()** (16 connections) — `server/database.py`
- **reset_database()** (9 connections) — `server/database_helpers.py`
- **test_reset_database()** (6 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **_reset_database_url_state()** (5 connections) — `server/database.py`
- **test_reset_database()** (5 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **reset_db_state()** (4 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **reset_db_state()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **reset_db()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **reset_db()** (4 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_reset_database_resets_module_url()** (3 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_reset_database_resets_module_url()** (3 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **fixture** (1 connections)
- **fixture** (1 connections)
- **fixture** (1 connections)
- **fixture** (1 connections)
- **Reset database state for testing. This function resets the DatabaseManager…** (1 connections) — `server/database_helpers.py`
- **Reset the database connection state (for testing). This resets the…** (1 connections) — `server/database.py`
- **Reset database URL state for testing. This is a public function to reset the…** (1 connections) — `server/database.py`
- **Reset database state before each test.** (1 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **Test reset_database resets module-level _database_url.** (1 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **Reset database state before each test.** (1 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **Test reset_database resets both singleton and module-level URL.** (1 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **Reset database state before each test.** (1 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **Test reset_database resets DatabaseManager singleton and module state.** (1 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **Reset database state before each test.** (1 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- *... and 1 more nodes in this community*

## Relationships

- [server database databasemanager](server_database_databasemanager.md) (10 shared connections)
- [claude rules sqlalchemy](claude_rules_sqlalchemy.md) (6 shared connections)
- [server database databasemanager get instance](server_database_databasemanager_get_instance.md) (6 shared connections)
- [server database helpers close db](server_database_helpers_close_db.md) (3 shared connections)
- [server database close db](server_database_close_db.md) (3 shared connections)

## Source Files

- `server/database.py`
- `server/database_helpers.py`
- `server/tests/unit/infrastructure/test_database_error_handling.py`
- `server/tests/unit/infrastructure/test_database_extended.py`
- `server/tests/unit/infrastructure/test_database_helpers.py`
- `server/tests/unit/infrastructure/test_database_init.py`

## Audit Trail

- EXTRACTED: 50 (94%)
- INFERRED: 3 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*