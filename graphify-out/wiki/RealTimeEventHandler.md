# RealTimeEventHandler

> 260 nodes

## Key Concepts

- **RealTimeEventHandler** (44 connections) — `server/realtime/event_handler.py`
- **PlayerEventHandlerUtils** (42 connections) — `server/realtime/player_event_handlers_utils.py`
- **PlayerRespawnEventHandler** (33 connections) — `server/realtime/player_event_handlers_respawn.py`
- **player_event_handlers_respawn.py** (33 connections) — `server/realtime/player_event_handlers_respawn.py`
- **PlayerRoomEventHandler** (30 connections) — `server/realtime/player_event_handlers_room.py`
- **PlayerEventHandler** (26 connections) — `server/realtime/player_event_handlers.py`
- **player_event_handlers.py** (26 connections) — `server/realtime/player_event_handlers.py`
- **MessageBuilder** (22 connections) — `server/realtime/message_builders.py`
- **RoomOccupantManager** (22 connections) — `server/realtime/room_occupant_manager.py`
- **realtime/conftest.py** (22 connections) — `server/tests/unit/realtime/conftest.py`
- **player_event_handlers_room.py** (17 connections) — `server/realtime/player_event_handlers_room.py`
- **player_event_handlers_utils.py** (16 connections) — `server/realtime/player_event_handlers_utils.py`
- **fixture** (15 connections)
- **PlayerStateEventHandler** (14 connections) — `server/realtime/player_event_handlers_state.py`
- **UUID** (12 connections)
- **Any** (10 connections)
- **.__init__()** (9 connections) — `server/realtime/event_handler.py`
- **._extract_occupant_names()** (9 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.handle_player_entered()** (9 connections) — `server/realtime/player_event_handlers_room.py`
- **Any** (9 connections)
- **test_player_event_handlers_utils_grace_period.py** (9 connections) — `server/tests/unit/realtime/test_player_event_handlers_utils_grace_period.py`
- **._initialize_modules()** (8 connections) — `server/realtime/event_handler.py`
- **._get_next_sequence()** (8 connections) — `server/realtime/message_builders.py`
- **.__init__()** (8 connections) — `server/realtime/player_event_handlers.py`
- **._initialize_handlers()** (7 connections) — `server/realtime/player_event_handlers.py`
- *... and 235 more nodes in this community*

## Relationships

- [event_types.py](event_types.py.md) (45 shared connections)
- [RespawnPlayerEventPayload](RespawnPlayerEventPayload.md) (20 shared connections)
- [get_logger](get_logger.md) (16 shared connections)
- [websocket_initial_state.py](websocket_initial_state.py.md) (12 shared connections)
- [PlayerNameExtractor](PlayerNameExtractor.md) (12 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (9 shared connections)
- [test_player_event_handlers_respawn.py](test_player_event_handlers_respawn.py.md) (7 shared connections)
- [test_login_grace_period_visual_indicator.py](test_login_grace_period_visual_indicator.py.md) (7 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (5 shared connections)
- [test_player_event_handlers_state.py](test_player_event_handlers_state.py.md) (5 shared connections)
- [build_event](build_event.md) (5 shared connections)
- [Player](Player.md) (5 shared connections)

## Source Files

- `server/realtime/event_handler.py`
- `server/realtime/message_builders.py`
- `server/realtime/player_event_handlers.py`
- `server/realtime/player_event_handlers_respawn.py`
- `server/realtime/player_event_handlers_room.py`
- `server/realtime/player_event_handlers_state.py`
- `server/realtime/player_event_handlers_utils.py`
- `server/realtime/room_occupant_manager.py`
- `server/tests/unit/realtime/conftest.py`
- `server/tests/unit/realtime/test_event_handler.py`
- `server/tests/unit/realtime/test_player_event_handlers_utils_grace_period.py`

## Audit Trail

- EXTRACTED: 549 (93%)
- INFERRED: 41 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*