# server database helpers get database

> 6 nodes

## Key Concepts

- **get_database_url()** (7 connections) — `server/database_helpers.py`
- **test_get_database_url()** (5 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_database_url_returns_none()** (5 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **Get the database URL, initializing if necessary. Returns: str | None: The…** (1 connections) — `server/database_helpers.py`
- **Test get_database_url returns URL from DatabaseManager.** (1 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **Test get_database_url returns None when not configured.** (1 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`

## Relationships

- [server database databasemanager](server_database_databasemanager.md) (5 shared connections)
- [server database helpers close db](server_database_helpers_close_db.md) (3 shared connections)
- [server database databasemanager get instance](server_database_databasemanager_get_instance.md) (1 shared connections)
- [claude rules sqlalchemy](claude_rules_sqlalchemy.md) (1 shared connections)

## Source Files

- `server/database_helpers.py`
- `server/tests/unit/infrastructure/test_database_helpers.py`

## Audit Trail

- EXTRACTED: 12 (80%)
- INFERRED: 3 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*