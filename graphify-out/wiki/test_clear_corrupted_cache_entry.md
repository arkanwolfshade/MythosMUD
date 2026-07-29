# test clear corrupted cache entry

> 46 nodes

## Key Concepts

- **logout_commands.py** (20 connections) — `server/commands/logout_commands.py`
- **test_logout_commands_helpers.py** (15 connections) — `server/tests/unit/commands/test_logout_commands_helpers.py`
- **_get_player_position_from_connection_manager()** (14 connections) — `server/commands/logout_commands.py`
- **_clear_corrupted_cache_entry()** (12 connections) — `server/commands/logout_commands.py`
- **_sync_player_position()** (12 connections) — `server/commands/logout_commands.py`
- **test_clear_corrupted_cache_entry_with_cache()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_clear_corrupted_cache_entry_no_cache()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_clear_corrupted_cache_entry_no_request()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_get_player_position_from_connection_manager_by_id()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_get_player_position_from_connection_manager_by_name()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_get_player_position_from_connection_manager_not_found()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_get_player_position_from_connection_manager_no_manager()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_sync_player_position_updates_stats()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_sync_player_position_no_change()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_sync_player_position_none_value()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_clear_corrupted_cache_entry()** (3 connections) — `server/tests/unit/commands/test_logout_commands_helpers.py`
- **test_clear_corrupted_cache_entry_no_request()** (3 connections) — `server/tests/unit/commands/test_logout_commands_helpers.py`
- **test_clear_corrupted_cache_entry_no_state()** (3 connections) — `server/tests/unit/commands/test_logout_commands_helpers.py`
- **test_get_player_position_from_connection_manager()** (3 connections) — `server/tests/unit/commands/test_logout_commands_helpers.py`
- **test_get_player_position_from_connection_manager_by_name()** (3 connections) — `server/tests/unit/commands/test_logout_commands_helpers.py`
- **test_get_player_position_from_connection_manager_no_manager()** (3 connections) — `server/tests/unit/commands/test_logout_commands_helpers.py`
- **test_get_player_position_from_connection_manager_not_found()** (3 connections) — `server/tests/unit/commands/test_logout_commands_helpers.py`
- **test_sync_player_position()** (3 connections) — `server/tests/unit/commands/test_logout_commands_helpers.py`
- **test_sync_player_position_none()** (3 connections) — `server/tests/unit/commands/test_logout_commands_helpers.py`
- **test_sync_player_position_no_change()** (3 connections) — `server/tests/unit/commands/test_logout_commands_helpers.py`
- *... and 21 more nodes in this community*

## Relationships

- [disconnect player connections()](disconnect_player_connections%28%29.md) (25 shared connections)
- [Any](Any.md) (3 shared connections)
- [test player cache](test_player_cache.md) (3 shared connections)
- [main()](main%28%29.md) (2 shared connections)
- [utility commands](utility_commands.md) (1 shared connections)

## Source Files

- `server/commands/logout_commands.py`
- `server/tests/unit/commands/test_logout_commands.py`
- `server/tests/unit/commands/test_logout_commands_helpers.py`

## Audit Trail

- EXTRACTED: 158 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*