# Player Position Service

> 243 nodes

## Key Concepts

- **command_service.py** (92 connections) — `server/commands/command_service.py`
- **.__init__()** (71 connections) — `server/commands/command_service.py`
- **get_username_from_user()** (50 connections) — `server/utils/command_helpers.py`
- **admin_mute_commands.py** (29 connections) — `server/commands/admin_mute_commands.py`
- **processing.py** (25 connections) — `server/command_handler/processing.py`
- **test_follow_commands.py** (23 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **handle_mute_command()** (20 connections) — `server/commands/admin_mute_commands.py`
- **CommandService** (20 connections) — `server/commands/command_service.py`
- **test_communication_commands_channels.py** (20 connections) — `server/tests/unit/commands/test_communication_commands_channels.py`
- **handle_follow_command()** (19 connections) — `server/commands/follow_commands.py`
- **Any** (16 connections)
- **follow_commands.py** (15 connections) — `server/commands/follow_commands.py`
- **skills_commands.py** (15 connections) — `server/commands/skills_commands.py`
- **handle_inventory_command()** (14 connections) — `server/commands/inventory_commands.py`
- **teach_command.py** (14 connections) — `server/commands/teach_command.py`
- **get_help_content()** (14 connections) — `server/help/help_content.py`
- **handle_unmute_command()** (13 connections) — `server/commands/admin_mute_commands.py`
- **system_commands.py** (13 connections) — `server/commands/system_commands.py`
- **handle_teach_command()** (13 connections) — `server/commands/teach_command.py`
- **strip_ansi_codes()** (13 connections) — `server/validators/security_validator.py`
- **handle_add_admin_command()** (12 connections) — `server/commands/admin_mute_commands.py`
- **handle_mutes_command()** (12 connections) — `server/commands/admin_mute_commands.py`
- **handle_global_command()** (12 connections) — `server/commands/communication_commands.py`
- **handle_help_command()** (12 connections) — `server/commands/system_commands.py`
- **help_content.py** (12 connections) — `server/help/help_content.py`
- *... and 218 more nodes in this community*

## Relationships

- [Any](Any.md) (50 shared connections)
- [test command factories inventory](test_command_factories_inventory.md) (36 shared connections)
- [handle global command()](handle_global_command%28%29.md) (30 shared connections)
- [CombatService](CombatService.md) (22 shared connections)
- [world](world.md) (19 shared connections)
- [. get persistence from app()](_get_persistence_from_app%28%29.md) (14 shared connections)
- [CommandHandler](CommandHandler.md) (12 shared connections)
- [test magic commands](test_magic_commands.md) (11 shared connections)
- [Spell Targeting](Spell_Targeting.md) (10 shared connections)
- [.validate topic()](validate_topic%28%29.md) (9 shared connections)
- [test movement service](test_movement_service.md) (8 shared connections)
- [real time](real_time.md) (8 shared connections)

## Source Files

- `server/command_handler/processing.py`
- `server/commands/admin_mute_commands.py`
- `server/commands/command_service.py`
- `server/commands/communication_commands.py`
- `server/commands/follow_commands.py`
- `server/commands/help_commands.py`
- `server/commands/inventory_commands.py`
- `server/commands/skills_commands.py`
- `server/commands/system_commands.py`
- `server/commands/teach_command.py`
- `server/help/__init__.py`
- `server/help/help_content.py`
- `server/tests/unit/commands/test_command_service.py`
- `server/tests/unit/commands/test_communication_commands_channels.py`
- `server/tests/unit/commands/test_follow_commands.py`
- `server/tests/unit/commands/test_help_commands.py`
- `server/tests/unit/commands/test_teach_command.py`
- `server/tests/unit/realtime/test_websocket_handler_help.py`
- `server/tests/unit/utils/test_command_helpers.py`
- `server/tests/unit/utils/test_command_helpers_functions.py`

## Audit Trail

- EXTRACTED: 990 (86%)
- INFERRED: 161 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*