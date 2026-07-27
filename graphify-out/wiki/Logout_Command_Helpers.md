# Logout Command Helpers

> 34 nodes · cohesion 0.08

## Key Concepts

- **_get_player_position_from_connection_manager()** (14 connections) — `server/commands/logout_commands.py`
- **test_logout_commands_helpers.py** (14 connections) — `server/tests/unit/commands/test_logout_commands_helpers.py`
- **_sync_player_position()** (12 connections) — `server/commands/logout_commands.py`
- **Test _get_player_position_from_connection_manager retrieves position by player_i** (6 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_clear_corrupted_cache_entry()** (3 connections) — `server/tests/unit/commands/test_logout_commands_helpers.py`
- **test_clear_corrupted_cache_entry_no_request()** (3 connections) — `server/tests/unit/commands/test_logout_commands_helpers.py`
- **test_clear_corrupted_cache_entry_no_state()** (3 connections) — `server/tests/unit/commands/test_logout_commands_helpers.py`
- **test_get_player_position_from_connection_manager()** (3 connections) — `server/tests/unit/commands/test_logout_commands_helpers.py`
- **test_get_player_position_from_connection_manager_by_name()** (3 connections) — `server/tests/unit/commands/test_logout_commands_helpers.py`
- **test_get_player_position_from_connection_manager_no_manager()** (3 connections) — `server/tests/unit/commands/test_logout_commands_helpers.py`
- **test_get_player_position_from_connection_manager_not_found()** (3 connections) — `server/tests/unit/commands/test_logout_commands_helpers.py`
- **test_sync_player_position()** (3 connections) — `server/tests/unit/commands/test_logout_commands_helpers.py`
- **test_sync_player_position_no_change()** (3 connections) — `server/tests/unit/commands/test_logout_commands_helpers.py`
- **test_sync_player_position_none()** (3 connections) — `server/tests/unit/commands/test_logout_commands_helpers.py`
- **test_get_player_position_from_connection_manager_by_id()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_get_player_position_from_connection_manager_by_name()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_get_player_position_from_connection_manager_no_manager()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_get_player_position_from_connection_manager_not_found()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_sync_player_position_no_change()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_sync_player_position_none_value()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_sync_player_position_updates_stats()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **Test _sync_player_position() does nothing when position is None.** (2 connections) — `server/tests/unit/commands/test_logout_commands_helpers.py`
- **Get player's current position from connection manager.      Args:         connec** (1 connections) — `server/commands/logout_commands.py`
- **Synchronize player's position from connection manager to player stats.      Args** (1 connections) — `server/commands/logout_commands.py`
- **Unit tests for logout_commands helper functions.  Tests helper functions in logo** (1 connections) — `server/tests/unit/commands/test_logout_commands_helpers.py`
- *... and 9 more nodes in this community*

## Relationships

- [[Logout and Quit Commands]] (17 shared connections)
- [[Alias Expansion Logic]] (2 shared connections)

## Source Files

- `server/commands/logout_commands.py`
- `server/tests/unit/commands/test_logout_commands.py`
- `server/tests/unit/commands/test_logout_commands_helpers.py`

## Audit Trail

- EXTRACTED: 111 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
