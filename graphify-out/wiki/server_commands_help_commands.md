# server commands help commands

> 44 nodes

## Key Concepts

- **get_help_content()** (15 connections) — `server/help/help_content.py`
- **system_commands.py** (13 connections) — `server/commands/system_commands.py`
- **handle_help_command()** (11 connections) — `server/commands/system_commands.py`
- **handle_system_command()** (10 connections) — `server/commands/system_commands.py`
- **test_system_commands.py** (7 connections) — `server/tests/unit/commands/test_system_commands.py`
- **test_help_commands.py** (6 connections) — `server/tests/unit/commands/test_help_commands.py`
- **test_websocket_handler_help.py** (6 connections) — `server/tests/unit/realtime/test_websocket_handler_help.py`
- **test_handle_help_command_no_topic()** (4 connections) — `server/tests/unit/commands/test_help_commands.py`
- **test_handle_help_command_unknown_topic()** (4 connections) — `server/tests/unit/commands/test_help_commands.py`
- **test_handle_help_command_with_topic()** (4 connections) — `server/tests/unit/commands/test_help_commands.py`
- **test_handle_system_command()** (4 connections) — `server/tests/unit/commands/test_system_commands.py`
- **test_handle_system_command_no_chat_service()** (4 connections) — `server/tests/unit/commands/test_system_commands.py`
- **test_handle_system_command_no_message()** (4 connections) — `server/tests/unit/commands/test_system_commands.py`
- **help_commands.py** (4 connections) — `server/commands/help_commands.py`
- **_get_general_help()** (3 connections) — `server/help/help_content.py`
- **test_get_help_content()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_get_help_content_with_command()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_get_help_content_general()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_help.py`
- **test_get_help_content_specific()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_help.py`
- **test_get_help_content_talk()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_help.py`
- **help/__init__.py** (3 connections) — `server/help/__init__.py`
- **asyncio** (3 connections)
- **asyncio** (3 connections)
- **Any** (2 connections)
- **Test handle_system_command() handles missing message.** (2 connections) — `server/tests/unit/commands/test_system_commands.py`
- *... and 19 more nodes in this community*

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (7 shared connections)
- [server alias storage aliasstorage](server_alias_storage_aliasstorage.md) (3 shared connections)
- [server realtime websocket handler commands](server_realtime_websocket_handler_commands.md) (3 shared connections)
- [server commands alias commands](server_commands_alias_commands.md) (2 shared connections)
- [server commands admin commands](server_commands_admin_commands.md) (2 shared connections)
- [server command handler command execution](server_command_handler_command_execution.md) (2 shared connections)
- [claude rules pytest](claude_rules_pytest.md) (2 shared connections)
- [server commands look helpers lookrequest](server_commands_look_helpers_lookrequest.md) (1 shared connections)
- [server commands rescue commands](server_commands_rescue_commands.md) (1 shared connections)
- [aliaspayload](aliaspayload.md) (1 shared connections)

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

- EXTRACTED: 79 (93%)
- INFERRED: 6 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*