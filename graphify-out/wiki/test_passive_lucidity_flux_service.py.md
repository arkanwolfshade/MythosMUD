# test_passive_lucidity_flux_service.py

> 46 nodes

## Key Concepts

- **test_passive_lucidity_flux_service.py** (35 connections) — `server/tests/unit/services/test_passive_lucidity_flux_service.py`
- **_make_service()** (24 connections) — `server/tests/unit/services/test_passive_lucidity_flux_service.py`
- **PassiveFluxContext** (14 connections) — `server/services/passive_lucidity_flux/models.py`
- **FluxServiceConfig** (10 connections) — `server/services/passive_lucidity_flux/config.py`
- **PlayerFluxCtx** (9 connections) — `server/services/passive_lucidity_flux/service.py`
- **PassiveLucidityFluxService** (9 connections)
- **._apply_player_flux_adjustment()** (8 connections) — `server/services/passive_lucidity_flux/service.py`
- **passive_lucidity_flux/models.py** (8 connections) — `server/services/passive_lucidity_flux/models.py`
- **asyncio** (7 connections)
- **test_default_cadence_is_once_per_real_minute()** (6 connections) — `server/tests/unit/services/test_passive_lucidity_flux_service.py`
- **test_process_single_player_skips_missing_player_fk()** (6 connections) — `server/tests/unit/services/test_passive_lucidity_flux_service.py`
- **passive_lucidity_flux/__init__.py** (6 connections) — `server/services/passive_lucidity_flux/__init__.py`
- **test_process_single_player_no_delta()** (5 connections) — `server/tests/unit/services/test_passive_lucidity_flux_service.py`
- **test_process_tick_applies_adjustment()** (5 connections) — `server/tests/unit/services/test_passive_lucidity_flux_service.py`
- **test_resolve_context_with_custom_resolver()** (4 connections) — `server/tests/unit/services/test_passive_lucidity_flux_service.py`
- **test_build_room_cache()** (3 connections) — `server/tests/unit/services/test_passive_lucidity_flux_service.py`
- **test_get_room_cached_uses_persistence()** (3 connections) — `server/tests/unit/services/test_passive_lucidity_flux_service.py`
- **test_process_tick_skipped_when_not_due()** (3 connections) — `server/tests/unit/services/test_passive_lucidity_flux_service.py`
- **test_resolve_context_async_with_room()** (3 connections) — `server/tests/unit/services/test_passive_lucidity_flux_service.py`
- **test_apply_adaptive_resistance_positive_flux_unchanged()** (2 connections) — `server/tests/unit/services/test_passive_lucidity_flux_service.py`
- **test_apply_adaptive_resistance_reduces_negative_flux()** (2 connections) — `server/tests/unit/services/test_passive_lucidity_flux_service.py`
- **test_apply_residual_accumulates_and_emits_delta()** (2 connections) — `server/tests/unit/services/test_passive_lucidity_flux_service.py`
- **test_apply_residual_negative_delta()** (2 connections) — `server/tests/unit/services/test_passive_lucidity_flux_service.py`
- **test_companion_modifier_with_lucid_and_destabilizing()** (2 connections) — `server/tests/unit/services/test_passive_lucidity_flux_service.py`
- **test_count_companion_tiers()** (2 connections) — `server/tests/unit/services/test_passive_lucidity_flux_service.py`
- *... and 21 more nodes in this community*

## Relationships

- [passive_lucidity_flux/service.py](passive_lucidity_flux-service.py.md) (17 shared connections)
- [passive_corruption_flux/config.py](passive_corruption_flux-config.py.md) (5 shared connections)
- [LucidityService](LucidityService.md) (3 shared connections)
- [CombatService](CombatService.md) (3 shared connections)
- [_handle_admin_hallucinate_command](_handle_admin_hallucinate_command.md) (1 shared connections)
- [endpoints.py](endpoints.py.md) (1 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (1 shared connections)
- [PlayerDeathService](PlayerDeathService.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [PassiveCorruptionFluxService](PassiveCorruptionFluxService.md) (1 shared connections)

## Source Files

- `server/services/passive_lucidity_flux/__init__.py`
- `server/services/passive_lucidity_flux/config.py`
- `server/services/passive_lucidity_flux/models.py`
- `server/services/passive_lucidity_flux/service.py`
- `server/tests/unit/services/test_passive_lucidity_flux_service.py`

## Audit Trail

- EXTRACTED: 116 (94%)
- INFERRED: 7 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*