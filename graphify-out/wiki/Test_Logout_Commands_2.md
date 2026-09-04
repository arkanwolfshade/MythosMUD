# Test Logout Commands

> 85 nodes

## Key Concepts

- **test_logout_commands.py** (43 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **logout_commands.py** (31 connections) — `server/commands/logout_commands.py`
- **handle_logout_command()** (25 connections) — `server/commands/logout_commands.py`
- **asyncio** (18 connections)
- **_get_player_for_logout()** (15 connections) — `server/commands/logout_commands.py`
- **handle_quit_command()** (13 connections) — `server/commands/logout_commands.py`
- **_clear_corrupted_cache_entry()** (12 connections) — `server/commands/logout_commands.py`
- **_sync_player_position()** (12 connections) — `server/commands/logout_commands.py`
- **Any** (12 connections)
- **_disconnect_player_connections()** (9 connections) — `server/commands/logout_commands.py`
- **_is_player_in_combat_for_logout()** (9 connections) — `server/commands/logout_commands.py`
- **connection_manager()** (9 connections) — `server/tests/unit/game/test_follow_service.py`
- **_prepare_player_for_logout()** (7 connections) — `server/commands/logout_commands.py`
- **_update_and_save_player_last_active()** (7 connections) — `server/commands/logout_commands.py`
- **_get_app_services()** (5 connections) — `server/commands/logout_commands.py`
- **_coerce_player_uuid()** (4 connections) — `server/commands/logout_commands.py`
- **_force_disconnect_player()** (4 connections) — `server/commands/logout_commands.py`
- **_mark_quit_intentional()** (4 connections) — `server/commands/logout_commands.py`
- **_resolve_disconnect_player_id()** (4 connections) — `server/commands/logout_commands.py`
- **test_disconnect_player_connections_error()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_disconnect_player_connections_no_manager()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_disconnect_player_connections_success()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_get_player_for_logout_corrupted_cache()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_get_player_for_logout_from_cache()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_get_player_for_logout_from_persistence()** (4 connections) — `server/tests/unit/commands/test_logout_commands.py`
- *... and 60 more nodes in this community*

## Relationships

- [Test Logout Commands Helpers](Test_Logout_Commands_Helpers.md) (17 shared connections)
- [Test Logout Command](Test_Logout_Command.md) (8 shared connections)
- [Test Rest Command](Test_Rest_Command.md) (4 shared connections)
- [Test Logout Commands](Test_Logout_Commands.md) (4 shared connections)
- [Test Who Commands](Test_Who_Commands.md) (3 shared connections)
- [Player Model & Migrations](Player_Model_&_Migrations.md) (3 shared connections)
- [Test Follow Service](Test_Follow_Service.md) (2 shared connections)
- [Player Event Handlers Respawn Room](Player_Event_Handlers_Respawn_Room.md) (1 shared connections)
- [Players](Players.md) (1 shared connections)
- [Real Time](Real_Time.md) (1 shared connections)
- [Test Position Commands](Test_Position_Commands.md) (1 shared connections)
- [Correlation Middleware](Correlation_Middleware.md) (1 shared connections)

## Source Files

- `server/commands/logout_commands.py`
- `server/tests/unit/commands/test_logout_commands.py`
- `server/tests/unit/game/test_follow_service.py`

## Audit Trail

- EXTRACTED: 203 (93%)
- INFERRED: 15 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*