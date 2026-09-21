# NPCCacheService

> 28 nodes

## Key Concepts

- **NPCCacheService** (21 connections) — `server/caching/cache_service.py`
- **test_cache_service.py** (21 connections) — `server/tests/unit/caching/test_cache_service.py`
- **cache_service.py** (14 connections) — `server/caching/cache_service.py`
- **lru_cache.py** (13 connections) — `server/caching/lru_cache.py`
- **server/caching/__init__.py** (12 connections) — `server/caching/__init__.py`
- **asyncio** (10 connections)
- **TestNPCCacheService** (9 connections) — `server/tests/unit/caching/test_cache_service.py`
- **_NpcDef** (5 connections) — `server/tests/unit/caching/test_cache_service.py`
- **reset_cache_manager()** (5 connections) — `server/caching/lru_cache.py`
- **_SpawnRule** (4 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.npc_service()** (4 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_get_definitions_cache_hit()** (4 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_get_npc_definition_hit_and_miss()** (4 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_get_spawn_rules_cache_hit()** (4 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_invalidate_caches()** (4 connections) — `server/tests/unit/caching/test_cache_service.py`
- **_reset_cache_manager()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_get_definitions_cache_miss()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_get_spawn_rules_cache_miss()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.invalidate_npc_definitions()** (2 connections) — `server/caching/cache_service.py`
- **.invalidate_spawn_rules()** (2 connections) — `server/caching/cache_service.py`
- **Cache service for MythosMUD server. This module provides caching services that…** (1 connections) — `server/caching/cache_service.py`
- **Service for caching NPC definitions and spawn rules.** (1 connections) — `server/caching/cache_service.py`
- **Invalidate all NPC definition caches.** (1 connections) — `server/caching/cache_service.py`
- **Invalidate all NPC spawn rule caches.** (1 connections) — `server/caching/cache_service.py`
- **Caching module for MythosMUD server. This module provides comprehensive caching…** (1 connections) — `server/caching/__init__.py`
- *... and 3 more nodes in this community*

## Relationships

- [RoomCacheService](RoomCacheService.md) (13 shared connections)
- [ProfessionCacheService](ProfessionCacheService.md) (7 shared connections)
- [cached](cached.md) (7 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [Any](Any.md) (4 shared connections)
- [LRUCache](LRUCache.md) (4 shared connections)
- [CacheService](CacheService.md) (4 shared connections)
- [bench_cache_npc.py](bench_cache_npc.py.md) (2 shared connections)
- [CacheManager](CacheManager.md) (2 shared connections)
- [RoomService](RoomService.md) (1 shared connections)
- [test_lru_cache.py](test_lru_cache.py.md) (1 shared connections)

## Source Files

- `server/caching/__init__.py`
- `server/caching/cache_service.py`
- `server/caching/lru_cache.py`
- `server/tests/unit/caching/test_cache_service.py`

## Audit Trail

- EXTRACTED: 101 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*