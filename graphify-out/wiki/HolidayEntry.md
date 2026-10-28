# HolidayEntry

> 101 nodes · cohesion 0.03

## Key Concepts

- **test_room_sync_service.py** (40 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **RoomSyncService** (22 connections) — `server/services/room_sync_service.py`
- **asyncio** (14 connections)
- **.__init__()** (9 connections) — `server/realtime/event_handler.py`
- **get_room_sync_service()** (8 connections) — `server/services/room_sync_service.py`
- **chat_logger()** (8 connections) — `server/tests/unit/services/test_chat_logger.py`
- **Any** (7 connections)
- **._handle_stale_room_data()** (6 connections) — `server/services/room_sync_service.py`
- **.__init__()** (6 connections) — `server/services/room_sync_service.py`
- **room_sync_service()** (5 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **.__init__()** (4 connections) — `server/services/rate_limiter.py`
- **._fetch_fresh_room_data()** (4 connections) — `server/services/room_sync_service.py`
- **._process_room_update_with_validation()** (4 connections) — `server/services/room_sync_service.py`
- **fixture** (4 connections)
- **room_sync_service_with_room_service()** (4 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **sample_event()** (4 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_fetch_fresh_room_data_handles_error()** (4 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_process_room_update_with_validation_handles_error()** (4 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **.get_room_data_cache_stats()** (3 connections) — `server/services/room_sync_service.py`
- **._invalidate_stale_cache()** (3 connections) — `server/services/room_sync_service.py`
- **.process_event_with_ordering()** (3 connections) — `server/services/room_sync_service.py`
- **._process_room_transition()** (3 connections) — `server/services/room_sync_service.py`
- **.set_room_service()** (3 connections) — `server/services/room_sync_service.py`
- **mock_room_service()** (3 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_fetch_fresh_room_data_no_room_service()** (3 connections) — `server/tests/unit/services/test_room_sync_service.py`
- *... and 76 more nodes in this community*

## Relationships

- [Room](Room.md) (6 shared connections)
- [get_username_from_user](get_username_from_user.md) (3 shared connections)
- [security.ts](security.ts.md) (3 shared connections)
- [PlayerRespawnWrapper](PlayerRespawnWrapper.md) (2 shared connections)
- [ZoneConfiguration](ZoneConfiguration.md) (2 shared connections)
- [test_room_renderer.py](test_room_renderer.py.md) (2 shared connections)
- [WearableContainerService](WearableContainerService.md) (2 shared connections)
- [test_npc_threading_messages.py](test_npc_threading_messages.py.md) (2 shared connections)
- [test_utility_threat.py](test_utility_threat.py.md) (2 shared connections)
- [look_container.py](look_container.py.md) (1 shared connections)
- [test_player_combat_service.py](test_player_combat_service.py.md) (1 shared connections)
- [_StubPlayerRepo](_StubPlayerRepo.md) (1 shared connections)

## Source Files

- `server/realtime/event_handler.py`
- `server/services/rate_limiter.py`
- `server/services/room_sync_service.py`
- `server/tests/unit/services/test_chat_logger.py`
- `server/tests/unit/services/test_room_sync_service.py`

## Audit Trail

- EXTRACTED: 148 (91%)
- INFERRED: 14 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*