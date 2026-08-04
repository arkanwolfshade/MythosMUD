# Database Access Layer

> 388 nodes

## Key Concepts

- **ValidationError** (582 connections) — `server/exceptions.py`
- **.get_instance()** (88 connections) — `server/database.py`
- **.reset_instance()** (87 connections) — `server/database.py`
- **database.py** (76 connections) — `server/database.py`
- **get_async_session()** (54 connections) — `server/database.py`
- **test_database_helpers.py** (46 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_database_extended.py** (43 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_error_handling.py** (41 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_database_init.py** (36 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **database_helpers.py** (30 connections) — `server/database_helpers.py`
- **DatabaseManager** (29 connections) — `server/database.py`
- **database_config_helpers.py** (24 connections) — `server/database_config_helpers.py`
- **core.py** (19 connections) — `server/container/bundles/core.py`
- **._initialize_database()** (17 connections) — `server/database.py`
- **reset_database()** (16 connections) — `server/database.py`
- **get_database_path()** (16 connections) — `server/database_helpers.py`
- **async_persistence_direct_queries.py** (15 connections) — `server/async_persistence_direct_queries.py`
- **get_async_session()** (13 connections) — `server/database_helpers.py`
- **.initialize()** (12 connections) — `server/container/bundles/core.py`
- **get_database_path()** (12 connections) — `server/database.py`
- **npc_combat_lucidity.py** (12 connections) — `server/services/npc_combat_lucidity.py`
- **init_db()** (11 connections) — `server/database.py`
- **MythosValidationError** (10 connections)
- **fetch_user_by_username_case_insensitive()** (9 connections) — `server/async_persistence_direct_queries.py`
- **fetch_professions()** (9 connections) — `server/async_persistence_direct_queries.py`
- *... and 363 more nodes in this community*

## Relationships

- [Loot Generation](Loot_Generation.md) (112 shared connections)
- [Database Config](Database_Config.md) (64 shared connections)
- [Exception Containers](Exception_Containers.md) (30 shared connections)
- [command inventory models](command_inventory_models.md) (30 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (28 shared connections)
- [exceptions rationale error](exceptions_rationale_error.md) (28 shared connections)
- [npc commands admin](npc_commands_admin.md) (24 shared connections)
- [command factories create](command_factories_create.md) (20 shared connections)
- [player effects endpoints](player_effects_endpoints.md) (18 shared connections)
- [persistence container item](persistence_container_item.md) (18 shared connections)
- [command communication models](command_communication_models.md) (17 shared connections)
- [auth endpoints rationale](auth_endpoints_rationale.md) (16 shared connections)

## Source Files

- `scripts/add_flavor_text_column.py`
- `scripts/load_seed_using_project_db.py`
- `scripts/verify_and_load_seed.py`
- `server/async_persistence_direct_queries.py`
- `server/async_persistence_room_loader.py`
- `server/container/bundles/core.py`
- `server/database.py`
- `server/database_config_helpers.py`
- `server/database_helpers.py`
- `server/exceptions.py`
- `server/game/player_service.py`
- `server/npc/combat_integration.py`
- `server/npc_database.py`
- `server/services/environmental_container_loader.py`
- `server/services/npc_combat_lucidity.py`
- `server/tests/unit/commands/test_command_service.py`
- `server/tests/unit/infrastructure/test_database.py`
- `server/tests/unit/infrastructure/test_database_error_handling.py`
- `server/tests/unit/infrastructure/test_database_extended.py`
- `server/tests/unit/infrastructure/test_database_helpers.py`

## Audit Trail

- EXTRACTED: 1738 (77%)
- INFERRED: 531 (23%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*