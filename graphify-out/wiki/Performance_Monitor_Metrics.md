# Performance Monitor Metrics

> 69 nodes · cohesion 0.06

## Key Concepts

- **PassiveLucidityFluxService** (34 connections) — `server/services/passive_lucidity_flux/service.py`
- **service.py** (30 connections) — `server/services/passive_lucidity_flux/service.py`
- **.process_tick()** (14 connections) — `server/services/passive_lucidity_flux/service.py`
- **._process_single_player()** (12 connections) — `server/services/passive_lucidity_flux/service.py`
- **config.py** (11 connections) — `server/services/passive_lucidity_flux/config.py`
- **._resolve_context_async()** (10 connections) — `server/services/passive_lucidity_flux/service.py`
- **PassiveFluxContext** (9 connections) — `server/services/passive_lucidity_flux/models.py`
- **._resolve_context()** (9 connections) — `server/services/passive_lucidity_flux/service.py`
- **datetime** (9 connections)
- **._filter_active_players()** (8 connections) — `server/services/passive_lucidity_flux/service.py`
- **Any** (8 connections)
- **Player** (8 connections)
- **.__init__()** (7 connections) — `server/services/passive_lucidity_flux/service.py`
- **FluxServiceConfig** (6 connections) — `server/services/passive_lucidity_flux/config.py`
- **period_label()** (6 connections) — `server/services/passive_lucidity_flux/config.py`
- **__init__.py** (6 connections) — `server/services/passive_lucidity_flux/__init__.py`
- **models.py** (6 connections) — `server/services/passive_lucidity_flux/models.py`
- **CachedRoom** (6 connections) — `server/services/passive_lucidity_flux/models.py`
- **._get_room_cached()** (6 connections) — `server/services/passive_lucidity_flux/service.py`
- **._get_room_for_context()** (6 connections) — `server/services/passive_lucidity_flux/service.py`
- **._is_player_active()** (6 connections) — `server/services/passive_lucidity_flux/service.py`
- **._load_players()** (6 connections) — `server/services/passive_lucidity_flux/service.py`
- **._lookup_base_flux_for_room()** (6 connections) — `server/services/passive_lucidity_flux/service.py`
- **normalize_environment_config()** (5 connections) — `server/services/passive_lucidity_flux/config.py`
- **._build_room_cache()** (5 connections) — `server/services/passive_lucidity_flux/service.py`
- *... and 44 more nodes in this community*

## Relationships

- [Event Bus Serialization](Event_Bus_Serialization.md) (7 shared connections)
- [Lucidity Rate Overrides](Lucidity_Rate_Overrides.md) (4 shared connections)
- [Memory Leak Metrics](Memory_Leak_Metrics.md) (4 shared connections)
- [Rescue Service Tests](Rescue_Service_Tests.md) (4 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (4 shared connections)
- [Lucidity State Models](Lucidity_State_Models.md) (3 shared connections)
- [Hallucination Trigger Service](Hallucination_Trigger_Service.md) (3 shared connections)
- [Realtime Connection Impl](Realtime_Connection_Impl.md) (2 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (2 shared connections)
- [Player Death Service Tests](Player_Death_Service_Tests.md) (2 shared connections)
- [Dependency Injection Tests](Dependency_Injection_Tests.md) (1 shared connections)
- [Commands Inventory Item](Commands_Inventory_Item.md) (1 shared connections)

## Source Files

- `server/services/passive_lucidity_flux/__init__.py`
- `server/services/passive_lucidity_flux/config.py`
- `server/services/passive_lucidity_flux/models.py`
- `server/services/passive_lucidity_flux/rate_overrides.py`
- `server/services/passive_lucidity_flux/service.py`
- `server/services/passive_lucidity_flux_service.py`

## Audit Trail

- EXTRACTED: 307 (95%)
- INFERRED: 15 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*