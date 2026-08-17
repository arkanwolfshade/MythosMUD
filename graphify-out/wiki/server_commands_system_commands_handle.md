# server commands system commands handle

> 11 nodes

## Key Concepts

- **handle_system_command()** (10 connections) — `server/commands/system_commands.py`
- **test_system_commands.py** (7 connections) — `server/tests/unit/commands/test_system_commands.py`
- **test_handle_system_command()** (4 connections) — `server/tests/unit/commands/test_system_commands.py`
- **test_handle_system_command_no_chat_service()** (4 connections) — `server/tests/unit/commands/test_system_commands.py`
- **test_handle_system_command_no_message()** (4 connections) — `server/tests/unit/commands/test_system_commands.py`
- **asyncio** (3 connections)
- **Any** (2 connections)
- **Test handle_system_command() handles missing message.** (2 connections) — `server/tests/unit/commands/test_system_commands.py`
- **Broadcast a system-level message via the chat service if available.** (1 connections) — `server/commands/system_commands.py`
- **Unit tests for system command handlers. Tests the system command functionality.** (1 connections) — `server/tests/unit/commands/test_system_commands.py`
- **Test handle_system_command() broadcasts system message.** (1 connections) — `server/tests/unit/commands/test_system_commands.py`

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [server commands container helpers inventory](server_commands_container_helpers_inventory.md) (2 shared connections)
- [server alias storage aliasstorage](server_alias_storage_aliasstorage.md) (1 shared connections)
- [server commands alias commands](server_commands_alias_commands.md) (1 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/commands/system_commands.py`
- `server/tests/unit/commands/test_system_commands.py`

## Audit Trail

- EXTRACTED: 21 (91%)
- INFERRED: 2 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*