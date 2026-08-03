# rate lucidity services

> 38 nodes

## Key Concepts

- **get_asyncpg_server_settings_for_database_url()** (19 connections) — `server/database_config_helpers.py`
- **rate_overrides.py** (18 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **_process_override_row()** (11 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **test_database_config_helpers_asyncpg_settings.py** (9 connections) — `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- **_async_load_lucidity_rate_overrides()** (6 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
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
- **Build asyncpg ``server_settings`` so unqualified table names resolve like SQLAlc** (1 connections) — `server/database_config_helpers.py`
- **TypedDict** (1 connections)
- **Record** (1 connections)
- **Load lucidity rate overrides from PostgreSQL zones/subzones.** (1 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **Build override key from plane/zone/subzone hierarchy.** (1 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- *... and 13 more nodes in this community*

## Relationships

- [Database Access Layer](Database_Access_Layer.md) (4 shared connections)
- [lucidity flux passive](lucidity_flux_passive.md) (4 shared connections)
- [commands admin mute](commands_admin_mute.md) (2 shared connections)
- [spell game magic](spell_game_magic.md) (2 shared connections)
- [holiday service services](holiday_service_services.md) (2 shared connections)
- [Error Conversion](Error_Conversion.md) (2 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)
- [npc shopkeeper rationale](npc_shopkeeper_rationale.md) (1 shared connections)

## Source Files

- `server/database_config_helpers.py`
- `server/services/passive_lucidity_flux/rate_overrides.py`
- `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`

## Audit Trail

- EXTRACTED: 129 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*