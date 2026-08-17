# get_database_path

> 19 nodes

## Key Concepts

- **get_database_path()** (12 connections) — `server/database.py`
- **get_database_url()** (6 connections) — `server/database.py`
- **test_get_database_path_none_url()** (6 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **.get_database_path()** (5 connections) — `server/database.py`
- **test_get_database_url_initializes_database()** (5 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_database_path_module_level_none()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_get_database_path_module_level_postgresql()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_get_database_path_unsupported()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_database_path_postgresql()** (3 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **Path** (2 connections)
- **Get the database file path. DEPRECATED: PostgreSQL does not use file paths.…** (1 connections) — `server/database.py`
- **Get the database file path (deprecated for PostgreSQL). Returns: Path | None:…** (1 connections) — `server/database.py`
- **Get the database URL from DatabaseManager. Returns: str | None: The database URL** (1 connections) — `server/database.py`
- **Test get_database_path returns None for PostgreSQL.** (1 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **Test get_database_path raises for unsupported URL.** (1 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **Test get_database_path raises for None URL.** (1 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **Test get_database_url initializes database if not already initialized.** (1 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **Test get_database_path handles module-level empty URL.** (1 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **Test get_database_path returns None for module-level PostgreSQL URL.** (1 connections) — `server/tests/unit/infrastructure/test_database_init.py`

## Relationships

- [.reset_instance](reset_instance.md) (8 shared connections)
- [DatabaseManager](DatabaseManager.md) (7 shared connections)
- [test_database_extended.py](test_database_extended.py.md) (6 shared connections)
- [DatabaseError](DatabaseError.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)

## Source Files

- `server/database.py`
- `server/tests/unit/infrastructure/test_database_extended.py`
- `server/tests/unit/infrastructure/test_database_init.py`

## Audit Trail

- EXTRACTED: 38 (86%)
- INFERRED: 6 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*