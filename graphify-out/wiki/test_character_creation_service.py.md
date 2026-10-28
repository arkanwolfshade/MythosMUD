# test_character_creation_service.py

> 58 nodes · cohesion 0.07

## Key Concepts

- **test_rate_overrides.py** (38 connections) — `server/tests/unit/services/test_rate_overrides.py`
- **passive_lucidity_flux/rate_overrides.py** (20 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **get_asyncpg_server_settings_for_database_url()** (19 connections) — `server/database_config_helpers.py`
- **_process_override_row()** (15 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **build_override_key()** (12 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **_async_load_lucidity_rate_overrides()** (10 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
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
- **MonkeyPatch** (3 connections)
- **test_load_lucidity_rate_overrides_returns_empty_on_error()** (3 connections) — `server/tests/unit/services/test_rate_overrides.py`
- **test_load_lucidity_rate_overrides_success()** (3 connections) — `server/tests/unit/services/test_rate_overrides.py`
- **test_build_override_key_full_hierarchy()** (2 connections) — `server/tests/unit/services/test_passive_corruption_flux_rate_overrides.py`
- *... and 33 more nodes in this community*

## Relationships

- [RoomMapEditorRuntime.tsx](RoomMapEditorRuntime.tsx.md) (6 shared connections)
- [fixture](fixture.md) (6 shared connections)
- [ExitEdge.tsx](ExitEdge.tsx.md) (5 shared connections)
- [combat_taunt.py](combat_taunt.py.md) (3 shared connections)
- [Room](Room.md) (3 shared connections)
- [test_message_category_invariants.py](test_message_category_invariants.py.md) (2 shared connections)
- [start_grace_period](start_grace_period.md) (2 shared connections)
- [populate_npc_sample_data.py](populate_npc_sample_data.py.md) (1 shared connections)
- [test_admin_teleport_commands.py](test_admin_teleport_commands.py.md) (1 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (1 shared connections)
- [cleanse_command.py](cleanse_command.py.md) (1 shared connections)

## Source Files

- `server/database_config_helpers.py`
- `server/services/passive_lucidity_flux/rate_overrides.py`
- `server/tests/unit/services/test_passive_corruption_flux_rate_overrides.py`
- `server/tests/unit/services/test_rate_overrides.py`

## Audit Trail

- EXTRACTED: 144 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*