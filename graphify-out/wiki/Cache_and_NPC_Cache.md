# Cache and NPC Cache

> 62 nodes · cohesion 0.05

## Key Concepts

- **ProfessionCacheService** (20 connections) — `server/caching/cache_service.py`
- **get_cache_manager()** (16 connections) — `server/caching/lru_cache.py`
- **NPCCacheService** (15 connections) — `server/caching/cache_service.py`
- **Any** (14 connections) — `server/caching/cache_service.py`
- **cache_service.py** (13 connections) — `server/caching/cache_service.py`
- **__init__.py** (12 connections) — `server/caching/__init__.py`
- **lru_cache.py** (9 connections) — `server/caching/lru_cache.py`
- **CacheService** (8 connections) — `server/caching/cache_service.py`
- **.__init__()** (7 connections) — `server/caching/cache_service.py`
- **bench_cache_professions.py** (6 connections) — `scripts/bench_cache_professions.py`
- **bench_profession_cache()** (6 connections) — `scripts/bench_cache_professions.py`
- **cached()** (5 connections) — `server/caching/cache_service.py`
- **.__init__()** (5 connections) — `server/caching/cache_service.py`
- **.get_all_professions()** (5 connections) — `server/caching/cache_service.py`
- **.__init__()** (5 connections) — `server/caching/cache_service.py`
- **.__init__()** (5 connections) — `server/caching/cache_service.py`
- **_FakePersistence** (5 connections) — `scripts/bench_cache_professions.py`
- **.preload_frequently_accessed_data()** (4 connections) — `server/caching/cache_service.py`
- **.get_profession_by_id()** (4 connections) — `server/caching/cache_service.py`
- **.get_room_sync()** (4 connections) — `server/caching/cache_service.py`
- **.get_all_professions()** (4 connections) — `scripts/bench_cache_professions.py`
- **Any** (4 connections) — `scripts/bench_cache_professions.py`
- **.get_cache_stats()** (3 connections) — `server/caching/cache_service.py`
- **.get_npc_definition()** (3 connections) — `server/caching/cache_service.py`
- **.get_npc_definitions()** (3 connections) — `server/caching/cache_service.py`
- *... and 37 more nodes in this community*

## Relationships

- [[Game Service Bundle]] (13 shared connections)
- [[LRU Cache Manager]] (11 shared connections)
- [[NPC Admin API]] (5 shared connections)
- [[Bench Cache Npc]] (4 shared connections)
- [[Database Manager Tests]] (3 shared connections)
- [[Monitoring API Endpoints]] (2 shared connections)
- [[System Monitoring API]] (2 shared connections)
- [[App Lifespan Management]] (1 shared connections)
- [[Memory Leak Metrics]] (1 shared connections)
- [[Communication Command Flows]] (1 shared connections)

## Source Files

- `scripts/bench_cache_professions.py`
- `server/caching/__init__.py`
- `server/caching/cache_service.py`
- `server/caching/lru_cache.py`

## Audit Trail

- EXTRACTED: 216 (92%)
- INFERRED: 19 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
