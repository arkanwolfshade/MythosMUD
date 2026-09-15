# DatabaseManager

> 357 nodes

## Key Concepts

- **DatabaseManager** (113 connections) — `server/database.py`
- **.get_instance()** (88 connections) — `server/database.py`
- **.reset_instance()** (87 connections) — `server/database.py`
- **get_async_session()** (61 connections) — `server/database.py`
- **test_database_helpers.py** (46 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_database_extended.py** (43 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_error_handling.py** (41 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_database_init.py** (36 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **database_helpers.py** (30 connections) — `server/database_helpers.py`
- **get_database_path()** (17 connections) — `server/database_helpers.py`
- **reset_database()** (16 connections) — `server/database.py`
- **._initialize_database()** (15 connections) — `server/database.py`
- **asyncio** (14 connections)
- **.initialize()** (12 connections) — `server/container/bundles/core.py`
- **get_database_path()** (12 connections) — `server/database.py`
- **get_async_session()** (12 connections) — `server/database_helpers.py`
- **asyncio** (12 connections)
- **get_session_maker()** (10 connections) — `server/database_helpers.py`
- **init_db()** (10 connections) — `server/database.py`
- **get_engine()** (9 connections) — `server/database.py`
- **get_engine()** (9 connections) — `server/database_helpers.py`
- **reset_database()** (9 connections) — `server/database_helpers.py`
- **close_db()** (8 connections) — `server/database_helpers.py`
- **init_db()** (8 connections) — `server/database_helpers.py`
- **get_database_url()** (7 connections) — `server/database_helpers.py`
- *... and 332 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (81 shared connections)
- [get_session_maker](get_session_maker.md) (11 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (4 shared connections)
- [get_config](get_config.md) (3 shared connections)
- [rescue_commands.py](rescue_commands.py.md) (3 shared connections)
- [cleanse_command.py](cleanse_command.py.md) (3 shared connections)
- [LucidityService](LucidityService.md) (3 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (2 shared connections)
- [catatonia_check.py](catatonia_check.py.md) (2 shared connections)
- [admin_hallucinate_command.py](admin_hallucinate_command.py.md) (2 shared connections)
- [test_admin_setlucidity_command.py](test_admin_setlucidity_command.py.md) (2 shared connections)
- [admin_setstat_command.py](admin_setstat_command.py.md) (2 shared connections)

## Source Files

- `scripts/add_flavor_text_column.py`
- `scripts/load_seed_using_project_db.py`
- `scripts/verify_and_load_seed.py`
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

- EXTRACTED: 780 (87%)
- INFERRED: 113 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*