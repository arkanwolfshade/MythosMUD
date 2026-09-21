# test_database_helpers.py

> 89 nodes

## Key Concepts

- **test_database_helpers.py** (46 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **database_helpers.py** (30 connections) — `server/database_helpers.py`
- **get_database_path()** (17 connections) — `server/database_helpers.py`
- **asyncio** (14 connections)
- **get_async_session()** (12 connections) — `server/database_helpers.py`
- **get_session_maker()** (10 connections) — `server/database_helpers.py`
- **get_engine()** (9 connections) — `server/database_helpers.py`
- **close_db()** (8 connections) — `server/database_helpers.py`
- **init_db()** (8 connections) — `server/database_helpers.py`
- **get_database_url()** (7 connections) — `server/database_helpers.py`
- **ensure_database_directory()** (6 connections) — `server/database_helpers.py`
- **test_get_engine_raises_validation_error()** (6 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_session_maker_raises_validation_error()** (6 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_close_db_engine_initialization_failure()** (5 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_database_url()** (5 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_database_url_returns_none()** (5 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_engine()** (5 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_session_maker()** (5 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **_get_database_url_state()** (4 connections) — `server/database.py`
- **reset_db()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_close_db_raises_runtime_error_on_failure()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_close_db_success()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_async_session_finally_block_executes()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_async_session_http_exception_passthrough()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_async_session_http_exception_propagates()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- *... and 64 more nodes in this community*

## Relationships

- [DatabaseManager](DatabaseManager.md) (36 shared connections)
- [ValidationError](ValidationError.md) (8 shared connections)
- [PlayerLucidity](PlayerLucidity.md) (4 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (2 shared connections)
- [Invite](Invite.md) (1 shared connections)
- [Player](Player.md) (1 shared connections)
- [User](User.md) (1 shared connections)

## Source Files

- `server/database.py`
- `server/database_helpers.py`
- `server/tests/unit/infrastructure/test_database_helpers.py`

## Audit Trail

- EXTRACTED: 184 (93%)
- INFERRED: 14 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*