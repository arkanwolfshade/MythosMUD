# Real-Time Architecture Docs

> 17 nodes · cohesion 0.15

## Key Concepts

- **RoomCacheService** (17 connections) — `server/caching/cache_service.py`
- **bench_cache.py** (6 connections) — `scripts/bench_cache.py`
- **_FakePersistence** (6 connections) — `scripts/bench_cache.py`
- **bench_room_cache()** (5 connections) — `scripts/bench_cache.py`
- **.get_room()** (3 connections) — `server/caching/cache_service.py`
- **.async_get_room()** (2 connections) — `scripts/bench_cache.py`
- **main()** (2 connections) — `scripts/bench_cache.py`
- **Any** (2 connections)
- **.invalidate_room()** (2 connections) — `server/caching/cache_service.py`
- **.preload_rooms()** (2 connections) — `server/caching/cache_service.py`
- **.__init__()** (1 connections) — `scripts/bench_cache.py`
- **Lightweight cache benchmark for CI artifacts.  Measures miss vs. hit timings for** (1 connections) — `scripts/bench_cache.py`
- **Fake persistence layer providing async_get_room with simulated latency.** (1 connections) — `scripts/bench_cache.py`
- **Service for caching room data.** (1 connections) — `server/caching/cache_service.py`
- **Get room data with caching.          Args:             room_id: The room ID** (1 connections) — `server/caching/cache_service.py`
- **Invalidate cached room data.          Args:             room_id: The room ID to** (1 connections) — `server/caching/cache_service.py`
- **Preload multiple rooms into cache.          Args:             room_ids: List of** (1 connections) — `server/caching/cache_service.py`

## Relationships

- [Cache and NPC Cache](Cache_and_NPC_Cache.md) (5 shared connections)
- [Weapon Resolution Helpers](Weapon_Resolution_Helpers.md) (3 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (2 shared connections)
- [LRU Cache Manager](LRU_Cache_Manager.md) (1 shared connections)
- [ASCII Map API](ASCII_Map_API.md) (1 shared connections)

## Source Files

- `scripts/bench_cache.py`
- `server/caching/cache_service.py`

## Audit Trail

- EXTRACTED: 48 (89%)
- INFERRED: 6 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*