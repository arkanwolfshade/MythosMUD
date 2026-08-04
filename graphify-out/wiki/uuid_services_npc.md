# uuid services npc

> 16 nodes

## Key Concepts

- **NPCCacheService** (30 connections) — `server/caching/cache_service.py`
- **TestNPCCacheService** (12 connections) — `server/tests/unit/caching/test_cache_service.py`
- **_NpcDef** (9 connections) — `server/tests/unit/caching/test_cache_service.py`
- **_SpawnRule** (8 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_invalidate_caches()** (4 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.npc_service()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_get_definitions_cache_hit()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_get_npc_definition_hit_and_miss()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_get_spawn_rules_cache_hit()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.invalidate_npc_definitions()** (2 connections) — `server/caching/cache_service.py`
- **.invalidate_spawn_rules()** (2 connections) — `server/caching/cache_service.py`
- **.test_get_definitions_cache_miss()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_get_spawn_rules_cache_miss()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **Service for caching NPC definitions and spawn rules.** (1 connections) — `server/caching/cache_service.py`
- **Invalidate all NPC definition caches.** (1 connections) — `server/caching/cache_service.py`
- **Invalidate all NPC spawn rule caches.** (1 connections) — `server/caching/cache_service.py`

## Relationships

- [commands skills rationale](commands_skills_rationale.md) (7 shared connections)
- [startup npc service](startup_npc_service.md) (6 shared connections)
- [services lucidity repository](services_lucidity_repository.md) (5 shared connections)
- [cache caching service](cache_caching_service.md) (4 shared connections)
- [config rationale config()](config_rationale_config%28%29.md) (4 shared connections)
- [ascii map renderer](ascii_map_renderer.md) (3 shared connections)
- [caching lru cache](caching_lru_cache.md) (1 shared connections)

## Source Files

- `server/caching/cache_service.py`
- `server/tests/unit/caching/test_cache_service.py`

## Audit Trail

- EXTRACTED: 63 (73%)
- INFERRED: 23 (27%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*