# RealTimeEventHandler

> 424 nodes

## Key Concepts

- **RealTimeEventHandler** (44 connections) — `server/realtime/event_handler.py`
- **PlayerEventHandlerUtils** (42 connections) — `server/realtime/player_event_handlers_utils.py`
- **test_event_handler.py** (41 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **PlayerLeftRoom** (40 connections) — `server/events/event_types.py`
- **PlayerDPUpdated** (37 connections) — `server/events/event_types.py`
- **event_handler.py** (35 connections) — `server/realtime/event_handler.py`
- **PlayerRespawnEventHandler** (33 connections) — `server/realtime/player_event_handlers_respawn.py`
- **player_event_handlers_respawn.py** (33 connections) — `server/realtime/player_event_handlers_respawn.py`
- **test_player_event_handlers_state.py** (33 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **PlayerXPAwardEvent** (32 connections) — `server/services/player_combat_service.py`
- **PlayerRoomEventHandler** (30 connections) — `server/realtime/player_event_handlers_room.py`
- **NPCEventHandler** (26 connections) — `server/realtime/npc_event_handlers.py`
- **PlayerEventHandler** (26 connections) — `server/realtime/player_event_handlers.py`
- **player_event_handlers.py** (26 connections) — `server/realtime/player_event_handlers.py`
- **player_event_handlers_state.py** (23 connections) — `server/realtime/player_event_handlers_state.py`
- **MessageBuilder** (22 connections) — `server/realtime/message_builders.py`
- **RoomOccupantManager** (22 connections) — `server/realtime/room_occupant_manager.py`
- **realtime/conftest.py** (22 connections) — `server/tests/unit/realtime/conftest.py`
- **room_occupant_manager.py** (19 connections) — `server/realtime/room_occupant_manager.py`
- **asyncio** (19 connections)
- **player_event_handlers_room.py** (17 connections) — `server/realtime/player_event_handlers_room.py`
- **PlayerRespawnedEvent** (16 connections) — `server/events/event_types.py`
- **npc_event_handlers.py** (16 connections) — `server/realtime/npc_event_handlers.py`
- **player_event_handlers_utils.py** (16 connections) — `server/realtime/player_event_handlers_utils.py`
- **fixture** (15 connections)
- *... and 399 more nodes in this community*

## Relationships

- [event_types.py](event_types.py.md) (32 shared connections)
- [get_logger](get_logger.md) (25 shared connections)
- [PlayerNameExtractor](PlayerNameExtractor.md) (16 shared connections)
- [websocket_initial_state.py](websocket_initial_state.py.md) (15 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (15 shared connections)
- [.handle_npc_entered](handle_npc_entered.md) (15 shared connections)
- [EventBus](EventBus.md) (13 shared connections)
- [Any](Any.md) (13 shared connections)
- [build_event](build_event.md) (13 shared connections)
- [test_player_event_handlers.py](test_player_event_handlers.py.md) (12 shared connections)
- [ConnectionManager](ConnectionManager.md) (12 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (12 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/npc/spawning_service.py`
- `server/realtime/event_handler.py`
- `server/realtime/message_builders.py`
- `server/realtime/npc_event_handlers.py`
- `server/realtime/player_event_handlers.py`
- `server/realtime/player_event_handlers_respawn.py`
- `server/realtime/player_event_handlers_room.py`
- `server/realtime/player_event_handlers_state.py`
- `server/realtime/player_event_handlers_utils.py`
- `server/realtime/player_name_utils.py`
- `server/realtime/room_occupant_manager.py`
- `server/services/player_combat_service.py`
- `server/services/room_sync_service.py`
- `server/tests/unit/npc/test_population_control.py`
- `server/tests/unit/realtime/conftest.py`
- `server/tests/unit/realtime/test_event_handler.py`
- `server/tests/unit/realtime/test_player_event_handlers_state.py`
- `server/tests/unit/realtime/test_player_event_handlers_utils_grace_period.py`
- `server/tests/unit/services/test_player_combat_service.py`

## Audit Trail

- EXTRACTED: 971 (94%)
- INFERRED: 57 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*