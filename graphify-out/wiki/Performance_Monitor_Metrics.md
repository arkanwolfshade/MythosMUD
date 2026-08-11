# Performance Monitor Metrics

> 35 nodes

## Key Concepts

- **LucidityFluxService** (31 connections) — `server/services/passive_lucidity_flux/service.py`
- **.process_tick()** (16 connections) — `server/services/passive_lucidity_flux/service.py`
- **._process_single_player()** (10 connections) — `server/services/passive_lucidity_flux/service.py`
- **._resolve_context_async()** (10 connections) — `server/services/passive_lucidity_flux/service.py`
- **._resolve_context()** (9 connections) — `server/services/passive_lucidity_flux/service.py`
- **Any** (8 connections)
- **Player** (8 connections)
- **._evaluate_players_tick()** (7 connections) — `server/services/passive_lucidity_flux/service.py`
- **._get_room_cached()** (6 connections) — `server/services/passive_lucidity_flux/service.py`
- **._load_players()** (6 connections) — `server/services/passive_lucidity_flux/service.py`
- **._lookup_base_flux_for_room()** (6 connections) — `server/services/passive_lucidity_flux/service.py`
- **._get_room_for_context()** (6 connections) — `server/services/passive_lucidity_flux/service.py`
- **._build_room_cache()** (5 connections) — `server/services/passive_lucidity_flux/service.py`
- **AsyncSession** (5 connections)
- **._count_companion_tiers()** (5 connections) — `server/services/passive_lucidity_flux/service.py`
- **._companion_modifier()** (5 connections) — `server/services/passive_lucidity_flux/service.py`
- **._lookup_world_override_flux()** (5 connections) — `server/services/passive_lucidity_flux/service.py`
- **._commit_flux_adjustments()** (4 connections) — `server/services/passive_lucidity_flux/service.py`
- **._load_lucidity_records()** (4 connections) — `server/services/passive_lucidity_flux/service.py`
- **._should_process_tick()** (2 connections) — `server/services/passive_lucidity_flux/service.py`
- **._apply_adaptive_resistance()** (2 connections) — `server/services/passive_lucidity_flux/service.py`
- **._apply_residual()** (2 connections) — `server/services/passive_lucidity_flux/service.py`
- **._prune_trackers()** (2 connections) — `server/services/passive_lucidity_flux/service.py`
- **._emit_telemetry()** (2 connections) — `server/services/passive_lucidity_flux/service.py`
- **Applies passive LCD flux each in-game minute with structured telemetry.** (1 connections) — `server/services/passive_lucidity_flux/service.py`
- *... and 10 more nodes in this community*

## Relationships

- [End-to-End Validation](End-to-End_Validation.md) (14 shared connections)
- [Cursor Plans Postgresql](Cursor_Plans_Postgresql.md) (10 shared connections)
- [Enhanced Logging Exceptions](Enhanced_Logging_Exceptions.md) (7 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (2 shared connections)
- [Help and WebSocket Core](Help_and_WebSocket_Core.md) (1 shared connections)
- [Hallucination Trigger Service](Hallucination_Trigger_Service.md) (1 shared connections)
- [Zone Config Loader](Zone_Config_Loader.md) (1 shared connections)
- [Test Migration Report](Test_Migration_Report.md) (1 shared connections)

## Source Files

- `server/services/passive_lucidity_flux/service.py`

## Audit Trail

- EXTRACTED: 169 (95%)
- INFERRED: 8 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*