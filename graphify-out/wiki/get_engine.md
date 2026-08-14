# get_engine

> 7 nodes

## Key Concepts

- **get_engine()** (8 connections) — `server/database_helpers.py`
- **test_get_engine_raises_validation_error()** (5 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_engine()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **AsyncEngine** (1 connections)
- **Get the database engine, initializing if necessary. Returns: AsyncEngine: The…** (1 connections) — `server/database_helpers.py`
- **Test get_engine returns engine from DatabaseManager.** (1 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **Test get_engine raises ValidationError when database cannot be initialized.** (1 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`

## Relationships

- [test_database_helpers.py](test_database_helpers.py.md) (4 shared connections)
- [.get_instance](get_instance.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)

## Source Files

- `server/database_helpers.py`
- `server/tests/unit/infrastructure/test_database_helpers.py`

## Audit Trail

- EXTRACTED: 15 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*