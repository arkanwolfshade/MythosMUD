# useWebSocketConnectionTestFixtures useWe

> 78 nodes

## Key Concepts

- **database.py** (76 connections) — `server/database.py`
- **get_async_session()** (54 connections) — `server/database.py`
- **test_database_extended.py** (43 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **get_database_path()** (12 connections) — `server/database.py`
- **init_db()** (11 connections) — `server/database.py`
- **close_db()** (9 connections) — `server/database.py`
- **get_engine()** (8 connections) — `server/database.py`
- **main()** (6 connections) — `scripts/verify_and_load_seed.py`
- **.get_database_path()** (6 connections) — `server/database.py`
- **Path** (6 connections)
- **get_database_url()** (6 connections) — `server/database.py`
- **test_get_engine_initializes_database()** (5 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_get_database_path_unsupported()** (5 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_database_path_none_url()** (5 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **load_seed_data()** (4 connections) — `scripts/load_seed_using_project_db.py`
- **verify_and_load_seed.py** (4 connections) — `scripts/verify_and_load_seed.py`
- **ensure_database_directory()** (4 connections) — `server/database.py`
- **list_active_invites.py** (4 connections) — `server/scripts/list_active_invites.py`
- **test_get_session_maker_initializes_database()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_database_url_initializes_database()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_get_database_url_initializes()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_get_database_path_postgresql()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_close_without_engine()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_close_dispose_error()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_database_path_unsupported()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- *... and 53 more nodes in this community*

## Relationships

- [Database Access Layer](Database_Access_Layer.md) (32 shared connections)
- [manager subject services](manager_subject_services.md) (14 shared connections)
- [add used user](add_used_user.md) (10 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (9 shared connections)
- [command parser rationale](command_parser_rationale.md) (7 shared connections)
- [command inventory models](command_inventory_models.md) (7 shared connections)
- [endpoints auth rationale](endpoints_auth_rationale.md) (5 shared connections)
- [game models player](game_models_player.md) (5 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (4 shared connections)
- [maps handle ascii](maps_handle_ascii.md) (4 shared connections)
- [player requests schemas](player_requests_schemas.md) (4 shared connections)
- [command factories create](command_factories_create.md) (4 shared connections)

## Source Files

- `scripts/add_flavor_text_column.py`
- `scripts/load_seed_using_project_db.py`
- `scripts/verify_and_load_seed.py`
- `server/database.py`
- `server/scripts/list_active_invites.py`
- `server/tests/unit/infrastructure/test_database_extended.py`

## Audit Trail

- EXTRACTED: 374 (98%)
- INFERRED: 9 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*