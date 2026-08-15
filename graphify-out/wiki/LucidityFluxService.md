# LucidityFluxService

> 105 nodes

## Key Concepts

- **LucidityFluxService** (32 connections) — `server/services/passive_lucidity_flux/service.py`
- **test_passive_lucidity_flux_service.py** (32 connections) — `server/tests/unit/services/test_passive_lucidity_flux_service.py`
- **_make_service()** (22 connections) — `server/tests/unit/services/test_passive_lucidity_flux_service.py`
- **.process_tick()** (15 connections) — `server/services/passive_lucidity_flux/service.py`
- **PassiveFluxContext** (13 connections) — `server/services/passive_lucidity_flux/models.py`
- **._resolve_context_async()** (12 connections) — `server/services/passive_lucidity_flux/service.py`
- **config.py** (12 connections) — `server/services/passive_lucidity_flux/config.py`
- **._process_single_player()** (10 connections) — `server/services/passive_lucidity_flux/service.py`
- **._resolve_context()** (10 connections) — `server/services/passive_lucidity_flux/service.py`
- **Player** (10 connections)
- **FluxServiceConfig** (9 connections) — `server/services/passive_lucidity_flux/config.py`
- **FluxRoom** (9 connections) — `server/services/passive_lucidity_flux/service.py`
- **._lookup_base_flux_for_room()** (9 connections) — `server/services/passive_lucidity_flux/service.py`
- **._filter_active_players()** (8 connections) — `server/services/passive_lucidity_flux/service.py`
- **PassiveLucidityFluxService** (8 connections)
- **datetime** (8 connections)
- **PlayerFluxCtx** (7 connections) — `server/services/passive_lucidity_flux/service.py`
- **._evaluate_players_tick()** (7 connections) — `server/services/passive_lucidity_flux/service.py`
- **.__init__()** (7 connections) — `server/services/passive_lucidity_flux/service.py`
- **passive_lucidity_flux/models.py** (7 connections) — `server/services/passive_lucidity_flux/models.py`
- **CachedRoom** (6 connections) — `server/services/passive_lucidity_flux/models.py`
- **period_label()** (6 connections) — `server/services/passive_lucidity_flux/config.py`
- **._build_room_cache()** (6 connections) — `server/services/passive_lucidity_flux/service.py`
- **._is_player_active()** (6 connections) — `server/services/passive_lucidity_flux/service.py`
- **._lookup_world_override_flux()** (6 connections) — `server/services/passive_lucidity_flux/service.py`
- *... and 80 more nodes in this community*

## Relationships

- [Player](Player.md) (29 shared connections)
- [PerformanceMonitor](PerformanceMonitor.md) (2 shared connections)
- [database_config_helpers.py](database_config_helpers.py.md) (2 shared connections)
- [lucidity_trigger_handlers.py](lucidity_trigger_handlers.py.md) (1 shared connections)
- [PhantomHostileService](PhantomHostileService.md) (1 shared connections)
- [lifespan.py](lifespan.py.md) (1 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/services/passive_lucidity_flux/__init__.py`
- `server/services/passive_lucidity_flux/config.py`
- `server/services/passive_lucidity_flux/models.py`
- `server/services/passive_lucidity_flux/rate_overrides.py`
- `server/services/passive_lucidity_flux/service.py`
- `server/tests/unit/services/test_passive_lucidity_flux_service.py`

## Audit Trail

- EXTRACTED: 241 (96%)
- INFERRED: 11 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*