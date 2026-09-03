# Test Rate Overrides

> 57 nodes

## Key Concepts

- **test_rate_overrides.py** (39 connections) — `server/tests/unit/services/test_rate_overrides.py`
- **rate_overrides.py** (20 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **get_asyncpg_server_settings_for_database_url()** (17 connections) — `server/database_config_helpers.py`
- **_process_override_row()** (15 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **_async_load_lucidity_rate_overrides()** (9 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **build_override_key()** (8 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
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
- **test_load_lucidity_rate_overrides_returns_empty_on_error()** (3 connections) — `server/tests/unit/services/test_rate_overrides.py`
- **test_load_lucidity_rate_overrides_success()** (3 connections) — `server/tests/unit/services/test_rate_overrides.py`
- **MonkeyPatch** (3 connections)
- **test_build_override_key_full_hierarchy()** (2 connections) — `server/tests/unit/services/test_rate_overrides.py`
- *... and 32 more nodes in this community*

## Relationships

- [Test Database Config Helpers Asyncpg](Test_Database_Config_Helpers_Asyncpg.md) (6 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (5 shared connections)
- [Service](Service.md) (5 shared connections)
- [Test Zone Config Loader](Test_Zone_Config_Loader.md) (2 shared connections)
- [Holiday Calendar Validation](Holiday_Calendar_Validation.md) (2 shared connections)
- [Database](Database.md) (2 shared connections)
- [Test Npc Database](Test_Npc_Database.md) (1 shared connections)
- [Test Schedule Service](Test_Schedule_Service.md) (1 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)

## Source Files

- `server/database_config_helpers.py`
- `server/services/passive_lucidity_flux/rate_overrides.py`
- `server/tests/unit/services/test_rate_overrides.py`

## Audit Trail

- EXTRACTED: 140 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*