# test logout command

> 27 nodes

## Key Concepts

- **TestLogoutCommand** (13 connections) — `server/tests/unit/commands/test_logout_command.py`
- **Any** (8 connections)
- **.test_logout_command_success()** (4 connections) — `server/tests/unit/commands/test_logout_command.py`
- **.test_logout_command_persists_position()** (4 connections) — `server/tests/unit/commands/test_logout_command.py`
- **.test_logout_command_no_persistence()** (4 connections) — `server/tests/unit/commands/test_logout_command.py`
- **.test_logout_command_persistence_error()** (4 connections) — `server/tests/unit/commands/test_logout_command.py`
- **.test_logout_command_connection_error()** (4 connections) — `server/tests/unit/commands/test_logout_command.py`
- **.test_logout_command_with_args()** (4 connections) — `server/tests/unit/commands/test_logout_command.py`
- **.test_logout_command_player_not_found()** (4 connections) — `server/tests/unit/commands/test_logout_command.py`
- **.test_logout_command_general_error_handling()** (4 connections) — `server/tests/unit/commands/test_logout_command.py`
- **test_logout_command.py** (3 connections) — `server/tests/unit/commands/test_logout_command.py`
- **.mock_request()** (2 connections) — `server/tests/unit/commands/test_logout_command.py`
- **.mock_current_user()** (2 connections) — `server/tests/unit/commands/test_logout_command.py`
- **.mock_alias_storage()** (2 connections) — `server/tests/unit/commands/test_logout_command.py`
- **Unit tests for the logout command handler.** (1 connections) — `server/tests/unit/commands/test_logout_command.py`
- **Test cases for the logout command handler.** (1 connections) — `server/tests/unit/commands/test_logout_command.py`
- **Create a mock request object.** (1 connections) — `server/tests/unit/commands/test_logout_command.py`
- **Create a mock current user.** (1 connections) — `server/tests/unit/commands/test_logout_command.py`
- **Create a mock alias storage.** (1 connections) — `server/tests/unit/commands/test_logout_command.py`
- **Test successful logout command execution.** (1 connections) — `server/tests/unit/commands/test_logout_command.py`
- **Ensure logout syncs in-memory position back to persistence.** (1 connections) — `server/tests/unit/commands/test_logout_command.py`
- **Test logout command when persistence is not available.** (1 connections) — `server/tests/unit/commands/test_logout_command.py`
- **Test logout command when persistence operations fail.** (1 connections) — `server/tests/unit/commands/test_logout_command.py`
- **Test logout command when connection cleanup fails.** (1 connections) — `server/tests/unit/commands/test_logout_command.py`
- **Test logout command with arguments (should be ignored).** (1 connections) — `server/tests/unit/commands/test_logout_command.py`
- *... and 2 more nodes in this community*

## Relationships

- [disconnect player connections()](disconnect_player_connections%28%29.md) (8 shared connections)
- [utility commands](utility_commands.md) (1 shared connections)

## Source Files

- `server/tests/unit/commands/test_logout_command.py`

## Audit Trail

- EXTRACTED: 67 (89%)
- INFERRED: 8 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*