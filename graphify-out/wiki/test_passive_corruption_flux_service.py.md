# test_passive_corruption_flux_service.py

> 36 nodes

## Key Concepts

- **test_passive_corruption_flux_service.py** (37 connections) — `server/tests/unit/services/test_passive_corruption_flux_service.py`
- **_make_service()** (22 connections) — `server/tests/unit/services/test_passive_corruption_flux_service.py`
- **_room()** (14 connections) — `server/tests/unit/services/test_passive_corruption_flux_service.py`
- **CorruptionFluxServiceConfig** (9 connections) — `server/services/passive_corruption_flux/config.py`
- **test_innsmouth_pier_converges_upward_and_clamps_at_its_own_ceiling()** (9 connections) — `server/tests/unit/services/test_passive_corruption_flux_service.py`
- **test_process_tick_for_player_applies_bounded_rising_delta()** (8 connections) — `server/tests/unit/services/test_passive_corruption_flux_service.py`
- **CorruptionUpdateResult** (7 connections) — `server/services/corruption_service.py`
- **test_default_cadence_derived_from_tick_rate()** (6 connections) — `server/tests/unit/services/test_passive_corruption_flux_service.py`
- **test_lookup_db_override_wins_over_static_config()** (5 connections) — `server/tests/unit/services/test_passive_corruption_flux_service.py`
- **test_process_tick_for_player_zero_delta_skips_write()** (5 connections) — `server/tests/unit/services/test_passive_corruption_flux_service.py`
- **test_room_attribute_rate_wins_over_db_override()** (5 connections) — `server/tests/unit/services/test_passive_corruption_flux_service.py`
- **test_room_attribute_target_wins_over_db_override()** (5 connections) — `server/tests/unit/services/test_passive_corruption_flux_service.py`
- **asyncio** (5 connections)
- **_player()** (4 connections) — `server/tests/unit/services/test_passive_corruption_flux_service.py`
- **test_room_authoring_only_rate_still_inherits_db_target()** (4 connections) — `server/tests/unit/services/test_passive_corruption_flux_service.py`
- **test_lookup_rate_and_target_environment_defaults()** (3 connections) — `server/tests/unit/services/test_passive_corruption_flux_service.py`
- **test_lookup_rate_night_profile_differs_from_day()** (3 connections) — `server/tests/unit/services/test_passive_corruption_flux_service.py`
- **test_lookup_target_room_attribute_takes_precedence()** (3 connections) — `server/tests/unit/services/test_passive_corruption_flux_service.py`
- **test_process_tick_for_player_no_persistence_is_noop()** (3 connections) — `server/tests/unit/services/test_passive_corruption_flux_service.py`
- **test_process_tick_for_player_skipped_off_cadence()** (3 connections) — `server/tests/unit/services/test_passive_corruption_flux_service.py`
- **test_room_attribute_rate_wins_over_environment_default()** (3 connections) — `server/tests/unit/services/test_passive_corruption_flux_service.py`
- **test_apply_residual_accumulates_then_emits_delta()** (2 connections) — `server/tests/unit/services/test_passive_corruption_flux_service.py`
- **test_bound_delta_caps_rise_at_room_target()** (2 connections) — `server/tests/unit/services/test_passive_corruption_flux_service.py`
- **test_bound_delta_floors_fall_at_current_tier_bottom()** (2 connections) — `server/tests/unit/services/test_passive_corruption_flux_service.py`
- **test_should_process_tick()** (2 connections) — `server/tests/unit/services/test_passive_corruption_flux_service.py`
- *... and 11 more nodes in this community*

## Relationships

- [PassiveCorruptionFluxService](PassiveCorruptionFluxService.md) (12 shared connections)
- [test_passive_corruption_flux_rate_overrides.py](test_passive_corruption_flux_rate_overrides.py.md) (7 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [CombatService](CombatService.md) (3 shared connections)
- [CorruptionTier](CorruptionTier.md) (3 shared connections)
- [.apply_corruption_adjustment](apply_corruption_adjustment.md) (2 shared connections)
- [passive_corruption_flux/config.py](passive_corruption_flux-config.py.md) (2 shared connections)

## Source Files

- `server/services/corruption_service.py`
- `server/services/passive_corruption_flux/config.py`
- `server/tests/unit/services/test_passive_corruption_flux_service.py`

## Audit Trail

- EXTRACTED: 99 (92%)
- INFERRED: 9 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*