# cache caching service

> 59 nodes

## Key Concepts

- **RoomCacheService** (17 connections) — `server/caching/cache_service.py`
- **NPCCacheService** (14 connections) — `server/caching/cache_service.py`
- **Any** (13 connections)
- **CacheService** (8 connections) — `server/caching/cache_service.py`
- **_FakeNPCService** (7 connections) — `scripts/bench_cache_npc.py`
- **bench_npc_cache()** (7 connections) — `scripts/bench_cache_npc.py`
- **.__init__()** (7 connections) — `server/caching/cache_service.py`
- **bench_cache.py** (6 connections) — `scripts/bench_cache.py`
- **_FakePersistence** (6 connections) — `scripts/bench_cache.py`
- **bench_cache_npc.py** (6 connections) — `scripts/bench_cache_npc.py`
- **bench_room_cache()** (5 connections) — `scripts/bench_cache.py`
- **.get_all_professions()** (5 connections) — `server/caching/cache_service.py`
- **.get_npc_definitions()** (4 connections) — `scripts/bench_cache_npc.py`
- **Any** (4 connections)
- **.get_spawn_rules()** (4 connections) — `scripts/bench_cache_npc.py`
- **.__init__()** (4 connections) — `server/caching/cache_service.py`
- **.get_room_sync()** (4 connections) — `server/caching/cache_service.py`
- **.__init__()** (4 connections) — `server/caching/cache_service.py`
- **.get_profession_by_id()** (4 connections) — `server/caching/cache_service.py`
- **.preload_frequently_accessed_data()** (4 connections) — `server/caching/cache_service.py`
- **.get_npc_definition()** (3 connections) — `scripts/bench_cache_npc.py`
- **.get_room()** (3 connections) — `server/caching/cache_service.py`
- **.get_npc_definitions()** (3 connections) — `server/caching/cache_service.py`
- **.get_npc_definition()** (3 connections) — `server/caching/cache_service.py`
- **.get_spawn_rules()** (3 connections) — `server/caching/cache_service.py`
- *... and 34 more nodes in this community*

## Relationships

- [NATS Messaging](NATS_Messaging.md) (9 shared connections)
- [bench cache professions](bench_cache_professions.md) (4 shared connections)
- [commands communication flows](commands_communication_flows.md) (3 shared connections)
- [caching lru cache](caching_lru_cache.md) (3 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (3 shared connections)
- [health models rationale](health_models_rationale.md) (3 shared connections)
- [database helpers infrastructure](database_helpers_infrastructure.md) (1 shared connections)

## Source Files

- `scripts/bench_cache.py`
- `scripts/bench_cache_npc.py`
- `server/caching/cache_service.py`

## Audit Trail

- EXTRACTED: 177 (92%)
- INFERRED: 15 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*