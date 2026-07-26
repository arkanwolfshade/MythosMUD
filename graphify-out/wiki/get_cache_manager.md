# get_cache_manager

> 66 nodes · cohesion 0.05

## Key Concepts

- **get_cache_manager()** (16 connections) — `server/caching/lru_cache.py`
- **ProfessionCacheService** (15 connections) — `server/caching/cache_service.py`
- **NPCCacheService** (14 connections) — `server/caching/cache_service.py`
- **Any** (13 connections)
- **__init__.py** (12 connections) — `server/caching/__init__.py`
- **CacheService** (8 connections) — `server/caching/cache_service.py`
- **bench_npc_cache()** (7 connections) — `scripts/bench_cache_npc.py`
- **_FakeNPCService** (7 connections) — `scripts/bench_cache_npc.py`
- **bench_cache_professions.py** (7 connections) — `scripts/bench_cache_professions.py`
- **.__init__()** (7 connections) — `server/caching/cache_service.py`
- **bench_cache_npc.py** (6 connections) — `scripts/bench_cache_npc.py`
- **bench_profession_cache()** (6 connections) — `scripts/bench_cache_professions.py`
- **_FakePersistence** (5 connections) — `scripts/bench_cache_professions.py`
- **.get_all_professions()** (5 connections) — `scripts/bench_cache_professions.py`
- **cached()** (5 connections) — `server/caching/cache_service.py`
- **.get_all_professions()** (5 connections) — `server/caching/cache_service.py`
- **.get_npc_definitions()** (4 connections) — `scripts/bench_cache_npc.py`
- **.get_spawn_rules()** (4 connections) — `scripts/bench_cache_npc.py`
- **Any** (4 connections)
- **_get_empty_dict()** (4 connections) — `scripts/bench_cache_professions.py`
- **.preload_frequently_accessed_data()** (4 connections) — `server/caching/cache_service.py`
- **.__init__()** (4 connections) — `server/caching/cache_service.py`
- **.get_profession_by_id()** (4 connections) — `server/caching/cache_service.py`
- **.__init__()** (4 connections) — `server/caching/cache_service.py`
- **.get_room_sync()** (4 connections) — `server/caching/cache_service.py`
- *... and 41 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (11 shared connections)
- [LRUCache](LRUCache.md) (6 shared connections)
- [RoomCacheService](RoomCacheService.md) (5 shared connections)
- [test_communication_commands_flows.py](test_communication_commands_flows.py.md) (4 shared connections)
- [__init__.py](__init__.py.md) (3 shared connections)
- [lifespan.py](lifespan.py.md) (3 shared connections)
- [monitoring.py](monitoring.py.md) (2 shared connections)
- [TaskRegistry](TaskRegistry.md) (1 shared connections)

## Source Files

- `scripts/bench_cache_npc.py`
- `scripts/bench_cache_professions.py`
- `server/caching/__init__.py`
- `server/caching/cache_service.py`
- `server/caching/lru_cache.py`

## Audit Trail

- EXTRACTED: 221 (93%)
- INFERRED: 16 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*