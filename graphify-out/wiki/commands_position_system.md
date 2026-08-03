# commands position system

> 13 nodes

## Key Concepts

- **handle_system_command()** (10 connections) — `server/commands/system_commands.py`
- **chat_service** (6 connections) — `docs/examples/logging/websocket_integration.py`
- **test_system_commands.py** (6 connections) — `server/tests/unit/commands/test_system_commands.py`
- **test_handle_system_command()** (3 connections) — `server/tests/unit/commands/test_system_commands.py`
- **test_handle_system_command_no_message()** (3 connections) — `server/tests/unit/commands/test_system_commands.py`
- **test_handle_system_command_no_chat_service()** (3 connections) — `server/tests/unit/commands/test_system_commands.py`
- **.process_message()** (2 connections) — `docs/examples/logging/websocket_integration.py`
- **Any** (2 connections)
- **Broadcast a system-level message via the chat service if available.** (1 connections) — `server/commands/system_commands.py`
- **Unit tests for system command handlers.  Tests the system command functionality.** (1 connections) — `server/tests/unit/commands/test_system_commands.py`
- **Test handle_system_command() broadcasts system message.** (1 connections) — `server/tests/unit/commands/test_system_commands.py`
- **Test handle_system_command() handles missing message.** (1 connections) — `server/tests/unit/commands/test_system_commands.py`
- **Test handle_system_command() handles missing chat service.** (1 connections) — `server/tests/unit/commands/test_system_commands.py`

## Relationships

- [commands alias rationale](commands_alias_rationale.md) (5 shared connections)
- [System Metrics](System_Metrics.md) (2 shared connections)
- [commands communication flows](commands_communication_flows.md) (1 shared connections)
- [commands emote rationale](commands_emote_rationale.md) (1 shared connections)
- [realtime game state](realtime_game_state.md) (1 shared connections)

## Source Files

- `docs/examples/logging/websocket_integration.py`
- `server/commands/system_commands.py`
- `server/tests/unit/commands/test_system_commands.py`

## Audit Trail

- EXTRACTED: 34 (85%)
- INFERRED: 6 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*