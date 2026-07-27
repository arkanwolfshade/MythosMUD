# Player Left Room Tests

> 84 nodes · cohesion 0.02

## Key Concepts

- **test_player_event_handlers_room.py** (36 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`
- **test_player_event_handlers_room_left.py** (14 connections) — `server/tests/unit/realtime/test_player_event_handlers_room_left.py`
- **test_handle_player_left_disconnecting()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_room_left.py`
- **test_handle_player_left_error_handling()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_room_left.py`
- **test_handle_player_left_no_player_info()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_room_left.py`
- **test_handle_player_left_success()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_room_left.py`
- **test_handle_player_entered_no_player_info()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`
- **test_handle_player_entered_success()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`
- **test_process_player_entered_event_no_player_info()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`
- **test_process_player_entered_event_no_room_id()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`
- **test_process_player_entered_event_success()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`
- **Test unsubscribe_player_from_room() handles string player_id.** (2 connections) — `server/tests/unit/realtime/test_player_event_handlers_room_left.py`
- **test_broadcast_player_left_message_disconnecting()** (2 connections) — `server/tests/unit/realtime/test_player_event_handlers_room_left.py`
- **test_broadcast_player_left_message_no_room_id()** (2 connections) — `server/tests/unit/realtime/test_player_event_handlers_room_left.py`
- **test_broadcast_player_left_message_not_disconnecting()** (2 connections) — `server/tests/unit/realtime/test_player_event_handlers_room_left.py`
- **test_log_occupants_info()** (2 connections) — `server/tests/unit/realtime/test_player_event_handlers_room_left.py`
- **test_unsubscribe_player_from_room_invalid_id()** (2 connections) — `server/tests/unit/realtime/test_player_event_handlers_room_left.py`
- **test_unsubscribe_player_from_room_string_id()** (2 connections) — `server/tests/unit/realtime/test_player_event_handlers_room_left.py`
- **test_unsubscribe_player_from_room_success()** (2 connections) — `server/tests/unit/realtime/test_player_event_handlers_room_left.py`
- **Test broadcast_player_entered_message() skips when room_id is None.** (2 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`
- **Test log_player_movement() logs player joined.** (2 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`
- **test_broadcast_player_entered_message()** (2 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`
- **test_broadcast_player_entered_message_no_room_id()** (2 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`
- **test_build_room_occupants_message()** (2 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`
- **test_log_player_movement_error_handling()** (2 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`
- *... and 59 more nodes in this community*

## Relationships

- [[Distributed Event Bus]] (6 shared connections)
- [[Player Event Handler Tests]] (5 shared connections)
- [[NPC Services Bundle]] (5 shared connections)

## Source Files

- `server/tests/unit/realtime/test_player_event_handlers_room.py`
- `server/tests/unit/realtime/test_player_event_handlers_room_left.py`

## Audit Trail

- EXTRACTED: 186 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
