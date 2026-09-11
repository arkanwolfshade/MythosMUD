# test_database_extended.py

> 43 nodes

## Key Concepts

- **test_database_extended.py** (43 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **get_database_path()** (12 connections) — `server/database.py`
- **get_database_url()** (6 connections) — `server/database.py`
- **test_database_manager_close_dispose_error()** (6 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_close_with_engine()** (6 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_close_without_engine()** (6 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_get_database_path_unsupported()** (6 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_database_path_none_url()** (6 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **.get_database_path()** (5 connections) — `server/database.py`
- **test_database_manager_get_database_path_postgresql()** (5 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_get_database_url_initializes()** (5 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_get_engine_event_loop_check()** (5 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_get_engine_initializes()** (5 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_get_engine_no_running_loop()** (5 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_get_engine_reinitializes_if_none()** (5 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_get_session_maker_initializes()** (5 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_database_url_initializes_database()** (5 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_engine_initializes_database()** (5 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_session_maker_initializes_database()** (5 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_database_path_unsupported()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_database_path_postgresql()** (3 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **Path** (2 connections)
- **Get the database file path. DEPRECATED: PostgreSQL does not use file paths.…** (1 connections) — `server/database.py`
- **Get the database file path (deprecated for PostgreSQL). Returns: Path | None:…** (1 connections) — `server/database.py`
- **Get the database URL from DatabaseManager. Returns: str | None: The database URL** (1 connections) — `server/database.py`
- *... and 18 more nodes in this community*

## Relationships

- [DatabaseManager](DatabaseManager.md) (49 shared connections)
- [get_async_session](get_async_session.md) (15 shared connections)
- [get_logger](get_logger.md) (9 shared connections)
- [reset_database](reset_database.md) (3 shared connections)
- [MemoryMonitor](MemoryMonitor.md) (2 shared connections)
- [get_session_maker](get_session_maker.md) (2 shared connections)
- [ensure_database_directory](ensure_database_directory.md) (2 shared connections)

## Source Files

- `server/database.py`
- `server/tests/unit/infrastructure/test_database_extended.py`

## Audit Trail

- EXTRACTED: 112 (87%)
- INFERRED: 17 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*