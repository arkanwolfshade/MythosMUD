# test_players_procedures.py

> 20 nodes · cohesion 0.17

## Key Concepts

- **logout_commands.py** (35 connections) — `server/commands/logout_commands.py`
- **handle_quit_command()** (14 connections) — `server/commands/logout_commands.py`
- **Any** (12 connections)
- **_is_player_in_combat_for_logout()** (8 connections) — `server/commands/logout_commands.py`
- **_prepare_player_for_logout()** (7 connections) — `server/commands/logout_commands.py`
- **_update_and_save_player_last_active()** (7 connections) — `server/commands/logout_commands.py`
- **_resolve_disconnect_player_id()** (5 connections) — `server/commands/logout_commands.py`
- **_coerce_player_uuid()** (4 connections) — `server/commands/logout_commands.py`
- **_force_disconnect_player()** (4 connections) — `server/commands/logout_commands.py`
- **_get_app_services()** (4 connections) — `server/commands/logout_commands.py`
- **_is_coroutine_object()** (3 connections) — `server/commands/logout_commands.py`
- **_mark_quit_intentional()** (3 connections) — `server/commands/logout_commands.py`
- **UUID** (3 connections)
- **Player** (2 connections)
- **Logout and quit command handlers for MythosMUD. This module contains handlers…** (1 connections) — `server/commands/logout_commands.py`
- **Update and save player's last active timestamp. Args: persistence: Persistence…** (1 connections) — `server/commands/logout_commands.py`
- **Check whether `player` is currently in combat, for the quit/logout combat…** (1 connections) — `server/commands/logout_commands.py`
- **Handle the quit command for disconnecting from the game. Args: command_data:…** (1 connections) — `server/commands/logout_commands.py`
- **Normalize player_id to uuid.UUID. Production Player.player_id is a UUID string…** (1 connections) — `server/commands/logout_commands.py`
- **True when value is an awaitable coroutine (not a Player).** (1 connections) — `server/commands/logout_commands.py`

## Relationships

- [ConnectionErrorHandler](ConnectionErrorHandler.md) (20 shared connections)
- [Any](Any.md) (7 shared connections)
- [command_parser.py](command_parser.py.md) (3 shared connections)
- [session_factory](session_factory.md) (3 shared connections)
- [test_follow_commands.py](test_follow_commands.py.md) (3 shared connections)
- [test_player_respawn_service.py](test_player_respawn_service.py.md) (2 shared connections)
- [Room](Room.md) (2 shared connections)
- [test_player_event_handlers_utils.py](test_player_event_handlers_utils.py.md) (2 shared connections)
- [P4 · Intent Sweep — Core Feature Issues](P4_·_Intent_Sweep_—_Core_Feature_Issues.md) (2 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (2 shared connections)
- [fixtures/auth.ts](fixtures-auth.ts.md) (1 shared connections)
- [test_websocket_helpers.py](test_websocket_helpers.py.md) (1 shared connections)

## Source Files

- `server/commands/logout_commands.py`

## Audit Trail

- EXTRACTED: 82 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*