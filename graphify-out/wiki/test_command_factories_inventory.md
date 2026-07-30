# test command factories inventory

> 117 nodes

## Key Concepts

- **admin_teleport_commands.py** (38 connections) — `server/commands/admin_teleport_commands.py`
- **admin_commands.py** (33 connections) — `server/commands/admin_commands.py`
- **admin_setstat_command.py** (28 connections) — `server/commands/admin_setstat_command.py`
- **get_admin_actions_logger()** (25 connections) — `server/structured_logging/admin_actions_logger.py`
- **teleport_helpers.py** (23 connections) — `server/commands/teleport_helpers.py`
- **handle_teleport_command()** (20 connections) — `server/commands/admin_teleport_commands.py`
- **goto_helpers.py** (20 connections) — `server/commands/goto_helpers.py`
- **handle_goto_command()** (15 connections) — `server/commands/admin_teleport_commands.py`
- **admin_actions_logger.py** (15 connections) — `server/structured_logging/admin_actions_logger.py`
- **validate_admin_permission()** (13 connections) — `server/commands/admin_permission_utils.py`
- **admin_teleport_utils.py** (13 connections) — `server/commands/admin_teleport_utils.py`
- **create_teleport_effect_message()** (13 connections) — `server/commands/admin_teleport_utils.py`
- **test_admin_commands_helpers.py** (13 connections) — `server/tests/unit/commands/test_admin_commands_helpers.py`
- **broadcast_teleport_effects()** (11 connections) — `server/commands/admin_teleport_utils.py`
- **get_online_player_by_display_name()** (10 connections) — `server/commands/admin_teleport_utils.py`
- **notify_player_of_teleport()** (10 connections) — `server/commands/admin_teleport_utils.py`
- **handle_confirm_teleport_command()** (9 connections) — `server/commands/admin_teleport_commands.py`
- **handle_confirm_goto_command()** (9 connections) — `server/commands/admin_teleport_commands.py`
- **execute_goto_teleport()** (9 connections) — `server/commands/goto_helpers.py`
- **Any** (9 connections)
- **execute_confirm_teleport()** (9 connections) — `server/commands/teleport_helpers.py`
- **admin_permission_utils.py** (8 connections) — `server/commands/admin_permission_utils.py`
- **_apply_stat_change_and_build_result()** (8 connections) — `server/commands/admin_setstat_command.py`
- **execute_confirm_goto()** (8 connections) — `server/commands/goto_helpers.py`
- **update_player_room_location()** (8 connections) — `server/commands/teleport_helpers.py`
- *... and 92 more nodes in this community*

## Relationships

- [Player Position Service](Player_Position_Service.md) (21 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (16 shared connections)
- [admin setstat command](admin_setstat_command.md) (14 shared connections)
- [real time](real_time.md) (10 shared connections)
- [DropResolved](DropResolved.md) (10 shared connections)
- [test magic commands](test_magic_commands.md) (7 shared connections)
- [Any](Any.md) (7 shared connections)
- [admin setlucidity command](admin_setlucidity_command.md) (6 shared connections)
- [AuthSlice](AuthSlice.md) (3 shared connections)
- [get health status()](get_health_status%28%29.md) (2 shared connections)
- [AdminActionsLogger](AdminActionsLogger.md) (2 shared connections)
- [websocket handler app state](websocket_handler_app_state.md) (1 shared connections)

## Source Files

- `server/commands/admin_commands.py`
- `server/commands/admin_permission_utils.py`
- `server/commands/admin_setstat_command.py`
- `server/commands/admin_teleport_commands.py`
- `server/commands/admin_teleport_utils.py`
- `server/commands/goto_helpers.py`
- `server/commands/teleport_helpers.py`
- `server/structured_logging/admin_actions_logger.py`
- `server/tests/unit/commands/test_admin_commands_helpers.py`

## Audit Trail

- EXTRACTED: 589 (99%)
- INFERRED: 6 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*