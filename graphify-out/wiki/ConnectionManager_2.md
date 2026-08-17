# ConnectionManager

> 1105 nodes

## Key Concepts

- **ConnectionManager** (167 connections) — `server/realtime/connection_manager.py`
- **connection_manager.py** (126 connections) — `server/realtime/connection_manager.py`
- **event_types.py** (87 connections) — `server/events/event_types.py`
- **BaseEvent** (81 connections) — `server/events/event_types.py`
- **PlayerEnteredRoom** (76 connections) — `server/events/event_types.py`
- **NATSError** (70 connections) — `server/services/nats_exceptions.py`
- **test_population_control.py** (66 connections) — `server/tests/unit/npc/test_population_control.py`
- **websocket_handler.py** (65 connections) — `server/realtime/websocket_handler.py`
- **asyncio.md** (55 connections) — `.claude/rules/asyncio.md`
- **PlayerLeftRoom** (49 connections) — `server/events/event_types.py`
- **NPCEnteredRoom** (46 connections) — `server/events/event_types.py`
- **websocket_initial_state.py** (46 connections) — `server/realtime/websocket_initial_state.py`
- **NPCLeftRoom** (43 connections) — `server/events/event_types.py`
- **population_control.py** (42 connections) — `server/npc/population_control.py`
- **player_event_handlers.py** (42 connections) — `server/realtime/player_event_handlers.py`
- **test_event_handler.py** (42 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_room_sync_service.py** (41 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **PlayerDPUpdated** (38 connections) — `server/events/event_types.py`
- **spawning_service.py** (38 connections) — `server/npc/spawning_service.py`
- **DeadLetterQueue** (37 connections) — `server/realtime/dead_letter_queue.py`
- **nats_exceptions.py** (37 connections) — `server/services/nats_exceptions.py`
- **RealTimeEventHandler** (36 connections) — `server/realtime/event_handler.py`
- **event_handler.py** (36 connections) — `server/realtime/event_handler.py`
- **nats_message_handler.py** (35 connections) — `server/realtime/nats_message_handler.py`
- **NATSPublishError** (34 connections) — `server/services/nats_exceptions.py`
- *... and 1080 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (133 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (102 shared connections)
- [build_event](build_event.md) (59 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (58 shared connections)
- [npc_base.py](npc_base.py.md) (44 shared connections)
- [UUID](UUID.md) (42 shared connections)
- [EventBus](EventBus.md) (41 shared connections)
- [PlayerRoomEventHandler](PlayerRoomEventHandler.md) (37 shared connections)
- [connection_manager_methods.py](connection_manager_methods.py.md) (29 shared connections)
- [test_websocket_helpers.py](test_websocket_helpers.py.md) (26 shared connections)
- [event_serialization.py](event_serialization.py.md) (25 shared connections)
- [test_websocket_handler_coverage_gaps.py](test_websocket_handler_coverage_gaps.py.md) (21 shared connections)

## Source Files

- `.claude/rules/asyncio.md`
- `server/app/tracked_task_manager.py`
- `server/container/bundles/realtime.py`
- `server/events/__init__.py`
- `server/events/distributed_event_bus.py`
- `server/events/event_bus.py`
- `server/events/event_types.py`
- `server/events/nats_event_bridge.py`
- `server/game/follow_service.py`
- `server/game/party_service.py`
- `server/npc/movement_integration.py`
- `server/npc/population_control.py`
- `server/npc/population_stats.py`
- `server/npc/spawning_service.py`
- `server/realtime/__init__.py`
- `server/realtime/connection_manager.py`
- `server/realtime/connection_manager_api.py`
- `server/realtime/connection_manager_lazy.py`
- `server/realtime/connection_manager_utils.py`
- `server/realtime/connection_websocket_close.py`

## Audit Trail

- EXTRACTED: 2964 (88%)
- INFERRED: 401 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*