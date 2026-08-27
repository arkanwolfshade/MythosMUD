# lint_sql_guardrails.py

> 15 nodes

## Key Concepts

- **_format_room_posture_message()** (10 connections) — `server/commands/position_commands.py`
- **test_position_commands_helpers.py** (9 connections) — `server/tests/unit/commands/test_position_commands_helpers.py`
- **test_format_room_posture_message_lying()** (3 connections) — `server/tests/unit/commands/test_position_commands_helpers.py`
- **test_format_room_posture_message_sitting()** (3 connections) — `server/tests/unit/commands/test_position_commands_helpers.py`
- **test_format_room_posture_message_standing_from_lying()** (3 connections) — `server/tests/unit/commands/test_position_commands_helpers.py`
- **test_format_room_posture_message_standing_from_sitting()** (3 connections) — `server/tests/unit/commands/test_position_commands_helpers.py`
- **test_format_room_posture_message_standing_no_previous()** (3 connections) — `server/tests/unit/commands/test_position_commands_helpers.py`
- **test_format_room_posture_message_unknown()** (3 connections) — `server/tests/unit/commands/test_position_commands_helpers.py`
- **Test _format_room_posture_message() formats sitting message.** (2 connections) — `server/tests/unit/commands/test_position_commands_helpers.py`
- **Create a descriptive room message for posture changes.** (1 connections) — `server/commands/position_commands.py`
- **Unit tests for position command helper functions. Tests helper functions in…** (1 connections) — `server/tests/unit/commands/test_position_commands_helpers.py`
- **Test _format_room_posture_message() formats lying message.** (1 connections) — `server/tests/unit/commands/test_position_commands_helpers.py`
- **Test _format_room_posture_message() formats standing from lying message.** (1 connections) — `server/tests/unit/commands/test_position_commands_helpers.py`
- **Test _format_room_posture_message() formats standing with no previous position.** (1 connections) — `server/tests/unit/commands/test_position_commands_helpers.py`
- **Test _format_room_posture_message() handles unknown position.** (1 connections) — `server/tests/unit/commands/test_position_commands_helpers.py`

## Relationships

- [generate_invites_db.py](generate_invites_db.py.md) (2 shared connections)
- [test_combat_integration_base.py](test_combat_integration_base.py.md) (1 shared connections)

## Source Files

- `server/commands/position_commands.py`
- `server/tests/unit/commands/test_position_commands_helpers.py`

## Audit Trail

- EXTRACTED: 24 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*