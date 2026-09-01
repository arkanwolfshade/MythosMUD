# build_event

> 155 nodes

## Key Concepts

- **build_event()** (112 connections) — `server/realtime/envelope.py`
- **player_event_handlers_state.py** (31 connections) — `server/realtime/player_event_handlers_state.py`
- **envelope.py** (29 connections) — `server/realtime/envelope.py`
- **test_envelope.py** (29 connections) — `server/tests/unit/realtime/test_envelope.py`
- **emit_posture_change()** (27 connections) — `server/realtime/posture_notify.py`
- **posture_notify.py** (22 connections) — `server/realtime/posture_notify.py`
- **websocket_handler_connection.py** (19 connections) — `server/realtime/websocket_handler_connection.py`
- **_dispatch_player_dp_updated_payload()** (13 connections) — `server/realtime/player_event_handlers_state.py`
- **format_room_posture_message()** (13 connections) — `server/realtime/posture_notify.py`
- **test_posture_notify.py** (12 connections) — `server/tests/unit/realtime/test_posture_notify.py`
- **_dispatch_player_dp_decay_payload()** (9 connections) — `server/realtime/player_event_handlers_state.py`
- **test_position_commands_helpers.py** (9 connections) — `server/tests/unit/commands/test_position_commands_helpers.py`
- **UUIDEncoder** (8 connections) — `server/realtime/envelope.py`
- **_maybe_attach_decay_posture_cross()** (8 connections) — `server/realtime/player_event_handlers_state.py`
- **_send_player_death_notification()** (8 connections) — `server/realtime/player_event_handlers_state.py`
- **_PostureConnectionManager** (7 connections) — `server/realtime/posture_notify.py`
- **_attach_dp_updated_posture_fields()** (7 connections) — `server/realtime/player_event_handlers_state.py`
- **utc_now_z()** (6 connections) — `server/realtime/envelope.py`
- **_player_snapshot_for_dp()** (6 connections) — `server/realtime/player_event_handlers_state.py`
- **send_welcome_event()** (6 connections) — `server/realtime/websocket_handler_connection.py`
- **ConnectionManager** (6 connections)
- **.__init__()** (5 connections) — `server/realtime/player_event_handlers_state.py`
- **_send_personal_posture_message()** (5 connections) — `server/realtime/posture_notify.py`
- **cleanup_websocket_connection()** (5 connections) — `server/realtime/websocket_handler_connection.py`
- **setup_initial_connection_state()** (5 connections) — `server/realtime/websocket_handler_connection.py`
- *... and 130 more nodes in this community*

## Relationships

- [event_types.py](event_types.py.md) (17 shared connections)
- [PlayerRespawnEventHandler](PlayerRespawnEventHandler.md) (16 shared connections)
- [admin_setstat_command.py](admin_setstat_command.py.md) (14 shared connections)
- [CombatMessagingService](CombatMessagingService.md) (10 shared connections)
- [ConnectionManager](ConnectionManager.md) (10 shared connections)
- [get_logger](get_logger.md) (7 shared connections)
- [FollowService](FollowService.md) (6 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (6 shared connections)
- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) (5 shared connections)
- [admin_teleport_commands.py](admin_teleport_commands.py.md) (4 shared connections)
- [rest_countdown_task.py](rest_countdown_task.py.md) (4 shared connections)
- [test_message_broadcaster.py](test_message_broadcaster.py.md) (4 shared connections)

## Source Files

- `server/realtime/envelope.py`
- `server/realtime/player_event_handlers_state.py`
- `server/realtime/posture_notify.py`
- `server/realtime/websocket_handler_connection.py`
- `server/services/position_messages.py`
- `server/tests/unit/commands/test_position_commands_helpers.py`
- `server/tests/unit/realtime/test_envelope.py`
- `server/tests/unit/realtime/test_posture_notify.py`

## Audit Trail

- EXTRACTED: 411 (97%)
- INFERRED: 13 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*