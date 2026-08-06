# lucidity flux passive

> 48 nodes

## Key Concepts

- **PassiveLucidityFluxService** (41 connections) — `server/services/passive_lucidity_flux/service.py`
- **.process_tick()** (14 connections) — `server/services/passive_lucidity_flux/service.py`
- **._process_single_player()** (12 connections) — `server/services/passive_lucidity_flux/service.py`
- **._resolve_context_async()** (10 connections) — `server/services/passive_lucidity_flux/service.py`
- **datetime** (9 connections)
- **._resolve_context()** (9 connections) — `server/services/passive_lucidity_flux/service.py`
- **Any** (8 connections)
- **Player** (8 connections)
- **._filter_active_players()** (8 connections) — `server/services/passive_lucidity_flux/service.py`
- **._get_room_cached()** (6 connections) — `server/services/passive_lucidity_flux/service.py`
- **._load_players()** (6 connections) — `server/services/passive_lucidity_flux/service.py`
- **._is_player_active()** (6 connections) — `server/services/passive_lucidity_flux/service.py`
- **._lookup_base_flux_for_room()** (6 connections) — `server/services/passive_lucidity_flux/service.py`
- **._get_room_for_context()** (6 connections) — `server/services/passive_lucidity_flux/service.py`
- **._build_room_cache()** (5 connections) — `server/services/passive_lucidity_flux/service.py`
- **._normalize_datetime_timezone()** (5 connections) — `server/services/passive_lucidity_flux/service.py`
- **._count_companion_tiers()** (5 connections) — `server/services/passive_lucidity_flux/service.py`
- **._companion_modifier()** (5 connections) — `server/services/passive_lucidity_flux/service.py`
- **._lookup_world_override_flux()** (5 connections) — `server/services/passive_lucidity_flux/service.py`
- **AsyncSession** (4 connections)
- **._parse_last_active()** (4 connections) — `server/services/passive_lucidity_flux/service.py`
- **._load_lucidity_records()** (4 connections) — `server/services/passive_lucidity_flux/service.py`
- **passive_lucidity_flux_service.py** (3 connections) — `server/services/passive_lucidity_flux_service.py`
- **._should_process_tick()** (2 connections) — `server/services/passive_lucidity_flux/service.py`
- **._apply_adaptive_resistance()** (2 connections) — `server/services/passive_lucidity_flux/service.py`
- *... and 23 more nodes in this community*

## Relationships

- [command parser rationale](command_parser_rationale.md) (14 shared connections)
- [cache lru caching](cache_lru_caching.md) (6 shared connections)
- [player room realtime](player_room_realtime.md) (5 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (2 shared connections)
- [catatonia registry services](catatonia_registry_services.md) (1 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (1 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (1 shared connections)
- [models lucidity rationale](models_lucidity_rationale.md) (1 shared connections)
- [npc population stats](npc_population_stats.md) (1 shared connections)
- [persistence rationale players](persistence_rationale_players.md) (1 shared connections)
- [rate lucidity services](rate_lucidity_services.md) (1 shared connections)
- [Error Conversion](Error_Conversion.md) (1 shared connections)

## Source Files

- `server/services/passive_lucidity_flux/service.py`
- `server/services/passive_lucidity_flux_service.py`
- `server/tests/unit/services/test_passive_lucidity_flux_service.py`

## Audit Trail

- EXTRACTED: 213 (96%)
- INFERRED: 10 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*