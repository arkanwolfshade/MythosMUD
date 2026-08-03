# services lucidity repository

> 31 nodes

## Key Concepts

- **RoomCacheService** (17 connections) — `server/caching/cache_service.py`
- **ProfessionCacheService** (15 connections) — `server/caching/cache_service.py`
- **bench_cache_professions.py** (7 connections) — `scripts/bench_cache_professions.py`
- **.__init__()** (7 connections) — `server/caching/cache_service.py`
- **bench_cache.py** (6 connections) — `scripts/bench_cache.py`
- **_FakePersistence** (6 connections) — `scripts/bench_cache.py`
- **bench_profession_cache()** (6 connections) — `scripts/bench_cache_professions.py`
- **bench_room_cache()** (5 connections) — `scripts/bench_cache.py`
- **_FakePersistence** (5 connections) — `scripts/bench_cache_professions.py`
- **.get_all_professions()** (5 connections) — `scripts/bench_cache_professions.py`
- **_get_empty_dict()** (4 connections) — `scripts/bench_cache_professions.py`
- **Any** (3 connections)
- **.async_get_room()** (2 connections) — `scripts/bench_cache.py`
- **Any** (2 connections)
- **main()** (2 connections) — `scripts/bench_cache.py`
- **main()** (2 connections) — `scripts/bench_cache_professions.py`
- **.invalidate_room()** (2 connections) — `server/caching/cache_service.py`
- **.preload_rooms()** (2 connections) — `server/caching/cache_service.py`
- **.invalidate_professions()** (2 connections) — `server/caching/cache_service.py`
- **.__init__()** (1 connections) — `scripts/bench_cache.py`
- **Lightweight cache benchmark for CI artifacts.  Measures miss vs. hit timings for** (1 connections) — `scripts/bench_cache.py`
- **Fake persistence layer providing async_get_room with simulated latency.** (1 connections) — `scripts/bench_cache.py`
- **.__init__()** (1 connections) — `scripts/bench_cache_professions.py`
- **Professions cache micro-benchmark for CI artifacts. Measures miss vs. hit timing** (1 connections) — `scripts/bench_cache_professions.py`
- **Helper function to return empty dict for mock methods.** (1 connections) — `scripts/bench_cache_professions.py`
- *... and 6 more nodes in this community*

## Relationships

- [cache caching service](cache_caching_service.md) (9 shared connections)
- [Error Conversion](Error_Conversion.md) (6 shared connections)
- [command inventory factories](command_inventory_factories.md) (4 shared connections)
- [time service rationale](time_service_rationale.md) (2 shared connections)
- [combat messaging service](combat_messaging_service.md) (2 shared connections)
- [commands communication flows](commands_communication_flows.md) (1 shared connections)
- [room game service](room_game_service.md) (1 shared connections)
- [command combat models](command_combat_models.md) (1 shared connections)

## Source Files

- `scripts/bench_cache.py`
- `scripts/bench_cache_professions.py`
- `server/caching/cache_service.py`

## Audit Trail

- EXTRACTED: 99 (88%)
- INFERRED: 13 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*