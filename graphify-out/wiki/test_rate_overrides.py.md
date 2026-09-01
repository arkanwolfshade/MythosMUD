# test_rate_overrides.py

> 55 nodes

## Key Concepts

- **test_rate_overrides.py** (39 connections) — `server/tests/unit/services/test_rate_overrides.py`
- **rate_overrides.py** (20 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
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
- **test_build_override_key_missing_parts_default_to_wildcard()** (2 connections) — `server/tests/unit/services/test_rate_overrides.py`
- *... and 30 more nodes in this community*

## Relationships

- [service.py](service.py.md) (5 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [HolidayService](HolidayService.md) (2 shared connections)
- [event_types.py](event_types.py.md) (1 shared connections)
- [EventBus](EventBus.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/services/passive_lucidity_flux/rate_overrides.py`
- `server/tests/unit/services/test_rate_overrides.py`

## Audit Trail

- EXTRACTED: 125 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*