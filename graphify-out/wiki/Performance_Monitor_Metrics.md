# Performance Monitor Metrics

> 75 nodes

## Key Concepts

- **player.py** (82 connections) — `server/models/player.py`
- **service.py** (31 connections) — `server/services/passive_lucidity_flux/service.py`
- **LucidityFluxService** (31 connections) — `server/services/passive_lucidity_flux/service.py`
- **.process_tick()** (16 connections) — `server/services/passive_lucidity_flux/service.py`
- **config.py** (11 connections) — `server/services/passive_lucidity_flux/config.py`
- **PassiveFluxContext** (10 connections) — `server/services/passive_lucidity_flux/models.py`
- **._process_single_player()** (10 connections) — `server/services/passive_lucidity_flux/service.py`
- **._resolve_context_async()** (10 connections) — `server/services/passive_lucidity_flux/service.py`
- **PlayerFluxCtx** (9 connections) — `server/services/passive_lucidity_flux/service.py`
- **._resolve_context()** (9 connections) — `server/services/passive_lucidity_flux/service.py`
- **Any** (8 connections)
- **datetime** (8 connections)
- **Player** (8 connections)
- **._filter_active_players()** (8 connections) — `server/services/passive_lucidity_flux/service.py`
- **FluxServiceConfig** (7 connections) — `server/services/passive_lucidity_flux/config.py`
- **CachedRoom** (7 connections) — `server/services/passive_lucidity_flux/models.py`
- **.__init__()** (7 connections) — `server/services/passive_lucidity_flux/service.py`
- **._evaluate_players_tick()** (7 connections) — `server/services/passive_lucidity_flux/service.py`
- **period_label()** (6 connections) — `server/services/passive_lucidity_flux/config.py`
- **models.py** (6 connections) — `server/services/passive_lucidity_flux/models.py`
- **._get_room_cached()** (6 connections) — `server/services/passive_lucidity_flux/service.py`
- **._load_players()** (6 connections) — `server/services/passive_lucidity_flux/service.py`
- **._is_player_active()** (6 connections) — `server/services/passive_lucidity_flux/service.py`
- **._lookup_base_flux_for_room()** (6 connections) — `server/services/passive_lucidity_flux/service.py`
- **._get_room_for_context()** (6 connections) — `server/services/passive_lucidity_flux/service.py`
- *... and 50 more nodes in this community*

## Relationships

- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (14 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (13 shared connections)
- [Player Creation Service](Player_Creation_Service.md) (10 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (8 shared connections)
- [Memory Leak Metrics](Memory_Leak_Metrics.md) (5 shared connections)
- [Combat Messaging Tests](Combat_Messaging_Tests.md) (4 shared connections)
- [Dependency Upgrade Report](Dependency_Upgrade_Report.md) (4 shared connections)
- [Test Migration Report](Test_Migration_Report.md) (4 shared connections)
- [Whisper Remediation Plan](Whisper_Remediation_Plan.md) (3 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (3 shared connections)
- [Restart Invalidating JWT](Restart_Invalidating_JWT.md) (3 shared connections)
- [NATS Message Broker](NATS_Message_Broker.md) (3 shared connections)

## Source Files

- `server/models/player.py`
- `server/services/passive_lucidity_flux/__init__.py`
- `server/services/passive_lucidity_flux/config.py`
- `server/services/passive_lucidity_flux/models.py`
- `server/services/passive_lucidity_flux/rate_overrides.py`
- `server/services/passive_lucidity_flux/service.py`

## Audit Trail

- EXTRACTED: 405 (95%)
- INFERRED: 21 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*