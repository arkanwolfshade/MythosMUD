# DatabaseManager

> 325 nodes

## Key Concepts

- **DatabaseManager** (113 connections) — `server/database.py`
- **.get_instance()** (88 connections) — `server/database.py`
- **.reset_instance()** (87 connections) — `server/database.py`
- **test_database_helpers.py** (48 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_database_extended.py** (44 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_error_handling.py** (43 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_database_init.py** (37 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **database_helpers.py** (32 connections) — `server/database_helpers.py`
- **get_database_path()** (17 connections) — `server/database_helpers.py`
- **reset_database()** (16 connections) — `server/database.py`
- **asyncio** (14 connections)
- **get_database_path()** (12 connections) — `server/database.py`
- **get_async_session()** (12 connections) — `server/database_helpers.py`
- **asyncio** (12 connections)
- **get_session_maker()** (10 connections) — `server/database_helpers.py`
- **init_db()** (10 connections) — `server/database.py`
- **get_engine()** (9 connections) — `server/database_helpers.py`
- **reset_database()** (9 connections) — `server/database_helpers.py`
- **close_db()** (8 connections) — `server/database_helpers.py`
- **init_db()** (8 connections) — `server/database_helpers.py`
- **test_database.py** (8 connections) — `server/tests/unit/infrastructure/test_database.py`
- **get_engine()** (7 connections) — `server/database.py`
- **get_database_url()** (7 connections) — `server/database_helpers.py`
- **test_close_handles_attribute_error_during_dispose()** (7 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **asyncio** (7 connections)
- *... and 300 more nodes in this community*

## Relationships

- [database.py](database.py.md) (28 shared connections)
- [ValidationError](ValidationError.md) (22 shared connections)
- [DatabaseError](DatabaseError.md) (8 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (8 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (5 shared connections)
- [pytest.md](pytest.md.md) (5 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (3 shared connections)
- [get_session_maker](get_session_maker.md) (3 shared connections)
- [lucidity.py](lucidity.py.md) (3 shared connections)
- [ExplorationService](ExplorationService.md) (2 shared connections)
- [DistributedEventBus](DistributedEventBus.md) (2 shared connections)
- [Player](Player.md) (2 shared connections)

## Source Files

- `server/database.py`
- `server/database_helpers.py`
- `server/tests/unit/infrastructure/test_database.py`
- `server/tests/unit/infrastructure/test_database_error_handling.py`
- `server/tests/unit/infrastructure/test_database_extended.py`
- `server/tests/unit/infrastructure/test_database_helpers.py`
- `server/tests/unit/infrastructure/test_database_init.py`

## Audit Trail

- EXTRACTED: 670 (85%)
- INFERRED: 118 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*