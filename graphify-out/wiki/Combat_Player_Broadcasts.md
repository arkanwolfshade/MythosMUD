# Combat Player Broadcasts

> 94 nodes · cohesion 0.05

## Key Concepts

- **admin_teleport_commands.py** (38 connections) — `server/commands/admin_teleport_commands.py`
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
- **handle_confirm_goto_command()** (9 connections) — `server/commands/admin_teleport_commands.py`
- **handle_confirm_teleport_command()** (9 connections) — `server/commands/admin_teleport_commands.py`
- **execute_goto_teleport()** (9 connections) — `server/commands/goto_helpers.py`
- **execute_confirm_teleport()** (9 connections) — `server/commands/teleport_helpers.py`
- **Any** (9 connections)
- **admin_permission_utils.py** (8 connections) — `server/commands/admin_permission_utils.py`
- **execute_confirm_goto()** (8 connections) — `server/commands/goto_helpers.py`
- **update_player_room_location()** (8 connections) — `server/commands/teleport_helpers.py`
- **log_goto_failure()** (7 connections) — `server/commands/goto_helpers.py`
- **Any** (7 connections)
- **broadcast_teleport_updates()** (7 connections) — `server/commands/teleport_helpers.py`
- *... and 69 more nodes in this community*

## Relationships

- [Admin Set Lucidity Command](Admin_Set_Lucidity_Command.md) (29 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (12 shared connections)
- [Health Check Models](Health_Check_Models.md) (7 shared connections)
- [Realtime Connection Impl](Realtime_Connection_Impl.md) (5 shared connections)
- [Connection Disconnection Cleanup](Connection_Disconnection_Cleanup.md) (4 shared connections)
- [Combat Monitoring Service](Combat_Monitoring_Service.md) (3 shared connections)
- [Structured Logging Admin](Structured_Logging_Admin.md) (2 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (1 shared connections)
- [Admin Shutdown Commands](Admin_Shutdown_Commands.md) (1 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (1 shared connections)

## Source Files

- `server/commands/admin_permission_utils.py`
- `server/commands/admin_teleport_commands.py`
- `server/commands/admin_teleport_utils.py`
- `server/commands/goto_helpers.py`
- `server/commands/teleport_helpers.py`
- `server/structured_logging/admin_actions_logger.py`
- `server/tests/unit/commands/test_admin_commands_helpers.py`

## Audit Trail

- EXTRACTED: 469 (99%)
- INFERRED: 6 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*