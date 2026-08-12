# NPCEventHandler

> 59 nodes

## Key Concepts

- **NPCEventHandler** (25 connections) — `server/realtime/npc_event_handlers.py`
- **test_npc_event_handlers_helpers.py** (14 connections) — `server/tests/unit/realtime/test_npc_event_handlers_helpers.py`
- **.handle_npc_entered()** (8 connections) — `server/realtime/npc_event_handlers.py`
- **._send_npc_left_message()** (8 connections) — `server/realtime/npc_event_handlers.py`
- **._get_npc_spawn_message()** (7 connections) — `server/realtime/npc_event_handlers.py`
- **.handle_npc_left()** (6 connections) — `server/realtime/npc_event_handlers.py`
- **._send_room_message()** (6 connections) — `server/realtime/npc_event_handlers.py`
- **._get_npc_instance()** (5 connections) — `server/realtime/npc_event_handlers.py`
- **._get_npc_name()** (5 connections) — `server/realtime/npc_event_handlers.py`
- **.__init__()** (5 connections) — `server/realtime/npc_event_handlers.py`
- **Any** (5 connections)
- **._determine_direction_from_rooms()** (4 connections) — `server/realtime/npc_event_handlers.py`
- **._extract_spawn_message_from_config()** (4 connections) — `server/realtime/npc_event_handlers.py`
- **._get_behavior_config_from_instance()** (4 connections) — `server/realtime/npc_event_handlers.py`
- **._get_npc_departure_message()** (4 connections) — `server/realtime/npc_event_handlers.py`
- **._parse_behavior_config()** (4 connections) — `server/realtime/npc_event_handlers.py`
- **._schedule_room_occupants_update()** (4 connections) — `server/realtime/npc_event_handlers.py`
- **._validate_npc_left_room()** (4 connections) — `server/realtime/npc_event_handlers.py`
- **npc_event_handler()** (4 connections) — `server/tests/unit/realtime/test_npc_event_handlers_helpers.py`
- **mock_connection_manager()** (3 connections) — `server/tests/unit/realtime/test_npc_event_handlers_helpers.py`
- **mock_message_builder()** (3 connections) — `server/tests/unit/realtime/test_npc_event_handlers_helpers.py`
- **test_determine_direction_from_rooms()** (3 connections) — `server/tests/unit/realtime/test_npc_event_handlers_helpers.py`
- **test_determine_direction_from_rooms_not_found()** (3 connections) — `server/tests/unit/realtime/test_npc_event_handlers_helpers.py`
- **fixture** (3 connections)
- **test_extract_spawn_message_from_config()** (2 connections) — `server/tests/unit/realtime/test_npc_event_handlers_helpers.py`
- *... and 34 more nodes in this community*

## Relationships

- [get_npc_instance_service](get_npc_instance_service.md) (13 shared connections)
- [time.py](time.py.md) (3 shared connections)
- [test_npc_event_handlers.py](test_npc_event_handlers.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [RealTimeEventHandler](RealTimeEventHandler.md) (1 shared connections)

## Source Files

- `server/realtime/npc_event_handlers.py`
- `server/tests/unit/realtime/test_npc_event_handlers_helpers.py`

## Audit Trail

- EXTRACTED: 100 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*