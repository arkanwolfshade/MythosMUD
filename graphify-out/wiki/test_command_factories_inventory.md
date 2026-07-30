# test command factories inventory

> 152 nodes

## Key Concepts

- **admin_teleport_commands.py** (38 connections) — `server/commands/admin_teleport_commands.py`
- **test_admin_commands.py** (37 connections) — `server/tests/unit/commands/test_admin_commands.py`
- **admin_commands.py** (33 connections) — `server/commands/admin_commands.py`
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
- **execute_confirm_goto()** (8 connections) — `server/commands/goto_helpers.py`
- **update_player_room_location()** (8 connections) — `server/commands/teleport_helpers.py`
- **Any** (7 connections)
- *... and 127 more nodes in this community*

## Relationships

- [Player Position Service](Player_Position_Service.md) (36 shared connections)
- [world](world.md) (14 shared connections)
- [admin setstat command](admin_setstat_command.md) (13 shared connections)
- [real time](real_time.md) (10 shared connections)
- [Any](Any.md) (9 shared connections)
- [admin setlucidity command](admin_setlucidity_command.md) (6 shared connections)
- [DropResolved](DropResolved.md) (6 shared connections)
- [circuit breaker](circuit_breaker.md) (4 shared connections)
- [AsyncSessionFactory](AsyncSessionFactory.md) (2 shared connections)
- [AdminActionsLogger](AdminActionsLogger.md) (2 shared connections)
- [handle global command()](handle_global_command%28%29.md) (1 shared connections)
- [close db()](close_db%28%29.md) (1 shared connections)

## Source Files

- `server/commands/admin_commands.py`
- `server/commands/admin_permission_utils.py`
- `server/commands/admin_teleport_commands.py`
- `server/commands/admin_teleport_utils.py`
- `server/commands/goto_helpers.py`
- `server/commands/teleport_helpers.py`
- `server/structured_logging/admin_actions_logger.py`
- `server/tests/unit/commands/test_admin_commands.py`
- `server/tests/unit/commands/test_admin_commands_helpers.py`

## Audit Trail

- EXTRACTED: 627 (96%)
- INFERRED: 29 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*