# Database Access Layer

> 284 nodes

## Key Concepts

- **.get_instance()** (88 connections) — `server/database.py`
- **.reset_instance()** (87 connections) — `server/database.py`
- **database.py** (76 connections) — `server/database.py`
- **get_async_session()** (54 connections) — `server/database.py`
- **test_database_extended.py** (43 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_error_handling.py** (41 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_database_init.py** (36 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **DatabaseManager** (29 connections) — `server/database.py`
- **npc_database.py** (27 connections) — `server/npc_database.py`
- **database_config_helpers.py** (24 connections) — `server/database_config_helpers.py`
- **._initialize_database()** (17 connections) — `server/database.py`
- **channel_commands.py** (16 connections) — `server/commands/channel_commands.py`
- **reset_database()** (16 connections) — `server/database.py`
- **get_database_path()** (12 connections) — `server/database.py`
- **init_db()** (11 connections) — `server/database.py`
- **async_persistence_room_loader.py** (9 connections) — `server/async_persistence_room_loader.py`
- **handle_channel_command()** (9 connections) — `server/commands/channel_commands.py`
- **close_db()** (9 connections) — `server/database.py`
- **set_test_database_url()** (9 connections) — `server/database_config_helpers.py`
- **get_postgres_connect_args()** (9 connections) — `server/database_config_helpers.py`
- **get_engine()** (8 connections) — `server/database.py`
- **load_database_url()** (7 connections) — `server/database_config_helpers.py`
- **test_database.py** (7 connections) — `server/tests/unit/infrastructure/test_database.py`
- **main()** (6 connections) — `scripts/verify_and_load_seed.py`
- **_handle_default_channel_setting()** (6 connections) — `server/commands/channel_commands.py`
- *... and 259 more nodes in this community*

## Relationships

- [Database Config](Database_Config.md) (66 shared connections)
- [command inventory models](command_inventory_models.md) (54 shared connections)
- [commands admin mute](commands_admin_mute.md) (12 shared connections)
- [command commands talk](command_commands_talk.md) (11 shared connections)
- [command inventory factories](command_inventory_factories.md) (7 shared connections)
- [Item Instances](Item_Instances.md) (6 shared connections)
- [auth users rationale](auth_users_rationale.md) (6 shared connections)
- [Error Conversion](Error_Conversion.md) (6 shared connections)
- [admin auth service](admin_auth_service.md) (5 shared connections)
- [player requests schemas](player_requests_schemas.md) (5 shared connections)
- [command helpers functions](command_helpers_functions.md) (4 shared connections)
- [lucidity npc combat](lucidity_npc_combat.md) (4 shared connections)

## Source Files

- `e2e-tests/load-tests/get_invite_codes.py`
- `scripts/add_flavor_text_column.py`
- `scripts/load_seed_using_project_db.py`
- `scripts/verify_and_load_seed.py`
- `server/async_persistence_room_loader.py`
- `server/commands/channel_commands.py`
- `server/database.py`
- `server/database_config_helpers.py`
- `server/npc_database.py`
- `server/tests/unit/infrastructure/test_database.py`
- `server/tests/unit/infrastructure/test_database_error_handling.py`
- `server/tests/unit/infrastructure/test_database_extended.py`
- `server/tests/unit/infrastructure/test_database_init.py`

## Audit Trail

- EXTRACTED: 1255 (96%)
- INFERRED: 56 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*