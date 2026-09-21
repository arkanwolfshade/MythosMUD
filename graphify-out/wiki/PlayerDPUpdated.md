# PlayerDPUpdated

> 81 nodes

## Key Concepts

- **PlayerDPUpdated** (39 connections) — `server/events/event_types.py`
- **player_event_handlers_state.py** (31 connections) — `server/realtime/player_event_handlers_state.py`
- **emit_posture_change()** (27 connections) — `server/realtime/posture_notify.py`
- **posture_notify.py** (22 connections) — `server/realtime/posture_notify.py`
- **_dispatch_player_dp_updated_payload()** (13 connections) — `server/realtime/player_event_handlers_state.py`
- **format_room_posture_message()** (13 connections) — `server/realtime/posture_notify.py`
- **normalize_posture()** (12 connections) — `server/realtime/posture_notify.py`
- **test_posture_notify.py** (11 connections) — `server/tests/unit/realtime/test_posture_notify.py`
- **_dispatch_player_dp_decay_payload()** (9 connections) — `server/realtime/player_event_handlers_state.py`
- **test_position_commands_helpers.py** (9 connections) — `server/tests/unit/commands/test_position_commands_helpers.py`
- **_maybe_attach_decay_posture_cross()** (8 connections) — `server/realtime/player_event_handlers_state.py`
- **_send_player_death_notification()** (8 connections) — `server/realtime/player_event_handlers_state.py`
- **_PostureConnectionManager** (7 connections) — `server/realtime/posture_notify.py`
- **_attach_dp_updated_posture_fields()** (7 connections) — `server/realtime/player_event_handlers_state.py`
- **_player_snapshot_for_dp()** (6 connections) — `server/realtime/player_event_handlers_state.py`
- **ConnectionManager** (6 connections)
- **.__init__()** (5 connections) — `server/realtime/player_event_handlers_state.py`
- **_send_personal_posture_message()** (5 connections) — `server/realtime/posture_notify.py`
- **BoundLogger** (5 connections)
- **_StatsPlayer** (4 connections) — `server/realtime/player_event_handlers_state.py`
- **_decay_previous_position_before_lying()** (4 connections) — `server/realtime/player_event_handlers_state.py`
- **_dp_player_update_payload()** (4 connections) — `server/realtime/player_event_handlers_state.py`
- **.handle_player_dp_updated()** (4 connections) — `server/realtime/player_event_handlers_state.py`
- **_broadcast_room_posture_change()** (4 connections) — `server/realtime/posture_notify.py`
- **UUID** (4 connections)
- *... and 56 more nodes in this community*

## Relationships

- [PlayerStateEventHandler](PlayerStateEventHandler.md) (14 shared connections)
- [build_event](build_event.md) (9 shared connections)
- [get_logger](get_logger.md) (8 shared connections)
- [PlayerEventHandlerUtils](PlayerEventHandlerUtils.md) (6 shared connections)
- [ConnectionManager](ConnectionManager.md) (6 shared connections)
- [admin_setstat_command.py](admin_setstat_command.py.md) (6 shared connections)
- [combat_service.py](combat_service.py.md) (5 shared connections)
- [test_combat_persistence_handler_events.py](test_combat_persistence_handler_events.py.md) (4 shared connections)
- [test_rest_command.py](test_rest_command.py.md) (4 shared connections)
- [Player](Player.md) (4 shared connections)
- [test_magic_healing_events.py](test_magic_healing_events.py.md) (3 shared connections)
- [test_player_event_handlers.py](test_player_event_handlers.py.md) (3 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/realtime/player_event_handlers.py`
- `server/realtime/player_event_handlers_state.py`
- `server/realtime/posture_notify.py`
- `server/services/position_messages.py`
- `server/tests/unit/commands/test_position_commands_helpers.py`
- `server/tests/unit/realtime/test_posture_notify.py`

## Audit Trail

- EXTRACTED: 209 (93%)
- INFERRED: 16 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*