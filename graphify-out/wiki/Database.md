# Database

> 64 nodes

## Key Concepts

- **database.py** (79 connections) — `server/database.py`
- **database_helpers.py** (32 connections) — `server/database_helpers.py`
- **database_config_helpers.py** (21 connections) — `server/database_config_helpers.py`
- **reset_database()** (16 connections) — `server/database.py`
- **generate_invites_db.py** (14 connections) — `tools/invite_tools/generate_invites_db.py`
- **set_test_database_url()** (9 connections) — `server/database_config_helpers.py`
- **reset_database()** (9 connections) — `server/database_helpers.py`
- **main()** (7 connections) — `tools/invite_tools/generate_invites_db.py`
- **get_test_database_url()** (6 connections) — `server/database_config_helpers.py`
- **normalize_database_url()** (6 connections) — `server/database_config_helpers.py`
- **create_invite_in_db()** (6 connections) — `tools/invite_tools/generate_invites_db.py`
- **_create_engine_or_raise()** (5 connections) — `server/database.py`
- **_reset_database_url_state()** (5 connections) — `server/database.py`
- **_sync_test_url_state()** (5 connections) — `server/database.py`
- **_set_database_url_from_env()** (5 connections) — `tools/invite_tools/generate_invites_db.py`
- **configure_pool_settings()** (4 connections) — `server/database_config_helpers.py`
- **load_database_url()** (4 connections) — `server/database_config_helpers.py`
- **validate_database_url()** (4 connections) — `server/database_config_helpers.py`
- **_dispose_engine_safely()** (4 connections) — `server/database.py`
- **_get_database_url_state()** (4 connections) — `server/database.py`
- **_normalize_connect_args_search_path()** (4 connections) — `server/database.py`
- **reset_db_state()** (4 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **reset_db()** (4 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **generate_unique_codes()** (4 connections) — `tools/invite_tools/generate_invites_db.py`
- **get_existing_codes()** (4 connections) — `tools/invite_tools/generate_invites_db.py`
- *... and 39 more nodes in this community*

## Relationships

- [Test Database Error Handling](Test_Database_Error_Handling.md) (26 shared connections)
- [Test Database Helpers](Test_Database_Helpers.md) (15 shared connections)
- [Test Database Extended](Test_Database_Extended.md) (10 shared connections)
- [Wearable Container Service](Wearable_Container_Service.md) (9 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (6 shared connections)
- [Async Persistence Direct Queries](Async_Persistence_Direct_Queries.md) (5 shared connections)
- [Player Model & Migrations](Player_Model_&_Migrations.md) (5 shared connections)
- [Error Handling & Exceptions](Error_Handling_&_Exceptions.md) (5 shared connections)
- [Lucidity & Rescue Service](Lucidity_&_Rescue_Service.md) (4 shared connections)
- [Test Invite](Test_Invite.md) (3 shared connections)
- [Test Npc Database](Test_Npc_Database.md) (3 shared connections)
- [Player Skill Repository](Player_Skill_Repository.md) (3 shared connections)

## Source Files

- `server/database.py`
- `server/database_config_helpers.py`
- `server/database_helpers.py`
- `server/tests/unit/infrastructure/test_database_error_handling.py`
- `server/tests/unit/infrastructure/test_database_init.py`
- `tools/invite_tools/generate_invites_db.py`

## Audit Trail

- EXTRACTED: 226 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*