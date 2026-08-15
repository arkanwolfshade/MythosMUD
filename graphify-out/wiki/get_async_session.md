# get_async_session

> 48 nodes

## Key Concepts

- **get_async_session()** (53 connections) — `server/database.py`
- **._initialize_database()** (15 connections) — `server/database.py`
- **generate_invites_db.py** (14 connections) — `tools/invite_tools/generate_invites_db.py`
- **set_test_database_url()** (9 connections) — `server/database_config_helpers.py`
- **main()** (7 connections) — `tools/invite_tools/generate_invites_db.py`
- **normalize_database_url()** (6 connections) — `server/database_config_helpers.py`
- **create_invite_in_db()** (6 connections) — `tools/invite_tools/generate_invites_db.py`
- **.get_session_maker()** (5 connections) — `server/database.py`
- **_sync_test_url_state()** (5 connections) — `server/database.py`
- **_set_database_url_from_env()** (5 connections) — `tools/invite_tools/generate_invites_db.py`
- **main()** (4 connections) — `scripts/verify_and_load_seed.py`
- **.get_engine()** (4 connections) — `server/database.py`
- **_dispose_engine_safely()** (4 connections) — `server/database.py`
- **generate_unique_codes()** (4 connections) — `tools/invite_tools/generate_invites_db.py`
- **get_existing_codes()** (4 connections) — `tools/invite_tools/generate_invites_db.py`
- **parse_expires_date()** (4 connections) — `tools/invite_tools/generate_invites_db.py`
- **verify_and_load_seed.py** (4 connections) — `scripts/verify_and_load_seed.py`
- **AsyncEngine** (4 connections)
- **add_flavor_text_column()** (3 connections) — `scripts/add_flavor_text_column.py`
- **load_seed_data()** (3 connections) — `scripts/load_seed_using_project_db.py`
- **.close()** (3 connections) — `server/database.py`
- **.get_database_url()** (3 connections) — `server/database.py`
- **generate_invite_code()** (3 connections) — `tools/invite_tools/generate_invites_db.py`
- **add_flavor_text_column.py** (3 connections) — `scripts/add_flavor_text_column.py`
- **load_seed_using_project_db.py** (3 connections) — `scripts/load_seed_using_project_db.py`
- *... and 23 more nodes in this community*

## Relationships

- [DatabaseError](DatabaseError.md) (26 shared connections)
- [DatabaseManager](DatabaseManager.md) (15 shared connections)
- [models/user.py](models-user.py.md) (4 shared connections)
- [database_config_helpers.py](database_config_helpers.py.md) (3 shared connections)
- [rescue_commands.py](rescue_commands.py.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [get_config](get_config.md) (2 shared connections)
- [api/player_respawn.py](api-player_respawn.py.md) (2 shared connections)
- [catatonia_check.py](catatonia_check.py.md) (2 shared connections)
- [test_admin_setlucidity_command.py](test_admin_setlucidity_command.py.md) (2 shared connections)
- [test_channel_commands.py](test_channel_commands.py.md) (2 shared connections)
- [debrief_command.py](debrief_command.py.md) (2 shared connections)

## Source Files

- `scripts/add_flavor_text_column.py`
- `scripts/load_seed_using_project_db.py`
- `scripts/verify_and_load_seed.py`
- `server/database.py`
- `server/database_config_helpers.py`
- `tools/invite_tools/generate_invites_db.py`

## Audit Trail

- EXTRACTED: 143 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*