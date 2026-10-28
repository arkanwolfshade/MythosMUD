# Persistence Layer Extraction - COMPLETE ✅

> 17 nodes · cohesion 0.23

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

- [LucidityTierCache](LucidityTierCache.md) (8 shared connections)
- [ConnectionManager Refactoring Summary](ConnectionManager_Refactoring_Summary.md) (5 shared connections)
- [fixture](fixture.md) (3 shared connections)
- [Codacy Rules](Codacy_Rules.md) (2 shared connections)
- [.get_upcoming_holidays](get_upcoming_holidays.md) (1 shared connections)
- [Test Coverage Summary: Disconnect Grace Period & Rest Command](Test_Coverage_Summary-_Disconnect_Grace_Period_&_Rest_Command.md) (1 shared connections)

## Source Files

- `server/caching/cache_service.py`
- `server/tests/unit/caching/test_cache_service.py`

## Audit Trail

- EXTRACTED: 49 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*