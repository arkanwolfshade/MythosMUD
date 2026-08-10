# Client Security Utilities

> 123 nodes

## Key Concepts

- **admin_teleport_commands.py** (38 connections) — `server/commands/admin_teleport_commands.py`
- **admin_setlucidity_command.py** (30 connections) — `server/commands/admin_setlucidity_command.py`
- **get_admin_actions_logger()** (25 connections) — `server/structured_logging/admin_actions_logger.py`
- **teleport_helpers.py** (23 connections) — `server/commands/teleport_helpers.py`
- **handle_teleport_command()** (20 connections) — `server/commands/admin_teleport_commands.py`
- **goto_helpers.py** (20 connections) — `server/commands/goto_helpers.py`
- **admin_actions_logger.py** (18 connections) — `server/structured_logging/admin_actions_logger.py`
- **validate_admin_permission()** (13 connections) — `server/commands/admin_permission_utils.py`
- **admin_teleport_utils.py** (13 connections) — `server/commands/admin_teleport_utils.py`
- **create_teleport_effect_message()** (13 connections) — `server/commands/admin_teleport_utils.py`
- **test_admin_commands_helpers.py** (13 connections) — `server/tests/unit/commands/test_admin_commands_helpers.py`
- **Any** (12 connections)
- **_execute_lucidity_change()** (12 connections) — `server/commands/admin_setlucidity_command.py`
- **_handle_admin_set_lucidity_command()** (11 connections) — `server/commands/admin_setlucidity_command.py`
- **broadcast_teleport_effects()** (11 connections) — `server/commands/admin_teleport_utils.py`
- **get_online_player_by_display_name()** (10 connections) — `server/commands/admin_teleport_utils.py`
- **notify_player_of_teleport()** (10 connections) — `server/commands/admin_teleport_utils.py`
- **handle_confirm_teleport_command()** (9 connections) — `server/commands/admin_teleport_commands.py`
- **handle_confirm_goto_command()** (9 connections) — `server/commands/admin_teleport_commands.py`
- **execute_goto_teleport()** (9 connections) — `server/commands/goto_helpers.py`
- **Any** (9 connections)
- **execute_confirm_teleport()** (9 connections) — `server/commands/teleport_helpers.py`
- **admin_permission_utils.py** (8 connections) — `server/commands/admin_permission_utils.py`
- **execute_confirm_goto()** (8 connections) — `server/commands/goto_helpers.py`
- **update_player_room_location()** (8 connections) — `server/commands/teleport_helpers.py`
- *... and 98 more nodes in this community*

## Relationships

- [Client Event Store](Client_Event_Store.md) (31 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (19 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (7 shared connections)
- [NPC Database Sessions](NPC_Database_Sessions.md) (6 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (5 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (4 shared connections)
- [Structured Logging Admin](Structured_Logging_Admin.md) (4 shared connections)
- [Admin Status Commands](Admin_Status_Commands.md) (3 shared connections)
- [Cursor Skills Harden](Cursor_Skills_Harden.md) (1 shared connections)
- [Room Drop Renderer](Room_Drop_Renderer.md) (1 shared connections)
- [Archive Frd Random](Archive_Frd_Random.md) (1 shared connections)
- [Logging Path Utilities](Logging_Path_Utilities.md) (1 shared connections)

## Source Files

- `server/commands/admin_permission_utils.py`
- `server/commands/admin_setlucidity_command.py`
- `server/commands/admin_teleport_commands.py`
- `server/commands/admin_teleport_utils.py`
- `server/commands/goto_helpers.py`
- `server/commands/teleport_helpers.py`
- `server/structured_logging/admin_actions_logger.py`
- `server/tests/unit/commands/test_admin_commands_helpers.py`

## Audit Trail

- EXTRACTED: 599 (99%)
- INFERRED: 8 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*