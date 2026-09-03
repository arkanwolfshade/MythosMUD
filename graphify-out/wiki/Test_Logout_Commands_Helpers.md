# Test Logout Commands Helpers

> 30 nodes

## Key Concepts

- **_get_player_position_from_connection_manager()** (15 connections) — `server/commands/logout_commands.py`
- **test_logout_commands_helpers.py** (15 connections) — `server/tests/unit/commands/test_logout_commands_helpers.py`
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
- **Test _sync_player_position() does nothing when position is None.** (2 connections) — `server/tests/unit/commands/test_logout_commands_helpers.py`
- **Test _get_player_position_from_connection_manager() returns position.** (2 connections) — `server/tests/unit/commands/test_logout_commands_helpers.py`
- **Get player's current position from connection manager. Args:…** (1 connections) — `server/commands/logout_commands.py`
- **Unit tests for logout_commands helper functions. Tests helper functions in…** (1 connections) — `server/tests/unit/commands/test_logout_commands_helpers.py`
- **Test _clear_corrupted_cache_entry() clears cache entry.** (1 connections) — `server/tests/unit/commands/test_logout_commands_helpers.py`
- **Test _clear_corrupted_cache_entry() handles None request.** (1 connections) — `server/tests/unit/commands/test_logout_commands_helpers.py`
- **Test _clear_corrupted_cache_entry() handles request without state.** (1 connections) — `server/tests/unit/commands/test_logout_commands_helpers.py`
- **Test _get_player_position_from_connection_manager() finds by display name.** (1 connections) — `server/tests/unit/commands/test_logout_commands_helpers.py`
- **Test _get_player_position_from_connection_manager() returns None when player…** (1 connections) — `server/tests/unit/commands/test_logout_commands_helpers.py`
- *... and 5 more nodes in this community*

## Relationships

- [Test Logout Commands](Test_Logout_Commands.md) (17 shared connections)
- [Admin Setstat Support](Admin_Setstat_Support.md) (1 shared connections)

## Source Files

- `server/commands/logout_commands.py`
- `server/tests/unit/commands/test_logout_commands.py`
- `server/tests/unit/commands/test_logout_commands_helpers.py`

## Audit Trail

- EXTRACTED: 52 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*