# server database config helpers get

> 18 nodes

## Key Concepts

- **get_asyncpg_server_settings_for_database_url()** (19 connections) — `server/database_config_helpers.py`
- **test_database_config_helpers_asyncpg_settings.py** (10 connections) — `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- **clear_postgres_search_path()** (4 connections) — `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- **test_mythos_unit_defaults_search_path_to_db_name()** (4 connections) — `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- **test_respects_postgres_search_path_when_matches_db_name()** (4 connections) — `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- **test_unknown_database_empty_when_no_env()** (4 connections) — `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- **test_unknown_database_uses_postgres_search_path_when_set()** (4 connections) — `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- **test_mythos_e2e_defaults_search_path_to_db_name()** (3 connections) — `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- **MonkeyPatch** (3 connections)
- **usefixtures** (3 connections)
- **fixture** (1 connections)
- **Build asyncpg ``server_settings`` so unqualified table names resolve like…** (1 connections) — `server/database_config_helpers.py`
- **Unit tests for get_asyncpg_server_settings_for_database_url.** (1 connections) — `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- **Ensure POSTGRES_SEARCH_PATH does not leak between cases.** (1 connections) — `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- **Known env DBs must set search_path to the database name when env override is…** (1 connections) — `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- **When POSTGRES_SEARCH_PATH matches the DB name, keep that search_path.** (1 connections) — `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- **Non-mythos_* URLs still honor POSTGRES_SEARCH_PATH.** (1 connections) — `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- **Other databases without POSTGRES_SEARCH_PATH get no server_settings.** (1 connections) — `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`

## Relationships

- [server command handler command input](server_command_handler_command_input.md) (2 shared connections)
- [server npc zone config loader](server_npc_zone_config_loader.md) (2 shared connections)
- [server container bundles game gamebundle](server_container_bundles_game_gamebundle.md) (2 shared connections)
- [server services passive lucidity flux](server_services_passive_lucidity_flux.md) (2 shared connections)
- [claude rules sqlalchemy](claude_rules_sqlalchemy.md) (2 shared connections)
- [server database config helpers get](server_database_config_helpers_get.md) (1 shared connections)
- [server services schedule service databaseloadresult](server_services_schedule_service_databaseloadresult.md) (1 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (1 shared connections)
- [claude rules pytest](claude_rules_pytest.md) (1 shared connections)

## Source Files

- `server/database_config_helpers.py`
- `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`

## Audit Trail

- EXTRACTED: 40 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*