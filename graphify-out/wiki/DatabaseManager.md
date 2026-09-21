# DatabaseManager

> 292 nodes

## Key Concepts

- **DatabaseManager** (113 connections) — `server/database.py`
- **.get_instance()** (88 connections) — `server/database.py`
- **.reset_instance()** (87 connections) — `server/database.py`
- **database.py** (85 connections) — `server/database.py`
- **get_async_session()** (61 connections) — `server/database.py`
- **test_database_extended.py** (43 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_error_handling.py** (41 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_database_init.py** (36 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **database_config_helpers.py** (24 connections) — `server/database_config_helpers.py`
- **reset_database()** (16 connections) — `server/database.py`
- **._initialize_database()** (15 connections) — `server/database.py`
- **async_persistence_direct_queries.py** (15 connections) — `server/async_persistence_direct_queries.py`
- **.initialize()** (12 connections) — `server/container/bundles/core.py`
- **get_database_path()** (12 connections) — `server/database.py`
- **asyncio** (12 connections)
- **init_db()** (10 connections) — `server/database.py`
- **fetch_user_by_username_case_insensitive()** (9 connections) — `server/async_persistence_direct_queries.py`
- **set_test_database_url()** (9 connections) — `server/database_config_helpers.py`
- **get_engine()** (9 connections) — `server/database.py`
- **reset_database()** (9 connections) — `server/database_helpers.py`
- **fetch_professions()** (8 connections) — `server/async_persistence_direct_queries.py`
- **_create_engine_or_raise()** (8 connections) — `server/database.py`
- **load_database_url()** (7 connections) — `server/database_config_helpers.py`
- **test_close_handles_attribute_error_during_dispose()** (7 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_database.py** (7 connections) — `server/tests/unit/infrastructure/test_database.py`
- *... and 267 more nodes in this community*

## Relationships

- [test_database_helpers.py](test_database_helpers.py.md) (36 shared connections)
- [DatabaseError](DatabaseError.md) (24 shared connections)
- [ValidationError](ValidationError.md) (21 shared connections)
- [get_session_maker](get_session_maker.md) (19 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (10 shared connections)
- [async_persistence.py](async_persistence.py.md) (7 shared connections)
- [get_config](get_config.md) (6 shared connections)
- [User](User.md) (6 shared connections)
- [Player](Player.md) (5 shared connections)
- [npc_database.py](npc_database.py.md) (5 shared connections)
- [corruption_service.py](corruption_service.py.md) (5 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (4 shared connections)

## Source Files

- `scripts/add_flavor_text_column.py`
- `scripts/load_seed_using_project_db.py`
- `scripts/verify_and_load_seed.py`
- `server/async_persistence_direct_queries.py`
- `server/container/bundles/core.py`
- `server/database.py`
- `server/database_config_helpers.py`
- `server/database_helpers.py`
- `server/tests/unit/infrastructure/test_database.py`
- `server/tests/unit/infrastructure/test_database_error_handling.py`
- `server/tests/unit/infrastructure/test_database_extended.py`
- `server/tests/unit/infrastructure/test_database_helpers.py`
- `server/tests/unit/infrastructure/test_database_init.py`

## Audit Trail

- EXTRACTED: 742 (86%)
- INFERRED: 117 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*