# Cache Service

> 23 nodes

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
- **.get_npc_definition()** (3 connections) — `server/caching/cache_service.py`
- **.get_npc_definitions()** (3 connections) — `server/caching/cache_service.py`
- **.get_spawn_rules()** (3 connections) — `server/caching/cache_service.py`
- **.test_get_definitions_cache_miss()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_get_spawn_rules_cache_miss()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.invalidate_npc_definitions()** (2 connections) — `server/caching/cache_service.py`
- **.invalidate_spawn_rules()** (2 connections) — `server/caching/cache_service.py`
- **Service for caching NPC definitions and spawn rules.** (1 connections) — `server/caching/cache_service.py`
- **Get NPC definitions with caching. Args: session: Database session Returns: List…** (1 connections) — `server/caching/cache_service.py`
- **Get a specific NPC definition with caching. Args: session: Database session…** (1 connections) — `server/caching/cache_service.py`
- **Get NPC spawn rules with caching. Args: session: Database session Returns: List…** (1 connections) — `server/caching/cache_service.py`
- **Invalidate all NPC definition caches.** (1 connections) — `server/caching/cache_service.py`
- **Invalidate all NPC spawn rule caches.** (1 connections) — `server/caching/cache_service.py`

## Relationships

- [Cache Service](Cache_Service.md) (9 shared connections)
- [Test Cache Service](Test_Cache_Service.md) (7 shared connections)
- [Bench Cache Npc](Bench_Cache_Npc.md) (2 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (1 shared connections)
- [Lru Cache](Lru_Cache.md) (1 shared connections)

## Source Files

- `server/caching/cache_service.py`
- `server/tests/unit/caching/test_cache_service.py`

## Audit Trail

- EXTRACTED: 55 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*