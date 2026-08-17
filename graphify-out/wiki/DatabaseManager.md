# DatabaseManager

> 275 nodes

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
- **get_async_session()** (12 connections) — `server/database_helpers.py`
- **get_session_maker()** (10 connections) — `server/database_helpers.py`
- **set_test_database_url()** (9 connections) — `server/database_config_helpers.py`
- **get_engine()** (9 connections) — `server/database_helpers.py`
- **reset_database()** (9 connections) — `server/database_helpers.py`
- **close_db()** (8 connections) — `server/database_helpers.py`
- **init_db()** (8 connections) — `server/database_helpers.py`
- **test_database.py** (8 connections) — `server/tests/unit/infrastructure/test_database.py`
- **get_database_url()** (7 connections) — `server/database_helpers.py`
- **test_close_handles_attribute_error_during_dispose()** (7 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **asyncio** (7 connections)
- **get_test_database_url()** (6 connections) — `server/database_config_helpers.py`
- **ensure_database_directory()** (6 connections) — `server/database_helpers.py`
- **test_close_handles_closed_event_loop()** (6 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_close_handles_dispose_timeout()** (6 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- *... and 250 more nodes in this community*

## Relationships

- [test_database_extended.py](test_database_extended.py.md) (41 shared connections)
- [ValidationError](ValidationError.md) (19 shared connections)
- [get_session_maker](get_session_maker.md) (14 shared connections)
- [DatabaseError](DatabaseError.md) (12 shared connections)
- [database_config_helpers.py](database_config_helpers.py.md) (9 shared connections)
- [pytest.md](pytest.md.md) (5 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (3 shared connections)
- [lucidity.py](lucidity.py.md) (3 shared connections)
- [User](User.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [ExplorationService](ExplorationService.md) (1 shared connections)
- [._get_room_uuid_by_stable_id](_get_room_uuid_by_stable_id.md) (1 shared connections)

## Source Files

- `server/database.py`
- `server/database_config_helpers.py`
- `server/database_helpers.py`
- `server/tests/unit/infrastructure/test_database.py`
- `server/tests/unit/infrastructure/test_database_error_handling.py`
- `server/tests/unit/infrastructure/test_database_extended.py`
- `server/tests/unit/infrastructure/test_database_helpers.py`
- `server/tests/unit/infrastructure/test_database_init.py`

## Audit Trail

- EXTRACTED: 583 (83%)
- INFERRED: 116 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*