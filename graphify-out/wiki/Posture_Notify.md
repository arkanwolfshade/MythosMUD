# Posture Notify

> 40 nodes

## Key Concepts

- **emit_posture_change()** (27 connections) — `server/realtime/posture_notify.py`
- **posture_notify.py** (20 connections) — `server/realtime/posture_notify.py`
- **format_room_posture_message()** (13 connections) — `server/realtime/posture_notify.py`
- **test_posture_notify.py** (12 connections) — `server/tests/unit/realtime/test_posture_notify.py`
- **test_position_commands_helpers.py** (9 connections) — `server/tests/unit/commands/test_position_commands_helpers.py`
- **_PostureConnectionManager** (7 connections) — `server/realtime/posture_notify.py`
- **_send_personal_posture_message()** (4 connections) — `server/realtime/posture_notify.py`
- **UUID** (4 connections)
- **asyncio** (4 connections)
- **_broadcast_room_posture_change()** (3 connections) — `server/realtime/posture_notify.py`
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
- **position_messages.py** (3 connections) — `server/services/position_messages.py`
- **.broadcast_to_room()** (2 connections) — `server/realtime/posture_notify.py`
- **_self_posture_message()** (2 connections) — `server/realtime/posture_notify.py`
- **test_format_room_posture_message_standing_from_lying()** (2 connections) — `server/tests/unit/realtime/test_posture_notify.py`
- *... and 15 more nodes in this community*

## Relationships

- [Player Event Handlers State](Player_Event_Handlers_State.md) (9 shared connections)
- [Test Rest Command](Test_Rest_Command.md) (4 shared connections)
- [Admin Setstat Support](Admin_Setstat_Support.md) (3 shared connections)
- [Test Position Commands](Test_Position_Commands.md) (3 shared connections)
- [Follow Movement](Follow_Movement.md) (3 shared connections)
- [Async Persistence & NPC Events](Async_Persistence_&_NPC_Events.md) (2 shared connections)
- [Test Player Event Handlers Respawn](Test_Player_Event_Handlers_Respawn.md) (1 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (1 shared connections)
- [Test Envelope](Test_Envelope.md) (1 shared connections)
- [Test Player Position Service](Test_Player_Position_Service.md) (1 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)

## Source Files

- `server/realtime/posture_notify.py`
- `server/services/position_messages.py`
- `server/tests/unit/commands/test_position_commands_helpers.py`
- `server/tests/unit/realtime/test_posture_notify.py`

## Audit Trail

- EXTRACTED: 95 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*