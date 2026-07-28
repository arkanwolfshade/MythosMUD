# Server Infrastructure (5)

> 90 nodes

## Key Concepts

- **test_database_helpers.py** (46 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **get_database_path()** (16 connections) — `server/database_helpers.py`
- **get_async_session()** (13 connections) — `server/database_helpers.py`
- **get_engine()** (9 connections) — `server/database_helpers.py`
- **get_session_maker()** (9 connections) — `server/database_helpers.py`
- **close_db()** (9 connections) — `server/database_helpers.py`
- **reset_database()** (8 connections) — `server/database_helpers.py`
- **init_db()** (8 connections) — `server/database_helpers.py`
- **ensure_database_directory()** (7 connections) — `server/database_helpers.py`
- **get_database_url()** (6 connections) — `server/database_helpers.py`
- **_reset_database_url_state()** (5 connections) — `server/database.py`
- **test_get_engine_raises_validation_error()** (5 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_session_maker_raises_validation_error()** (5 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **_get_database_url_state()** (4 connections) — `server/database.py`
- **AsyncSession** (4 connections)
- **test_reset_database()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_engine()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_session_maker()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_database_url()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_database_url_returns_none()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_database_path_unsupported_url_raises()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_database_path_empty_string_url_raises()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_close_db_engine_initialization_failure()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **AsyncEngine** (3 connections)
- **async_sessionmaker** (3 connections)
- *... and 65 more nodes in this community*

## Relationships

- [Server Infrastructure (2)](Server_Infrastructure_%282%29.md) (20 shared connections)
- [Server Services](Server_Services.md) (12 shared connections)
- [Server Utils](Server_Utils.md) (11 shared connections)
- [Server Admin](Server_Admin.md) (4 shared connections)
- [Server Tools](Server_Tools.md) (2 shared connections)
- [Server Infrastructure](Server_Infrastructure.md) (1 shared connections)
- [Server Infrastructure (7)](Server_Infrastructure_%287%29.md) (1 shared connections)

## Source Files

- `server/database.py`
- `server/database_helpers.py`
- `server/npc_database.py`
- `server/tests/unit/infrastructure/test_database_helpers.py`

## Audit Trail

- EXTRACTED: 292 (96%)
- INFERRED: 11 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*