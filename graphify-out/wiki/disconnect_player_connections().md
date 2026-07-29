# disconnect player connections()

> 55 nodes

## Key Concepts

- **test_logout_commands.py** (42 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **handle_logout_command()** (26 connections) — `server/commands/logout_commands.py`
- **_get_player_for_logout()** (13 connections) — `server/commands/logout_commands.py`
- **handle_quit_command()** (11 connections) — `server/commands/logout_commands.py`
- **Any** (8 connections)
- **_disconnect_player_connections()** (8 connections) — `server/commands/logout_commands.py`
- **_update_and_save_player_last_active()** (7 connections) — `server/commands/logout_commands.py`
- **test_get_player_for_logout_from_cache()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_get_player_for_logout_from_persistence()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_get_player_for_logout_corrupted_cache()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_get_player_for_logout_persistence_error()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_get_player_for_logout_persistence_returns_coroutine()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_update_and_save_player_last_active_success()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_update_and_save_player_last_active_no_persistence()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_disconnect_player_connections_success()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_disconnect_player_connections_no_manager()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_disconnect_player_connections_error()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_handle_quit_command_success()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_handle_quit_command_no_persistence()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_handle_quit_command_persistence_error()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_handle_logout_command_success()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_handle_logout_command_no_player()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_handle_logout_command_no_persistence()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_handle_logout_command_error_handling()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_handle_logout_command_syncs_position()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- *... and 30 more nodes in this community*

## Relationships

- [test clear corrupted cache entry](test_clear_corrupted_cache_entry.md) (25 shared connections)
- [test logout command](test_logout_command.md) (8 shared connections)
- [Any](Any.md) (4 shared connections)
- [test player cache](test_player_cache.md) (2 shared connections)
- [. get persistence from app()](_get_persistence_from_app%28%29.md) (2 shared connections)
- [utility commands](utility_commands.md) (2 shared connections)

## Source Files

- `server/commands/logout_commands.py`
- `server/tests/unit/commands/test_logout_commands.py`

## Audit Trail

- EXTRACTED: 193 (94%)
- INFERRED: 12 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*