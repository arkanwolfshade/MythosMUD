# event_handler.py

> 127 nodes

## Key Concepts

- **event_handler.py** (42 connections) — `server/realtime/event_handler.py`
- **NPCEventHandler** (41 connections) — `server/realtime/npc_event_handlers.py`
- **MessageBuilder** (38 connections) — `server/realtime/message_builders.py`
- **RealTimeEventHandler** (35 connections) — `server/realtime/event_handler.py`
- **test_npc_event_handlers_segments.py** (18 connections) — `server/tests/unit/realtime/test_npc_event_handlers_segments.py`
- **.call()** (15 connections) — `server/realtime/circuit_breaker.py`
- **.__init__()** (9 connections) — `server/realtime/event_handler.py`
- **_named()** (9 connections) — `server/tests/unit/realtime/test_npc_event_handlers_segments.py`
- **._initialize_modules()** (8 connections) — `server/realtime/event_handler.py`
- **._get_next_sequence()** (8 connections) — `server/realtime/message_builders.py`
- **test_authored_spawn_text_stays_plain()** (8 connections) — `server/tests/unit/realtime/test_npc_event_handlers_segments.py`
- **._get_npc_spawn_message()** (7 connections) — `server/realtime/npc_event_handlers.py`
- **_drive_npc_room_messages()** (7 connections) — `server/tests/unit/realtime/test_message_category_invariants.py`
- **test_default_departure_line_styles_the_name_and_authored_text_does_not()** (7 connections) — `server/tests/unit/realtime/test_npc_event_handlers_segments.py`
- **test_default_spawn_line_styles_the_name()** (7 connections) — `server/tests/unit/realtime/test_npc_event_handlers_segments.py`
- **test_movement_into_the_room_styles_the_name_by_disposition()** (7 connections) — `server/tests/unit/realtime/test_npc_event_handlers_segments.py`
- **test_movement_out_of_the_room_styles_the_name_by_disposition()** (7 connections) — `server/tests/unit/realtime/test_npc_event_handlers_segments.py`
- **Any** (7 connections)
- **.handle_npc_left()** (6 connections) — `server/realtime/npc_event_handlers.py`
- **._send_room_message()** (6 connections) — `server/realtime/npc_event_handlers.py`
- **Any** (6 connections)
- **._send_room_occupants_update_internal()** (5 connections) — `server/realtime/event_handler.py`
- **.build_occupants_update_message()** (5 connections) — `server/realtime/message_builders.py`
- **.create_player_entered_message()** (5 connections) — `server/realtime/message_builders.py`
- **.create_player_left_message()** (5 connections) — `server/realtime/message_builders.py`
- *... and 102 more nodes in this community*

## Relationships

- [NpcDisposition](NpcDisposition.md) (32 shared connections)
- [EventBus](EventBus.md) (18 shared connections)
- [player_event_handlers.py](player_event_handlers.py.md) (10 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (10 shared connections)
- [AttributeError](AttributeError.md) (8 shared connections)
- [CircuitBreaker](CircuitBreaker.md) (8 shared connections)
- [get_logger](get_logger.md) (8 shared connections)
- [test_message_category_invariants.py](test_message_category_invariants.py.md) (7 shared connections)
- [test_event_handler.py](test_event_handler.py.md) (5 shared connections)
- [PlayerNameExtractor](PlayerNameExtractor.md) (4 shared connections)
- [NPCOccupantProcessor](NPCOccupantProcessor.md) (4 shared connections)
- [test_room_system_message_categories.py](test_room_system_message_categories.py.md) (4 shared connections)

## Source Files

- `server/realtime/circuit_breaker.py`
- `server/realtime/event_handler.py`
- `server/realtime/message_builders.py`
- `server/realtime/npc_event_handlers.py`
- `server/tests/unit/realtime/test_event_handler.py`
- `server/tests/unit/realtime/test_message_builders.py`
- `server/tests/unit/realtime/test_message_category_invariants.py`
- `server/tests/unit/realtime/test_npc_event_handlers_segments.py`

## Audit Trail

- EXTRACTED: 291 (87%)
- INFERRED: 43 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*