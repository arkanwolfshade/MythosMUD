# services lucidity repository

> 24 nodes

## Key Concepts

- **ProfessionCacheService** (29 connections) — `server/caching/cache_service.py`
- **TestProfessionCacheService** (10 connections) — `server/tests/unit/caching/test_cache_service.py`
- **_Profession** (8 connections) — `server/tests/unit/caching/test_cache_service.py`
- **bench_cache_professions.py** (7 connections) — `scripts/bench_cache_professions.py`
- **bench_profession_cache()** (6 connections) — `scripts/bench_cache_professions.py`
- **._initialize_caching_services()** (6 connections) — `server/container/bundles/game.py`
- **_FakePersistence** (5 connections) — `scripts/bench_cache_professions.py`
- **_get_empty_dict()** (4 connections) — `scripts/bench_cache_professions.py`
- **.get_all_professions()** (4 connections) — `scripts/bench_cache_professions.py`
- **Any** (3 connections)
- **.test_get_profession_by_id_hit_and_miss()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **main()** (2 connections) — `scripts/bench_cache_professions.py`
- **.invalidate_professions()** (2 connections) — `server/caching/cache_service.py`
- **.persistence()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_get_all_professions_hit_and_miss()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_get_profession_by_id_not_found()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_invalidate_professions()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.persistence()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.__init__()** (1 connections) — `scripts/bench_cache_professions.py`
- **Professions cache micro-benchmark for CI artifacts. Measures miss vs. hit timing** (1 connections) — `scripts/bench_cache_professions.py`
- **Helper function to return empty dict for mock methods.** (1 connections) — `scripts/bench_cache_professions.py`
- **Service for caching profession data.** (1 connections) — `server/caching/cache_service.py`
- **Invalidate all profession caches.** (1 connections) — `server/caching/cache_service.py`
- **Create room and profession cache services; set to None on RuntimeError.** (1 connections) — `server/container/bundles/game.py`

## Relationships

- [config rationale config()](config_rationale_config%28%29.md) (5 shared connections)
- [uuid services npc](uuid_services_npc.md) (5 shared connections)
- [startup npc service](startup_npc_service.md) (5 shared connections)
- [commands skills rationale](commands_skills_rationale.md) (4 shared connections)
- [Error Conversion](Error_Conversion.md) (3 shared connections)
- [cache caching service](cache_caching_service.md) (3 shared connections)
- [room realtime occupant](room_realtime_occupant.md) (2 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (2 shared connections)
- [caching lru cache](caching_lru_cache.md) (1 shared connections)
- [game magic regeneration](game_magic_regeneration.md) (1 shared connections)

## Source Files

- `scripts/bench_cache_professions.py`
- `server/caching/cache_service.py`
- `server/container/bundles/game.py`
- `server/tests/unit/caching/test_cache_service.py`

## Audit Trail

- EXTRACTED: 82 (78%)
- INFERRED: 23 (22%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*