# get_async_session

> 48 nodes

## Key Concepts

- **get_async_session()** (53 connections) — `server/database.py`
- **test_database_extended.py** (43 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **asyncio** (12 connections)
- **fetch_professions()** (7 connections) — `server/async_persistence_direct_queries.py`
- **close_db()** (6 connections) — `server/database.py`
- **test_database_manager_close_dispose_error()** (5 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_close_with_engine()** (5 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_close_without_engine()** (5 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **ensure_database_directory()** (4 connections) — `server/database.py`
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
- **test_ensure_database_directory_postgresql()** (3 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_database_path_postgresql()** (3 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_database_path_unsupported()** (3 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **add_flavor_text_column.py** (3 connections) — `scripts/add_flavor_text_column.py`
- **load_seed_using_project_db.py** (3 connections) — `scripts/load_seed_using_project_db.py`
- *... and 23 more nodes in this community*

## Relationships

- [DatabaseError](DatabaseError.md) (13 shared connections)
- [.get_instance](get_instance.md) (10 shared connections)
- [.reset_instance](reset_instance.md) (7 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (6 shared connections)
- [get_database_path](get_database_path.md) (5 shared connections)
- [User](User.md) (4 shared connections)
- [.state](state.md) (3 shared connections)
- [reset_database](reset_database.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (2 shared connections)
- [catatonia_check.py](catatonia_check.py.md) (2 shared connections)
- [admin_teleport_commands.py](admin_teleport_commands.py.md) (2 shared connections)

## Source Files

- `scripts/add_flavor_text_column.py`
- `scripts/load_seed_using_project_db.py`
- `server/async_persistence_direct_queries.py`
- `server/database.py`
- `server/tests/unit/infrastructure/test_database_extended.py`

## Audit Trail

- EXTRACTED: 152 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*