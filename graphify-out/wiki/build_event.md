# build_event

> 56 nodes

## Key Concepts

- **build_event()** (116 connections) — `server/realtime/envelope.py`
- **envelope.py** (32 connections) — `server/realtime/envelope.py`
- **test_envelope.py** (28 connections) — `server/tests/unit/realtime/test_envelope.py`
- **UUIDEncoder** (8 connections) — `server/realtime/envelope.py`
- **utc_now_z()** (6 connections) — `server/realtime/envelope.py`
- **_SupportsEventSequence** (4 connections) — `server/realtime/envelope.py`
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
- **test_build_event_uses_global_sequence_when_no_manager()** (3 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_build_event_with_player_id_string()** (3 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_build_event_with_player_id_uuid()** (3 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_build_event_with_room_id()** (3 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_build_event_with_sequence_number()** (3 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_utc_now_z_format()** (3 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_utc_now_z_is_utc()** (3 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_uuid_encoder_handles_uuid()** (3 connections) — `server/tests/unit/realtime/test_envelope.py`
- *... and 31 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (16 shared connections)
- [PlayerDPUpdated](PlayerDPUpdated.md) (9 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (8 shared connections)
- [NATSRetryHandler](NATSRetryHandler.md) (6 shared connections)
- [ConnectionManager](ConnectionManager.md) (5 shared connections)
- [websocket_room_updates.py](websocket_room_updates.py.md) (5 shared connections)
- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) (5 shared connections)
- [admin_teleport_utils.py](admin_teleport_utils.py.md) (4 shared connections)
- [rest_countdown_task.py](rest_countdown_task.py.md) (4 shared connections)
- [send_game_event](send_game_event.md) (4 shared connections)
- [test_websocket_handler_core.py](test_websocket_handler_core.py.md) (4 shared connections)
- [test_message_broadcaster.py](test_message_broadcaster.py.md) (4 shared connections)

## Source Files

- `server/realtime/envelope.py`
- `server/tests/unit/realtime/test_envelope.py`

## Audit Trail

- EXTRACTED: 203 (98%)
- INFERRED: 5 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*