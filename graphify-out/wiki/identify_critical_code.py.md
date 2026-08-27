# identify_critical_code.py

> 23 nodes

## Key Concepts

- **ProfessionCacheService** (17 connections) — `server/caching/cache_service.py`
- **TestProfessionCacheService** (7 connections) — `server/tests/unit/caching/test_cache_service.py`
- **bench_cache_professions.py** (7 connections) — `scripts/bench_cache_professions.py`
- **bench_profession_cache()** (5 connections) — `scripts/bench_cache_professions.py`
- **fixture** (5 connections)
- **_FakePersistence** (4 connections) — `scripts/bench_cache_professions.py`
- **_Profession** (4 connections) — `server/tests/unit/caching/test_cache_service.py`
- **_get_empty_dict()** (4 connections) — `scripts/bench_cache_professions.py`
- **.get_all_professions()** (3 connections) — `scripts/bench_cache_professions.py`
- **.persistence()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.persistence()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_get_profession_by_id_hit_and_miss()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **Any** (3 connections)
- **main()** (2 connections) — `scripts/bench_cache_professions.py`
- **.invalidate_professions()** (2 connections) — `server/caching/cache_service.py`
- **.test_get_all_professions_hit_and_miss()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_get_profession_by_id_not_found()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_invalidate_professions()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.__init__()** (1 connections) — `scripts/bench_cache_professions.py`
- **Professions cache micro-benchmark for CI artifacts. Measures miss vs. hit…** (1 connections) — `scripts/bench_cache_professions.py`
- **Helper function to return empty dict for mock methods.** (1 connections) — `scripts/bench_cache_professions.py`
- **Service for caching profession data.** (1 connections) — `server/caching/cache_service.py`
- **Invalidate all profession caches.** (1 connections) — `server/caching/cache_service.py`

## Relationships

- [populate_npc_sample_data.py](populate_npc_sample_data.py.md) (4 shared connections)
- [required](required.md) (4 shared connections)
- [test_event_publisher_helpers.py](test_event_publisher_helpers.py.md) (4 shared connections)
- [main](main.md) (1 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (1 shared connections)
- [.create_get_command](create_get_command.md) (1 shared connections)

## Source Files

- `scripts/bench_cache_professions.py`
- `server/caching/cache_service.py`
- `server/tests/unit/caching/test_cache_service.py`

## Audit Trail

- EXTRACTED: 46 (94%)
- INFERRED: 3 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*