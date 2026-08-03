# cache caching service

> 44 nodes

## Key Concepts

- **NPCCacheService** (14 connections) — `server/caching/cache_service.py`
- **Any** (13 connections)
- **CacheService** (8 connections) — `server/caching/cache_service.py`
- **_FakeNPCService** (7 connections) — `scripts/bench_cache_npc.py`
- **bench_npc_cache()** (7 connections) — `scripts/bench_cache_npc.py`
- **bench_cache_npc.py** (6 connections) — `scripts/bench_cache_npc.py`
- **.get_all_professions()** (5 connections) — `server/caching/cache_service.py`
- **.get_npc_definitions()** (4 connections) — `scripts/bench_cache_npc.py`
- **Any** (4 connections)
- **.get_spawn_rules()** (4 connections) — `scripts/bench_cache_npc.py`
- **.__init__()** (4 connections) — `server/caching/cache_service.py`
- **.get_room_sync()** (4 connections) — `server/caching/cache_service.py`
- **.__init__()** (4 connections) — `server/caching/cache_service.py`
- **.__init__()** (4 connections) — `server/caching/cache_service.py`
- **.get_profession_by_id()** (4 connections) — `server/caching/cache_service.py`
- **.preload_frequently_accessed_data()** (4 connections) — `server/caching/cache_service.py`
- **.get_npc_definition()** (3 connections) — `scripts/bench_cache_npc.py`
- **.get_room()** (3 connections) — `server/caching/cache_service.py`
- **.get_npc_definitions()** (3 connections) — `server/caching/cache_service.py`
- **.get_npc_definition()** (3 connections) — `server/caching/cache_service.py`
- **.get_spawn_rules()** (3 connections) — `server/caching/cache_service.py`
- **.get_cache_stats()** (3 connections) — `server/caching/cache_service.py`
- **main()** (2 connections) — `scripts/bench_cache_npc.py`
- **.invalidate_npc_definitions()** (2 connections) — `server/caching/cache_service.py`
- **.invalidate_spawn_rules()** (2 connections) — `server/caching/cache_service.py`
- *... and 19 more nodes in this community*

## Relationships

- [services lucidity repository](services_lucidity_repository.md) (9 shared connections)
- [command inventory factories](command_inventory_factories.md) (5 shared connections)
- [commands communication flows](commands_communication_flows.md) (3 shared connections)
- [command combat models](command_combat_models.md) (3 shared connections)
- [combat messaging service](combat_messaging_service.md) (2 shared connections)
- [time service rationale](time_service_rationale.md) (1 shared connections)

## Source Files

- `scripts/bench_cache_npc.py`
- `server/caching/cache_service.py`

## Audit Trail

- EXTRACTED: 130 (94%)
- INFERRED: 9 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*