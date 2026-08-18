# test_logout_commands.py

> 84 nodes

## Key Concepts

- **test_logout_commands.py** (43 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **logout_commands.py** (26 connections) — `server/commands/logout_commands.py`
- **handle_logout_command()** (24 connections) — `server/commands/logout_commands.py`
- **asyncio** (18 connections)
- **_get_player_position_from_connection_manager()** (14 connections) — `server/commands/logout_commands.py`
- **_get_player_for_logout()** (13 connections) — `server/commands/logout_commands.py`
- **handle_quit_command()** (13 connections) — `server/commands/logout_commands.py`
- **Any** (13 connections)
- **_clear_corrupted_cache_entry()** (12 connections) — `server/commands/logout_commands.py`
- **_sync_player_position()** (12 connections) — `server/commands/logout_commands.py`
- **_disconnect_player_connections()** (9 connections) — `server/commands/logout_commands.py`
- **_prepare_player_for_logout()** (7 connections) — `server/commands/logout_commands.py`
- **_update_and_save_player_last_active()** (7 connections) — `server/commands/logout_commands.py`
- **_force_disconnect_player()** (4 connections) — `server/commands/logout_commands.py`
- **_get_app_services()** (4 connections) — `server/commands/logout_commands.py`
- **_resolve_disconnect_player_id()** (4 connections) — `server/commands/logout_commands.py`
- **test_disconnect_player_connections_error()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_disconnect_player_connections_no_manager()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_disconnect_player_connections_success()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_get_player_for_logout_corrupted_cache()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_get_player_for_logout_from_cache()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_get_player_for_logout_from_persistence()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_get_player_for_logout_persistence_error()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_get_player_for_logout_persistence_returns_coroutine()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_handle_logout_command_error_handling()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- *... and 59 more nodes in this community*

## Relationships

- [test_logout_commands_helpers.py](test_logout_commands_helpers.py.md) (14 shared connections)
- [TestLogoutCommand](TestLogoutCommand.md) (8 shared connections)
- [get_cached_player](get_cached_player.md) (5 shared connections)
- [command_service.py](command_service.py.md) (4 shared connections)
- [fixture](fixture.md) (4 shared connections)
- [test_who_commands.py](test_who_commands.py.md) (3 shared connections)
- [AliasStorage](AliasStorage.md) (3 shared connections)
- [get_username_from_user](get_username_from_user.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/commands/logout_commands.py`
- `server/tests/unit/commands/test_logout_commands.py`

## Audit Trail

- EXTRACTED: 195 (94%)
- INFERRED: 12 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*