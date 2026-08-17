# server services passive lucidity flux

> 31 nodes

## Key Concepts

- **LucidityFluxService** (32 connections) — `server/services/passive_lucidity_flux/service.py`
- **.process_tick()** (15 connections) — `server/services/passive_lucidity_flux/service.py`
- **._process_single_player()** (10 connections) — `server/services/passive_lucidity_flux/service.py`
- **Player** (10 connections)
- **PlayerFluxCtx** (7 connections) — `server/services/passive_lucidity_flux/service.py`
- **._evaluate_players_tick()** (7 connections) — `server/services/passive_lucidity_flux/service.py`
- **CachedRoom** (6 connections) — `server/services/passive_lucidity_flux/models.py`
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
- **Cached room entry with timestamp for TTL management.** (1 connections) — `server/services/passive_lucidity_flux/models.py`
- **Build room cache for all players.** (1 connections) — `server/services/passive_lucidity_flux/service.py`
- **Process a single player's passive flux.** (1 connections) — `server/services/passive_lucidity_flux/service.py`
- **Evaluate passive LCD flux for the current tick.** (1 connections) — `server/services/passive_lucidity_flux/service.py`
- *... and 6 more nodes in this community*

## Relationships

- [server services passive lucidity flux](server_services_passive_lucidity_flux.md) (23 shared connections)
- [server commands admin setlucidity command](server_commands_admin_setlucidity_command.md) (7 shared connections)
- [passivelucidityfluxservice](passivelucidityfluxservice.md) (4 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (3 shared connections)
- [server monitoring init getattr](server_monitoring_init_getattr.md) (1 shared connections)

## Source Files

- `server/services/passive_lucidity_flux/models.py`
- `server/services/passive_lucidity_flux/service.py`

## Audit Trail

- EXTRACTED: 88 (95%)
- INFERRED: 5 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*