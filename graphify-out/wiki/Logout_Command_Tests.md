# Logout Command Tests

> 47 nodes

## Key Concepts

- **handle_logout_command()** (24 connections) — `server/commands/logout_commands.py`
- **TestLogoutCommand** (13 connections) — `server/tests/unit/commands/test_logout_command.py`
- **_disconnect_player_connections()** (9 connections) — `server/commands/logout_commands.py`
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
- **test_disconnect_player_connections_success()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_disconnect_player_connections_no_manager()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_disconnect_player_connections_error()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_handle_logout_command_success()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_handle_logout_command_no_player()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_handle_logout_command_no_persistence()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_handle_logout_command_error_handling()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_handle_logout_command_syncs_position()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **.mock_request()** (2 connections) — `server/tests/unit/commands/test_logout_command.py`
- **.mock_current_user()** (2 connections) — `server/tests/unit/commands/test_logout_command.py`
- **.mock_alias_storage()** (2 connections) — `server/tests/unit/commands/test_logout_command.py`
- **Disconnect player from all connections.      Args:         connection_manager: C** (1 connections) — `server/commands/logout_commands.py`
- *... and 22 more nodes in this community*

## Relationships

- [Logging Migration Examples](Logging_Migration_Examples.md) (17 shared connections)
- [Server Process Termination](Server_Process_Termination.md) (2 shared connections)
- [Player Schema Converter](Player_Schema_Converter.md) (1 shared connections)
- [Container Open Events](Container_Open_Events.md) (1 shared connections)
- [Rate Limiter Utilities](Rate_Limiter_Utilities.md) (1 shared connections)

## Source Files

- `server/commands/logout_commands.py`
- `server/tests/unit/commands/test_logout_command.py`
- `server/tests/unit/commands/test_logout_commands.py`

## Audit Trail

- EXTRACTED: 124 (87%)
- INFERRED: 18 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*