# LucidityFluxService

> 55 nodes

## Key Concepts

- **LucidityFluxService** (32 connections) — `server/services/passive_lucidity_flux/service.py`
- **.process_tick()** (15 connections) — `server/services/passive_lucidity_flux/service.py`
- **._resolve_context_async()** (12 connections) — `server/services/passive_lucidity_flux/service.py`
- **._process_single_player()** (10 connections) — `server/services/passive_lucidity_flux/service.py`
- **._resolve_context()** (10 connections) — `server/services/passive_lucidity_flux/service.py`
- **Player** (10 connections)
- **FluxRoom** (9 connections) — `server/services/passive_lucidity_flux/service.py`
- **._lookup_base_flux_for_room()** (9 connections) — `server/services/passive_lucidity_flux/service.py`
- **._filter_active_players()** (8 connections) — `server/services/passive_lucidity_flux/service.py`
- **datetime** (8 connections)
- **PlayerFluxCtx** (7 connections) — `server/services/passive_lucidity_flux/service.py`
- **._evaluate_players_tick()** (7 connections) — `server/services/passive_lucidity_flux/service.py`
- **CachedRoom** (6 connections) — `server/services/passive_lucidity_flux/models.py`
- **._build_room_cache()** (6 connections) — `server/services/passive_lucidity_flux/service.py`
- **._is_player_active()** (6 connections) — `server/services/passive_lucidity_flux/service.py`
- **._lookup_world_override_flux()** (6 connections) — `server/services/passive_lucidity_flux/service.py`
- **_as_float()** (5 connections) — `server/services/passive_lucidity_flux/service.py`
- **._companion_modifier()** (5 connections) — `server/services/passive_lucidity_flux/service.py`
- **._count_companion_tiers()** (5 connections) — `server/services/passive_lucidity_flux/service.py`
- **._get_room_cached()** (5 connections) — `server/services/passive_lucidity_flux/service.py`
- **._get_room_for_context()** (5 connections) — `server/services/passive_lucidity_flux/service.py`
- **._load_players()** (5 connections) — `server/services/passive_lucidity_flux/service.py`
- **._normalize_datetime_timezone()** (5 connections) — `server/services/passive_lucidity_flux/service.py`
- **AsyncSession** (5 connections)
- **_as_str_attr()** (4 connections) — `server/services/passive_lucidity_flux/service.py`
- *... and 30 more nodes in this community*

## Relationships

- [test_passive_lucidity_flux_service.py](test_passive_lucidity_flux_service.py.md) (11 shared connections)
- [get_logger](get_logger.md) (8 shared connections)
- [LucidityService](LucidityService.md) (7 shared connections)
- [database_config_helpers.py](database_config_helpers.py.md) (2 shared connections)
- [PerformanceMonitor](PerformanceMonitor.md) (1 shared connections)
- [PhantomHostileService](PhantomHostileService.md) (1 shared connections)

## Source Files

- `server/services/passive_lucidity_flux/models.py`
- `server/services/passive_lucidity_flux/service.py`

## Audit Trail

- EXTRACTED: 136 (96%)
- INFERRED: 5 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*