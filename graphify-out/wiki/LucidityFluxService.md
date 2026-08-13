# LucidityFluxService

> 93 nodes

## Key Concepts

- **LucidityFluxService** (31 connections) — `server/services/passive_lucidity_flux/service.py`
- **service.py** (31 connections) — `server/services/passive_lucidity_flux/service.py`
- **PerformanceMonitor** (25 connections) — `server/monitoring/performance_monitor.py`
- **.process_tick()** (16 connections) — `server/services/passive_lucidity_flux/service.py`
- **config.py** (11 connections) — `server/services/passive_lucidity_flux/config.py`
- **PassiveFluxContext** (10 connections) — `server/services/passive_lucidity_flux/models.py`
- **._process_single_player()** (10 connections) — `server/services/passive_lucidity_flux/service.py`
- **._resolve_context_async()** (10 connections) — `server/services/passive_lucidity_flux/service.py`
- **PlayerFluxCtx** (9 connections) — `server/services/passive_lucidity_flux/service.py`
- **._resolve_context()** (9 connections) — `server/services/passive_lucidity_flux/service.py`
- **PerformanceMetric** (8 connections) — `server/monitoring/performance_monitor.py`
- **._filter_active_players()** (8 connections) — `server/services/passive_lucidity_flux/service.py`
- **Any** (8 connections)
- **datetime** (8 connections)
- **Player** (8 connections)
- **FluxServiceConfig** (7 connections) — `server/services/passive_lucidity_flux/config.py`
- **CachedRoom** (7 connections) — `server/services/passive_lucidity_flux/models.py`
- **._evaluate_players_tick()** (7 connections) — `server/services/passive_lucidity_flux/service.py`
- **.__init__()** (7 connections) — `server/services/passive_lucidity_flux/service.py`
- **.record_metric()** (6 connections) — `server/monitoring/performance_monitor.py`
- **period_label()** (6 connections) — `server/services/passive_lucidity_flux/config.py`
- **._is_player_active()** (6 connections) — `server/services/passive_lucidity_flux/service.py`
- **._lookup_base_flux_for_room()** (6 connections) — `server/services/passive_lucidity_flux/service.py`
- **passive_lucidity_flux/models.py** (6 connections) — `server/services/passive_lucidity_flux/models.py`
- **.export_metrics()** (5 connections) — `server/monitoring/performance_monitor.py`
- *... and 68 more nodes in this community*

## Relationships

- [MonitoringDashboard](MonitoringDashboard.md) (13 shared connections)
- [LucidityService](LucidityService.md) (12 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [rate_overrides.py](rate_overrides.py.md) (4 shared connections)
- [log_and_raise](log_and_raise.md) (4 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (3 shared connections)
- [hallucinations.py](hallucinations.py.md) (3 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (2 shared connections)
- [fastapi_integration.py](fastapi_integration.py.md) (1 shared connections)
- [deque](deque.md) (1 shared connections)

## Source Files

- `server/monitoring/performance_monitor.py`
- `server/services/passive_lucidity_flux/__init__.py`
- `server/services/passive_lucidity_flux/config.py`
- `server/services/passive_lucidity_flux/models.py`
- `server/services/passive_lucidity_flux/rate_overrides.py`
- `server/services/passive_lucidity_flux/service.py`

## Audit Trail

- EXTRACTED: 221 (95%)
- INFERRED: 12 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*