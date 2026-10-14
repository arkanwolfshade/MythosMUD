# get_engine

> 11 nodes

## Key Concepts

- **get_engine()** (9 connections) — `server/database.py`
- **test_get_engine_initializes_database()** (5 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **.get_engine()** (4 connections) — `server/database.py`
- **_dispose_engine_safely()** (4 connections) — `server/database.py`
- **AsyncEngine** (4 connections)
- **.close()** (3 connections) — `server/database.py`
- **Dispose database engine with Windows/asyncpg-safe cleanup.** (1 connections) — `server/database.py`
- **Get the database engine, initializing if necessary. Returns: AsyncEngine: The…** (1 connections) — `server/database.py`
- **Close database connections.** (1 connections) — `server/database.py`
- **Get the database engine from DatabaseManager. Returns: AsyncEngine: The…** (1 connections) — `server/database.py`
- **Test get_engine initializes database if not already initialized.** (1 connections) — `server/tests/unit/infrastructure/test_database_extended.py`

## Relationships

- [DatabaseManager](DatabaseManager.md) (5 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [connection_initialization.py](connection_initialization.py.md) (2 shared connections)
- [test_database_extended.py](test_database_extended.py.md) (2 shared connections)
- [.initialize](initialize.md) (1 shared connections)

## Source Files

- `server/database.py`
- `server/tests/unit/infrastructure/test_database_extended.py`

## Audit Trail

- EXTRACTED: 23 (96%)
- INFERRED: 1 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*