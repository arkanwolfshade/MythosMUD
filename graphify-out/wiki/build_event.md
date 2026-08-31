# build_event

> 71 nodes

## Key Concepts

- **build_event()** (112 connections) — `server/realtime/envelope.py`
- **envelope.py** (29 connections) — `server/realtime/envelope.py`
- **test_envelope.py** (29 connections) — `server/tests/unit/realtime/test_envelope.py`
- **rest_countdown_task.py** (13 connections) — `server/commands/rest_countdown_task.py`
- **UUIDEncoder** (8 connections) — `server/realtime/envelope.py`
- **create_rest_countdown_task()** (7 connections) — `server/commands/rest_countdown_task.py`
- **_handle_countdown_loop()** (6 connections) — `server/commands/rest_countdown_task.py`
- **_send_countdown_message()** (6 connections) — `server/commands/rest_countdown_task.py`
- **utc_now_z()** (6 connections) — `server/realtime/envelope.py`
- **UUID** (6 connections)
- **_disconnect_player_after_rest()** (5 connections) — `server/commands/rest_countdown_task.py`
- **_is_rest_interrupted()** (5 connections) — `server/commands/rest_countdown_task.py`
- **Any** (5 connections)
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
- *... and 46 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (19 shared connections)
- [combat_messaging/base.py](combat_messaging-base.py.md) (10 shared connections)
- [player_event_handlers_state.py](player_event_handlers_state.py.md) (9 shared connections)
- [ConnectionManager](ConnectionManager.md) (5 shared connections)
- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) (5 shared connections)
- [admin_teleport_commands.py](admin_teleport_commands.py.md) (4 shared connections)
- [MessageBroadcaster](MessageBroadcaster.md) (4 shared connections)
- [websocket_handler_commands.py](websocket_handler_commands.py.md) (4 shared connections)
- [test_websocket_room_updates.py](test_websocket_room_updates.py.md) (4 shared connections)
- [test_rest_command.py](test_rest_command.py.md) (3 shared connections)
- [admin_setstat_command.py](admin_setstat_command.py.md) (3 shared connections)
- [admin_summon_command.py](admin_summon_command.py.md) (3 shared connections)

## Source Files

- `server/commands/rest_countdown_task.py`
- `server/realtime/envelope.py`
- `server/tests/unit/realtime/test_envelope.py`

## Audit Trail

- EXTRACTED: 228 (98%)
- INFERRED: 5 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*