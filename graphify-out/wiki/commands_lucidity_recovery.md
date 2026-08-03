# commands lucidity recovery

> 42 nodes

## Key Concepts

- **DatabaseManager** (29 connections) — `server/database.py`
- **database_config_helpers.py** (24 connections) — `server/database_config_helpers.py`
- **get_asyncpg_server_settings_for_database_url()** (19 connections) — `server/database_config_helpers.py`
- **._initialize_database()** (17 connections) — `server/database.py`
- **get_postgres_connect_args()** (9 connections) — `server/database_config_helpers.py`
- **test_database_config_helpers_asyncpg_settings.py** (9 connections) — `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- **load_database_url()** (7 connections) — `server/database_config_helpers.py`
- **.get_session_maker()** (6 connections) — `server/database.py`
- **validate_database_url()** (6 connections) — `server/database_config_helpers.py`
- **.get_engine()** (5 connections) — `server/database.py`
- **async_sessionmaker** (5 connections)
- **configure_pool_settings()** (5 connections) — `server/database_config_helpers.py`
- **AsyncEngine** (4 connections)
- **test_respects_postgres_search_path_when_matches_db_name()** (4 connections) — `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- **test_unknown_database_uses_postgres_search_path_when_set()** (4 connections) — `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- **.__init__()** (3 connections) — `server/database.py`
- **.get_database_url()** (3 connections) — `server/database.py`
- **AsyncEngine** (3 connections)
- **async_sessionmaker** (3 connections)
- **clear_postgres_search_path()** (3 connections) — `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- **MonkeyPatch** (3 connections)
- **test_mythos_unit_defaults_search_path_to_db_name()** (3 connections) — `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- **test_unknown_database_empty_when_no_env()** (3 connections) — `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- **Initialize database engine and session maker from configuration.          CRITIC** (2 connections) — `server/database.py`
- **test_mythos_e2e_defaults_search_path_to_db_name()** (2 connections) — `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- *... and 17 more nodes in this community*

## Relationships

- [Database Config](Database_Config.md) (10 shared connections)
- [command inventory models](command_inventory_models.md) (9 shared connections)
- [manager subject services](manager_subject_services.md) (9 shared connections)
- [combat npc services](combat_npc_services.md) (7 shared connections)
- [holiday service services](holiday_service_services.md) (6 shared connections)
- [memory lifespan app](memory_lifespan_app.md) (5 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (5 shared connections)
- [game models enums](game_models_enums.md) (4 shared connections)
- [player effects endpoints](player_effects_endpoints.md) (4 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (3 shared connections)
- [models npc rationale](models_npc_rationale.md) (3 shared connections)
- [schemas validator rationale](schemas_validator_rationale.md) (3 shared connections)

## Source Files

- `server/database.py`
- `server/database_config_helpers.py`
- `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`

## Audit Trail

- EXTRACTED: 175 (88%)
- INFERRED: 23 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*