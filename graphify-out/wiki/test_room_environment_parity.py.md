# test_room_environment_parity.py

> 11 nodes · cohesion 0.29

## Key Concepts

- **handle_system_command()** (11 connections) — `server/commands/system_commands.py`
- **test_system_commands.py** (6 connections) — `server/tests/unit/commands/test_system_commands.py`
- **test_handle_system_command()** (4 connections) — `server/tests/unit/commands/test_system_commands.py`
- **test_handle_system_command_no_chat_service()** (4 connections) — `server/tests/unit/commands/test_system_commands.py`
- **test_handle_system_command_no_message()** (4 connections) — `server/tests/unit/commands/test_system_commands.py`
- **asyncio** (3 connections)
- **Any** (1 connections)
- **Broadcast a system-level message via the chat service if available.** (1 connections) — `server/commands/system_commands.py`
- **Unit tests for system command handlers. Tests the system command functionality.** (1 connections) — `server/tests/unit/commands/test_system_commands.py`
- **Test handle_system_command() broadcasts system message.** (1 connections) — `server/tests/unit/commands/test_system_commands.py`
- **Test handle_system_command() handles missing message.** (1 connections) — `server/tests/unit/commands/test_system_commands.py`

## Relationships

- [command_parser.py](command_parser.py.md) (4 shared connections)
- [MessageBatcher](MessageBatcher.md) (1 shared connections)
- [test_container_helpers_inventory_ops.py](test_container_helpers_inventory_ops.py.md) (1 shared connections)

## Source Files

- `server/commands/system_commands.py`
- `server/tests/unit/commands/test_system_commands.py`

## Audit Trail

- EXTRACTED: 20 (91%)
- INFERRED: 2 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*