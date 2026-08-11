# Spell Registry Costs

> 395 nodes

## Key Concepts

- **ValidationError** (540 connections) — `server/exceptions.py`
- **.get_instance()** (88 connections) — `server/database.py`
- **.reset_instance()** (87 connections) — `server/database.py`
- **database.py** (79 connections) — `server/database.py`
- **get_async_session()** (53 connections) — `server/database.py`
- **test_database_helpers.py** (46 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_database_extended.py** (43 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_error_handling.py** (41 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_database_init.py** (36 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **database_helpers.py** (30 connections) — `server/database_helpers.py`
- **DatabaseManager** (29 connections) — `server/database.py`
- **database_config_helpers.py** (24 connections) — `server/database_config_helpers.py`
- **._initialize_database()** (19 connections) — `server/database.py`
- **reset_database()** (16 connections) — `server/database.py`
- **get_database_path()** (16 connections) — `server/database_helpers.py`
- **async_persistence_direct_queries.py** (15 connections) — `server/async_persistence_direct_queries.py`
- **npc_combat_lucidity.py** (13 connections) — `server/services/npc_combat_lucidity.py`
- **get_database_path()** (12 connections) — `server/database.py`
- **get_async_session()** (12 connections) — `server/database_helpers.py`
- **init_db()** (11 connections) — `server/database.py`
- **set_test_database_url()** (11 connections) — `server/database_config_helpers.py`
- **fetch_user_by_username_case_insensitive()** (9 connections) — `server/async_persistence_direct_queries.py`
- **async_persistence_room_loader.py** (9 connections) — `server/async_persistence_room_loader.py`
- **close_db()** (9 connections) — `server/database.py`
- **get_engine()** (9 connections) — `server/database_helpers.py`
- *... and 370 more nodes in this community*

## Relationships

- [Standardized Error Responses](Standardized_Error_Responses.md) (74 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (72 shared connections)
- [NPC Death Lifecycle](NPC_Death_Lifecycle.md) (45 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (43 shared connections)
- [NPC Definition Admin API](NPC_Definition_Admin_API.md) (37 shared connections)
- [Base Command Models](Base_Command_Models.md) (30 shared connections)
- [Room Service Tests](Room_Service_Tests.md) (28 shared connections)
- [Admin Summon Command](Admin_Summon_Command.md) (24 shared connections)
- [Combat Schema Validation](Combat_Schema_Validation.md) (22 shared connections)
- [Admin Command Models](Admin_Command_Models.md) (20 shared connections)
- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (15 shared connections)
- [Moderation Command Models](Moderation_Command_Models.md) (14 shared connections)

## Source Files

- `scripts/add_flavor_text_column.py`
- `scripts/load_seed_using_project_db.py`
- `scripts/verify_and_load_seed.py`
- `server/async_persistence.py`
- `server/async_persistence_direct_queries.py`
- `server/async_persistence_room_loader.py`
- `server/database.py`
- `server/database_config_helpers.py`
- `server/database_helpers.py`
- `server/exceptions.py`
- `server/game/emote_service.py`
- `server/game/movement_service.py`
- `server/game/profession_service.py`
- `server/services/npc_combat_lucidity.py`
- `server/tests/unit/infrastructure/test_database.py`
- `server/tests/unit/infrastructure/test_database_error_handling.py`
- `server/tests/unit/infrastructure/test_database_extended.py`
- `server/tests/unit/infrastructure/test_database_helpers.py`
- `server/tests/unit/infrastructure/test_database_init.py`
- `server/tests/unit/test_exceptions.py`

## Audit Trail

- EXTRACTED: 1714 (78%)
- INFERRED: 494 (22%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*