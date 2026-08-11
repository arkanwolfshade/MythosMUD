# NATS Subject Manager

> 79 nodes

## Key Concepts

- **database.py** (79 connections) — `server/database.py`
- **database_config_helpers.py** (24 connections) — `server/database_config_helpers.py`
- **._initialize_database()** (19 connections) — `server/database.py`
- **generate_invites_db.py** (14 connections) — `tools/invite_tools/generate_invites_db.py`
- **init_db()** (11 connections) — `server/database.py`
- **set_test_database_url()** (11 connections) — `server/database_config_helpers.py`
- **get_postgres_connect_args()** (9 connections) — `server/database_config_helpers.py`
- **_create_engine_or_raise()** (8 connections) — `server/database.py`
- **get_test_database_url()** (7 connections) — `server/database_config_helpers.py`
- **load_database_url()** (7 connections) — `server/database_config_helpers.py`
- **main()** (7 connections) — `tools/invite_tools/generate_invites_db.py`
- **main()** (6 connections) — `scripts/verify_and_load_seed.py`
- **AsyncEngine** (6 connections)
- **validate_database_url()** (6 connections) — `server/database_config_helpers.py`
- **normalize_database_url()** (6 connections) — `server/database_config_helpers.py`
- **create_invite_in_db()** (6 connections) — `tools/invite_tools/generate_invites_db.py`
- **_sync_test_url_state()** (5 connections) — `server/database.py`
- **.get_engine()** (5 connections) — `server/database.py`
- **configure_pool_settings()** (5 connections) — `server/database_config_helpers.py`
- **_set_database_url_from_env()** (5 connections) — `tools/invite_tools/generate_invites_db.py`
- **get_invite_codes.py** (4 connections) — `e2e-tests/load-tests/get_invite_codes.py`
- **get_10_active_invites()** (4 connections) — `e2e-tests/load-tests/get_invite_codes.py`
- **verify_and_load_seed.py** (4 connections) — `scripts/verify_and_load_seed.py`
- **_normalize_connect_args_search_path()** (4 connections) — `server/database.py`
- **_dispose_engine_safely()** (4 connections) — `server/database.py`
- *... and 54 more nodes in this community*

## Relationships

- [Schemas Maps Map](Schemas_Maps_Map.md) (38 shared connections)
- [Spell Registry Costs](Spell_Registry_Costs.md) (35 shared connections)
- [Command Parser Helpers](Command_Parser_Helpers.md) (7 shared connections)
- [Profession Get Mechanical Effects](Profession_Get_Mechanical_Effects.md) (6 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (5 shared connections)
- [Test Migration Report](Test_Migration_Report.md) (4 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (3 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (3 shared connections)
- [Combat Schema Validation](Combat_Schema_Validation.md) (3 shared connections)
- [Container Persistence Layer](Container_Persistence_Layer.md) (3 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (2 shared connections)
- [Alias Storage Layer](Alias_Storage_Layer.md) (2 shared connections)

## Source Files

- `e2e-tests/load-tests/get_invite_codes.py`
- `scripts/verify_and_load_seed.py`
- `server/database.py`
- `server/database_config_helpers.py`
- `server/scripts/check_invite_status.py`
- `server/scripts/list_active_invites.py`
- `server/tests/unit/infrastructure/test_database_extended.py`
- `tools/invite_tools/generate_invites_db.py`

## Audit Trail

- EXTRACTED: 353 (97%)
- INFERRED: 10 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*