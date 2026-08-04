# command player state

> 79 nodes

## Key Concepts

- **get_async_session()** (54 connections) — `server/database.py`
- **test_database_extended.py** (43 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **get_database_path()** (12 connections) — `server/database.py`
- **init_db()** (11 connections) — `server/database.py`
- **async_persistence_room_loader.py** (9 connections) — `server/async_persistence_room_loader.py`
- **main()** (6 connections) — `scripts/verify_and_load_seed.py`
- **.get_database_path()** (6 connections) — `server/database.py`
- **Path** (6 connections)
- **get_database_url()** (6 connections) — `server/database.py`
- **.apply_encounter_lucidity_effect()** (6 connections) — `server/services/npc_combat_lucidity.py`
- **test_database_manager_get_database_path_unsupported()** (5 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_database_path_none_url()** (5 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **load_seed_data()** (4 connections) — `scripts/load_seed_using_project_db.py`
- **verify_and_load_seed.py** (4 connections) — `scripts/verify_and_load_seed.py`
- **ensure_database_directory()** (4 connections) — `server/database.py`
- **._resolve_lucidity_category()** (4 connections) — `server/services/npc_combat_lucidity.py`
- **test_get_session_maker_initializes_database()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_database_url_initializes_database()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_get_engine_initializes()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_get_engine_reinitializes_if_none()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_get_session_maker_initializes()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_get_database_url_initializes()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_get_database_path_postgresql()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_close_with_engine()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_close_without_engine()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- *... and 54 more nodes in this community*

## Relationships

- [Database Access Layer](Database_Access_Layer.md) (32 shared connections)
- [game models enums](game_models_enums.md) (12 shared connections)
- [Loot Generation](Loot_Generation.md) (9 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (7 shared connections)
- [models profession rationale](models_profession_rationale.md) (6 shared connections)
- [NPC Combat](NPC_Combat.md) (5 shared connections)
- [aggro threat services](aggro_threat_services.md) (3 shared connections)
- [player requests schemas](player_requests_schemas.md) (3 shared connections)
- [combat services persistence](combat_services_persistence.md) (3 shared connections)
- [Database Config](Database_Config.md) (3 shared connections)
- [magic healing game](magic_healing_game.md) (3 shared connections)
- [models npc rationale](models_npc_rationale.md) (2 shared connections)

## Source Files

- `scripts/add_flavor_text_column.py`
- `scripts/load_seed_using_project_db.py`
- `scripts/verify_and_load_seed.py`
- `server/async_persistence_room_loader.py`
- `server/database.py`
- `server/services/npc_combat_lucidity.py`
- `server/tests/unit/infrastructure/test_database_extended.py`

## Audit Trail

- EXTRACTED: 306 (98%)
- INFERRED: 7 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*