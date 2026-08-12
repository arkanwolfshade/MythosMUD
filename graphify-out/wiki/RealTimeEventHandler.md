# RealTimeEventHandler

> 314 nodes

## Key Concepts

- **RealTimeEventHandler** (44 connections) — `server/realtime/event_handler.py`
- **PlayerRespawnEventHandler** (33 connections) — `server/realtime/player_event_handlers_respawn.py`
- **PlayerEventHandler** (26 connections) — `server/realtime/player_event_handlers.py`
- **player_event_handlers.py** (26 connections) — `server/realtime/player_event_handlers.py`
- **NPCEventHandler** (25 connections) — `server/realtime/npc_event_handlers.py`
- **MessageBuilder** (22 connections) — `server/realtime/message_builders.py`
- **RoomOccupantManager** (22 connections) — `server/realtime/room_occupant_manager.py`
- **realtime/conftest.py** (22 connections) — `server/tests/unit/realtime/conftest.py`
- **RoomIDUtils** (20 connections) — `server/realtime/room_id_utils.py`
- **room_occupant_manager.py** (19 connections) — `server/realtime/room_occupant_manager.py`
- **NPCOccupantProcessor** (18 connections) — `server/realtime/npc_occupant_processor.py`
- **player_event_handlers_room.py** (17 connections) — `server/realtime/player_event_handlers_room.py`
- **player_event_handlers_utils.py** (16 connections) — `server/realtime/player_event_handlers_utils.py`
- **test_room_occupant_manager.py** (16 connections) — `server/tests/unit/realtime/test_room_occupant_manager.py`
- **fixture** (15 connections)
- **RespawnPlayerEventPayload** (13 connections) — `server/realtime/player_event_handlers_respawn.py`
- **player_name_utils.py** (13 connections) — `server/realtime/player_name_utils.py`
- **Any** (11 connections)
- **.__init__()** (9 connections) — `server/realtime/event_handler.py`
- **._extract_occupant_names()** (9 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.__init__()** (9 connections) — `server/realtime/room_occupant_manager.py`
- **Any** (9 connections)
- **asyncio** (9 connections)
- **._initialize_modules()** (8 connections) — `server/realtime/event_handler.py`
- **._get_next_sequence()** (8 connections) — `server/realtime/message_builders.py`
- *... and 289 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (84 shared connections)
- [PlayerNameExtractor](PlayerNameExtractor.md) (12 shared connections)
- [PlayerEventHandlerUtils](PlayerEventHandlerUtils.md) (12 shared connections)
- [websocket_initial_state.py](websocket_initial_state.py.md) (11 shared connections)
- [test_room_id_utils.py](test_room_id_utils.py.md) (11 shared connections)
- [PlayerRoomEventHandler](PlayerRoomEventHandler.md) (10 shared connections)
- [player_combat_service.py](player_combat_service.py.md) (7 shared connections)
- [build_event](build_event.md) (6 shared connections)
- [PlayerStateEventHandler](PlayerStateEventHandler.md) (5 shared connections)
- [ConnectionManager](ConnectionManager.md) (4 shared connections)
- [test_player_event_handlers_respawn.py](test_player_event_handlers_respawn.py.md) (4 shared connections)
- [coerce_int](coerce_int.md) (4 shared connections)

## Source Files

- `server/realtime/event_handler.py`
- `server/realtime/message_builders.py`
- `server/realtime/npc_event_handlers.py`
- `server/realtime/npc_occupant_processor.py`
- `server/realtime/player_event_handlers.py`
- `server/realtime/player_event_handlers_respawn.py`
- `server/realtime/player_event_handlers_room.py`
- `server/realtime/player_event_handlers_utils.py`
- `server/realtime/player_name_utils.py`
- `server/realtime/room_id_utils.py`
- `server/realtime/room_occupant_manager.py`
- `server/tests/unit/realtime/conftest.py`
- `server/tests/unit/realtime/test_event_handler.py`
- `server/tests/unit/realtime/test_room_occupant_manager.py`

## Audit Trail

- EXTRACTED: 1100 (95%)
- INFERRED: 53 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*