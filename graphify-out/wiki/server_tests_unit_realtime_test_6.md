# server tests unit realtime test

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

- [server tests unit realtime test](server_tests_unit_realtime_test.md) (33 shared connections)

## Source Files

- `server/tests/unit/realtime/test_player_event_handlers_room.py`

## Audit Trail

- EXTRACTED: 43 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*