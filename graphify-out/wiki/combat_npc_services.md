# combat npc services

> 35 nodes

## Key Concepts

- **database.py** (76 connections) — `server/database.py`
- **get_async_session()** (54 connections) — `server/database.py`
- **async_persistence_direct_queries.py** (15 connections) — `server/async_persistence_direct_queries.py`
- **fetch_user_by_username_case_insensitive()** (9 connections) — `server/async_persistence_direct_queries.py`
- **fetch_professions()** (9 connections) — `server/async_persistence_direct_queries.py`
- **async_persistence_room_loader.py** (9 connections) — `server/async_persistence_room_loader.py`
- **main()** (6 connections) — `scripts/verify_and_load_seed.py`
- **.get_database_path()** (6 connections) — `server/database.py`
- **Path** (6 connections)
- **get_database_url()** (6 connections) — `server/database.py`
- **load_seed_data()** (4 connections) — `scripts/load_seed_using_project_db.py`
- **verify_and_load_seed.py** (4 connections) — `scripts/verify_and_load_seed.py`
- **.get_user_by_username_case_insensitive()** (4 connections) — `server/async_persistence.py`
- **test_get_database_url_initializes_database()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **add_flavor_text_column.py** (3 connections) — `scripts/add_flavor_text_column.py`
- **add_flavor_text_column()** (3 connections) — `scripts/add_flavor_text_column.py`
- **load_seed_using_project_db.py** (3 connections) — `scripts/load_seed_using_project_db.py`
- **Profession** (3 connections)
- **test_get_async_session_http_exception_re_raised()** (3 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_async_session_rollback_on_error()** (3 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **Add flavor_text column if missing.** (1 connections) — `scripts/add_flavor_text_column.py`
- **Load all seed data files.** (1 connections) — `scripts/load_seed_using_project_db.py`
- **Load seed data and verify.** (1 connections) — `scripts/verify_and_load_seed.py`
- **Get a user by username (case-insensitive).          MULTI-CHARACTER: Usernames a** (1 connections) — `server/async_persistence.py`
- **Direct async SQL queries used by AsyncPersistenceLayer.  Extracted to keep async** (1 connections) — `server/async_persistence_direct_queries.py`
- *... and 10 more nodes in this community*

## Relationships

- [Database Config](Database_Config.md) (29 shared connections)
- [memory lifespan app](memory_lifespan_app.md) (12 shared connections)
- [command inventory models](command_inventory_models.md) (8 shared connections)
- [models npc rationale](models_npc_rationale.md) (7 shared connections)
- [NPC Combat](NPC_Combat.md) (7 shared connections)
- [admin auth service](admin_auth_service.md) (7 shared connections)
- [commands lucidity recovery](commands_lucidity_recovery.md) (7 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (6 shared connections)
- [command inventory factories](command_inventory_factories.md) (5 shared connections)
- [manager subject services](manager_subject_services.md) (5 shared connections)
- [player requests schemas](player_requests_schemas.md) (4 shared connections)
- [command helpers functions](command_helpers_functions.md) (4 shared connections)

## Source Files

- `scripts/add_flavor_text_column.py`
- `scripts/load_seed_using_project_db.py`
- `scripts/verify_and_load_seed.py`
- `server/async_persistence.py`
- `server/async_persistence_direct_queries.py`
- `server/async_persistence_room_loader.py`
- `server/database.py`
- `server/tests/unit/infrastructure/test_database_extended.py`

## Audit Trail

- EXTRACTED: 234 (96%)
- INFERRED: 11 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*