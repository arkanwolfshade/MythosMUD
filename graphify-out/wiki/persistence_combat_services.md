# persistence combat services

> 41 nodes

## Key Concepts

- **get_help_content()** (15 connections) — `server/help/help_content.py`
- **handle_help_command()** (11 connections) — `server/commands/system_commands.py`
- **handle_system_command()** (10 connections) — `server/commands/system_commands.py`
- **test_system_commands.py** (6 connections) — `server/tests/unit/commands/test_system_commands.py`
- **test_websocket_handler_help.py** (6 connections) — `server/tests/unit/realtime/test_websocket_handler_help.py`
- **test_help_commands.py** (5 connections) — `server/tests/unit/commands/test_help_commands.py`
- **help_commands.py** (4 connections) — `server/commands/help_commands.py`
- **__init__.py** (3 connections) — `server/help/__init__.py`
- **_get_general_help()** (3 connections) — `server/help/help_content.py`
- **test_handle_help_command_no_topic()** (3 connections) — `server/tests/unit/commands/test_help_commands.py`
- **test_handle_help_command_with_topic()** (3 connections) — `server/tests/unit/commands/test_help_commands.py`
- **test_handle_help_command_unknown_topic()** (3 connections) — `server/tests/unit/commands/test_help_commands.py`
- **test_handle_system_command()** (3 connections) — `server/tests/unit/commands/test_system_commands.py`
- **test_handle_system_command_no_message()** (3 connections) — `server/tests/unit/commands/test_system_commands.py`
- **test_handle_system_command_no_chat_service()** (3 connections) — `server/tests/unit/commands/test_system_commands.py`
- **test_get_help_content()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_get_help_content_with_command()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_get_help_content_general()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_help.py`
- **test_get_help_content_specific()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_help.py`
- **test_get_help_content_talk()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_help.py`
- **Any** (2 connections)
- **Help command adapter module.  The original help command handler lives in system_** (1 connections) — `server/commands/help_commands.py`
- **Broadcast a system-level message via the chat service if available.** (1 connections) — `server/commands/system_commands.py`
- **Handle the help command.      Args:         command_data: Command data dictionar** (1 connections) — `server/commands/system_commands.py`
- **Help system for MythosMUD.  This package provides help content and command docum** (1 connections) — `server/help/__init__.py`
- *... and 16 more nodes in this community*

## Relationships

- [logging examples fastapi](logging_examples_fastapi.md) (9 shared connections)
- [chat logger services](chat_logger_services.md) (3 shared connections)
- [commands npc admin](commands_npc_admin.md) (2 shared connections)
- [character creation service](character_creation_service.md) (2 shared connections)
- [command commands handler](command_commands_handler.md) (2 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (1 shared connections)
- [shutdown admin command](shutdown_admin_command.md) (1 shared connections)

## Source Files

- `server/commands/help_commands.py`
- `server/commands/system_commands.py`
- `server/help/__init__.py`
- `server/help/help_content.py`
- `server/tests/unit/commands/test_help_commands.py`
- `server/tests/unit/commands/test_system_commands.py`
- `server/tests/unit/realtime/test_websocket_handler_core.py`
- `server/tests/unit/realtime/test_websocket_handler_help.py`

## Audit Trail

- EXTRACTED: 110 (93%)
- INFERRED: 8 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*