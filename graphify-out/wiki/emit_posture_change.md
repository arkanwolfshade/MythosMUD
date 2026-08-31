# emit_posture_change

> 64 nodes

## Key Concepts

- **emit_posture_change()** (27 connections) — `server/realtime/posture_notify.py`
- **player_event_handlers_state.py** (26 connections) — `server/realtime/player_event_handlers_state.py`
- **posture_notify.py** (22 connections) — `server/realtime/posture_notify.py`
- **_dispatch_player_dp_updated_payload()** (13 connections) — `server/realtime/player_event_handlers_state.py`
- **format_room_posture_message()** (13 connections) — `server/realtime/posture_notify.py`
- **normalize_posture()** (12 connections) — `server/realtime/posture_notify.py`
- **test_posture_notify.py** (12 connections) — `server/tests/unit/realtime/test_posture_notify.py`
- **test_position_commands_helpers.py** (9 connections) — `server/tests/unit/commands/test_position_commands_helpers.py`
- **_send_player_death_notification()** (8 connections) — `server/realtime/player_event_handlers_state.py`
- **_PostureConnectionManager** (7 connections) — `server/realtime/posture_notify.py`
- **_player_snapshot_for_dp()** (6 connections) — `server/realtime/player_event_handlers_state.py`
- **.handle_player_dp_decay()** (6 connections) — `server/realtime/player_event_handlers_state.py`
- **_send_personal_posture_message()** (5 connections) — `server/realtime/posture_notify.py`
- **_dp_player_update_payload()** (4 connections) — `server/realtime/player_event_handlers_state.py`
- **.handle_player_died()** (4 connections) — `server/realtime/player_event_handlers_state.py`
- **_broadcast_room_posture_change()** (4 connections) — `server/realtime/posture_notify.py`
- **BoundLogger** (4 connections)
- **UUID** (4 connections)
- **asyncio** (4 connections)
- **_dp_posture_from_stats()** (3 connections) — `server/realtime/player_event_handlers_state.py`
- **.send_personal_message()** (3 connections) — `server/realtime/posture_notify.py`
- **test_format_room_posture_message_lying()** (3 connections) — `server/tests/unit/commands/test_position_commands_helpers.py`
- **test_format_room_posture_message_sitting()** (3 connections) — `server/tests/unit/commands/test_position_commands_helpers.py`
- **test_format_room_posture_message_standing_from_lying()** (3 connections) — `server/tests/unit/commands/test_position_commands_helpers.py`
- **test_format_room_posture_message_standing_from_sitting()** (3 connections) — `server/tests/unit/commands/test_position_commands_helpers.py`
- *... and 39 more nodes in this community*

## Relationships

- [player_event_handlers.py](player_event_handlers.py.md) (14 shared connections)
- [build_event](build_event.md) (9 shared connections)
- [admin_setstat_command.py](admin_setstat_command.py.md) (6 shared connections)
- [test_rest_command.py](test_rest_command.py.md) (4 shared connections)
- [event_types.py](event_types.py.md) (4 shared connections)
- [ConnectionManager](ConnectionManager.md) (3 shared connections)
- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (3 shared connections)
- [AliasStorage](AliasStorage.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [test_player_death_service.py](test_player_death_service.py.md) (2 shared connections)
- [coerce_int](coerce_int.md) (2 shared connections)
- [Player](Player.md) (2 shared connections)

## Source Files

- `server/realtime/player_event_handlers_state.py`
- `server/realtime/posture_notify.py`
- `server/services/position_messages.py`
- `server/tests/unit/commands/test_position_commands_helpers.py`
- `server/tests/unit/realtime/test_posture_notify.py`

## Audit Trail

- EXTRACTED: 162 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*