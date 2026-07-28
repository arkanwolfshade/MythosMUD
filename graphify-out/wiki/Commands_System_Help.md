# Commands System Help

> 11 nodes · cohesion 0.24

## Key Concepts

- **handle_system_command()** (10 connections) — `server/commands/system_commands.py`
- **test_system_commands.py** (6 connections) — `server/tests/unit/commands/test_system_commands.py`
- **test_handle_system_command()** (3 connections) — `server/tests/unit/commands/test_system_commands.py`
- **test_handle_system_command_no_chat_service()** (3 connections) — `server/tests/unit/commands/test_system_commands.py`
- **test_handle_system_command_no_message()** (3 connections) — `server/tests/unit/commands/test_system_commands.py`
- **Any** (2 connections)
- **Broadcast a system-level message via the chat service if available.** (1 connections) — `server/commands/system_commands.py`
- **Unit tests for system command handlers.  Tests the system command functionality.** (1 connections) — `server/tests/unit/commands/test_system_commands.py`
- **Test handle_system_command() broadcasts system message.** (1 connections) — `server/tests/unit/commands/test_system_commands.py`
- **Test handle_system_command() handles missing message.** (1 connections) — `server/tests/unit/commands/test_system_commands.py`
- **Test handle_system_command() handles missing chat service.** (1 connections) — `server/tests/unit/commands/test_system_commands.py`

## Relationships

- [Admin Set Lucidity Command](Admin_Set_Lucidity_Command.md) (4 shared connections)
- [Memory Leak Metrics](Memory_Leak_Metrics.md) (1 shared connections)
- [Look Command Helpers](Look_Command_Helpers.md) (1 shared connections)

## Source Files

- `server/commands/system_commands.py`
- `server/tests/unit/commands/test_system_commands.py`

## Audit Trail

- EXTRACTED: 30 (94%)
- INFERRED: 2 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*