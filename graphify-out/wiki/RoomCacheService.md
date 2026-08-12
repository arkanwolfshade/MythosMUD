# RoomCacheService

> 15 nodes

## Key Concepts

- **RoomCacheService** (17 connections) — `server/caching/cache_service.py`
- **_FakePersistence** (6 connections) — `scripts/bench_cache.py`
- **bench_cache.py** (6 connections) — `scripts/bench_cache.py`
- **bench_room_cache()** (5 connections) — `scripts/bench_cache.py`
- **.async_get_room()** (2 connections) — `scripts/bench_cache.py`
- **main()** (2 connections) — `scripts/bench_cache.py`
- **.invalidate_room()** (2 connections) — `server/caching/cache_service.py`
- **.preload_rooms()** (2 connections) — `server/caching/cache_service.py`
- **Any** (2 connections)
- **.__init__()** (1 connections) — `scripts/bench_cache.py`
- **Lightweight cache benchmark for CI artifacts. Measures miss vs. hit timings for…** (1 connections) — `scripts/bench_cache.py`
- **Fake persistence layer providing async_get_room with simulated latency.** (1 connections) — `scripts/bench_cache.py`
- **Service for caching room data.** (1 connections) — `server/caching/cache_service.py`
- **Invalidate cached room data. Args: room_id: The room ID to invalidate** (1 connections) — `server/caching/cache_service.py`
- **Preload multiple rooms into cache. Args: room_ids: List of room IDs to preload** (1 connections) — `server/caching/cache_service.py`

## Relationships

- [LRUCache](LRUCache.md) (4 shared connections)
- [NPCCacheService](NPCCacheService.md) (3 shared connections)
- [GameBundle](GameBundle.md) (2 shared connections)
- [bundles/game.py](bundles-game.py.md) (1 shared connections)
- [RoomService](RoomService.md) (1 shared connections)
- [time.py](time.py.md) (1 shared connections)

## Source Files

- `scripts/bench_cache.py`
- `server/caching/cache_service.py`

## Audit Trail

- EXTRACTED: 27 (87%)
- INFERRED: 4 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*