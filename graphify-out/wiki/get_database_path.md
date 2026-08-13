# get_database_path

> 15 nodes

## Key Concepts

- **get_database_path()** (12 connections) — `server/database.py`
- **get_database_url()** (6 connections) — `server/database.py`
- **.get_database_path()** (5 connections) — `server/database.py`
- **test_get_database_url_initializes_database()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_database_path_module_level_none()** (4 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_get_database_path_module_level_postgresql()** (4 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_get_database_path_module_level_unsupported()** (4 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **Path** (2 connections)
- **Get the database file path. DEPRECATED: PostgreSQL does not use file paths.…** (1 connections) — `server/database.py`
- **Get the database file path (deprecated for PostgreSQL). Returns: Path | None:…** (1 connections) — `server/database.py`
- **Get the database URL from DatabaseManager. Returns: str | None: The database URL** (1 connections) — `server/database.py`
- **Test get_database_url initializes database if not already initialized.** (1 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **Test get_database_path handles module-level empty URL.** (1 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **Test get_database_path returns None for module-level PostgreSQL URL.** (1 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **Test get_database_path raises for module-level unsupported URL.** (1 connections) — `server/tests/unit/infrastructure/test_database_init.py`

## Relationships

- [.get_instance](get_instance.md) (6 shared connections)
- [get_async_session](get_async_session.md) (5 shared connections)
- [.reset_instance](reset_instance.md) (4 shared connections)
- [DatabaseError](DatabaseError.md) (2 shared connections)
- [log_and_raise](log_and_raise.md) (1 shared connections)
- [DatabaseManager](DatabaseManager.md) (1 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (1 shared connections)

## Source Files

- `server/database.py`
- `server/tests/unit/infrastructure/test_database_extended.py`
- `server/tests/unit/infrastructure/test_database_init.py`

## Audit Trail

- EXTRACTED: 34 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*