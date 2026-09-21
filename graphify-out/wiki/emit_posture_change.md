# emit_posture_change

> 31 nodes

## Key Concepts

- **emit_posture_change()** (27 connections) — `server/realtime/posture_notify.py`
- **format_room_posture_message()** (13 connections) — `server/realtime/posture_notify.py`
- **normalize_posture()** (12 connections) — `server/realtime/posture_notify.py`
- **test_posture_notify.py** (11 connections) — `server/tests/unit/realtime/test_posture_notify.py`
- **test_position_commands_helpers.py** (9 connections) — `server/tests/unit/commands/test_position_commands_helpers.py`
- **asyncio** (4 connections)
- **test_format_room_posture_message_lying()** (3 connections) — `server/tests/unit/commands/test_position_commands_helpers.py`
- **test_format_room_posture_message_sitting()** (3 connections) — `server/tests/unit/commands/test_position_commands_helpers.py`
- **test_format_room_posture_message_standing_from_lying()** (3 connections) — `server/tests/unit/commands/test_position_commands_helpers.py`
- **test_format_room_posture_message_standing_from_sitting()** (3 connections) — `server/tests/unit/commands/test_position_commands_helpers.py`
- **test_format_room_posture_message_standing_no_previous()** (3 connections) — `server/tests/unit/commands/test_position_commands_helpers.py`
- **test_format_room_posture_message_unknown()** (3 connections) — `server/tests/unit/commands/test_position_commands_helpers.py`
- **test_emit_posture_change_attach_only_returns_message()** (3 connections) — `server/tests/unit/realtime/test_posture_notify.py`
- **test_emit_posture_change_broadcasts_room_and_sends_personal()** (3 connections) — `server/tests/unit/realtime/test_posture_notify.py`
- **test_emit_posture_change_no_op_when_unchanged()** (3 connections) — `server/tests/unit/realtime/test_posture_notify.py`
- **test_emit_posture_change_room_only_skips_personal()** (3 connections) — `server/tests/unit/realtime/test_posture_notify.py`
- **test_normalize_posture_enum_value()** (3 connections) — `server/tests/unit/realtime/test_posture_notify.py`
- **_self_posture_message()** (2 connections) — `server/realtime/posture_notify.py`
- **test_format_room_posture_message_standing_from_lying()** (2 connections) — `server/tests/unit/realtime/test_posture_notify.py`
- **Notify room (and optionally self) when posture actually changed. Returns the…** (1 connections) — `server/realtime/posture_notify.py`
- **Normalize posture from stats JSON or enum to lowercase string.** (1 connections) — `server/realtime/posture_notify.py`
- **Create a descriptive room message for posture changes.** (1 connections) — `server/realtime/posture_notify.py`
- **Unit tests for position command helper functions. Tests helper functions in…** (1 connections) — `server/tests/unit/commands/test_position_commands_helpers.py`
- **Test _format_room_posture_message() formats sitting message.** (1 connections) — `server/tests/unit/commands/test_position_commands_helpers.py`
- **Test _format_room_posture_message() formats lying message.** (1 connections) — `server/tests/unit/commands/test_position_commands_helpers.py`
- *... and 6 more nodes in this community*

## Relationships

- [PlayerDPUpdated](PlayerDPUpdated.md) (6 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [admin_setstat_command.py](admin_setstat_command.py.md) (5 shared connections)
- [test_rest_command.py](test_rest_command.py.md) (3 shared connections)
- [_PostureConnectionManager](_PostureConnectionManager.md) (3 shared connections)
- [command_service.py](command_service.py.md) (2 shared connections)
- [follow_service.py](follow_service.py.md) (2 shared connections)
- [PlayerRespawnEventHandler](PlayerRespawnEventHandler.md) (1 shared connections)
- [event_types.py](event_types.py.md) (1 shared connections)

## Source Files

- `server/realtime/posture_notify.py`
- `server/tests/unit/commands/test_position_commands_helpers.py`
- `server/tests/unit/realtime/test_posture_notify.py`

## Audit Trail

- EXTRACTED: 77 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*