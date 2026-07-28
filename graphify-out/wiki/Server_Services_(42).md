# Server Services (42)

> 42 nodes

## Key Concepts

- **database_config_helpers.py** (24 connections) — `server/database_config_helpers.py`
- **get_asyncpg_server_settings_for_database_url()** (19 connections) — `server/database_config_helpers.py`
- **rate_overrides.py** (18 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **_process_override_row()** (11 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **test_database_config_helpers_asyncpg_settings.py** (9 connections) — `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- **_async_load_lucidity_rate_overrides()** (6 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **configure_pool_settings()** (5 connections) — `server/database_config_helpers.py`
- **build_override_key()** (5 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **_LucidityRateLoadResult** (4 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **test_respects_postgres_search_path_when_matches_db_name()** (4 connections) — `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- **test_unknown_database_uses_postgres_search_path_when_set()** (4 connections) — `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- **rate_to_flux()** (3 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **extract_lucidity_rate()** (3 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **_normalize_database_url()** (3 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **_parse_zone_stable_id()** (3 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **_parse_special_rules_from_raw()** (3 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **clear_postgres_search_path()** (3 connections) — `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- **MonkeyPatch** (3 connections)
- **test_mythos_unit_defaults_search_path_to_db_name()** (3 connections) — `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- **test_unknown_database_empty_when_no_env()** (3 connections) — `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- **_warn_if_rate_exceeds_threshold()** (2 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **test_mythos_e2e_defaults_search_path_to_db_name()** (2 connections) — `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- **Database configuration helper functions.  This module provides utility functions** (1 connections) — `server/database_config_helpers.py`
- **Build asyncpg ``server_settings`` so unqualified table names resolve like SQLAlc** (1 connections) — `server/database_config_helpers.py`
- **Configure pool settings based on database URL and config.      When full config** (1 connections) — `server/database_config_helpers.py`
- *... and 17 more nodes in this community*

## Relationships

- [Server Tools](Server_Tools.md) (6 shared connections)
- [Server Admin](Server_Admin.md) (4 shared connections)
- [Server Infrastructure (7)](Server_Infrastructure_%287%29.md) (3 shared connections)
- [Server Services](Server_Services.md) (3 shared connections)
- [Server Commands (10)](Server_Commands_%2810%29.md) (3 shared connections)
- [Server Services (15)](Server_Services_%2815%29.md) (3 shared connections)
- [Server Utils (14)](Server_Utils_%2814%29.md) (3 shared connections)
- [Server Config (2)](Server_Config_%282%29.md) (2 shared connections)
- [Server Npc (15)](Server_Npc_%2815%29.md) (2 shared connections)
- [Server Commands](Server_Commands.md) (2 shared connections)
- [Server Utils](Server_Utils.md) (1 shared connections)
- [Server Api](Server_Api.md) (1 shared connections)

## Source Files

- `server/database_config_helpers.py`
- `server/services/passive_lucidity_flux/rate_overrides.py`
- `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`

## Audit Trail

- EXTRACTED: 160 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*