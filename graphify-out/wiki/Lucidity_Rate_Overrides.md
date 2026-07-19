# Lucidity Rate Overrides

> 42 nodes · cohesion 0.07

## Key Concepts

- **get_asyncpg_server_settings_for_database_url()** (19 connections) — `server/database_config_helpers.py`
- **rate_overrides.py** (17 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **_process_override_row()** (11 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **test_database_config_helpers_asyncpg_settings.py** (9 connections) — `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- **_async_load_lucidity_rate_overrides()** (6 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **._async_load_from_database()** (6 connections) — `server/services/schedule_service.py`
- **build_override_key()** (5 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **._async_load_emotes()** (4 connections) — `server/game/emote_service.py`
- **_LucidityRateLoadResult** (4 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **test_respects_postgres_search_path_when_matches_db_name()** (4 connections) — `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- **test_unknown_database_uses_postgres_search_path_when_set()** (4 connections) — `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- **extract_lucidity_rate()** (3 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **_normalize_database_url()** (3 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **_parse_special_rules_from_raw()** (3 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **_parse_zone_stable_id()** (3 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **rate_to_flux()** (3 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **MonkeyPatch** (3 connections) — `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- **_resolve_asyncpg_database_url()** (3 connections) — `server/services/schedule_service.py`
- **clear_postgres_search_path()** (3 connections) — `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- **test_mythos_unit_defaults_search_path_to_db_name()** (3 connections) — `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- **test_unknown_database_empty_when_no_env()** (3 connections) — `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- **Async helper to load emotes from PostgreSQL database.** (2 connections) — `server/game/emote_service.py`
- **_warn_if_rate_exceeds_threshold()** (2 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **test_mythos_e2e_defaults_search_path_to_db_name()** (2 connections) — `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- **Load lucidity rate overrides from PostgreSQL zones/subzones.** (1 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- *... and 17 more nodes in this community*

## Relationships

- [[NPC Admin API]] (8 shared connections)
- [[Performance Monitor Metrics]] (4 shared connections)
- [[Emote Schema Validator]] (2 shared connections)
- [[Zone Config Loader]] (2 shared connections)
- [[Chat Message Helpers]] (1 shared connections)
- [[Dependency Risk Analyzer]] (1 shared connections)
- [[NPC Database Sessions]] (1 shared connections)
- [[Holiday Persistence Models]] (1 shared connections)
- [[Schedule Service Loader]] (1 shared connections)
- [[Calendar Holiday Schemas]] (1 shared connections)
- [[Game Service Bundle]] (1 shared connections)

## Source Files

- `server/database_config_helpers.py`
- `server/game/emote_service.py`
- `server/services/passive_lucidity_flux/rate_overrides.py`
- `server/services/schedule_service.py`
- `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`

## Audit Trail

- EXTRACTED: 142 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
