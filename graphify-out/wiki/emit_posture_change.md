# emit_posture_change

> 45 nodes

## Key Concepts

- **emit_posture_change()** (27 connections) — `server/realtime/posture_notify.py`
- **posture_notify.py** (22 connections) — `server/realtime/posture_notify.py`
- **format_room_posture_message()** (13 connections) — `server/realtime/posture_notify.py`
- **normalize_posture()** (12 connections) — `server/realtime/posture_notify.py`
- **test_posture_notify.py** (11 connections) — `server/tests/unit/realtime/test_posture_notify.py`
- **test_position_commands_helpers.py** (9 connections) — `server/tests/unit/commands/test_position_commands_helpers.py`
- **_PostureConnectionManager** (7 connections) — `server/realtime/posture_notify.py`
- **_send_personal_posture_message()** (5 connections) — `server/realtime/posture_notify.py`
- **_broadcast_room_posture_change()** (4 connections) — `server/realtime/posture_notify.py`
- **UUID** (4 connections)
- **asyncio** (4 connections)
- **.send_personal_message()** (3 connections) — `server/realtime/posture_notify.py`
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
- **position_messages.py** (3 connections) — `server/services/position_messages.py`
- **.broadcast_to_room()** (2 connections) — `server/realtime/posture_notify.py`
- *... and 20 more nodes in this community*

## Relationships

- [PlayerDPUpdated](PlayerDPUpdated.md) (7 shared connections)
- [admin_setstat_command.py](admin_setstat_command.py.md) (6 shared connections)
- [build_event](build_event.md) (4 shared connections)
- [test_rest_command.py](test_rest_command.py.md) (4 shared connections)
- [command_service.py](command_service.py.md) (3 shared connections)
- [follow_movement.py](follow_movement.py.md) (3 shared connections)
- [PlayerRespawnEventHandler](PlayerRespawnEventHandler.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [PlayerPositionService](PlayerPositionService.md) (1 shared connections)

## Source Files

- `server/realtime/posture_notify.py`
- `server/services/position_messages.py`
- `server/tests/unit/commands/test_position_commands_helpers.py`
- `server/tests/unit/realtime/test_posture_notify.py`

## Audit Trail

- EXTRACTED: 107 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*