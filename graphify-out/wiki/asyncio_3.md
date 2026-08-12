# asyncio

> 11 nodes

## Key Concepts

- **asyncio** (33 connections)
- **test_broadcast_player_entered_message_no_room_id()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`
- **test_log_player_movement_error_handling()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`
- **test_log_player_movement_no_connection_manager()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`
- **test_query_room_occupants_snapshot()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`
- **test_send_room_update_to_player_success()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`
- **Test broadcast_player_entered_message() skips when room_id is None.** (1 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`
- **Test send_room_update_to_player() successfully sends room update.** (1 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`
- **Test query_room_occupants_snapshot() queries occupants.** (1 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`
- **Test log_player_movement() skips when connection manager not available.** (1 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`
- **Test log_player_movement() handles errors.** (1 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`

## Relationships

- [test_player_event_handlers_room.py](test_player_event_handlers_room.py.md) (9 shared connections)
- [test_broadcast_player_entered_message](test_broadcast_player_entered_message.md) (1 shared connections)
- [test_build_room_occupants_message](test_build_room_occupants_message.md) (1 shared connections)
- [test_handle_player_entered_no_connection_manager](test_handle_player_entered_no_connection_manager.md) (1 shared connections)
- [test_handle_player_entered_no_player_info](test_handle_player_entered_no_player_info.md) (1 shared connections)
- [test_handle_player_entered_success](test_handle_player_entered_success.md) (1 shared connections)
- [test_log_player_movement_joined](test_log_player_movement_joined.md) (1 shared connections)
- [test_log_player_movement_left](test_log_player_movement_left.md) (1 shared connections)
- [test_log_player_movement_no_room](test_log_player_movement_no_room.md) (1 shared connections)
- [test_prepare_room_data_with_to_dict](test_prepare_room_data_with_to_dict.md) (1 shared connections)
- [test_process_player_entered_event_no_player_info](test_process_player_entered_event_no_player_info.md) (1 shared connections)
- [test_process_player_entered_event_success](test_process_player_entered_event_success.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_player_event_handlers_room.py`

## Audit Trail

- EXTRACTED: 53 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*