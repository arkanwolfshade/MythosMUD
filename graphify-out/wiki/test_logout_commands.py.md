# test_logout_commands.py

> 41 nodes

## Key Concepts

- **test_logout_commands.py** (43 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **asyncio** (18 connections)
- **_get_player_for_logout()** (13 connections) — `server/commands/logout_commands.py`
- **test_disconnect_player_connections_error()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_disconnect_player_connections_no_manager()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_disconnect_player_connections_success()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_get_player_for_logout_corrupted_cache()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_get_player_for_logout_from_cache()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_get_player_for_logout_from_persistence()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_get_player_for_logout_persistence_error()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_get_player_for_logout_persistence_returns_coroutine()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_handle_logout_command_error_handling()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_handle_logout_command_no_persistence()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_handle_logout_command_no_player()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_handle_logout_command_success()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_handle_logout_command_syncs_position()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_handle_quit_command_no_persistence()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_handle_quit_command_persistence_error()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_handle_quit_command_success()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_update_and_save_player_last_active_no_persistence()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_update_and_save_player_last_active_success()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **Get player for logout, handling cache corruption and persistence fallback.…** (1 connections) — `server/commands/logout_commands.py`
- **Unit tests for logout commands. Tests the logout and quit command handlers for…** (1 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **Test _get_player_for_logout retrieves player from persistence when not in cache.** (1 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **Test _get_player_for_logout handles corrupted cache (coroutine instead of…** (1 connections) — `server/tests/unit/commands/test_logout_commands.py`
- *... and 16 more nodes in this community*

## Relationships

- [logout_commands.py](logout_commands.py.md) (25 shared connections)
- [_clear_corrupted_cache_entry](_clear_corrupted_cache_entry.md) (5 shared connections)
- [test_logout_commands_helpers.py](test_logout_commands_helpers.py.md) (5 shared connections)
- [fixture](fixture.md) (4 shared connections)
- [get_cached_player](get_cached_player.md) (2 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/commands/logout_commands.py`
- `server/tests/unit/commands/test_logout_commands.py`

## Audit Trail

- EXTRACTED: 104 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*