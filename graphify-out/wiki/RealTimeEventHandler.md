# RealTimeEventHandler

> 90 nodes

## Key Concepts

- **RealTimeEventHandler** (35 connections) — `server/realtime/event_handler.py`
- **MessageBuilder** (28 connections) — `server/realtime/message_builders.py`
- **test_message_builders.py** (15 connections) — `server/tests/unit/realtime/test_message_builders.py`
- **.__init__()** (9 connections) — `server/realtime/event_handler.py`
- **._initialize_modules()** (8 connections) — `server/realtime/event_handler.py`
- **._get_next_sequence()** (8 connections) — `server/realtime/message_builders.py`
- **send_personalized_occupants_update()** (8 connections) — `server/realtime/room_viewer_fanout.py`
- **_builder()** (8 connections) — `server/tests/unit/realtime/test_message_builders.py`
- **Any** (6 connections)
- **._send_room_occupants_update_internal()** (5 connections) — `server/realtime/event_handler.py`
- **.create_player_entered_message()** (5 connections) — `server/realtime/message_builders.py`
- **.create_player_left_message()** (5 connections) — `server/realtime/message_builders.py`
- **.build_occupants_update_message()** (4 connections) — `server/realtime/message_builders.py`
- **.build_room_state_message()** (4 connections) — `server/realtime/message_builders.py`
- **.build_room_update_message()** (4 connections) — `server/realtime/message_builders.py`
- **test_create_player_entered_message()** (4 connections) — `server/tests/unit/realtime/test_message_builders.py`
- **test_create_player_left_message()** (4 connections) — `server/tests/unit/realtime/test_message_builders.py`
- **._create_player_entered_message()** (3 connections) — `server/realtime/event_handler.py`
- **._create_player_left_message()** (3 connections) — `server/realtime/event_handler.py`
- **._handle_npc_entered()** (3 connections) — `server/realtime/event_handler.py`
- **._handle_npc_left()** (3 connections) — `server/realtime/event_handler.py`
- **._handle_player_delirium_respawned()** (3 connections) — `server/realtime/event_handler.py`
- **._handle_player_died()** (3 connections) — `server/realtime/event_handler.py`
- **._handle_player_dp_decay()** (3 connections) — `server/realtime/event_handler.py`
- **._handle_player_dp_updated()** (3 connections) — `server/realtime/event_handler.py`
- *... and 65 more nodes in this community*

## Relationships

- [event_types.py](event_types.py.md) (20 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (10 shared connections)
- [PlayerEventHandler](PlayerEventHandler.md) (7 shared connections)
- [build_event](build_event.md) (5 shared connections)
- [NPCEventHandler](NPCEventHandler.md) (4 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (3 shared connections)
- [PlayerNameExtractor](PlayerNameExtractor.md) (2 shared connections)
- [NPCOccupantProcessor](NPCOccupantProcessor.md) (2 shared connections)
- [PlayerDPUpdated](PlayerDPUpdated.md) (2 shared connections)
- [EventBus](EventBus.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [TaskRegistry](TaskRegistry.md) (1 shared connections)

## Source Files

- `server/realtime/event_handler.py`
- `server/realtime/message_builders.py`
- `server/realtime/room_viewer_fanout.py`
- `server/tests/unit/realtime/test_event_handler.py`
- `server/tests/unit/realtime/test_message_builders.py`

## Audit Trail

- EXTRACTED: 159 (92%)
- INFERRED: 14 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*