# command_service.py

> 102 nodes

## Key Concepts

- **command_service.py** (110 connections) — `server/commands/command_service.py`
- **server/commands/__init__.py** (29 connections) — `server/commands/__init__.py`
- **test_communication_commands_say_me_pose.py** (22 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **position_commands.py** (20 connections) — `server/commands/position_commands.py`
- **handle_say_command()** (16 connections) — `server/commands/communication_commands.py`
- **asyncio** (15 connections)
- **handle_pose_command()** (14 connections) — `server/commands/communication_commands.py`
- **system_commands.py** (13 connections) — `server/commands/system_commands.py`
- **test_position_commands.py** (12 connections) — `server/tests/unit/commands/test_position_commands.py`
- **_handle_position_change()** (11 connections) — `server/commands/position_commands.py`
- **handle_help_command()** (11 connections) — `server/commands/system_commands.py`
- **handle_stand_command()** (10 connections) — `server/commands/position_commands.py`
- **handle_lie_command()** (9 connections) — `server/commands/position_commands.py`
- **handle_system_command()** (9 connections) — `server/commands/system_commands.py`
- **SupportsPlayerPersistence** (8 connections) — `server/services/player_position_service.py`
- **handle_sit_command()** (8 connections) — `server/commands/position_commands.py`
- **SupportsConnectionManager** (7 connections) — `server/services/player_position_service.py`
- **handle_me_command()** (7 connections) — `server/commands/communication_commands.py`
- **_get_position_command_services()** (7 connections) — `server/commands/position_commands.py`
- **test_system_commands.py** (6 connections) — `server/tests/unit/commands/test_system_commands.py`
- **test_handle_pose_command_clear_pose()** (5 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_handle_pose_command_player_not_found()** (5 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_handle_pose_command_set_pose()** (5 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_handle_say_command_chat_service_failure()** (5 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **test_handle_say_command_delegates_broadcast_to_chat_service_with_ids()** (5 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- *... and 77 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (18 shared connections)
- [request_with_app_container](request_with_app_container.md) (14 shared connections)
- [AliasStorage](AliasStorage.md) (13 shared connections)
- [test_communication_commands_flows.py](test_communication_commands_flows.py.md) (13 shared connections)
- [PlayerPositionService](PlayerPositionService.md) (10 shared connections)
- [test_admin_commands.py](test_admin_commands.py.md) (10 shared connections)
- [test_alias_commands.py](test_alias_commands.py.md) (8 shared connections)
- [rescue_commands.py](rescue_commands.py.md) (7 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (6 shared connections)
- [test_magic_commands.py](test_magic_commands.py.md) (6 shared connections)
- [TargetResolutionResult](TargetResolutionResult.md) (5 shared connections)
- [admin_shutdown_command.py](admin_shutdown_command.py.md) (4 shared connections)

## Source Files

- `server/commands/__init__.py`
- `server/commands/command_service.py`
- `server/commands/communication_commands.py`
- `server/commands/help_commands.py`
- `server/commands/position_commands.py`
- `server/commands/system_commands.py`
- `server/services/player_position_service.py`
- `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- `server/tests/unit/commands/test_help_commands.py`
- `server/tests/unit/commands/test_position_commands.py`
- `server/tests/unit/commands/test_system_commands.py`

## Audit Trail

- EXTRACTED: 291 (81%)
- INFERRED: 69 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*