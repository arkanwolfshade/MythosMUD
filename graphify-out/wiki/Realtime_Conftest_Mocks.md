# Realtime Conftest Mocks

> 164 nodes

## Key Concepts

- **database.py** (79 connections) — `server/database.py`
- **error_logging.py** (55 connections) — `server/utils/error_logging.py`
- **get_async_session()** (53 connections) — `server/database.py`
- **test_database_extended.py** (43 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **database_config_helpers.py** (24 connections) — `server/database_config_helpers.py`
- **._initialize_database()** (19 connections) — `server/database.py`
- **profession_repository.py** (17 connections) — `server/persistence/repositories/profession_repository.py`
- **reset_database()** (16 connections) — `server/database.py`
- **async_persistence_direct_queries.py** (15 connections) — `server/async_persistence_direct_queries.py`
- **generate_invites_db.py** (14 connections) — `tools/invite_tools/generate_invites_db.py`
- **spell_repository.py** (13 connections) — `server/persistence/repositories/spell_repository.py`
- **get_database_path()** (12 connections) — `server/database.py`
- **init_db()** (11 connections) — `server/database.py`
- **set_test_database_url()** (11 connections) — `server/database_config_helpers.py`
- **profession.py** (10 connections) — `server/models/profession.py`
- **fetch_user_by_username_case_insensitive()** (9 connections) — `server/async_persistence_direct_queries.py`
- **fetch_professions()** (9 connections) — `server/async_persistence_direct_queries.py`
- **async_persistence_room_loader.py** (9 connections) — `server/async_persistence_room_loader.py`
- **close_db()** (9 connections) — `server/database.py`
- **get_postgres_connect_args()** (9 connections) — `server/database_config_helpers.py`
- **_create_engine_or_raise()** (8 connections) — `server/database.py`
- **get_engine()** (8 connections) — `server/database.py`
- **get_test_database_url()** (7 connections) — `server/database_config_helpers.py`
- **load_database_url()** (7 connections) — `server/database_config_helpers.py`
- **main()** (7 connections) — `tools/invite_tools/generate_invites_db.py`
- *... and 139 more nodes in this community*

## Relationships

- [Spell Registry Costs](Spell_Registry_Costs.md) (61 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (52 shared connections)
- [React Node Upgrade Summary](React_Node_Upgrade_Summary.md) (18 shared connections)
- [Client Event Store](Client_Event_Store.md) (15 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (15 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (10 shared connections)
- [Playwright Remediation Plan](Playwright_Remediation_Plan.md) (10 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (7 shared connections)
- [Ground and Rescue Commands](Ground_and_Rescue_Commands.md) (6 shared connections)
- [Rest Command Flow](Rest_Command_Flow.md) (5 shared connections)
- [Chat Channel Logger](Chat_Channel_Logger.md) (5 shared connections)
- [Chat Logger Service Tests](Chat_Logger_Service_Tests.md) (5 shared connections)

## Source Files

- `scripts/add_flavor_text_column.py`
- `scripts/load_seed_using_project_db.py`
- `scripts/verify_and_load_seed.py`
- `server/async_persistence.py`
- `server/async_persistence_direct_queries.py`
- `server/async_persistence_room_loader.py`
- `server/database.py`
- `server/database_config_helpers.py`
- `server/models/profession.py`
- `server/persistence/repositories/profession_repository.py`
- `server/persistence/repositories/spell_repository.py`
- `server/tests/unit/infrastructure/test_database_error_handling.py`
- `server/tests/unit/infrastructure/test_database_extended.py`
- `server/tests/unit/infrastructure/test_database_init.py`
- `server/utils/error_logging.py`
- `tools/invite_tools/generate_invites_db.py`

## Audit Trail

- EXTRACTED: 777 (97%)
- INFERRED: 25 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*