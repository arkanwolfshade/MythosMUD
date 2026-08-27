# .create_get_command

> 24 nodes

## Key Concepts

- **RoomCacheService** (25 connections) — `server/caching/cache_service.py`
- **get_cache_manager()** (21 connections) — `server/caching/lru_cache.py`
- **TestRoomCacheService** (14 connections) — `server/tests/unit/caching/test_cache_service.py`
- **_RoomObj** (5 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.persistence()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_get_room_cache_hit()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_get_room_miss_returns_none()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_get_room_miss_with_to_dict()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_get_room_sync_miss_with_to_dict()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_init_concurrent_create_uses_existing()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_init_lazy_creates_rooms_cache()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_init_uses_existing_rooms_cache()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_preload_rooms()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.invalidate_room()** (2 connections) — `server/caching/cache_service.py`
- **.preload_rooms()** (2 connections) — `server/caching/cache_service.py`
- **.to_dict()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_get_room_sync_cache_hit()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_get_room_sync_miss_caches_dict()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_invalidate_room()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **Any** (1 connections)
- **Service for caching room data.** (1 connections) — `server/caching/cache_service.py`
- **Invalidate cached room data. Args: room_id: The room ID to invalidate** (1 connections) — `server/caching/cache_service.py`
- **Preload multiple rooms into cache. Args: room_ids: List of room IDs to preload** (1 connections) — `server/caching/cache_service.py`
- **Get the global cache manager instance. Returns: The global cache manager…** (1 connections) — `server/caching/lru_cache.py`

## Relationships

- [populate_npc_sample_data.py](populate_npc_sample_data.py.md) (8 shared connections)
- [test_event_publisher_helpers.py](test_event_publisher_helpers.py.md) (7 shared connections)
- [required](required.md) (6 shared connections)
- [MythosMUD Logging Standards](MythosMUD_Logging_Standards.md) (2 shared connections)
- [AGENTS.md](AGENTS.md.md) (2 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (2 shared connections)
- [test_game_tick_processing_async.py](test_game_tick_processing_async.py.md) (1 shared connections)
- [debrief_command.py](debrief_command.py.md) (1 shared connections)
- [analyze_coverage_gaps.py](analyze_coverage_gaps.py.md) (1 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (1 shared connections)
- [inventory_equip_command.py](inventory_equip_command.py.md) (1 shared connections)
- [identify_critical_code.py](identify_critical_code.py.md) (1 shared connections)

## Source Files

- `server/caching/cache_service.py`
- `server/caching/lru_cache.py`
- `server/tests/unit/caching/test_cache_service.py`

## Audit Trail

- EXTRACTED: 69 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*