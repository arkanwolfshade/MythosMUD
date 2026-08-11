# E2E Suite Overview

> 94 nodes

## Key Concepts

- **admin_teleport_commands.py** (38 connections) — `server/commands/admin_teleport_commands.py`
- **get_admin_actions_logger()** (25 connections) — `server/structured_logging/admin_actions_logger.py`
- **teleport_helpers.py** (23 connections) — `server/commands/teleport_helpers.py`
- **handle_teleport_command()** (20 connections) — `server/commands/admin_teleport_commands.py`
- **goto_helpers.py** (20 connections) — `server/commands/goto_helpers.py`
- **admin_actions_logger.py** (18 connections) — `server/structured_logging/admin_actions_logger.py`
- **handle_goto_command()** (15 connections) — `server/commands/admin_teleport_commands.py`
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
- **log_goto_failure()** (7 connections) — `server/commands/goto_helpers.py`
- **broadcast_teleport_updates()** (7 connections) — `server/commands/teleport_helpers.py`
- *... and 69 more nodes in this community*

## Relationships

- [UI Player Event Handlers](UI_Player_Event_Handlers.md) (15 shared connections)
- [Client Event Store](Client_Event_Store.md) (13 shared connections)
- [Spell Effect Protocols](Spell_Effect_Protocols.md) (6 shared connections)
- [Schemas Maps Map](Schemas_Maps_Map.md) (6 shared connections)
- [Player Schema Converter](Player_Schema_Converter.md) (5 shared connections)
- [Chat NATS Publisher](Chat_NATS_Publisher.md) (5 shared connections)
- [Pylint Unique Findings](Pylint_Unique_Findings.md) (4 shared connections)
- [Client Security Utilities](Client_Security_Utilities.md) (4 shared connections)
- [Structured Logging Admin](Structured_Logging_Admin.md) (4 shared connections)
- [Admin Status Commands](Admin_Status_Commands.md) (3 shared connections)
- [Room Drop Renderer](Room_Drop_Renderer.md) (1 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (1 shared connections)

## Source Files

- `server/commands/admin_permission_utils.py`
- `server/commands/admin_teleport_commands.py`
- `server/commands/admin_teleport_utils.py`
- `server/commands/goto_helpers.py`
- `server/commands/teleport_helpers.py`
- `server/structured_logging/admin_actions_logger.py`
- `server/tests/unit/commands/test_admin_commands_helpers.py`

## Audit Trail

- EXTRACTED: 472 (99%)
- INFERRED: 6 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*