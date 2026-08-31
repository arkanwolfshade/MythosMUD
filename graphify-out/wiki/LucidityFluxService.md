# LucidityFluxService

> 40 nodes

## Key Concepts

- **LucidityFluxService** (32 connections) — `server/services/passive_lucidity_flux/service.py`
- **.process_tick()** (15 connections) — `server/services/passive_lucidity_flux/service.py`
- **._process_single_player()** (10 connections) — `server/services/passive_lucidity_flux/service.py`
- **Player** (10 connections)
- **._filter_active_players()** (8 connections) — `server/services/passive_lucidity_flux/service.py`
- **datetime** (8 connections)
- **PlayerFluxCtx** (7 connections) — `server/services/passive_lucidity_flux/service.py`
- **._evaluate_players_tick()** (7 connections) — `server/services/passive_lucidity_flux/service.py`
- **CachedRoom** (6 connections) — `server/services/passive_lucidity_flux/models.py`
- **._build_room_cache()** (6 connections) — `server/services/passive_lucidity_flux/service.py`
- **._is_player_active()** (6 connections) — `server/services/passive_lucidity_flux/service.py`
- **._companion_modifier()** (5 connections) — `server/services/passive_lucidity_flux/service.py`
- **._count_companion_tiers()** (5 connections) — `server/services/passive_lucidity_flux/service.py`
- **._get_room_cached()** (5 connections) — `server/services/passive_lucidity_flux/service.py`
- **._load_players()** (5 connections) — `server/services/passive_lucidity_flux/service.py`
- **._normalize_datetime_timezone()** (5 connections) — `server/services/passive_lucidity_flux/service.py`
- **AsyncSession** (5 connections)
- **._commit_flux_adjustments()** (4 connections) — `server/services/passive_lucidity_flux/service.py`
- **._load_lucidity_records()** (4 connections) — `server/services/passive_lucidity_flux/service.py`
- **._parse_last_active()** (4 connections) — `server/services/passive_lucidity_flux/service.py`
- **._apply_adaptive_resistance()** (2 connections) — `server/services/passive_lucidity_flux/service.py`
- **._apply_residual()** (2 connections) — `server/services/passive_lucidity_flux/service.py`
- **._emit_telemetry()** (2 connections) — `server/services/passive_lucidity_flux/service.py`
- **.get_flux_runtime_status()** (2 connections) — `server/services/passive_lucidity_flux/service.py`
- **._prune_trackers()** (2 connections) — `server/services/passive_lucidity_flux/service.py`
- *... and 15 more nodes in this community*

## Relationships

- [service.py](service.py.md) (18 shared connections)
- [LucidityService](LucidityService.md) (7 shared connections)
- [test_passive_lucidity_flux_service.py](test_passive_lucidity_flux_service.py.md) (4 shared connections)
- [passive_lucidity_flux/models.py](passive_lucidity_flux-models.py.md) (2 shared connections)
- [PerformanceMonitor](PerformanceMonitor.md) (1 shared connections)
- [test_hallucination_services.py](test_hallucination_services.py.md) (1 shared connections)

## Source Files

- `server/services/passive_lucidity_flux/models.py`
- `server/services/passive_lucidity_flux/service.py`

## Audit Trail

- EXTRACTED: 103 (95%)
- INFERRED: 5 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*