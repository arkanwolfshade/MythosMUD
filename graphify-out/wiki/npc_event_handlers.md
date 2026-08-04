# npc event handlers

> 135 nodes

## Key Concepts

- **test_npc_event_handlers.py** (44 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **NPCEventHandler** (25 connections) — `server/realtime/npc_event_handlers.py`
- **test_npc_event_handlers_helpers.py** (14 connections) — `server/tests/unit/realtime/test_npc_event_handlers_helpers.py`
- **.handle_npc_entered()** (8 connections) — `server/realtime/npc_event_handlers.py`
- **._send_npc_left_message()** (8 connections) — `server/realtime/npc_event_handlers.py`
- **._get_npc_spawn_message()** (7 connections) — `server/realtime/npc_event_handlers.py`
- **._send_room_message()** (6 connections) — `server/realtime/npc_event_handlers.py`
- **.handle_npc_left()** (6 connections) — `server/realtime/npc_event_handlers.py`
- **.__init__()** (5 connections) — `server/realtime/npc_event_handlers.py`
- **Any** (5 connections)
- **._get_npc_instance()** (5 connections) — `server/realtime/npc_event_handlers.py`
- **._get_npc_name()** (5 connections) — `server/realtime/npc_event_handlers.py`
- **._get_behavior_config_from_instance()** (4 connections) — `server/realtime/npc_event_handlers.py`
- **._parse_behavior_config()** (4 connections) — `server/realtime/npc_event_handlers.py`
- **._extract_spawn_message_from_config()** (4 connections) — `server/realtime/npc_event_handlers.py`
- **._determine_direction_from_rooms()** (4 connections) — `server/realtime/npc_event_handlers.py`
- **._get_npc_departure_message()** (4 connections) — `server/realtime/npc_event_handlers.py`
- **._validate_npc_left_room()** (4 connections) — `server/realtime/npc_event_handlers.py`
- **._schedule_room_occupants_update()** (4 connections) — `server/realtime/npc_event_handlers.py`
- **npc_event_handler()** (3 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **test_handle_npc_entered_room()** (3 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **test_handle_npc_left_room()** (3 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **test_handle_npc_entered_room_with_npc_instance()** (3 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **test_handle_npc_left_room_with_npc_instance()** (3 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **test_handle_npc_entered_no_connection_manager()** (3 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- *... and 110 more nodes in this community*

## Relationships

- [Realtime Subscribers](Realtime_Subscribers.md) (21 shared connections)
- [logging setup structured](logging_setup_structured.md) (3 shared connections)
- [schemas player rationale](schemas_player_rationale.md) (3 shared connections)
- [commands communication channels](commands_communication_channels.md) (2 shared connections)
- [realtime monitoring performance](realtime_monitoring_performance.md) (2 shared connections)
- [NPC Combat](NPC_Combat.md) (1 shared connections)
- [room look commands](room_look_commands.md) (1 shared connections)

## Source Files

- `server/realtime/npc_event_handlers.py`
- `server/tests/unit/realtime/test_npc_event_handlers.py`
- `server/tests/unit/realtime/test_npc_event_handlers_helpers.py`

## Audit Trail

- EXTRACTED: 341 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*