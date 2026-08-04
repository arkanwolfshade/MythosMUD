# manager subject services

> 11 nodes

## Key Concepts

- **handle_system_command()** (10 connections) — `server/commands/system_commands.py`
- **test_system_commands.py** (6 connections) — `server/tests/unit/commands/test_system_commands.py`
- **test_handle_system_command()** (3 connections) — `server/tests/unit/commands/test_system_commands.py`
- **test_handle_system_command_no_message()** (3 connections) — `server/tests/unit/commands/test_system_commands.py`
- **test_handle_system_command_no_chat_service()** (3 connections) — `server/tests/unit/commands/test_system_commands.py`
- **Any** (2 connections)
- **Broadcast a system-level message via the chat service if available.** (1 connections) — `server/commands/system_commands.py`
- **Unit tests for system command handlers.  Tests the system command functionality.** (1 connections) — `server/tests/unit/commands/test_system_commands.py`
- **Test handle_system_command() broadcasts system message.** (1 connections) — `server/tests/unit/commands/test_system_commands.py`
- **Test handle_system_command() handles missing message.** (1 connections) — `server/tests/unit/commands/test_system_commands.py`
- **Test handle_system_command() handles missing chat service.** (1 connections) — `server/tests/unit/commands/test_system_commands.py`

## Relationships

- [Loot Generation](Loot_Generation.md) (2 shared connections)
- [add hashed password](add_hashed_password.md) (1 shared connections)
- [commands party examples](commands_party_examples.md) (1 shared connections)
- [nats services metrics](nats_services_metrics.md) (1 shared connections)
- [commands alias rationale](commands_alias_rationale.md) (1 shared connections)

## Source Files

- `server/commands/system_commands.py`
- `server/tests/unit/commands/test_system_commands.py`

## Audit Trail

- EXTRACTED: 30 (94%)
- INFERRED: 2 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*