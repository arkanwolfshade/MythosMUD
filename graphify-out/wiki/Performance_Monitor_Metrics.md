# Performance Monitor Metrics

> 96 nodes · cohesion 0.05

## Key Concepts

- **PerformanceMonitor** (35 connections) — `server/monitoring/performance_monitor.py`
- **PassiveLucidityFluxService** (32 connections) — `server/services/passive_lucidity_flux/service.py`
- **passive_lucidity_flux_service.py** (30 connections) — `server/services/passive_lucidity_flux_service.py`
- **PassiveFluxContext** (20 connections) — `server/services/passive_lucidity_flux/models.py`
- **CachedRoom** (17 connections) — `server/services/passive_lucidity_flux/models.py`
- **FluxServiceConfig** (16 connections) — `server/services/passive_lucidity_flux/config.py`
- **.process_tick()** (13 connections) — `server/services/passive_lucidity_flux/service.py`
- **datetime** (13 connections) — `server/services/passive_lucidity_flux/service.py`
- **._process_single_player()** (12 connections) — `server/services/passive_lucidity_flux/service.py`
- **Any** (12 connections) — `server/services/passive_lucidity_flux/service.py`
- **Player** (12 connections) — `server/services/passive_lucidity_flux/service.py`
- **config.py** (11 connections) — `server/services/passive_lucidity_flux/config.py`
- **._resolve_context_async()** (10 connections) — `server/services/passive_lucidity_flux/service.py`
- **._resolve_context()** (9 connections) — `server/services/passive_lucidity_flux/service.py`
- **PerformanceMetric** (8 connections) — `server/monitoring/performance_monitor.py`
- **.record_metric()** (8 connections) — `server/monitoring/performance_monitor.py`
- **._filter_active_players()** (8 connections) — `server/services/passive_lucidity_flux/service.py`
- **AsyncSession** (8 connections) — `server/services/passive_lucidity_flux/service.py`
- **.__init__()** (7 connections) — `server/services/passive_lucidity_flux/service.py`
- **PlayerLucidity** (7 connections) — `server/services/passive_lucidity_flux/service.py`
- **.get_operation_stats()** (6 connections) — `server/monitoring/performance_monitor.py`
- **period_label()** (6 connections) — `server/services/passive_lucidity_flux/config.py`
- **models.py** (6 connections) — `server/services/passive_lucidity_flux/models.py`
- **._is_player_active()** (6 connections) — `server/services/passive_lucidity_flux/service.py`
- **._lookup_base_flux_for_room()** (6 connections) — `server/services/passive_lucidity_flux/service.py`
- *... and 71 more nodes in this community*

## Relationships

- [[App Lifespan Management]] (13 shared connections)
- [[Monitoring Bundle Services]] (4 shared connections)
- [[Lucidity Rate Overrides]] (4 shared connections)
- [[Hallucination Trigger Service]] (3 shared connections)
- [[NPC Admin API]] (3 shared connections)
- [[FastAPI Auth Integration]] (2 shared connections)
- [[Memory Leak Metrics]] (2 shared connections)
- [[Logging Correct Patterns]] (2 shared connections)
- [[SQLAlchemy Model Base]] (2 shared connections)
- [[Player Domain Model]] (2 shared connections)
- [[Lucidity Database Models]] (2 shared connections)
- [[Message Queue Cleanup]] (1 shared connections)

## Source Files

- `server/monitoring/performance_monitor.py`
- `server/services/passive_lucidity_flux/__init__.py`
- `server/services/passive_lucidity_flux/config.py`
- `server/services/passive_lucidity_flux/models.py`
- `server/services/passive_lucidity_flux/rate_overrides.py`
- `server/services/passive_lucidity_flux/service.py`
- `server/services/passive_lucidity_flux_service.py`

## Audit Trail

- EXTRACTED: 376 (76%)
- INFERRED: 122 (24%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
