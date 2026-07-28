# Cache and NPC Cache

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

- [Distributed Event Bus](Distributed_Event_Bus.md) (11 shared connections)
- [LRU Cache Manager](LRU_Cache_Manager.md) (6 shared connections)
- [Real-Time Architecture Docs](Real-Time_Architecture_Docs.md) (5 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (4 shared connections)
- [Weapon Resolution Helpers](Weapon_Resolution_Helpers.md) (3 shared connections)
- [Memory Leak Metrics](Memory_Leak_Metrics.md) (3 shared connections)
- [Monitoring Response Models](Monitoring_Response_Models.md) (2 shared connections)
- [Async Task Registry](Async_Task_Registry.md) (1 shared connections)

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