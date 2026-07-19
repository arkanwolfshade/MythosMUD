# Logout and Quit Commands

> 60 nodes · cohesion 0.05

## Key Concepts

- **test_logout_commands.py** (41 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **handle_logout_command()** (25 connections) — `server/commands/logout_commands.py`
- **_get_player_for_logout()** (13 connections) — `server/commands/logout_commands.py`
- **_clear_corrupted_cache_entry()** (12 connections) — `server/commands/logout_commands.py`
- **handle_quit_command()** (10 connections) — `server/commands/logout_commands.py`
- **_disconnect_player_connections()** (8 connections) — `server/commands/logout_commands.py`
- **Any** (8 connections) — `server/commands/logout_commands.py`
- **_update_and_save_player_last_active()** (7 connections) — `server/commands/logout_commands.py`
- **test_disconnect_player_connections_error()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_handle_logout_command_error_handling()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_clear_corrupted_cache_entry_no_cache()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_clear_corrupted_cache_entry_no_request()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_clear_corrupted_cache_entry_with_cache()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_disconnect_player_connections_no_manager()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_disconnect_player_connections_success()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_get_player_for_logout_corrupted_cache()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_get_player_for_logout_from_cache()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_get_player_for_logout_from_persistence()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_get_player_for_logout_persistence_error()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_get_player_for_logout_persistence_returns_coroutine()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_handle_logout_command_no_player()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_handle_logout_command_success()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_handle_logout_command_syncs_position()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_handle_quit_command_no_persistence()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_handle_quit_command_persistence_error()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- *... and 35 more nodes in this community*

## Relationships

- [[Logout Command Helpers]] (17 shared connections)
- [[Alias Expansion Logic]] (8 shared connections)
- [[Logout Command Tests]] (8 shared connections)
- [[Ground and Rescue Commands]] (3 shared connections)
- [[Player Cache]] (2 shared connections)
- [[Command Helper Utilities]] (2 shared connections)
- [[Database Manager Tests]] (2 shared connections)
- [[Command Service Tests]] (1 shared connections)
- [[Services Service Room]] (1 shared connections)

## Source Files

- `server/commands/logout_commands.py`
- `server/tests/unit/commands/test_logout_commands.py`

## Audit Trail

- EXTRACTED: 212 (95%)
- INFERRED: 12 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
