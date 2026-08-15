# PlayerEventHandlerUtils

> 412 nodes

## Key Concepts

- **PlayerEventHandlerUtils** (40 connections) — `server/realtime/player_event_handlers_utils.py`
- **RealTimeEventHandler** (36 connections) — `server/realtime/event_handler.py`
- **PlayerRespawnEventHandler** (33 connections) — `server/realtime/player_event_handlers_respawn.py`
- **player_event_handlers_respawn.py** (33 connections) — `server/realtime/player_event_handlers_respawn.py`
- **test_player_event_handlers_state.py** (33 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **PlayerRoomEventHandler** (30 connections) — `server/realtime/player_event_handlers_room.py`
- **MessageBuilder** (26 connections) — `server/realtime/message_builders.py`
- **NPCEventHandler** (26 connections) — `server/realtime/npc_event_handlers.py`
- **PlayerEventHandler** (26 connections) — `server/realtime/player_event_handlers.py`
- **player_event_handlers.py** (26 connections) — `server/realtime/player_event_handlers.py`
- **NATSMessageHandler** (23 connections) — `server/realtime/nats_message_handler.py`
- **RoomOccupantManager** (22 connections) — `server/realtime/room_occupant_manager.py`
- **realtime/conftest.py** (22 connections) — `server/tests/unit/realtime/conftest.py`
- **asyncio** (19 connections)
- **player_event_handlers_room.py** (17 connections) — `server/realtime/player_event_handlers_room.py`
- **player_event_handlers_utils.py** (16 connections) — `server/realtime/player_event_handlers_utils.py`
- **fixture** (15 connections)
- **PlayerStateEventHandler** (14 connections) — `server/realtime/player_event_handlers_state.py`
- **UUID** (12 connections)
- **RespawnPlayerEventPayload** (11 connections) — `server/realtime/player_event_handlers_respawn.py`
- **Any** (10 connections)
- **.__init__()** (9 connections) — `server/realtime/event_handler.py`
- **._extract_occupant_names()** (9 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.handle_player_entered()** (9 connections) — `server/realtime/player_event_handlers_room.py`
- **Any** (9 connections)
- *... and 387 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (116 shared connections)
- [PlayerNameExtractor](PlayerNameExtractor.md) (12 shared connections)
- [Player](Player.md) (12 shared connections)
- [build_event](build_event.md) (10 shared connections)
- [websocket_initial_state.py](websocket_initial_state.py.md) (7 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (6 shared connections)
- [ConnectionManager](ConnectionManager.md) (6 shared connections)
- [NATSRetryHandler](NATSRetryHandler.md) (4 shared connections)
- [test_player_event_handlers_respawn.py](test_player_event_handlers_respawn.py.md) (4 shared connections)
- [test_room_occupant_manager.py](test_room_occupant_manager.py.md) (3 shared connections)
- [NPCOccupantProcessor](NPCOccupantProcessor.md) (3 shared connections)
- [DeadLetterQueue](DeadLetterQueue.md) (2 shared connections)

## Source Files

- `server/realtime/event_handler.py`
- `server/realtime/message_builders.py`
- `server/realtime/nats_message_handler.py`
- `server/realtime/npc_event_handlers.py`
- `server/realtime/player_event_handlers.py`
- `server/realtime/player_event_handlers_respawn.py`
- `server/realtime/player_event_handlers_room.py`
- `server/realtime/player_event_handlers_state.py`
- `server/realtime/player_event_handlers_utils.py`
- `server/realtime/room_occupant_manager.py`
- `server/tests/unit/realtime/conftest.py`
- `server/tests/unit/realtime/test_event_handler.py`
- `server/tests/unit/realtime/test_message_builders.py`
- `server/tests/unit/realtime/test_player_event_handlers_state.py`
- `server/tests/unit/realtime/test_player_event_handlers_utils_grace_period.py`

## Audit Trail

- EXTRACTED: 784 (91%)
- INFERRED: 75 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*