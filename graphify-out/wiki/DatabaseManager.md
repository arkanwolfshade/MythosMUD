# DatabaseManager

> 286 nodes

## Key Concepts

- **DatabaseManager** (113 connections) — `server/database.py`
- **.get_instance()** (88 connections) — `server/database.py`
- **.reset_instance()** (87 connections) — `server/database.py`
- **test_database_helpers.py** (48 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_database_error_handling.py** (43 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_database_init.py** (37 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **database_helpers.py** (32 connections) — `server/database_helpers.py`
- **get_database_path()** (17 connections) — `server/database_helpers.py`
- **reset_database()** (16 connections) — `server/database.py`
- **asyncio** (14 connections)
- **get_database_path()** (12 connections) — `server/database.py`
- **get_async_session()** (12 connections) — `server/database_helpers.py`
- **get_session_maker()** (10 connections) — `server/database_helpers.py`
- **get_engine()** (9 connections) — `server/database_helpers.py`
- **reset_database()** (9 connections) — `server/database_helpers.py`
- **close_db()** (8 connections) — `server/database_helpers.py`
- **init_db()** (8 connections) — `server/database_helpers.py`
- **test_database.py** (8 connections) — `server/tests/unit/infrastructure/test_database.py`
- **get_database_url()** (7 connections) — `server/database_helpers.py`
- **test_close_handles_attribute_error_during_dispose()** (7 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **asyncio** (7 connections)
- **ensure_database_directory()** (6 connections) — `server/database_helpers.py`
- **test_close_handles_closed_event_loop()** (6 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_close_handles_dispose_timeout()** (6 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_close_handles_generic_exception_during_dispose()** (6 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- *... and 261 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (72 shared connections)
- [ValidationError](ValidationError.md) (20 shared connections)
- [User](User.md) (4 shared connections)
- [Player](Player.md) (4 shared connections)
- [pytest.md](pytest.md.md) (4 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (2 shared connections)
- [get_config](get_config.md) (1 shared connections)
- [ExplorationService](ExplorationService.md) (1 shared connections)
- [test_auth_utils.py](test_auth_utils.py.md) (1 shared connections)
- [LucidityService](LucidityService.md) (1 shared connections)
- [pydantic.md](pydantic.md.md) (1 shared connections)

## Source Files

- `server/database.py`
- `server/database_helpers.py`
- `server/tests/unit/infrastructure/test_database.py`
- `server/tests/unit/infrastructure/test_database_error_handling.py`
- `server/tests/unit/infrastructure/test_database_extended.py`
- `server/tests/unit/infrastructure/test_database_helpers.py`
- `server/tests/unit/infrastructure/test_database_init.py`

## Audit Trail

- EXTRACTED: 602 (84%)
- INFERRED: 111 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*