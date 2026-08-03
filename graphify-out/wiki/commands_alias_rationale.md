# commands alias rationale

> 320 nodes

## Key Concepts

- **AliasStorage** (231 connections) — `server/alias_storage.py`
- **command_service.py** (95 connections) — `server/commands/command_service.py`
- **alias_storage.py** (67 connections) — `server/alias_storage.py`
- **command_parser.py** (46 connections) — `server/utils/command_parser.py`
- **test_alias_commands.py** (30 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **__init__.py** (29 connections) — `server/commands/__init__.py`
- **processing.py** (25 connections) — `server/command_handler/processing.py`
- **debrief_command.py** (25 connections) — `server/commands/debrief_command.py`
- **handle_alias_command()** (24 connections) — `server/commands/alias_commands.py`
- **parse_command()** (24 connections) — `server/utils/command_parser.py`
- **player_service()** (23 connections) — `docs/examples/logging/fastapi_integration.py`
- **CommandService** (20 connections) — `server/commands/command_service.py`
- **party_commands.py** (19 connections) — `server/commands/party_commands.py`
- **position_commands.py** (19 connections) — `server/commands/position_commands.py`
- **player_position_service.py** (17 connections) — `server/services/player_position_service.py`
- **channel_commands.py** (16 connections) — `server/commands/channel_commands.py`
- **alias_commands.py** (15 connections) — `server/commands/alias_commands.py`
- **handle_debrief_command()** (15 connections) — `server/commands/debrief_command.py`
- **skills_commands.py** (15 connections) — `server/commands/skills_commands.py`
- **get_help_content()** (15 connections) — `server/help/help_content.py`
- **handle_goto_command()** (14 connections) — `server/commands/admin_teleport_commands.py`
- **handle_admin_command()** (13 connections) — `server/commands/admin_commands.py`
- **handle_inventory_command()** (13 connections) — `server/commands/inventory_commands.py`
- **system_commands.py** (13 connections) — `server/commands/system_commands.py`
- **command_processor.py** (13 connections) — `server/utils/command_processor.py`
- *... and 295 more nodes in this community*

## Relationships

- [NATS Messaging](NATS_Messaging.md) (43 shared connections)
- [commands admin mute](commands_admin_mute.md) (31 shared connections)
- [command handler unified](command_handler_unified.md) (25 shared connections)
- [lucidity active service](lucidity_active_service.md) (20 shared connections)
- [commands magic rationale](commands_magic_rationale.md) (20 shared connections)
- [inventory commands command](inventory_commands_command.md) (19 shared connections)
- [command parser rationale](command_parser_rationale.md) (17 shared connections)
- [commands communication say](commands_communication_say.md) (15 shared connections)
- [combat services turn](combat_services_turn.md) (14 shared connections)
- [command helpers functions](command_helpers_functions.md) (13 shared connections)
- [commands rescue rationale](commands_rescue_rationale.md) (13 shared connections)
- [command inventory factories](command_inventory_factories.md) (13 shared connections)

## Source Files

- `docs/examples/logging/fastapi_integration.py`
- `server/alias_storage.py`
- `server/command_handler/processing.py`
- `server/commands/__init__.py`
- `server/commands/admin_commands.py`
- `server/commands/admin_teleport_commands.py`
- `server/commands/alias_commands.py`
- `server/commands/channel_commands.py`
- `server/commands/command_service.py`
- `server/commands/communication_commands.py`
- `server/commands/debrief_command.py`
- `server/commands/exploration_commands.py`
- `server/commands/help_commands.py`
- `server/commands/inventory_commands.py`
- `server/commands/party_commands.py`
- `server/commands/position_commands.py`
- `server/commands/skills_commands.py`
- `server/commands/system_commands.py`
- `server/commands/time_commands.py`
- `server/help/__init__.py`

## Audit Trail

- EXTRACTED: 1612 (96%)
- INFERRED: 61 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*