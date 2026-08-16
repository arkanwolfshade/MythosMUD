# test_websocket_helpers.py

> 113 nodes

## Key Concepts

- **test_websocket_helpers.py** (42 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **websocket_helpers.py** (39 connections) — `server/realtime/websocket_helpers.py`
- **test_websocket_helpers_player.py** (24 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- **get_player_and_room()** (14 connections) — `server/realtime/websocket_helpers.py`
- **validate_occupant_name()** (14 connections) — `server/realtime/websocket_helpers.py`
- **prepare_player_data()** (12 connections) — `server/realtime/websocket_helpers.py`
- **convert_uuids_to_strings()** (11 connections) — `server/realtime/websocket_helpers.py`
- **is_websocket_disconnect_message()** (11 connections) — `server/realtime/websocket_helpers.py`
- **get_player_stats_data()** (9 connections) — `server/realtime/websocket_helpers.py`
- **is_client_disconnected_exception()** (9 connections) — `server/realtime/websocket_helpers.py`
- **handle_websocket_runtime_error()** (8 connections) — `server/realtime/websocket_handler_message_loop.py`
- **get_player_service_from_connection_manager()** (8 connections) — `server/realtime/websocket_helpers.py`
- **send_websocket_error_response()** (7 connections) — `server/realtime/websocket_handler_message_loop.py`
- **build_basic_player_data()** (7 connections) — `server/realtime/websocket_helpers.py`
- **convert_schema_to_dict()** (7 connections) — `server/realtime/websocket_helpers.py`
- **asyncio** (7 connections)
- **_ensure_player_in_room_occupancy()** (6 connections) — `server/realtime/websocket_helpers.py`
- **UUID** (6 connections)
- **_accumulate_valid_occupant_name()** (4 connections) — `server/realtime/websocket_helpers.py`
- **_get_tracked_player_from_connection_manager()** (4 connections) — `server/realtime/websocket_helpers.py`
- **test_get_player_and_room_adds_player_to_room()** (4 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- **test_get_player_and_room_player_not_found()** (4 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- **test_get_player_and_room_room_not_found()** (4 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- **test_get_player_and_room_success()** (4 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- **test_prepare_player_data_no_service()** (4 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- *... and 88 more nodes in this community*

## Relationships

- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) (13 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (12 shared connections)
- [check_shutdown_and_reject](check_shutdown_and_reject.md) (12 shared connections)
- [build_event](build_event.md) (10 shared connections)
- [websocket_handler_commands.py](websocket_handler_commands.py.md) (3 shared connections)
- [PersonalMessageSender](PersonalMessageSender.md) (3 shared connections)
- [ErrorType](ErrorType.md) (2 shared connections)
- [Room](Room.md) (2 shared connections)
- [test_async_persistence_delegates.py](test_async_persistence_delegates.py.md) (2 shared connections)
- [player_event_handlers_respawn.py](player_event_handlers_respawn.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [Player](Player.md) (2 shared connections)

## Source Files

- `server/realtime/websocket_handler_message_loop.py`
- `server/realtime/websocket_helpers.py`
- `server/tests/unit/realtime/test_websocket_helpers.py`
- `server/tests/unit/realtime/test_websocket_helpers_player.py`

## Audit Trail

- EXTRACTED: 239 (96%)
- INFERRED: 10 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*