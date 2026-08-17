# asyncio

> 19 nodes

## Key Concepts

- **asyncio** (16 connections)
- **test_handle_npc_entered_no_persistence()** (4 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **test_handle_npc_entered_room()** (4 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **test_handle_npc_left_no_persistence()** (4 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **test_handle_npc_left_room()** (4 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **test_handle_npc_left_room_not_found()** (4 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **test_handle_npc_left_room_with_npc_instance()** (4 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **test_determine_direction_from_rooms_no_match()** (3 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **test_determine_direction_from_rooms_room_not_found()** (3 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **test_send_room_message_no_room_manager()** (3 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **Test handle_npc_entered_room() processes event.** (1 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **Test handle_npc_left_room() processes event.** (1 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **Test handle_npc_left_room() with valid NPC instance.** (1 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **Test _determine_direction_from_rooms() returns None when room not found.** (1 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **Test _determine_direction_from_rooms() returns None when no matching exit.** (1 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **Test _send_room_message() handles missing room_manager.** (1 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **Test handle_npc_entered() handles missing persistence.** (1 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **Test handle_npc_left() handles missing persistence.** (1 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **Test handle_npc_left() handles room not found.** (1 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`

## Relationships

- [test_npc_event_handlers.py](test_npc_event_handlers.py.md) (9 shared connections)
- [ConnectionManager](ConnectionManager.md) (6 shared connections)
- [test_determine_direction_from_rooms_no_persistence](test_determine_direction_from_rooms_no_persistence.md) (1 shared connections)
- [test_handle_npc_entered_no_connection_manager](test_handle_npc_entered_no_connection_manager.md) (1 shared connections)
- [test_handle_npc_entered_room_not_found](test_handle_npc_entered_room_not_found.md) (1 shared connections)
- [test_handle_npc_entered_room_with_npc_instance](test_handle_npc_entered_room_with_npc_instance.md) (1 shared connections)
- [test_handle_npc_left_no_connection_manager](test_handle_npc_left_no_connection_manager.md) (1 shared connections)
- [test_schedule_room_occupants_update_does_not_leak_coro_when_register_fails](test_schedule_room_occupants_update_does_not_leak_coro_when_register_fails.md) (1 shared connections)
- [test_send_room_message_no_connection_manager](test_send_room_message_no_connection_manager.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_npc_event_handlers.py`

## Audit Trail

- EXTRACTED: 34 (85%)
- INFERRED: 6 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*