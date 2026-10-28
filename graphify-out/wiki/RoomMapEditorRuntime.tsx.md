# RoomMapEditorRuntime.tsx

> 50 nodes · cohesion 0.09

## Key Concepts

- **test_passive_corruption_flux_rate_overrides.py** (34 connections) — `server/tests/unit/services/test_passive_corruption_flux_rate_overrides.py`
- **CorruptionOverride** (24 connections) — `server/services/passive_corruption_flux/config.py`
- **passive_corruption_flux/rate_overrides.py** (20 connections) — `server/services/passive_corruption_flux/rate_overrides.py`
- **passive_corruption_flux/config.py** (15 connections) — `server/services/passive_corruption_flux/config.py`
- **_process_override_row()** (13 connections) — `server/services/passive_corruption_flux/rate_overrides.py`
- **_async_load_corruption_overrides()** (10 connections) — `server/services/passive_corruption_flux/rate_overrides.py`
- **_extract_corruption_override()** (10 connections) — `server/services/passive_corruption_flux/rate_overrides.py`
- **load_corruption_overrides()** (8 connections) — `server/services/passive_corruption_flux/rate_overrides.py`
- **_mock_row()** (8 connections) — `server/tests/unit/services/test_passive_corruption_flux_rate_overrides.py`
- **_CorruptionOverrideLoadResult** (7 connections) — `server/services/passive_corruption_flux/rate_overrides.py`
- **_parse_special_rules_from_raw()** (7 connections) — `server/services/passive_corruption_flux/rate_overrides.py`
- **_empty_result()** (7 connections) — `server/tests/unit/services/test_passive_corruption_flux_rate_overrides.py`
- **test_async_load_corruption_overrides_success()** (7 connections) — `server/tests/unit/services/test_passive_corruption_flux_rate_overrides.py`
- **_normalize_database_url()** (6 connections) — `server/services/passive_corruption_flux/rate_overrides.py`
- **_parse_zone_stable_id()** (6 connections) — `server/services/passive_corruption_flux/rate_overrides.py`
- **test_async_load_corruption_overrides_missing_database_url()** (5 connections) — `server/tests/unit/services/test_passive_corruption_flux_rate_overrides.py`
- **test_process_override_row_subzone_level()** (5 connections) — `server/tests/unit/services/test_passive_corruption_flux_rate_overrides.py`
- **test_process_override_row_zone_level()** (5 connections) — `server/tests/unit/services/test_passive_corruption_flux_rate_overrides.py`
- **test_load_corruption_overrides_success()** (4 connections) — `server/tests/unit/services/test_passive_corruption_flux_rate_overrides.py`
- **test_process_override_row_missing_keys_is_skipped()** (4 connections) — `server/tests/unit/services/test_passive_corruption_flux_rate_overrides.py`
- **MonkeyPatch** (3 connections)
- **test_extract_corruption_override_both()** (3 connections) — `server/tests/unit/services/test_passive_corruption_flux_rate_overrides.py`
- **test_extract_corruption_override_rate_only()** (3 connections) — `server/tests/unit/services/test_passive_corruption_flux_rate_overrides.py`
- **test_extract_corruption_override_target_only()** (3 connections) — `server/tests/unit/services/test_passive_corruption_flux_rate_overrides.py`
- **test_load_corruption_overrides_returns_empty_on_error()** (3 connections) — `server/tests/unit/services/test_passive_corruption_flux_rate_overrides.py`
- *... and 25 more nodes in this community*

## Relationships

- [cleanse_command.py](cleanse_command.py.md) (11 shared connections)
- [CorruptionTier](CorruptionTier.md) (8 shared connections)
- [test_character_creation_service.py](test_character_creation_service.py.md) (6 shared connections)
- [ExitEdge.tsx](ExitEdge.tsx.md) (3 shared connections)
- [Room](Room.md) (3 shared connections)
- [fixtures/auth.ts](fixtures-auth.ts.md) (1 shared connections)
- [test_websocket_helpers.py](test_websocket_helpers.py.md) (1 shared connections)
- [combat_taunt.py](combat_taunt.py.md) (1 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (1 shared connections)

## Source Files

- `server/services/passive_corruption_flux/config.py`
- `server/services/passive_corruption_flux/rate_overrides.py`
- `server/tests/unit/services/test_passive_corruption_flux_rate_overrides.py`

## Audit Trail

- EXTRACTED: 139 (96%)
- INFERRED: 6 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*