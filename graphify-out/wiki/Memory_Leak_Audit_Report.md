# Memory Leak Audit Report

> 35 nodes

## Key Concepts

- **test_passive_lucidity_flux_service.py** (33 connections) — `server/tests/unit/services/test_passive_lucidity_flux_service.py`
- **_make_service()** (22 connections) — `server/tests/unit/services/test_passive_lucidity_flux_service.py`
- **PassiveFluxContext** (9 connections) — `server/services/passive_lucidity_flux/models.py`
- **PlayerFluxCtx** (7 connections) — `server/services/passive_lucidity_flux/service.py`
- **FluxServiceConfig** (6 connections) — `server/services/passive_lucidity_flux/config.py`
- **PassiveLucidityFluxService** (6 connections)
- **asyncio** (6 connections)
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
- **test_emit_telemetry_records_metric()** (2 connections) — `server/tests/unit/services/test_passive_lucidity_flux_service.py`
- **test_emit_telemetry_with_error()** (2 connections) — `server/tests/unit/services/test_passive_lucidity_flux_service.py`
- **test_filter_active_players_includes_recent_and_null_last_active()** (2 connections) — `server/tests/unit/services/test_passive_lucidity_flux_service.py`
- **test_is_player_active_recent()** (2 connections) — `server/tests/unit/services/test_passive_lucidity_flux_service.py`
- **test_lookup_base_flux_for_room_overrides()** (2 connections) — `server/tests/unit/services/test_passive_lucidity_flux_service.py`
- *... and 10 more nodes in this community*

## Relationships

- [fixture](fixture.md) (6 shared connections)
- [test_health_monitor.py](test_health_monitor.py.md) (3 shared connections)
- [ContainerComponent](ContainerComponent.md) (3 shared connections)
- [NATSMetrics](NATSMetrics.md) (1 shared connections)

## Source Files

- `server/services/passive_lucidity_flux/config.py`
- `server/services/passive_lucidity_flux/models.py`
- `server/services/passive_lucidity_flux/service.py`
- `server/tests/unit/services/test_passive_lucidity_flux_service.py`

## Audit Trail

- EXTRACTED: 80 (96%)
- INFERRED: 3 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*