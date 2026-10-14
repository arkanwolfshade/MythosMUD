# system_commands.py

> 36 nodes

## Key Concepts

- **system_commands.py** (18 connections) — `server/commands/system_commands.py`
- **handle_help_command()** (16 connections) — `server/commands/system_commands.py`
- **test_help_commands.py** (16 connections) — `server/tests/unit/commands/test_help_commands.py`
- **handle_system_command()** (11 connections) — `server/commands/system_commands.py`
- **_text()** (6 connections) — `server/tests/unit/commands/test_help_commands.py`
- **asyncio** (6 connections)
- **test_system_commands.py** (6 connections) — `server/tests/unit/commands/test_system_commands.py`
- **test_handle_help_command_hides_admin_commands_from_players()** (5 connections) — `server/tests/unit/commands/test_help_commands.py`
- **test_handle_help_command_no_topic()** (5 connections) — `server/tests/unit/commands/test_help_commands.py`
- **test_handle_help_command_positional_arg_fallback()** (5 connections) — `server/tests/unit/commands/test_help_commands.py`
- **test_handle_help_command_too_many_args()** (5 connections) — `server/tests/unit/commands/test_help_commands.py`
- **test_handle_help_command_unknown_topic()** (5 connections) — `server/tests/unit/commands/test_help_commands.py`
- **test_handle_help_command_with_topic()** (5 connections) — `server/tests/unit/commands/test_help_commands.py`
- **test_handle_system_command()** (4 connections) — `server/tests/unit/commands/test_system_commands.py`
- **test_handle_system_command_no_chat_service()** (4 connections) — `server/tests/unit/commands/test_system_commands.py`
- **test_handle_system_command_no_message()** (4 connections) — `server/tests/unit/commands/test_system_commands.py`
- **help_commands.py** (4 connections) — `server/commands/help_commands.py`
- **_help_topic()** (3 connections) — `server/commands/system_commands.py`
- **asyncio** (3 connections)
- **Any** (1 connections)
- **Help command adapter module. The original help command handler lives in…** (1 connections) — `server/commands/help_commands.py`
- **System commands for MythosMUD. This module contains handlers for system-level…** (1 connections) — `server/commands/system_commands.py`
- **Broadcast a system-level message via the chat service if available.** (1 connections) — `server/commands/system_commands.py`
- **Topic from the validated command's ``topic`` field, falling back to the first…** (1 connections) — `server/commands/system_commands.py`
- **Handle the help command: ``help`` lists topics, ``help <command|alias|guide>``…** (1 connections) — `server/commands/system_commands.py`
- *... and 11 more nodes in this community*

## Relationships

- [command_parser.py](command_parser.py.md) (5 shared connections)
- [catalog_commands.py](catalog_commands.py.md) (4 shared connections)
- [command_error](command_error.md) (3 shared connections)
- [AliasStorage](AliasStorage.md) (3 shared connections)
- [MessageCategory](MessageCategory.md) (3 shared connections)
- [get_help_content](get_help_content.md) (2 shared connections)
- [test_alias_commands.py](test_alias_commands.py.md) (2 shared connections)
- [command_service.py](command_service.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [alias_storage.py](alias_storage.py.md) (2 shared connections)
- [.state](state.md) (1 shared connections)
- [help_content.py](help_content.py.md) (1 shared connections)

## Source Files

- `server/commands/help_commands.py`
- `server/commands/system_commands.py`
- `server/tests/unit/commands/test_help_commands.py`
- `server/tests/unit/commands/test_system_commands.py`

## Audit Trail

- EXTRACTED: 79 (89%)
- INFERRED: 10 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*