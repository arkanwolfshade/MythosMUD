# MessageBuilder

> 98 nodes

## Key Concepts

- **MessageBuilder** (26 connections) — `server/realtime/message_builders.py`
- **NPCEventHandler** (26 connections) — `server/realtime/npc_event_handlers.py`
- **test_message_builders.py** (15 connections) — `server/tests/unit/realtime/test_message_builders.py`
- **test_npc_event_handlers_helpers.py** (15 connections) — `server/tests/unit/realtime/test_npc_event_handlers_helpers.py`
- **._get_next_sequence()** (8 connections) — `server/realtime/message_builders.py`
- **.handle_npc_entered()** (8 connections) — `server/realtime/npc_event_handlers.py`
- **._send_npc_left_message()** (8 connections) — `server/realtime/npc_event_handlers.py`
- **_builder()** (8 connections) — `server/tests/unit/realtime/test_message_builders.py`
- **._get_npc_spawn_message()** (7 connections) — `server/realtime/npc_event_handlers.py`
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
- **.build_occupants_update_message()** (4 connections) — `server/realtime/message_builders.py`
- **.build_room_state_message()** (4 connections) — `server/realtime/message_builders.py`
- **.build_room_update_message()** (4 connections) — `server/realtime/message_builders.py`
- **._determine_direction_from_rooms()** (4 connections) — `server/realtime/npc_event_handlers.py`
- **._extract_spawn_message_from_config()** (4 connections) — `server/realtime/npc_event_handlers.py`
- **._get_behavior_config_from_instance()** (4 connections) — `server/realtime/npc_event_handlers.py`
- *... and 73 more nodes in this community*

## Relationships

- [event_types.py](event_types.py.md) (15 shared connections)
- [player_event_handlers.py](player_event_handlers.py.md) (10 shared connections)
- [test_npc_event_handlers.py](test_npc_event_handlers.py.md) (3 shared connections)
- [PlayerLeftRoom](PlayerLeftRoom.md) (3 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (3 shared connections)
- [TrackedTaskManager](TrackedTaskManager.md) (2 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [build_event](build_event.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/realtime/message_builders.py`
- `server/realtime/npc_event_handlers.py`
- `server/tests/unit/realtime/test_message_builders.py`
- `server/tests/unit/realtime/test_npc_event_handlers_helpers.py`

## Audit Trail

- EXTRACTED: 171 (95%)
- INFERRED: 9 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*