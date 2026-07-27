# NPC Event Handler Tests

> 69 nodes · cohesion 0.03

## Key Concepts

- **test_npc_event_handlers.py** (42 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **Test _parse_behavior_config() with JSON string.** (4 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **npc_event_handler()** (3 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **test_handle_npc_entered_no_connection_manager()** (3 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **test_handle_npc_entered_no_persistence()** (3 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **test_handle_npc_entered_room()** (3 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **test_handle_npc_entered_room_not_found()** (3 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **test_handle_npc_entered_room_with_npc_instance()** (3 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **test_handle_npc_left_no_connection_manager()** (3 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **test_handle_npc_left_no_persistence()** (3 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **test_handle_npc_left_room()** (3 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **test_handle_npc_left_room_not_found()** (3 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **test_handle_npc_left_room_with_npc_instance()** (3 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **mock_connection_manager()** (2 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **mock_message_builder()** (2 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **mock_send_occupants_update()** (2 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **Test _send_room_message() handles missing connection_manager.** (2 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **Test _get_behavior_config_from_instance() with method.** (2 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **test_determine_direction_from_rooms_no_match()** (2 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **test_determine_direction_from_rooms_no_persistence()** (2 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **test_get_behavior_config_from_instance_method()** (2 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **test_get_behavior_config_from_instance_none()** (2 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **test_get_behavior_config_from_instance_private_attr()** (2 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **test_get_behavior_config_from_instance_public_attr()** (2 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **test_get_npc_departure_message_no_config()** (2 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- *... and 44 more nodes in this community*

## Relationships

- [[Distributed Event Bus]] (6 shared connections)
- [[NPC Services Bundle]] (6 shared connections)
- [[Player Respawn Events]] (2 shared connections)
- [[Realtime Npc Event]] (1 shared connections)
- [[Target Resolution Service]] (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_npc_event_handlers.py`

## Audit Trail

- EXTRACTED: 162 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
