# Community 1162

> 11 nodes

## Key Concepts

- **handle_system_command()** (9 connections) — `server/commands/system_commands.py`
- **test_system_commands.py** (6 connections) — `server/tests/unit/commands/test_system_commands.py`
- **test_handle_system_command()** (4 connections) — `server/tests/unit/commands/test_system_commands.py`
- **test_handle_system_command_no_chat_service()** (4 connections) — `server/tests/unit/commands/test_system_commands.py`
- **test_handle_system_command_no_message()** (4 connections) — `server/tests/unit/commands/test_system_commands.py`
- **asyncio** (3 connections)
- **Test handle_system_command() handles missing message.** (2 connections) — `server/tests/unit/commands/test_system_commands.py`
- **Any** (1 connections)
- **Broadcast a system-level message via the chat service if available.** (1 connections) — `server/commands/system_commands.py`
- **Unit tests for system command handlers. Tests the system command functionality.** (1 connections) — `server/tests/unit/commands/test_system_commands.py`
- **Test handle_system_command() broadcasts system message.** (1 connections) — `server/tests/unit/commands/test_system_commands.py`

## Relationships

- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (3 shared connections)
- [Community 533](Community_533.md) (1 shared connections)

## Source Files

- `server/commands/system_commands.py`
- `server/tests/unit/commands/test_system_commands.py`

## Audit Trail

- EXTRACTED: 19 (95%)
- INFERRED: 1 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*