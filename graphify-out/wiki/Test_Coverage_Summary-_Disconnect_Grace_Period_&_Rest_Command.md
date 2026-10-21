# Test Coverage Summary: Disconnect Grace Period & Rest Command

> 15 nodes · cohesion 0.19

## Key Concepts

- **ProfessionCacheService** (20 connections) — `server/caching/cache_service.py`
- **TestProfessionCacheService** (7 connections) — `server/tests/unit/caching/test_cache_service.py`
- **fixture** (5 connections)
- **.__init__()** (4 connections) — `server/caching/cache_service.py`
- **_Profession** (4 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.persistence()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.persistence()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_get_profession_by_id_hit_and_miss()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.invalidate_professions()** (2 connections) — `server/caching/cache_service.py`
- **.test_get_all_professions_hit_and_miss()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_get_profession_by_id_not_found()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_invalidate_professions()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **Service for caching profession data.** (1 connections) — `server/caching/cache_service.py`
- **Initialize the profession cache service. Args: persistence: Persistence layer…** (1 connections) — `server/caching/cache_service.py`
- **Invalidate all profession caches.** (1 connections) — `server/caching/cache_service.py`

## Relationships

- [LucidityTierCache](LucidityTierCache.md) (7 shared connections)
- [ConnectionManager Refactoring Summary](ConnectionManager_Refactoring_Summary.md) (4 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (3 shared connections)
- [Quieter Skill](Quieter_Skill.md) (2 shared connections)
- [.get_upcoming_holidays](get_upcoming_holidays.md) (1 shared connections)
- [Persistence Layer Extraction - COMPLETE ✅](Persistence_Layer_Extraction_-_COMPLETE_✅.md) (1 shared connections)
- [fixture](fixture.md) (1 shared connections)
- [Skill: Create a New Worktree for a Task](Skill-_Create_a_New_Worktree_for_a_Task.md) (1 shared connections)

## Source Files

- `server/caching/cache_service.py`
- `server/tests/unit/caching/test_cache_service.py`

## Audit Trail

- EXTRACTED: 37 (92%)
- INFERRED: 3 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*