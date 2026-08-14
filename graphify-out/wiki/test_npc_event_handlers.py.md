# test_npc_event_handlers.py

> 141 nodes

## Key Concepts

- **test_npc_event_handlers.py** (45 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **NPCEventHandler** (26 connections) — `server/realtime/npc_event_handlers.py`
- **asyncio** (16 connections)
- **test_npc_event_handlers_helpers.py** (14 connections) — `server/tests/unit/realtime/test_npc_event_handlers_helpers.py`
- **.handle_npc_entered()** (8 connections) — `server/realtime/npc_event_handlers.py`
- **._send_npc_left_message()** (8 connections) — `server/realtime/npc_event_handlers.py`
- **._get_npc_spawn_message()** (7 connections) — `server/realtime/npc_event_handlers.py`
- **.handle_npc_left()** (6 connections) — `server/realtime/npc_event_handlers.py`
- **._send_room_message()** (6 connections) — `server/realtime/npc_event_handlers.py`
- **._get_npc_instance()** (5 connections) — `server/realtime/npc_event_handlers.py`
- **._get_npc_name()** (5 connections) — `server/realtime/npc_event_handlers.py`
- **.__init__()** (5 connections) — `server/realtime/npc_event_handlers.py`
- **._schedule_room_occupants_update()** (5 connections) — `server/realtime/npc_event_handlers.py`
- **Any** (5 connections)
- **._determine_direction_from_rooms()** (4 connections) — `server/realtime/npc_event_handlers.py`
- **._extract_spawn_message_from_config()** (4 connections) — `server/realtime/npc_event_handlers.py`
- **._get_behavior_config_from_instance()** (4 connections) — `server/realtime/npc_event_handlers.py`
- **._get_npc_departure_message()** (4 connections) — `server/realtime/npc_event_handlers.py`
- **._parse_behavior_config()** (4 connections) — `server/realtime/npc_event_handlers.py`
- **._validate_npc_left_room()** (4 connections) — `server/realtime/npc_event_handlers.py`
- **npc_event_handler()** (4 connections) — `server/tests/unit/realtime/test_npc_event_handlers_helpers.py`
- **npc_event_handler()** (4 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **test_handle_npc_entered_no_connection_manager()** (4 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **test_handle_npc_entered_no_persistence()** (4 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **test_handle_npc_entered_room()** (4 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- *... and 116 more nodes in this community*

## Relationships

- [event_types.py](event_types.py.md) (15 shared connections)
- [lifecycle_manager.py](lifecycle_manager.py.md) (9 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (3 shared connections)
- [TrackedTaskManager](TrackedTaskManager.md) (2 shared connections)
- [RealTimeEventHandler](RealTimeEventHandler.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [build_event](build_event.md) (1 shared connections)

## Source Files

- `server/realtime/npc_event_handlers.py`
- `server/tests/unit/realtime/test_npc_event_handlers.py`
- `server/tests/unit/realtime/test_npc_event_handlers_helpers.py`

## Audit Trail

- EXTRACTED: 214 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*