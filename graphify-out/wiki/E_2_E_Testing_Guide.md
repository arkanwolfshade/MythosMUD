# E 2 E Testing Guide

> 15 nodes

## Key Concepts

- **RoomCacheService** (17 connections) — `server/caching/cache_service.py`
- **bench_cache.py** (6 connections) — `scripts/bench_cache.py`
- **_FakePersistence** (6 connections) — `scripts/bench_cache.py`
- **bench_room_cache()** (5 connections) — `scripts/bench_cache.py`
- **.async_get_room()** (2 connections) — `scripts/bench_cache.py`
- **Any** (2 connections)
- **main()** (2 connections) — `scripts/bench_cache.py`
- **.invalidate_room()** (2 connections) — `server/caching/cache_service.py`
- **.preload_rooms()** (2 connections) — `server/caching/cache_service.py`
- **.__init__()** (1 connections) — `scripts/bench_cache.py`
- **Lightweight cache benchmark for CI artifacts.  Measures miss vs. hit timings for** (1 connections) — `scripts/bench_cache.py`
- **Fake persistence layer providing async_get_room with simulated latency.** (1 connections) — `scripts/bench_cache.py`
- **Service for caching room data.** (1 connections) — `server/caching/cache_service.py`
- **Invalidate cached room data.          Args:             room_id: The room ID to** (1 connections) — `server/caching/cache_service.py`
- **Preload multiple rooms into cache.          Args:             room_ids: List of** (1 connections) — `server/caching/cache_service.py`

## Relationships

- [Alias Command Models](Alias_Command_Models.md) (4 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (2 shared connections)
- [Command Factory Tests](Command_Factory_Tests.md) (2 shared connections)
- [Realtime Service Bundle](Realtime_Service_Bundle.md) (1 shared connections)
- [Grace Period Blocking Tests](Grace_Period_Blocking_Tests.md) (1 shared connections)
- [WebSocket Code Review](WebSocket_Code_Review.md) (1 shared connections)
- [Mythos Time HUD](Mythos_Time_HUD.md) (1 shared connections)

## Source Files

- `scripts/bench_cache.py`
- `server/caching/cache_service.py`

## Audit Trail

- EXTRACTED: 44 (88%)
- INFERRED: 6 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*