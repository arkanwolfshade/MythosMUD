# Commands System Help

> 23 nodes · cohesion 0.11

## Key Concepts

- **handle_help_command()** (11 connections) — `server/commands/system_commands.py`
- **handle_system_command()** (8 connections) — `server/commands/system_commands.py`
- **test_system_commands.py** (5 connections) — `server/tests/unit/commands/test_system_commands.py`
- **test_help_commands.py** (4 connections) — `server/tests/unit/commands/test_help_commands.py`
- **test_handle_help_command_no_topic()** (3 connections) — `server/tests/unit/commands/test_help_commands.py`
- **test_handle_help_command_unknown_topic()** (3 connections) — `server/tests/unit/commands/test_help_commands.py`
- **test_handle_help_command_with_topic()** (3 connections) — `server/tests/unit/commands/test_help_commands.py`
- **test_handle_system_command()** (3 connections) — `server/tests/unit/commands/test_system_commands.py`
- **test_handle_system_command_no_chat_service()** (3 connections) — `server/tests/unit/commands/test_system_commands.py`
- **test_handle_system_command_no_message()** (3 connections) — `server/tests/unit/commands/test_system_commands.py`
- **help_commands.py** (2 connections) — `server/commands/help_commands.py`
- **Test handle_system_command() handles missing message.** (2 connections) — `server/tests/unit/commands/test_system_commands.py`
- **AliasStorage** (2 connections) — `server/commands/system_commands.py`
- **Any** (2 connections) — `server/commands/system_commands.py`
- **Help command adapter module.  The original help command handler lives in system_** (1 connections) — `server/commands/help_commands.py`
- **Broadcast a system-level message via the chat service if available.** (1 connections) — `server/commands/system_commands.py`
- **Handle the help command.      Args:         command_data: Command data dictionar** (1 connections) — `server/commands/system_commands.py`
- **Unit tests for help command handlers.  Tests the help command functionality.** (1 connections) — `server/tests/unit/commands/test_help_commands.py`
- **Test handle_help_command() returns general help when no topic.** (1 connections) — `server/tests/unit/commands/test_help_commands.py`
- **Test handle_help_command() returns help for specific topic.** (1 connections) — `server/tests/unit/commands/test_help_commands.py`
- **Test handle_help_command() handles unknown topic.** (1 connections) — `server/tests/unit/commands/test_help_commands.py`
- **Unit tests for system command handlers.  Tests the system command functionality.** (1 connections) — `server/tests/unit/commands/test_system_commands.py`
- **Test handle_system_command() broadcasts system message.** (1 connections) — `server/tests/unit/commands/test_system_commands.py`

## Relationships

- [[Alias Expansion Logic]] (4 shared connections)
- [[Help and WebSocket Core]] (1 shared connections)

## Source Files

- `server/commands/help_commands.py`
- `server/commands/system_commands.py`
- `server/tests/unit/commands/test_help_commands.py`
- `server/tests/unit/commands/test_system_commands.py`

## Audit Trail

- EXTRACTED: 57 (90%)
- INFERRED: 6 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
