# character creation service

> 38 nodes

## Key Concepts

- **command_service.py** (95 connections) — `server/commands/command_service.py`
- **__init__.py** (29 connections) — `server/commands/__init__.py`
- **position_commands.py** (19 connections) — `server/commands/position_commands.py`
- **_handle_position_change()** (11 connections) — `server/commands/position_commands.py`
- **test_position_commands.py** (11 connections) — `server/tests/unit/commands/test_position_commands.py`
- **_format_room_posture_message()** (10 connections) — `server/commands/position_commands.py`
- **handle_stand_command()** (9 connections) — `server/commands/position_commands.py`
- **handle_lie_command()** (9 connections) — `server/commands/position_commands.py`
- **test_position_commands_helpers.py** (9 connections) — `server/tests/unit/commands/test_position_commands_helpers.py`
- **handle_sit_command()** (8 connections) — `server/commands/position_commands.py`
- **Any** (4 connections)
- **test_handle_sit_command()** (3 connections) — `server/tests/unit/commands/test_position_commands.py`
- **test_handle_stand_command()** (3 connections) — `server/tests/unit/commands/test_position_commands.py`
- **test_handle_lie_command()** (3 connections) — `server/tests/unit/commands/test_position_commands.py`
- **test_format_room_posture_message_sitting()** (3 connections) — `server/tests/unit/commands/test_position_commands_helpers.py`
- **test_format_room_posture_message_lying()** (3 connections) — `server/tests/unit/commands/test_position_commands_helpers.py`
- **test_format_room_posture_message_standing_from_lying()** (3 connections) — `server/tests/unit/commands/test_position_commands_helpers.py`
- **test_format_room_posture_message_standing_from_sitting()** (3 connections) — `server/tests/unit/commands/test_position_commands_helpers.py`
- **test_format_room_posture_message_standing_no_previous()** (3 connections) — `server/tests/unit/commands/test_position_commands_helpers.py`
- **test_format_room_posture_message_unknown()** (3 connections) — `server/tests/unit/commands/test_position_commands_helpers.py`
- **Command processing system for MythosMUD.  This package provides the command proc** (1 connections) — `server/commands/__init__.py`
- **Command service for MythosMUD.  This module provides the main command processing** (1 connections) — `server/commands/command_service.py`
- **Command handlers for posture adjustments within MythosMUD.  According to margina** (1 connections) — `server/commands/position_commands.py`
- **Create a descriptive room message for posture changes.** (1 connections) — `server/commands/position_commands.py`
- **Shared entry point for posture-changing commands.** (1 connections) — `server/commands/position_commands.py`
- *... and 13 more nodes in this community*

## Relationships

- [commands admin mute](commands_admin_mute.md) (10 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (9 shared connections)
- [realtime real time](realtime_real_time.md) (8 shared connections)
- [commands npc admin](commands_npc_admin.md) (8 shared connections)
- [command factories create](command_factories_create.md) (7 shared connections)
- [character creation service](character_creation_service.md) (6 shared connections)
- [zone configuration npc](zone_configuration_npc.md) (6 shared connections)
- [commands magic rationale](commands_magic_rationale.md) (6 shared connections)
- [eventLog projectorRoom roomMergeUtils](eventLog_projectorRoom_roomMergeUtils.md) (4 shared connections)
- [shutdown command commands](shutdown_command_commands.md) (4 shared connections)
- [mythosApp appLazyScreens mythosAppViewMo](mythosApp_appLazyScreens_mythosAppViewMo.md) (4 shared connections)
- [message broadcast realtime](message_broadcast_realtime.md) (3 shared connections)

## Source Files

- `server/commands/__init__.py`
- `server/commands/command_service.py`
- `server/commands/position_commands.py`
- `server/tests/unit/commands/test_position_commands.py`
- `server/tests/unit/commands/test_position_commands_helpers.py`

## Audit Trail

- EXTRACTED: 258 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*