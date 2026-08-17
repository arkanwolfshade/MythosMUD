# LucidityFluxService

> 29 nodes

## Key Concepts

- **LucidityFluxService** (32 connections) — `server/services/passive_lucidity_flux/service.py`
- **.process_tick()** (15 connections) — `server/services/passive_lucidity_flux/service.py`
- **._process_single_player()** (10 connections) — `server/services/passive_lucidity_flux/service.py`
- **Player** (10 connections)
- **PlayerFluxCtx** (7 connections) — `server/services/passive_lucidity_flux/service.py`
- **._evaluate_players_tick()** (7 connections) — `server/services/passive_lucidity_flux/service.py`
- **._build_room_cache()** (6 connections) — `server/services/passive_lucidity_flux/service.py`
- **._companion_modifier()** (5 connections) — `server/services/passive_lucidity_flux/service.py`
- **._count_companion_tiers()** (5 connections) — `server/services/passive_lucidity_flux/service.py`
- **._get_room_cached()** (5 connections) — `server/services/passive_lucidity_flux/service.py`
- **._load_players()** (5 connections) — `server/services/passive_lucidity_flux/service.py`
- **AsyncSession** (5 connections)
- **._commit_flux_adjustments()** (4 connections) — `server/services/passive_lucidity_flux/service.py`
- **._load_lucidity_records()** (4 connections) — `server/services/passive_lucidity_flux/service.py`
- **._apply_adaptive_resistance()** (2 connections) — `server/services/passive_lucidity_flux/service.py`
- **._apply_residual()** (2 connections) — `server/services/passive_lucidity_flux/service.py`
- **._emit_telemetry()** (2 connections) — `server/services/passive_lucidity_flux/service.py`
- **.get_flux_runtime_status()** (2 connections) — `server/services/passive_lucidity_flux/service.py`
- **._prune_trackers()** (2 connections) — `server/services/passive_lucidity_flux/service.py`
- **._should_process_tick()** (2 connections) — `server/services/passive_lucidity_flux/service.py`
- **Build room cache for all players.** (1 connections) — `server/services/passive_lucidity_flux/service.py`
- **Process a single player's passive flux.** (1 connections) — `server/services/passive_lucidity_flux/service.py`
- **Evaluate passive LCD flux for the current tick.** (1 connections) — `server/services/passive_lucidity_flux/service.py`
- **Snapshot of scheduler state for ops and tests.** (1 connections) — `server/services/passive_lucidity_flux/service.py`
- **Get room from cache or fetch from database with TTL management.** (1 connections) — `server/services/passive_lucidity_flux/service.py`
- *... and 4 more nodes in this community*

## Relationships

- [ApplicationContainer](ApplicationContainer.md) (12 shared connections)
- [._resolve_context_async](_resolve_context_async.md) (11 shared connections)
- [._filter_active_players](_filter_active_players.md) (8 shared connections)
- [test_passive_lucidity_flux_service.py](test_passive_lucidity_flux_service.py.md) (4 shared connections)
- [PerformanceMonitor](PerformanceMonitor.md) (1 shared connections)
- [PhantomHostileService](PhantomHostileService.md) (1 shared connections)

## Source Files

- `server/services/passive_lucidity_flux/service.py`

## Audit Trail

- EXTRACTED: 84 (94%)
- INFERRED: 5 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*