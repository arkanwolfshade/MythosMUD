# build_event

> 123 nodes

## Key Concepts

- **build_event()** (123 connections) — `server/realtime/envelope.py`
- **envelope.py** (35 connections) — `server/realtime/envelope.py`
- **test_envelope.py** (33 connections) — `server/tests/unit/realtime/test_envelope.py`
- **emit_posture_change()** (31 connections) — `server/realtime/posture_notify.py`
- **posture_notify.py** (27 connections) — `server/realtime/posture_notify.py`
- **rest_countdown_task.py** (18 connections) — `server/commands/rest_countdown_task.py`
- **test_posture_notify.py** (16 connections) — `server/tests/unit/realtime/test_posture_notify.py`
- **format_room_posture_message()** (13 connections) — `server/realtime/posture_notify.py`
- **attach_posture_self_message()** (12 connections) — `server/realtime/posture_notify.py`
- **create_rest_countdown_task()** (9 connections) — `server/commands/rest_countdown_task.py`
- **test_position_commands_helpers.py** (9 connections) — `server/tests/unit/commands/test_position_commands_helpers.py`
- **UUIDEncoder** (8 connections) — `server/realtime/envelope.py`
- **_PostureConnectionManager** (7 connections) — `server/realtime/posture_notify.py`
- **_handle_countdown_loop()** (7 connections) — `server/commands/rest_countdown_task.py`
- **_send_countdown_message()** (6 connections) — `server/commands/rest_countdown_task.py`
- **utc_now_z()** (6 connections) — `server/realtime/envelope.py`
- **_send_personal_posture_message()** (6 connections) — `server/realtime/posture_notify.py`
- **UUID** (6 connections)
- **_disconnect_player_after_rest()** (5 connections) — `server/commands/rest_countdown_task.py`
- **_is_rest_interrupted()** (5 connections) — `server/commands/rest_countdown_task.py`
- **Any** (5 connections)
- **_SupportsEventSequence** (4 connections) — `server/realtime/envelope.py`
- **_broadcast_room_posture_change()** (4 connections) — `server/realtime/posture_notify.py`
- **test_build_event_defaults_command_response_to_command_output()** (4 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_build_event_json_serializable()** (4 connections) — `server/tests/unit/realtime/test_envelope.py`
- *... and 98 more nodes in this community*

## Relationships

- [MessageCategory](MessageCategory.md) (16 shared connections)
- [admin_setstat_command.py](admin_setstat_command.py.md) (13 shared connections)
- [PlayerDPUpdated](PlayerDPUpdated.md) (13 shared connections)
- [get_logger](get_logger.md) (10 shared connections)
- [test_rest_command.py](test_rest_command.py.md) (9 shared connections)
- [AttributeError](AttributeError.md) (9 shared connections)
- [websocket_initial_state.py](websocket_initial_state.py.md) (8 shared connections)
- [alias_storage.py](alias_storage.py.md) (7 shared connections)
- [PlayerRespawnEventHandler](PlayerRespawnEventHandler.md) (7 shared connections)
- [test_message_category_invariants.py](test_message_category_invariants.py.md) (6 shared connections)
- [FollowService](FollowService.md) (5 shared connections)
- [test_container_websocket_events.py](test_container_websocket_events.py.md) (5 shared connections)

## Source Files

- `server/commands/rest_countdown_task.py`
- `server/realtime/envelope.py`
- `server/realtime/posture_notify.py`
- `server/services/position_messages.py`
- `server/tests/unit/commands/test_position_commands_helpers.py`
- `server/tests/unit/realtime/test_envelope.py`
- `server/tests/unit/realtime/test_posture_notify.py`

## Audit Trail

- EXTRACTED: 378 (98%)
- INFERRED: 9 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*