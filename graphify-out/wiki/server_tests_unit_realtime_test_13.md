# server tests unit realtime test

> 79 nodes

## Key Concepts

- **test_npc_event_handlers.py** (46 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **asyncio** (16 connections)
- **npc_event_handler()** (4 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **test_handle_npc_entered_no_connection_manager()** (4 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **test_handle_npc_entered_no_persistence()** (4 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **test_handle_npc_entered_room()** (4 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **test_handle_npc_entered_room_not_found()** (4 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **test_handle_npc_entered_room_with_npc_instance()** (4 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **test_handle_npc_left_no_connection_manager()** (4 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **test_handle_npc_left_no_persistence()** (4 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **test_handle_npc_left_room()** (4 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **test_handle_npc_left_room_not_found()** (4 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **test_handle_npc_left_room_with_npc_instance()** (4 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **test_schedule_room_occupants_update_does_not_leak_coro_when_register_fails()** (4 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **fixture** (4 connections)
- **mock_connection_manager()** (3 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **mock_message_builder()** (3 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **mock_send_occupants_update()** (3 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **test_determine_direction_from_rooms_no_match()** (3 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **test_determine_direction_from_rooms_no_persistence()** (3 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **test_determine_direction_from_rooms_room_not_found()** (3 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **test_send_room_message_no_connection_manager()** (3 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **test_send_room_message_no_room_manager()** (3 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **Test _parse_behavior_config() with invalid JSON.** (3 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **test_get_behavior_config_from_instance_method()** (2 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- *... and 54 more nodes in this community*

## Relationships

- [server events event bus](server_events_event_bus.md) (7 shared connections)
- [moduletype](moduletype.md) (6 shared connections)
- [server realtime event handler py](server_realtime_event_handler_py.md) (3 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_npc_event_handlers.py`

## Audit Trail

- EXTRACTED: 105 (90%)
- INFERRED: 12 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*