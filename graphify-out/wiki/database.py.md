# database.py

> 65 nodes

## Key Concepts

- **database.py** (82 connections) — `server/database.py`
- **database_config_helpers.py** (25 connections) — `server/database_config_helpers.py`
- **._initialize_database()** (15 connections) — `server/database.py`
- **generate_invites_db.py** (14 connections) — `tools/invite_tools/generate_invites_db.py`
- **async_persistence_room_loader.py** (10 connections) — `server/async_persistence_room_loader.py`
- **set_test_database_url()** (9 connections) — `server/database_config_helpers.py`
- **_create_engine_or_raise()** (8 connections) — `server/database.py`
- **load_database_url()** (7 connections) — `server/database_config_helpers.py`
- **main()** (7 connections) — `tools/invite_tools/generate_invites_db.py`
- **get_test_database_url()** (6 connections) — `server/database_config_helpers.py`
- **normalize_database_url()** (6 connections) — `server/database_config_helpers.py`
- **validate_database_url()** (6 connections) — `server/database_config_helpers.py`
- **create_invite_in_db()** (6 connections) — `tools/invite_tools/generate_invites_db.py`
- **configure_pool_settings()** (5 connections) — `server/database_config_helpers.py`
- **.get_session_maker()** (5 connections) — `server/database.py`
- **_sync_test_url_state()** (5 connections) — `server/database.py`
- **_set_database_url_from_env()** (5 connections) — `tools/invite_tools/generate_invites_db.py`
- **verify_and_load_seed.py** (5 connections) — `scripts/verify_and_load_seed.py`
- **main()** (4 connections) — `scripts/verify_and_load_seed.py`
- **.get_engine()** (4 connections) — `server/database.py`
- **_dispose_engine_safely()** (4 connections) — `server/database.py`
- **_normalize_connect_args_search_path()** (4 connections) — `server/database.py`
- **generate_unique_codes()** (4 connections) — `tools/invite_tools/generate_invites_db.py`
- **get_existing_codes()** (4 connections) — `tools/invite_tools/generate_invites_db.py`
- **parse_expires_date()** (4 connections) — `tools/invite_tools/generate_invites_db.py`
- *... and 40 more nodes in this community*

## Relationships

- [DatabaseManager](DatabaseManager.md) (28 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (14 shared connections)
- [get_session_maker](get_session_maker.md) (11 shared connections)
- [log_and_raise](log_and_raise.md) (9 shared connections)
- [Player](Player.md) (9 shared connections)
- [CombatInstance](CombatInstance.md) (5 shared connections)
- [ValidationError](ValidationError.md) (5 shared connections)
- [DatabaseError](DatabaseError.md) (5 shared connections)
- [npc_database.py](npc_database.py.md) (4 shared connections)
- [Invite](Invite.md) (4 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (4 shared connections)
- [test_zone_config_loader.py](test_zone_config_loader.py.md) (4 shared connections)

## Source Files

- `scripts/add_flavor_text_column.py`
- `scripts/load_seed_using_project_db.py`
- `scripts/verify_and_load_seed.py`
- `server/async_persistence_room_loader.py`
- `server/database.py`
- `server/database_config_helpers.py`
- `tools/invite_tools/generate_invites_db.py`

## Audit Trail

- EXTRACTED: 221 (98%)
- INFERRED: 5 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*