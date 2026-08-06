# realtime websocket initial

> 77 nodes

## Key Concepts

- **test_websocket_initial_state.py** (45 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **send_initial_room_state()** (19 connections) — `server/realtime/websocket_initial_state.py`
- **check_and_send_death_notification()** (14 connections) — `server/realtime/websocket_initial_state.py`
- **send_game_state_event_safely()** (10 connections) — `server/realtime/websocket_initial_state.py`
- **get_event_handler_for_initial_state()** (9 connections) — `server/realtime/websocket_initial_state.py`
- **add_npc_occupants_to_list()** (8 connections) — `server/realtime/websocket_initial_state.py`
- **send_occupants_snapshot_if_needed()** (8 connections) — `server/realtime/websocket_initial_state.py`
- **UUID** (6 connections)
- **WebSocket** (5 connections)
- **_get_player_for_death_check()** (5 connections) — `server/realtime/websocket_initial_state.py`
- **prepare_initial_room_data()** (5 connections) — `server/realtime/websocket_initial_state.py`
- **_get_death_location_name()** (4 connections) — `server/realtime/websocket_initial_state.py`
- **mock_connection_manager()** (4 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_send_initial_game_state_success()** (4 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_check_and_send_death_notification_player_dead()** (4 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_check_and_send_death_notification_player_alive()** (4 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_check_and_send_death_notification_in_limbo()** (4 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **_passthrough_room_data()** (3 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_prepare_room_data_with_occupants()** (3 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_send_game_state_event_safely_success()** (3 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_send_game_state_event_safely_disconnected()** (3 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_send_game_state_event_safely_close_message_sent()** (3 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_send_initial_game_state_player_not_found()** (3 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_send_initial_game_state_handles_exception()** (3 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_add_npc_occupants_to_list_success()** (3 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- *... and 52 more nodes in this community*

## Relationships

- [realtime maintenance connection](realtime_maintenance_connection.md) (24 shared connections)
- [game weapon player](game_weapon_player.md) (5 shared connections)
- [Room Broadcast](Room_Broadcast.md) (3 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (2 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (2 shared connections)
- [occupant formatter realtime](occupant_formatter_realtime.md) (2 shared connections)
- [player room realtime](player_room_realtime.md) (2 shared connections)
- [room models instance](room_models_instance.md) (2 shared connections)
- [Error Conversion](Error_Conversion.md) (1 shared connections)

## Source Files

- `server/realtime/websocket_initial_state.py`
- `server/tests/unit/realtime/test_websocket_initial_state.py`

## Audit Trail

- EXTRACTED: 254 (97%)
- INFERRED: 7 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*