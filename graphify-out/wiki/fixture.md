# fixture

> 22 nodes · cohesion 0.15

## Key Concepts

- **RoomCacheService** (29 connections) — `server/caching/cache_service.py`
- **TestRoomCacheService** (14 connections) — `server/tests/unit/caching/test_cache_service.py`
- **_RoomObj** (5 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_init_concurrent_create_uses_existing()** (4 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.persistence()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_get_room_cache_hit()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_get_room_miss_returns_none()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_get_room_miss_with_to_dict()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_get_room_sync_miss_with_to_dict()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_init_lazy_creates_rooms_cache()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_init_uses_existing_rooms_cache()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_preload_rooms()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.invalidate_room()** (2 connections) — `server/caching/cache_service.py`
- **.preload_rooms()** (2 connections) — `server/caching/cache_service.py`
- **.to_dict()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_get_room_sync_cache_hit()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_get_room_sync_miss_caches_dict()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_invalidate_room()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **Service for caching room data.** (1 connections) — `server/caching/cache_service.py`
- **Invalidate cached room data. Args: room_id: The room ID to invalidate** (1 connections) — `server/caching/cache_service.py`
- **Preload multiple rooms into cache. Args: room_ids: List of room IDs to preload** (1 connections) — `server/caching/cache_service.py`
- **Any** (1 connections)

## Relationships

- [LucidityTierCache](LucidityTierCache.md) (8 shared connections)
- [ConnectionManager Refactoring Summary](ConnectionManager_Refactoring_Summary.md) (4 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (3 shared connections)
- [Persistence Layer Extraction - COMPLETE ✅](Persistence_Layer_Extraction_-_COMPLETE_✅.md) (3 shared connections)
- [enum](enum.md) (2 shared connections)
- [useMythosAppActions.ts](useMythosAppActions.ts.md) (1 shared connections)
- [.get_upcoming_holidays](get_upcoming_holidays.md) (1 shared connections)
- [Test Coverage Summary: Disconnect Grace Period & Rest Command](Test_Coverage_Summary-_Disconnect_Grace_Period_&_Rest_Command.md) (1 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (1 shared connections)

## Source Files

- `server/caching/cache_service.py`
- `server/tests/unit/caching/test_cache_service.py`

## Audit Trail

- EXTRACTED: 54 (93%)
- INFERRED: 4 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*