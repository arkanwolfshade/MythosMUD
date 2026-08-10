# Logger Client Add To

> 12 nodes

## Key Concepts

- **handle_whoami_command()** (12 connections) — `server/commands/status_commands.py`
- **test_utility_commands_whoami.py** (5 connections) — `server/tests/unit/commands/test_utility_commands_whoami.py`
- **test_handle_whoami_command()** (3 connections) — `server/tests/unit/commands/test_status_commands.py`
- **test_handle_whoami_command()** (3 connections) — `server/tests/unit/commands/test_utility_commands_whoami.py`
- **test_handle_whoami_command_no_persistence()** (3 connections) — `server/tests/unit/commands/test_utility_commands_whoami.py`
- **test_handle_whoami_command_player_not_found()** (3 connections) — `server/tests/unit/commands/test_utility_commands_whoami.py`
- **Handle the whoami command as an alias for status.      Mirrors handle_status_com** (1 connections) — `server/commands/status_commands.py`
- **Test handle_whoami_command calls handle_status_command.** (1 connections) — `server/tests/unit/commands/test_status_commands.py`
- **Unit tests for utility command handlers.  Tests the whoami command functionality** (1 connections) — `server/tests/unit/commands/test_utility_commands_whoami.py`
- **Test handle_whoami_command() returns player information.** (1 connections) — `server/tests/unit/commands/test_utility_commands_whoami.py`
- **Test handle_whoami_command() handles missing persistence.** (1 connections) — `server/tests/unit/commands/test_utility_commands_whoami.py`
- **Test handle_whoami_command() handles player not found.** (1 connections) — `server/tests/unit/commands/test_utility_commands_whoami.py`

## Relationships

- [Status Command Handlers](Status_Command_Handlers.md) (5 shared connections)
- [Client Event Store](Client_Event_Store.md) (2 shared connections)
- [Commands System Help](Commands_System_Help.md) (2 shared connections)

## Source Files

- `server/commands/status_commands.py`
- `server/tests/unit/commands/test_status_commands.py`
- `server/tests/unit/commands/test_utility_commands_whoami.py`

## Audit Trail

- EXTRACTED: 28 (80%)
- INFERRED: 7 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*