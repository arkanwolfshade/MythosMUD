# NPCEventHandler

> 63 nodes

## Key Concepts

- **NPCEventHandler** (28 connections) — `server/realtime/npc_event_handlers.py`
- **test_npc_event_handlers_helpers.py** (14 connections) — `server/tests/unit/realtime/test_npc_event_handlers_helpers.py`
- **.handle_npc_entered()** (8 connections) — `server/realtime/npc_event_handlers.py`
- **._send_npc_left_message()** (8 connections) — `server/realtime/npc_event_handlers.py`
- **._get_npc_spawn_message()** (7 connections) — `server/realtime/npc_event_handlers.py`
- **Any** (7 connections)
- **.handle_npc_left()** (6 connections) — `server/realtime/npc_event_handlers.py`
- **._send_room_message()** (6 connections) — `server/realtime/npc_event_handlers.py`
- **._get_npc_departure_message()** (5 connections) — `server/realtime/npc_event_handlers.py`
- **._get_npc_instance()** (5 connections) — `server/realtime/npc_event_handlers.py`
- **._get_npc_name()** (5 connections) — `server/realtime/npc_event_handlers.py`
- **.__init__()** (5 connections) — `server/realtime/npc_event_handlers.py`
- **._resolve_active_npc_instance()** (5 connections) — `server/realtime/npc_event_handlers.py`
- **._schedule_room_occupants_update()** (5 connections) — `server/realtime/npc_event_handlers.py`
- **._determine_direction_from_rooms()** (4 connections) — `server/realtime/npc_event_handlers.py`
- **._extract_spawn_message_from_config()** (4 connections) — `server/realtime/npc_event_handlers.py`
- **._get_behavior_config_from_instance()** (4 connections) — `server/realtime/npc_event_handlers.py`
- **._parse_behavior_config()** (4 connections) — `server/realtime/npc_event_handlers.py`
- **._resolve_npc_behavior_config()** (4 connections) — `server/realtime/npc_event_handlers.py`
- **._validate_npc_left_room()** (4 connections) — `server/realtime/npc_event_handlers.py`
- **npc_event_handler()** (4 connections) — `server/tests/unit/realtime/test_npc_event_handlers_helpers.py`
- **mock_connection_manager()** (3 connections) — `server/tests/unit/realtime/test_npc_event_handlers_helpers.py`
- **mock_message_builder()** (3 connections) — `server/tests/unit/realtime/test_npc_event_handlers_helpers.py`
- **test_determine_direction_from_rooms()** (3 connections) — `server/tests/unit/realtime/test_npc_event_handlers_helpers.py`
- **test_determine_direction_from_rooms_not_found()** (3 connections) — `server/tests/unit/realtime/test_npc_event_handlers_helpers.py`
- *... and 38 more nodes in this community*

## Relationships

- [event_types.py](event_types.py.md) (9 shared connections)
- [PlayerEventHandlerUtils](PlayerEventHandlerUtils.md) (4 shared connections)
- [NPCDefinition](NPCDefinition.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [test_event_handler.py](test_event_handler.py.md) (1 shared connections)
- [build_event](build_event.md) (1 shared connections)

## Source Files

- `server/realtime/npc_event_handlers.py`
- `server/tests/unit/realtime/test_npc_event_handlers_helpers.py`

## Audit Trail

- EXTRACTED: 106 (95%)
- INFERRED: 5 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*