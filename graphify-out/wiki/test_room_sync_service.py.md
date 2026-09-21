# test_room_sync_service.py

> 96 nodes

## Key Concepts

- **test_room_sync_service.py** (40 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **RoomSyncService** (22 connections) — `server/services/room_sync_service.py`
- **asyncio** (14 connections)
- **.__init__()** (9 connections) — `server/realtime/event_handler.py`
- **get_room_sync_service()** (8 connections) — `server/services/room_sync_service.py`
- **Any** (7 connections)
- **._handle_stale_room_data()** (6 connections) — `server/services/room_sync_service.py`
- **.__init__()** (6 connections) — `server/services/room_sync_service.py`
- **room_sync_service()** (5 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **._fetch_fresh_room_data()** (4 connections) — `server/services/room_sync_service.py`
- **._process_room_update_with_validation()** (4 connections) — `server/services/room_sync_service.py`
- **room_sync_service_with_room_service()** (4 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **sample_event()** (4 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_fetch_fresh_room_data_handles_error()** (4 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_process_room_update_with_validation_handles_error()** (4 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **fixture** (4 connections)
- **.get_room_data_cache_stats()** (3 connections) — `server/services/room_sync_service.py`
- **._invalidate_stale_cache()** (3 connections) — `server/services/room_sync_service.py`
- **.process_event_with_ordering()** (3 connections) — `server/services/room_sync_service.py`
- **._process_room_transition()** (3 connections) — `server/services/room_sync_service.py`
- **.set_room_service()** (3 connections) — `server/services/room_sync_service.py`
- **mock_room_service()** (3 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_fetch_fresh_room_data_no_room_service()** (3 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_fetch_fresh_room_data_not_found()** (3 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **test_fetch_fresh_room_data_success()** (3 connections) — `server/tests/unit/services/test_room_sync_service.py`
- *... and 71 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (8 shared connections)
- [EventBus](EventBus.md) (3 shared connections)
- [AttributeError](AttributeError.md) (3 shared connections)
- [MessageBuilder](MessageBuilder.md) (2 shared connections)
- [RoomDataCache](RoomDataCache.md) (2 shared connections)
- [RoomDataValidator](RoomDataValidator.md) (2 shared connections)
- [TestRoomDataFixer](TestRoomDataFixer.md) (2 shared connections)
- [RealTimeEventHandler](RealTimeEventHandler.md) (2 shared connections)
- [PlayerEventHandlerUtils](PlayerEventHandlerUtils.md) (1 shared connections)
- [TaskRegistry](TaskRegistry.md) (1 shared connections)
- [test_chat_logger.py](test_chat_logger.py.md) (1 shared connections)

## Source Files

- `server/realtime/event_handler.py`
- `server/services/room_sync_service.py`
- `server/tests/unit/services/test_room_sync_service.py`

## Audit Trail

- EXTRACTED: 142 (93%)
- INFERRED: 10 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*