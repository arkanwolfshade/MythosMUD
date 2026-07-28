# Server Commands (4)

> 128 nodes

## Key Concepts

- **test_logout_commands.py** (42 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **handle_logout_command()** (26 connections) — `server/commands/logout_commands.py`
- **logout_commands.py** (20 connections) — `server/commands/logout_commands.py`
- **test_logout_commands_helpers.py** (15 connections) — `server/tests/unit/commands/test_logout_commands_helpers.py`
- **_get_player_position_from_connection_manager()** (14 connections) — `server/commands/logout_commands.py`
- **_get_player_for_logout()** (13 connections) — `server/commands/logout_commands.py`
- **TestLogoutCommand** (13 connections) — `server/tests/unit/commands/test_logout_command.py`
- **_clear_corrupted_cache_entry()** (12 connections) — `server/commands/logout_commands.py`
- **_sync_player_position()** (12 connections) — `server/commands/logout_commands.py`
- **handle_quit_command()** (11 connections) — `server/commands/logout_commands.py`
- **Any** (8 connections)
- **_disconnect_player_connections()** (8 connections) — `server/commands/logout_commands.py`
- **Any** (8 connections)
- **_update_and_save_player_last_active()** (7 connections) — `server/commands/logout_commands.py`
- **.test_logout_command_success()** (4 connections) — `server/tests/unit/commands/test_logout_command.py`
- **.test_logout_command_persists_position()** (4 connections) — `server/tests/unit/commands/test_logout_command.py`
- **.test_logout_command_no_persistence()** (4 connections) — `server/tests/unit/commands/test_logout_command.py`
- **.test_logout_command_persistence_error()** (4 connections) — `server/tests/unit/commands/test_logout_command.py`
- **.test_logout_command_connection_error()** (4 connections) — `server/tests/unit/commands/test_logout_command.py`
- **.test_logout_command_with_args()** (4 connections) — `server/tests/unit/commands/test_logout_command.py`
- **.test_logout_command_player_not_found()** (4 connections) — `server/tests/unit/commands/test_logout_command.py`
- **.test_logout_command_general_error_handling()** (4 connections) — `server/tests/unit/commands/test_logout_command.py`
- **test_logout_command.py** (3 connections) — `server/tests/unit/commands/test_logout_command.py`
- **test_clear_corrupted_cache_entry_with_cache()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_clear_corrupted_cache_entry_no_cache()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- *... and 103 more nodes in this community*

## Relationships

- [Server Commands](Server_Commands.md) (9 shared connections)
- [Server Utils (19)](Server_Utils_%2819%29.md) (5 shared connections)
- [Server Commands (10)](Server_Commands_%2810%29.md) (4 shared connections)
- [Server Utils (6)](Server_Utils_%286%29.md) (2 shared connections)

## Source Files

- `server/commands/logout_commands.py`
- `server/tests/unit/commands/test_logout_command.py`
- `server/tests/unit/commands/test_logout_commands.py`
- `server/tests/unit/commands/test_logout_commands_helpers.py`

## Audit Trail

- EXTRACTED: 418 (95%)
- INFERRED: 20 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*