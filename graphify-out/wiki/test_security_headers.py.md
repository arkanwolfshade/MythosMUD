# test_security_headers.py

> 42 nodes · cohesion 0.09

## Key Concepts

- **LucidityFluxService** (33 connections) — `server/services/passive_lucidity_flux/service.py`
- **.process_tick()** (15 connections) — `server/services/passive_lucidity_flux/service.py`
- **._process_single_player()** (11 connections) — `server/services/passive_lucidity_flux/service.py`
- **Player** (10 connections)
- **PlayerFluxCtx** (9 connections) — `server/services/passive_lucidity_flux/service.py`
- **._apply_player_flux_adjustment()** (8 connections) — `server/services/passive_lucidity_flux/service.py`
- **._filter_active_players()** (8 connections) — `server/services/passive_lucidity_flux/service.py`
- **datetime** (8 connections)
- **._evaluate_players_tick()** (7 connections) — `server/services/passive_lucidity_flux/service.py`
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
- **_PlayerFluxComputation** (4 connections) — `server/services/passive_lucidity_flux/service.py`
- **._apply_adaptive_resistance()** (2 connections) — `server/services/passive_lucidity_flux/service.py`
- **._apply_residual()** (2 connections) — `server/services/passive_lucidity_flux/service.py`
- **._emit_telemetry()** (2 connections) — `server/services/passive_lucidity_flux/service.py`
- **.get_flux_runtime_status()** (2 connections) — `server/services/passive_lucidity_flux/service.py`
- *... and 17 more nodes in this community*

## Relationships

- [ExitEdge.tsx](ExitEdge.tsx.md) (23 shared connections)
- [PopulationStats](PopulationStats.md) (8 shared connections)
- [properties](properties.md) (3 shared connections)
- [_prepare_command_for_processing](_prepare_command_for_processing.md) (1 shared connections)
- [test_config_models.py](test_config_models.py.md) (1 shared connections)

## Source Files

- `server/services/passive_lucidity_flux/service.py`

## Audit Trail

- EXTRACTED: 111 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*