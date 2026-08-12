# asyncio

> 11 nodes

## Key Concepts

- **asyncio** (33 connections)
- **test_handle_player_entered_error_handling()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`
- **test_process_player_entered_event_no_room_id()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`
- **test_build_room_occupants_message()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`
- **test_query_room_occupants_snapshot()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`
- **test_send_room_updates_to_entering_player_invalid_id()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`
- **Test build_room_occupants_message() builds correct message.** (1 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`
- **Test query_room_occupants_snapshot() queries occupants.** (1 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`
- **Test send_room_updates_to_entering_player() handles invalid player_id.** (1 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`
- **Test _process_player_entered_event() returns None when room_id is None.** (1 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`
- **Test handle_player_entered() handles errors.** (1 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`

## Relationships

- [test_player_event_handlers_room.py](test_player_event_handlers_room.py.md) (9 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [test_broadcast_player_entered_message](test_broadcast_player_entered_message.md) (1 shared connections)
- [test_handle_player_entered_no_connection_manager](test_handle_player_entered_no_connection_manager.md) (1 shared connections)
- [test_handle_player_entered_no_player_info](test_handle_player_entered_no_player_info.md) (1 shared connections)
- [test_handle_player_entered_success](test_handle_player_entered_success.md) (1 shared connections)
- [test_log_player_movement_error_handling](test_log_player_movement_error_handling.md) (1 shared connections)
- [test_log_player_movement_joined](test_log_player_movement_joined.md) (1 shared connections)
- [test_log_player_movement_left](test_log_player_movement_left.md) (1 shared connections)
- [test_log_player_movement_no_room](test_log_player_movement_no_room.md) (1 shared connections)
- [test_prepare_room_data_with_to_dict](test_prepare_room_data_with_to_dict.md) (1 shared connections)
- [test_process_player_entered_event_no_player_info](test_process_player_entered_event_no_player_info.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_player_event_handlers_room.py`

## Audit Trail

- EXTRACTED: 55 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*