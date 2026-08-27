# NPCCacheService

> 17 nodes

## Key Concepts

- **NPCCacheService** (21 connections) — `server/caching/cache_service.py`
- **asyncio** (10 connections)
- **TestNPCCacheService** (9 connections) — `server/tests/unit/caching/test_cache_service.py`
- **_NpcDef** (5 connections) — `server/tests/unit/caching/test_cache_service.py`
- **_SpawnRule** (4 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.npc_service()** (4 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_get_definitions_cache_hit()** (4 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_get_npc_definition_hit_and_miss()** (4 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_get_spawn_rules_cache_hit()** (4 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_invalidate_caches()** (4 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_get_definitions_cache_miss()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_get_spawn_rules_cache_miss()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.invalidate_npc_definitions()** (2 connections) — `server/caching/cache_service.py`
- **.invalidate_spawn_rules()** (2 connections) — `server/caching/cache_service.py`
- **Service for caching NPC definitions and spawn rules.** (1 connections) — `server/caching/cache_service.py`
- **Invalidate all NPC definition caches.** (1 connections) — `server/caching/cache_service.py`
- **Invalidate all NPC spawn rule caches.** (1 connections) — `server/caching/cache_service.py`

## Relationships

- [test_cache_service.py](test_cache_service.py.md) (8 shared connections)
- [Any](Any.md) (4 shared connections)
- [RoomCacheService](RoomCacheService.md) (3 shared connections)
- [bench_cache_npc.py](bench_cache_npc.py.md) (2 shared connections)
- [CacheService](CacheService.md) (1 shared connections)
- [LRUCache](LRUCache.md) (1 shared connections)
- [ProfessionCacheService](ProfessionCacheService.md) (1 shared connections)

## Source Files

- `server/caching/cache_service.py`
- `server/tests/unit/caching/test_cache_service.py`

## Audit Trail

- EXTRACTED: 49 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*