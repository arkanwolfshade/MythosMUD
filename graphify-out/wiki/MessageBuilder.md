# MessageBuilder

> 45 nodes

## Key Concepts

- **MessageBuilder** (28 connections) — `server/realtime/message_builders.py`
- **test_message_builders.py** (15 connections) — `server/tests/unit/realtime/test_message_builders.py`
- **.__init__()** (10 connections) — `server/realtime/player_event_handlers.py`
- **._initialize_modules()** (8 connections) — `server/realtime/event_handler.py`
- **._get_next_sequence()** (8 connections) — `server/realtime/message_builders.py`
- **_builder()** (8 connections) — `server/tests/unit/realtime/test_message_builders.py`
- **Any** (6 connections)
- **.create_player_entered_message()** (5 connections) — `server/realtime/message_builders.py`
- **.create_player_left_message()** (5 connections) — `server/realtime/message_builders.py`
- **.build_occupants_update_message()** (4 connections) — `server/realtime/message_builders.py`
- **.build_room_state_message()** (4 connections) — `server/realtime/message_builders.py`
- **.build_room_update_message()** (4 connections) — `server/realtime/message_builders.py`
- **test_create_player_entered_message()** (4 connections) — `server/tests/unit/realtime/test_message_builders.py`
- **test_create_player_left_message()** (4 connections) — `server/tests/unit/realtime/test_message_builders.py`
- **.__init__()** (3 connections) — `server/realtime/message_builders.py`
- **test_build_occupants_update_message()** (3 connections) — `server/tests/unit/realtime/test_message_builders.py`
- **test_build_room_state_message()** (3 connections) — `server/tests/unit/realtime/test_message_builders.py`
- **test_build_room_update_message()** (3 connections) — `server/tests/unit/realtime/test_message_builders.py`
- **test_create_npc_movement_message_variants()** (3 connections) — `server/tests/unit/realtime/test_message_builders.py`
- **test_get_next_sequence_non_callable_returns_zero()** (3 connections) — `server/tests/unit/realtime/test_message_builders.py`
- **test_get_next_sequence_uses_callable()** (3 connections) — `server/tests/unit/realtime/test_message_builders.py`
- **.create_npc_movement_message()** (2 connections) — `server/realtime/message_builders.py`
- **ChatLogger** (1 connections)
- **ConnectionManager** (1 connections)
- **Initialize specialized handler modules.** (1 connections) — `server/realtime/event_handler.py`
- *... and 20 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (10 shared connections)
- [PlayerEventHandlerUtils](PlayerEventHandlerUtils.md) (8 shared connections)
- [NPCEventHandler](NPCEventHandler.md) (3 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (3 shared connections)
- [RealTimeEventHandler](RealTimeEventHandler.md) (2 shared connections)
- [test_room_sync_service.py](test_room_sync_service.py.md) (2 shared connections)
- [PlayerNameExtractor](PlayerNameExtractor.md) (2 shared connections)
- [NPCOccupantProcessor](NPCOccupantProcessor.md) (2 shared connections)
- [get_viewer_phantom_names](get_viewer_phantom_names.md) (1 shared connections)

## Source Files

- `server/realtime/event_handler.py`
- `server/realtime/message_builders.py`
- `server/realtime/player_event_handlers.py`
- `server/tests/unit/realtime/test_message_builders.py`

## Audit Trail

- EXTRACTED: 90 (94%)
- INFERRED: 6 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*