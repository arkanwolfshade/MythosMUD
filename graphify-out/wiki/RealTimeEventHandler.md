# RealTimeEventHandler

> 157 nodes

## Key Concepts

- **RealTimeEventHandler** (36 connections) — `server/realtime/event_handler.py`
- **MessageBuilder** (26 connections) — `server/realtime/message_builders.py`
- **NPCEventHandler** (26 connections) — `server/realtime/npc_event_handlers.py`
- **test_message_builders.py** (15 connections) — `server/tests/unit/realtime/test_message_builders.py`
- **test_npc_event_handlers_helpers.py** (15 connections) — `server/tests/unit/realtime/test_npc_event_handlers_helpers.py`
- **.__init__()** (9 connections) — `server/realtime/event_handler.py`
- **._initialize_modules()** (8 connections) — `server/realtime/event_handler.py`
- **._get_next_sequence()** (8 connections) — `server/realtime/message_builders.py`
- **.handle_npc_entered()** (8 connections) — `server/realtime/npc_event_handlers.py`
- **._send_npc_left_message()** (8 connections) — `server/realtime/npc_event_handlers.py`
- **_builder()** (8 connections) — `server/tests/unit/realtime/test_message_builders.py`
- **._get_npc_spawn_message()** (7 connections) — `server/realtime/npc_event_handlers.py`
- **event_handler()** (7 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **.handle_npc_left()** (6 connections) — `server/realtime/npc_event_handlers.py`
- **._send_room_message()** (6 connections) — `server/realtime/npc_event_handlers.py`
- **Any** (6 connections)
- **.create_player_entered_message()** (5 connections) — `server/realtime/message_builders.py`
- **.create_player_left_message()** (5 connections) — `server/realtime/message_builders.py`
- **._get_npc_instance()** (5 connections) — `server/realtime/npc_event_handlers.py`
- **._get_npc_name()** (5 connections) — `server/realtime/npc_event_handlers.py`
- **.__init__()** (5 connections) — `server/realtime/npc_event_handlers.py`
- **._schedule_room_occupants_update()** (5 connections) — `server/realtime/npc_event_handlers.py`
- **Any** (5 connections)
- **._create_player_entered_message()** (4 connections) — `server/realtime/event_handler.py`
- **._create_player_left_message()** (4 connections) — `server/realtime/event_handler.py`
- *... and 132 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (48 shared connections)
- [PlayerRoomEventHandler](PlayerRoomEventHandler.md) (3 shared connections)
- [test_npc_event_handlers.py](test_npc_event_handlers.py.md) (3 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (3 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (2 shared connections)
- [NPCOccupantProcessor](NPCOccupantProcessor.md) (2 shared connections)
- [PlayerNameExtractor](PlayerNameExtractor.md) (2 shared connections)
- [test_room_sync_service.py](test_room_sync_service.py.md) (2 shared connections)
- [.initialize](initialize.md) (1 shared connections)
- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) (1 shared connections)
- [test_chat_logger.py](test_chat_logger.py.md) (1 shared connections)
- [build_event](build_event.md) (1 shared connections)

## Source Files

- `server/realtime/event_handler.py`
- `server/realtime/message_builders.py`
- `server/realtime/npc_event_handlers.py`
- `server/tests/unit/realtime/test_event_handler.py`
- `server/tests/unit/realtime/test_message_builders.py`
- `server/tests/unit/realtime/test_npc_event_handlers_helpers.py`

## Audit Trail

- EXTRACTED: 257 (91%)
- INFERRED: 25 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*