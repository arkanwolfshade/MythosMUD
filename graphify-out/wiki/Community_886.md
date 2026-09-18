# Community 886

> 17 nodes

## Key Concepts

- **NPCCacheService** (20 connections) — `server/caching/cache_service.py`
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

- [Community 750](Community_750.md) (7 shared connections)
- [Community 751](Community_751.md) (5 shared connections)
- [Community 752](Community_752.md) (3 shared connections)
- [Community 1182](Community_1182.md) (2 shared connections)
- [Community 1133](Community_1133.md) (2 shared connections)

## Source Files

- `server/caching/cache_service.py`
- `server/tests/unit/caching/test_cache_service.py`

## Audit Trail

- EXTRACTED: 49 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*