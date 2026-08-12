# logout_commands.py

> 27 nodes

## Key Concepts

- **logout_commands.py** (26 connections) — `server/commands/logout_commands.py`
- **handle_logout_command()** (24 connections) — `server/commands/logout_commands.py`
- **_get_player_for_logout()** (13 connections) — `server/commands/logout_commands.py`
- **handle_quit_command()** (13 connections) — `server/commands/logout_commands.py`
- **Any** (13 connections)
- **_sync_player_position()** (12 connections) — `server/commands/logout_commands.py`
- **_disconnect_player_connections()** (9 connections) — `server/commands/logout_commands.py`
- **_prepare_player_for_logout()** (7 connections) — `server/commands/logout_commands.py`
- **_update_and_save_player_last_active()** (7 connections) — `server/commands/logout_commands.py`
- **_force_disconnect_player()** (4 connections) — `server/commands/logout_commands.py`
- **_get_app_services()** (4 connections) — `server/commands/logout_commands.py`
- **_resolve_disconnect_player_id()** (4 connections) — `server/commands/logout_commands.py`
- **_mark_quit_intentional()** (3 connections) — `server/commands/logout_commands.py`
- **test_sync_player_position_no_change()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_sync_player_position_none_value()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_sync_player_position_updates_stats()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **UUID** (2 connections)
- **Logout and quit command handlers for MythosMUD. This module contains handlers…** (1 connections) — `server/commands/logout_commands.py`
- **Update and save player's last active timestamp. Args: persistence: Persistence…** (1 connections) — `server/commands/logout_commands.py`
- **Disconnect player from all connections. Args: connection_manager: Connection…** (1 connections) — `server/commands/logout_commands.py`
- **Handle the quit command for disconnecting from the game. Args: command_data:…** (1 connections) — `server/commands/logout_commands.py`
- **Handle the logout command for cleanly disconnecting from the game. This command…** (1 connections) — `server/commands/logout_commands.py`
- **Get player for logout, handling cache corruption and persistence fallback.…** (1 connections) — `server/commands/logout_commands.py`
- **Synchronize player's position from connection manager to player stats. Args:…** (1 connections) — `server/commands/logout_commands.py`
- **Test _sync_player_position updates player stats when position differs.** (1 connections) — `server/tests/unit/commands/test_logout_commands.py`
- *... and 2 more nodes in this community*

## Relationships

- [test_logout_commands.py](test_logout_commands.py.md) (28 shared connections)
- [TestLogoutCommand](TestLogoutCommand.md) (8 shared connections)
- [test_logout_commands_helpers.py](test_logout_commands_helpers.py.md) (8 shared connections)
- [get_cached_player](get_cached_player.md) (5 shared connections)
- [AliasStorage](AliasStorage.md) (5 shared connections)
- [_clear_corrupted_cache_entry](_clear_corrupted_cache_entry.md) (3 shared connections)
- [test_status_commands.py](test_status_commands.py.md) (3 shared connections)
- [get_username_from_user](get_username_from_user.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [alias_storage.py](alias_storage.py.md) (1 shared connections)
- [BaseCommand](BaseCommand.md) (1 shared connections)

## Source Files

- `server/commands/logout_commands.py`
- `server/tests/unit/commands/test_logout_commands.py`

## Audit Trail

- EXTRACTED: 101 (89%)
- INFERRED: 12 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*