# test_rate_overrides.py

> 76 nodes

## Key Concepts

- **test_rate_overrides.py** (38 connections) — `server/tests/unit/services/test_rate_overrides.py`
- **database_config_helpers.py** (24 connections) — `server/database_config_helpers.py`
- **passive_lucidity_flux/rate_overrides.py** (20 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **get_asyncpg_server_settings_for_database_url()** (19 connections) — `server/database_config_helpers.py`
- **_process_override_row()** (15 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **build_override_key()** (12 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **_async_load_lucidity_rate_overrides()** (9 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **test_database_config_helpers_asyncpg_settings.py** (9 connections) — `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- **_mock_row()** (8 connections) — `server/tests/unit/services/test_rate_overrides.py`
- **extract_lucidity_rate()** (7 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **load_lucidity_rate_overrides()** (7 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **_parse_special_rules_from_raw()** (7 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **_empty_result()** (7 connections) — `server/tests/unit/services/test_rate_overrides.py`
- **_LucidityRateLoadResult** (6 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **_normalize_database_url()** (6 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **_parse_zone_stable_id()** (6 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **rate_to_flux()** (6 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **test_async_load_lucidity_rate_overrides_success()** (6 connections) — `server/tests/unit/services/test_rate_overrides.py`
- **_warn_if_rate_exceeds_threshold()** (5 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **test_async_load_lucidity_rate_overrides_missing_database_url()** (5 connections) — `server/tests/unit/services/test_rate_overrides.py`
- **test_process_override_row_missing_rate_is_skipped()** (4 connections) — `server/tests/unit/services/test_rate_overrides.py`
- **test_process_override_row_subzone_level()** (4 connections) — `server/tests/unit/services/test_rate_overrides.py`
- **test_process_override_row_zone_level()** (4 connections) — `server/tests/unit/services/test_rate_overrides.py`
- **clear_postgres_search_path()** (4 connections) — `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- **test_mythos_unit_defaults_search_path_to_db_name()** (4 connections) — `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- *... and 51 more nodes in this community*

## Relationships

- [test_passive_corruption_flux_rate_overrides.py](test_passive_corruption_flux_rate_overrides.py.md) (7 shared connections)
- [get_logger](get_logger.md) (7 shared connections)
- [DatabaseError](DatabaseError.md) (6 shared connections)
- [passive_lucidity_flux/service.py](passive_lucidity_flux-service.py.md) (5 shared connections)
- [npc_database.py](npc_database.py.md) (3 shared connections)
- [test_zone_config_loader.py](test_zone_config_loader.py.md) (3 shared connections)
- [NPCDefinition](NPCDefinition.md) (3 shared connections)
- [DatabaseManager](DatabaseManager.md) (2 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (2 shared connections)
- [HolidayService](HolidayService.md) (1 shared connections)
- [test_passive_corruption_flux_service.py](test_passive_corruption_flux_service.py.md) (1 shared connections)
- [session_factory](session_factory.md) (1 shared connections)

## Source Files

- `server/database_config_helpers.py`
- `server/services/passive_lucidity_flux/rate_overrides.py`
- `server/tests/unit/services/test_passive_corruption_flux_rate_overrides.py`
- `server/tests/unit/services/test_rate_overrides.py`
- `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`

## Audit Trail

- EXTRACTED: 185 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*