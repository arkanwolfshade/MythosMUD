# benchmark model memory usage()

> 36 nodes

## Key Concepts

- **position_commands.py** (19 connections) — `server/commands/position_commands.py`
- **_handle_position_change()** (11 connections) — `server/commands/position_commands.py`
- **test_position_commands.py** (11 connections) — `server/tests/unit/commands/test_position_commands.py`
- **_format_room_posture_message()** (10 connections) — `server/commands/position_commands.py`
- **handle_stand_command()** (10 connections) — `server/commands/position_commands.py`
- **handle_lie_command()** (10 connections) — `server/commands/position_commands.py`
- **handle_sit_command()** (9 connections) — `server/commands/position_commands.py`
- **test_position_commands_helpers.py** (9 connections) — `server/tests/unit/commands/test_position_commands_helpers.py`
- **Any** (4 connections)
- **test_handle_sit_command()** (3 connections) — `server/tests/unit/commands/test_position_commands.py`
- **test_handle_stand_command()** (3 connections) — `server/tests/unit/commands/test_position_commands.py`
- **test_handle_lie_command()** (3 connections) — `server/tests/unit/commands/test_position_commands.py`
- **test_handle_ground_command()** (3 connections) — `server/tests/unit/commands/test_position_commands.py`
- **test_format_room_posture_message_sitting()** (3 connections) — `server/tests/unit/commands/test_position_commands_helpers.py`
- **test_format_room_posture_message_lying()** (3 connections) — `server/tests/unit/commands/test_position_commands_helpers.py`
- **test_format_room_posture_message_standing_from_lying()** (3 connections) — `server/tests/unit/commands/test_position_commands_helpers.py`
- **test_format_room_posture_message_standing_from_sitting()** (3 connections) — `server/tests/unit/commands/test_position_commands_helpers.py`
- **test_format_room_posture_message_standing_no_previous()** (3 connections) — `server/tests/unit/commands/test_position_commands_helpers.py`
- **test_format_room_posture_message_unknown()** (3 connections) — `server/tests/unit/commands/test_position_commands_helpers.py`
- **Command handlers for posture adjustments within MythosMUD.  According to margina** (1 connections) — `server/commands/position_commands.py`
- **Create a descriptive room message for posture changes.** (1 connections) — `server/commands/position_commands.py`
- **Shared entry point for posture-changing commands.** (1 connections) — `server/commands/position_commands.py`
- **Handle /stand command.** (1 connections) — `server/commands/position_commands.py`
- **Handle /lie command (accepts optional 'down').** (1 connections) — `server/commands/position_commands.py`
- **Unit tests for position command handlers.  Tests the sit, stand, lie, and ground** (1 connections) — `server/tests/unit/commands/test_position_commands.py`
- *... and 11 more nodes in this community*

## Relationships

- [Player Position Service](Player_Position_Service.md) (8 shared connections)
- [Any](Any.md) (6 shared connections)
- [handle global command()](handle_global_command%28%29.md) (4 shared connections)
- [circuit breaker](circuit_breaker.md) (3 shared connections)
- [PlayerPositionService](PlayerPositionService.md) (3 shared connections)
- [main()](main%28%29.md) (3 shared connections)
- [world](world.md) (2 shared connections)
- [Spell Targeting](Spell_Targeting.md) (1 shared connections)

## Source Files

- `server/commands/position_commands.py`
- `server/tests/unit/commands/test_position_commands.py`
- `server/tests/unit/commands/test_position_commands_helpers.py`

## Audit Trail

- EXTRACTED: 136 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*