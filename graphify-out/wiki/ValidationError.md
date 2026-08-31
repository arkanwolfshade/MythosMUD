# ValidationError

> 406 nodes

## Key Concepts

- **ValidationError** (314 connections) — `server/exceptions.py`
- **DatabaseManager** (113 connections) — `server/database.py`
- **.get_instance()** (88 connections) — `server/database.py`
- **.reset_instance()** (87 connections) — `server/database.py`
- **database.py** (83 connections) — `server/database.py`
- **get_async_session()** (53 connections) — `server/database.py`
- **test_database_helpers.py** (48 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_database_extended.py** (44 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_error_handling.py** (43 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_database_init.py** (37 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **database_helpers.py** (32 connections) — `server/database_helpers.py`
- **test_command_helpers.py** (28 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **database_config_helpers.py** (24 connections) — `server/database_config_helpers.py`
- **get_database_path()** (17 connections) — `server/database_helpers.py`
- **reset_database()** (16 connections) — `server/database.py`
- **async_persistence_direct_queries.py** (16 connections) — `server/async_persistence_direct_queries.py`
- **._initialize_database()** (15 connections) — `server/database.py`
- **asyncio** (14 connections)
- **.initialize()** (12 connections) — `server/container/bundles/core.py`
- **get_database_path()** (12 connections) — `server/database.py`
- **get_async_session()** (12 connections) — `server/database_helpers.py`
- **asyncio** (12 connections)
- **get_session_maker()** (10 connections) — `server/database_helpers.py`
- **init_db()** (10 connections) — `server/database.py`
- **MythosValidationError** (10 connections)
- *... and 381 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (25 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (24 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (19 shared connections)
- [pytest.md](pytest.md.md) (19 shared connections)
- [log_and_raise](log_and_raise.md) (18 shared connections)
- [UtilityCommandFactory](UtilityCommandFactory.md) (18 shared connections)
- [test_command_parser.py](test_command_parser.py.md) (16 shared connections)
- [DatabaseError](DatabaseError.md) (16 shared connections)
- [CommunicationCommandFactory](CommunicationCommandFactory.md) (15 shared connections)
- [npc_database.py](npc_database.py.md) (13 shared connections)
- [AliasStorage](AliasStorage.md) (12 shared connections)
- [log_and_raise_enhanced](log_and_raise_enhanced.md) (12 shared connections)

## Source Files

- `scripts/add_flavor_text_column.py`
- `scripts/load_seed_using_project_db.py`
- `scripts/verify_and_load_seed.py`
- `server/async_persistence.py`
- `server/async_persistence_direct_queries.py`
- `server/async_persistence_room_loader.py`
- `server/container/bundles/core.py`
- `server/database.py`
- `server/database_config_helpers.py`
- `server/database_helpers.py`
- `server/exceptions.py`
- `server/tests/unit/api/test_container_exception_handlers.py`
- `server/tests/unit/commands/test_command_service.py`
- `server/tests/unit/infrastructure/test_database.py`
- `server/tests/unit/infrastructure/test_database_error_handling.py`
- `server/tests/unit/infrastructure/test_database_extended.py`
- `server/tests/unit/infrastructure/test_database_helpers.py`
- `server/tests/unit/infrastructure/test_database_init.py`
- `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- `server/tests/unit/utils/test_command_helpers.py`

## Audit Trail

- EXTRACTED: 1080 (78%)
- INFERRED: 301 (22%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*