# NPCEnteredRoom

> 277 nodes

## Key Concepts

- **NPCEnteredRoom** (46 connections) — `server/events/event_types.py`
- **test_npc_event_handlers.py** (46 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **NPCLeftRoom** (43 connections) — `server/events/event_types.py`
- **test_event_handler.py** (42 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **RealTimeEventHandler** (36 connections) — `server/realtime/event_handler.py`
- **event_handler.py** (36 connections) — `server/realtime/event_handler.py`
- **test_lifecycle_manager.py** (27 connections) — `server/tests/unit/npc/test_lifecycle_manager.py`
- **NPCEventHandler** (26 connections) — `server/realtime/npc_event_handlers.py`
- **PlayerRespawnedEvent** (21 connections) — `server/events/event_types.py`
- **_make_manager()** (18 connections) — `server/tests/unit/npc/test_lifecycle_manager.py`
- **npc_event_handlers.py** (17 connections) — `server/realtime/npc_event_handlers.py`
- **PlayerDeliriumRespawnedEvent** (16 connections) — `server/events/event_types.py`
- **asyncio** (16 connections)
- **asyncio** (15 connections)
- **test_npc_event_handlers_helpers.py** (15 connections) — `server/tests/unit/realtime/test_npc_event_handlers_helpers.py`
- **.__init__()** (9 connections) — `server/realtime/event_handler.py`
- **._initialize_modules()** (8 connections) — `server/realtime/event_handler.py`
- **.handle_npc_entered()** (8 connections) — `server/realtime/npc_event_handlers.py`
- **._send_npc_left_message()** (8 connections) — `server/realtime/npc_event_handlers.py`
- **get_room_sync_service()** (8 connections) — `server/services/room_sync_service.py`
- **._get_npc_spawn_message()** (7 connections) — `server/realtime/npc_event_handlers.py`
- **event_handler()** (7 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **.handle_npc_left()** (6 connections) — `server/realtime/npc_event_handlers.py`
- **._send_room_message()** (6 connections) — `server/realtime/npc_event_handlers.py`
- **._get_npc_instance()** (5 connections) — `server/realtime/npc_event_handlers.py`
- *... and 252 more nodes in this community*

## Relationships

- [EventBus](EventBus.md) (27 shared connections)
- [player_event_handlers.py](player_event_handlers.py.md) (26 shared connections)
- [lifecycle_manager.py](lifecycle_manager.py.md) (12 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (12 shared connections)
- [NPCSpawningService](NPCSpawningService.md) (10 shared connections)
- [pytest.md](pytest.md.md) (10 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (9 shared connections)
- [get_logger](get_logger.md) (8 shared connections)
- [NATSError](NATSError.md) (8 shared connections)
- [test_follow_service.py](test_follow_service.py.md) (6 shared connections)
- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) (6 shared connections)
- [PlayerRespawnEventHandler](PlayerRespawnEventHandler.md) (6 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/npc/movement_integration.py`
- `server/realtime/event_handler.py`
- `server/realtime/npc_event_handlers.py`
- `server/realtime/player_event_handlers.py`
- `server/services/room_sync_service.py`
- `server/tests/unit/npc/test_lifecycle_manager.py`
- `server/tests/unit/realtime/test_event_handler.py`
- `server/tests/unit/realtime/test_npc_event_handlers.py`
- `server/tests/unit/realtime/test_npc_event_handlers_helpers.py`

## Audit Trail

- EXTRACTED: 540 (91%)
- INFERRED: 53 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*