# test_health_monitor.py

> 40 nodes

## Key Concepts

- **LucidityFluxService** (29 connections) — `server/services/passive_lucidity_flux/service.py`
- **.process_tick()** (15 connections) — `server/services/passive_lucidity_flux/service.py`
- **._process_single_player()** (10 connections) — `server/services/passive_lucidity_flux/service.py`
- **Player** (10 connections)
- **._filter_active_players()** (9 connections) — `server/services/passive_lucidity_flux/service.py`
- **datetime** (8 connections)
- **._evaluate_players_tick()** (7 connections) — `server/services/passive_lucidity_flux/service.py`
- **._is_player_active()** (7 connections) — `server/services/passive_lucidity_flux/service.py`
- **._build_room_cache()** (6 connections) — `server/services/passive_lucidity_flux/service.py`
- **._companion_modifier()** (5 connections) — `server/services/passive_lucidity_flux/service.py`
- **._count_companion_tiers()** (5 connections) — `server/services/passive_lucidity_flux/service.py`
- **._get_room_for_context()** (5 connections) — `server/services/passive_lucidity_flux/service.py`
- **._load_players()** (5 connections) — `server/services/passive_lucidity_flux/service.py`
- **._normalize_datetime_timezone()** (5 connections) — `server/services/passive_lucidity_flux/service.py`
- **AsyncSession** (5 connections)
- **._commit_flux_adjustments()** (4 connections) — `server/services/passive_lucidity_flux/service.py`
- **._get_room_cached()** (4 connections) — `server/services/passive_lucidity_flux/service.py`
- **._load_lucidity_records()** (4 connections) — `server/services/passive_lucidity_flux/service.py`
- **._parse_last_active()** (4 connections) — `server/services/passive_lucidity_flux/service.py`
- **LucidityUpdateResult** (3 connections)
- **PlayerLucidity** (3 connections)
- **._apply_adaptive_resistance()** (2 connections) — `server/services/passive_lucidity_flux/service.py`
- **._apply_residual()** (2 connections) — `server/services/passive_lucidity_flux/service.py`
- **._emit_telemetry()** (2 connections) — `server/services/passive_lucidity_flux/service.py`
- **.get_flux_runtime_status()** (2 connections) — `server/services/passive_lucidity_flux/service.py`
- *... and 15 more nodes in this community*

## Relationships

- [Entries](Entries.md) (13 shared connections)
- [Memory Leak Audit Report](Memory_Leak_Audit_Report.md) (3 shared connections)
- [ContainerComponent](ContainerComponent.md) (2 shared connections)
- [properties](properties.md) (2 shared connections)
- [Procedures as CRUD Boundary](Procedures_as_CRUD_Boundary.md) (1 shared connections)
- [TestMonitoringEndpoints](TestMonitoringEndpoints.md) (1 shared connections)
- [asyncio](asyncio.md) (1 shared connections)
- [look_command.py](look_command.py.md) (1 shared connections)

## Source Files

- `server/services/passive_lucidity_flux/service.py`

## Audit Trail

- EXTRACTED: 98 (97%)
- INFERRED: 3 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*