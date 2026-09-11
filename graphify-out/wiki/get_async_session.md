# get_async_session

> 31 nodes

## Key Concepts

- **get_async_session()** (59 connections) — `server/database.py`
- **asyncio** (12 connections)
- **init_db()** (10 connections) — `server/database.py`
- **close_db()** (6 connections) — `server/database.py`
- **test_close_db_error()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_close_db_success()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_async_session_http_exception_re_raised()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_async_session_rollback_error()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_async_session_rollback_on_error()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_async_session_success()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_init_db_connection_error()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_init_db_import_error()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_init_db_success()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **add_flavor_text_column()** (3 connections) — `scripts/add_flavor_text_column.py`
- **load_seed_data()** (3 connections) — `scripts/load_seed_using_project_db.py`
- **add_flavor_text_column.py** (3 connections) — `scripts/add_flavor_text_column.py`
- **load_seed_using_project_db.py** (3 connections) — `scripts/load_seed_using_project_db.py`
- **Add flavor_text column if missing.** (1 connections) — `scripts/add_flavor_text_column.py`
- **Load all seed data files.** (1 connections) — `scripts/load_seed_using_project_db.py`
- **Get an async database session as an async context manager. Usage: async for…** (1 connections) — `server/database.py`
- **Initialize the database (deprecated - kept for backward compatibility). This…** (1 connections) — `server/database.py`
- **Close database connections. This closes the database manager's engine and…** (1 connections) — `server/database.py`
- **Test get_async_session creates and yields session successfully.** (1 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **Test get_async_session re-raises HTTPException.** (1 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **Test get_async_session rolls back on error.** (1 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- *... and 6 more nodes in this community*

## Relationships

- [test_database_extended.py](test_database_extended.py.md) (15 shared connections)
- [get_logger](get_logger.md) (11 shared connections)
- [Player](Player.md) (7 shared connections)
- [User](User.md) (3 shared connections)
- [DatabaseManager](DatabaseManager.md) (2 shared connections)
- [Room](Room.md) (2 shared connections)
- [catatonia_check.py](catatonia_check.py.md) (2 shared connections)
- [admin_hallucinate_command.py](admin_hallucinate_command.py.md) (2 shared connections)
- [test_admin_setlucidity_command.py](test_admin_setlucidity_command.py.md) (2 shared connections)
- [test_channel_commands.py](test_channel_commands.py.md) (2 shared connections)
- [LucidityService](LucidityService.md) (2 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (2 shared connections)

## Source Files

- `scripts/add_flavor_text_column.py`
- `scripts/load_seed_using_project_db.py`
- `server/database.py`
- `server/tests/unit/infrastructure/test_database_extended.py`

## Audit Trail

- EXTRACTED: 110 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*