# get_database_url

> 6 nodes

## Key Concepts

- **get_database_url()** (7 connections) — `server/database_helpers.py`
- **test_get_database_url()** (5 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_database_url_returns_none()** (5 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **Get the database URL, initializing if necessary. Returns: str | None: The…** (1 connections) — `server/database_helpers.py`
- **Test get_database_url returns URL from DatabaseManager.** (1 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **Test get_database_url returns None when not configured.** (1 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`

## Relationships

- [DatabaseManager](DatabaseManager.md) (4 shared connections)
- [test_database_helpers.py](test_database_helpers.py.md) (3 shared connections)
- [.reset_instance](reset_instance.md) (2 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/database_helpers.py`
- `server/tests/unit/infrastructure/test_database_helpers.py`

## Audit Trail

- EXTRACTED: 12 (80%)
- INFERRED: 3 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*