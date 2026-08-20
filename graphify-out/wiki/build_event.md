# build_event

> 75 nodes

## Key Concepts

- **build_event()** (111 connections) — `server/realtime/envelope.py`
- **envelope.py** (29 connections) — `server/realtime/envelope.py`
- **test_envelope.py** (29 connections) — `server/tests/unit/realtime/test_envelope.py`
- **websocket_handler_connection.py** (18 connections) — `server/realtime/websocket_handler_connection.py`
- **UUIDEncoder** (8 connections) — `server/realtime/envelope.py`
- **utc_now_z()** (6 connections) — `server/realtime/envelope.py`
- **send_welcome_event()** (6 connections) — `server/realtime/websocket_handler_connection.py`
- **cleanup_websocket_connection()** (5 connections) — `server/realtime/websocket_handler_connection.py`
- **setup_initial_connection_state()** (5 connections) — `server/realtime/websocket_handler_connection.py`
- **UUID** (5 connections)
- **_SupportsEventSequence** (4 connections) — `server/realtime/envelope.py`
- **AsyncPersistenceRoomLookup** (4 connections) — `server/realtime/websocket_handler_connection.py`
- **PlayerDisconnectService** (4 connections) — `server/realtime/websocket_handler_connection.py`
- **.handle_player_dp_decay()** (4 connections) — `server/realtime/player_event_handlers_state.py`
- **test_build_event_json_serializable()** (4 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_build_event_sequence_priority()** (4 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_build_event_with_connection_manager()** (4 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_uuid_encoder_handles_other_types()** (4 connections) — `server/tests/unit/realtime/test_envelope.py`
- **_get_next_global_sequence()** (3 connections) — `server/realtime/envelope.py`
- **test_build_event_all_parameters()** (3 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_build_event_basic()** (3 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_build_event_empty_data()** (3 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_build_event_no_data_parameter()** (3 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_build_event_optional_parameters_none()** (3 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_build_event_timestamp_format()** (3 connections) — `server/tests/unit/realtime/test_envelope.py`
- *... and 50 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (16 shared connections)
- [player_event_handlers.py](player_event_handlers.py.md) (9 shared connections)
- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) (7 shared connections)
- [nats_exceptions.py](nats_exceptions.py.md) (6 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (6 shared connections)
- [admin_teleport_commands.py](admin_teleport_commands.py.md) (4 shared connections)
- [rest_countdown_task.py](rest_countdown_task.py.md) (4 shared connections)
- [send_game_event](send_game_event.md) (4 shared connections)
- [test_message_broadcaster.py](test_message_broadcaster.py.md) (4 shared connections)
- [websocket_handler_commands.py](websocket_handler_commands.py.md) (4 shared connections)
- [test_websocket_room_updates.py](test_websocket_room_updates.py.md) (4 shared connections)
- [ConnectionManager](ConnectionManager.md) (4 shared connections)

## Source Files

- `server/realtime/envelope.py`
- `server/realtime/player_event_handlers_state.py`
- `server/realtime/websocket_handler_connection.py`
- `server/tests/unit/realtime/test_envelope.py`

## Audit Trail

- EXTRACTED: 231 (97%)
- INFERRED: 8 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*