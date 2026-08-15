# DatabaseManager

> 327 nodes

## Key Concepts

- **DatabaseManager** (113 connections) — `server/database.py`
- **.get_instance()** (88 connections) — `server/database.py`
- **.reset_instance()** (87 connections) — `server/database.py`
- **test_database_helpers.py** (46 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_database_extended.py** (43 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_error_handling.py** (41 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_database_init.py** (36 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **database_helpers.py** (30 connections) — `server/database_helpers.py`
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
- **get_engine()** (7 connections) — `server/database.py`
- **get_database_url()** (7 connections) — `server/database_helpers.py`
- **test_close_handles_attribute_error_during_dispose()** (7 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_database.py** (7 connections) — `server/tests/unit/infrastructure/test_database.py`
- **asyncio** (7 connections)
- *... and 302 more nodes in this community*

## Relationships

- [DatabaseError](DatabaseError.md) (34 shared connections)
- [ValidationError](ValidationError.md) (22 shared connections)
- [get_async_session](get_async_session.md) (15 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (5 shared connections)
- [Player](Player.md) (5 shared connections)
- [database_config_helpers.py](database_config_helpers.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [RoomService](RoomService.md) (1 shared connections)
- [._get_room_uuid_by_stable_id](_get_room_uuid_by_stable_id.md) (1 shared connections)
- [AttributeError](AttributeError.md) (1 shared connections)
- [models/user.py](models-user.py.md) (1 shared connections)
- [User](User.md) (1 shared connections)

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

- EXTRACTED: 665 (85%)
- INFERRED: 118 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*