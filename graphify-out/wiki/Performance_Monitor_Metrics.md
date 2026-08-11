# Performance Monitor Metrics

> 71 nodes

## Key Concepts

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
- **__init__.py** (5 connections) — `server/services/passive_lucidity_flux/__init__.py`
- *... and 46 more nodes in this community*

## Relationships

- [Enhanced Logging Exceptions](Enhanced_Logging_Exceptions.md) (7 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (5 shared connections)
- [Client Event Store](Client_Event_Store.md) (5 shared connections)
- [Memory Leak Metrics](Memory_Leak_Metrics.md) (5 shared connections)
- [Test Migration Report](Test_Migration_Report.md) (4 shared connections)
- [Message Queue Cleanup](Message_Queue_Cleanup.md) (4 shared connections)
- [Hallucination Trigger Service](Hallucination_Trigger_Service.md) (3 shared connections)
- [Schemas Maps Map](Schemas_Maps_Map.md) (2 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (1 shared connections)
- [Calendar NPC Schedule](Calendar_NPC_Schedule.md) (1 shared connections)

## Source Files

- `server/services/passive_lucidity_flux/__init__.py`
- `server/services/passive_lucidity_flux/config.py`
- `server/services/passive_lucidity_flux/models.py`
- `server/services/passive_lucidity_flux/rate_overrides.py`
- `server/services/passive_lucidity_flux/service.py`

## Audit Trail

- EXTRACTED: 318 (94%)
- INFERRED: 21 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*