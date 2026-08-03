# combat services turn

> 70 nodes

## Key Concepts

- **admin_teleport_commands.py** (38 connections) — `server/commands/admin_teleport_commands.py`
- **get_admin_actions_logger()** (25 connections) — `server/structured_logging/admin_actions_logger.py`
- **teleport_helpers.py** (23 connections) — `server/commands/teleport_helpers.py`
- **goto_helpers.py** (20 connections) — `server/commands/goto_helpers.py`
- **handle_teleport_command()** (19 connections) — `server/commands/admin_teleport_commands.py`
- **admin_actions_logger.py** (15 connections) — `server/structured_logging/admin_actions_logger.py`
- **validate_admin_permission()** (13 connections) — `server/commands/admin_permission_utils.py`
- **admin_teleport_utils.py** (13 connections) — `server/commands/admin_teleport_utils.py`
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
- **log_goto_failure()** (7 connections) — `server/commands/goto_helpers.py`
- **broadcast_teleport_updates()** (7 connections) — `server/commands/teleport_helpers.py`
- **validate_goto_context()** (6 connections) — `server/commands/goto_helpers.py`
- **resolve_goto_target()** (6 connections) — `server/commands/goto_helpers.py`
- **validate_confirm_goto_context()** (6 connections) — `server/commands/goto_helpers.py`
- *... and 45 more nodes in this community*

## Relationships

- [commands alias rationale](commands_alias_rationale.md) (14 shared connections)
- [NATS Messaging](NATS_Messaging.md) (12 shared connections)
- [commands admin mute](commands_admin_mute.md) (9 shared connections)
- [commands inventory helpers](commands_inventory_helpers.md) (6 shared connections)
- [npc populate databases](npc_populate_databases.md) (4 shared connections)
- [commands admin helpers](commands_admin_helpers.md) (4 shared connections)
- [combat services messaging](combat_services_messaging.md) (4 shared connections)
- [command admin setlucidity](command_admin_setlucidity.md) (4 shared connections)
- [admin commands setstat](admin_commands_setstat.md) (2 shared connections)
- [admin structured logging](admin_structured_logging.md) (2 shared connections)
- [command inventory factories](command_inventory_factories.md) (1 shared connections)
- [shutdown admin command](shutdown_admin_command.md) (1 shared connections)

## Source Files

- `server/commands/admin_permission_utils.py`
- `server/commands/admin_teleport_commands.py`
- `server/commands/admin_teleport_utils.py`
- `server/commands/goto_helpers.py`
- `server/commands/teleport_helpers.py`
- `server/structured_logging/admin_actions_logger.py`

## Audit Trail

- EXTRACTED: 392 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*