# manager subject services

> 16 nodes

## Key Concepts

- **get_asyncpg_server_settings_for_database_url()** (19 connections) — `server/database_config_helpers.py`
- **test_database_config_helpers_asyncpg_settings.py** (9 connections) — `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- **test_respects_postgres_search_path_when_matches_db_name()** (4 connections) — `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- **test_unknown_database_uses_postgres_search_path_when_set()** (4 connections) — `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- **clear_postgres_search_path()** (3 connections) — `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- **MonkeyPatch** (3 connections)
- **test_mythos_unit_defaults_search_path_to_db_name()** (3 connections) — `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- **test_unknown_database_empty_when_no_env()** (3 connections) — `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- **test_mythos_e2e_defaults_search_path_to_db_name()** (2 connections) — `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- **Build asyncpg ``server_settings`` so unqualified table names resolve like SQLAlc** (1 connections) — `server/database_config_helpers.py`
- **Unit tests for get_asyncpg_server_settings_for_database_url.** (1 connections) — `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- **Ensure POSTGRES_SEARCH_PATH does not leak between cases.** (1 connections) — `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- **Known env DBs must set search_path to the database name when env override is uns** (1 connections) — `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- **When POSTGRES_SEARCH_PATH matches the DB name, keep that search_path.** (1 connections) — `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- **Non-mythos_* URLs still honor POSTGRES_SEARCH_PATH.** (1 connections) — `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- **Other databases without POSTGRES_SEARCH_PATH get no server_settings.** (1 connections) — `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`

## Relationships

- [game models enums](game_models_enums.md) (3 shared connections)
- [commands recovery lucidity](commands_recovery_lucidity.md) (2 shared connections)
- [spell game magic](spell_game_magic.md) (2 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (2 shared connections)
- [rate lucidity services](rate_lucidity_services.md) (2 shared connections)
- [persistence rationale players](persistence_rationale_players.md) (2 shared connections)

## Source Files

- `server/database_config_helpers.py`
- `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`

## Audit Trail

- EXTRACTED: 57 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*