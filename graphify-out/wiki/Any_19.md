# Any

> 21 nodes

## Key Concepts

- **track_player_connected_impl()** (16 connections) — `server/realtime/player_presence_tracker.py`
- **Any** (9 connections)
- **_resolve_room_id()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **_get_instance_manager_from_manager()** (6 connections) — `server/realtime/player_presence_tracker.py`
- **_resolve_room_id_for_tutorial_reconnect()** (5 connections) — `server/realtime/player_presence_tracker.py`
- **instance_manager()** (4 connections) — `server/tests/unit/game/test_instance_manager.py`
- **test_resolve_room_id_no_room_id()** (3 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_resolve_room_id_success()** (3 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_track_player_connected_impl_new_connection()** (3 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_track_player_connected_impl_existing_connection()** (3 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_track_player_connected_impl_no_room_id()** (3 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **Resolve canonical room ID from player's current_room_id.      Args:         play** (1 connections) — `server/realtime/player_presence_tracker.py`
- **For players with tutorial_instance_id, ensure instance exists and return first r** (1 connections) — `server/realtime/player_presence_tracker.py`
- **Extract InstanceManager from ConnectionManager via app.container.** (1 connections) — `server/realtime/player_presence_tracker.py`
- **Track when a player connects.      Args:         player_id: The player's ID** (1 connections) — `server/realtime/player_presence_tracker.py`
- **Create InstanceManager with tutorial template in cache.** (1 connections) — `server/tests/unit/game/test_instance_manager.py`
- **Test _resolve_room_id() returns None when no room_id.** (1 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **Test _resolve_room_id() resolves canonical room ID.** (1 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **Test track_player_connected_impl() tracks new connection.** (1 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **Test track_player_connected_impl() tracks additional connection.** (1 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **Test track_player_connected_impl() handles player with no room_id.** (1 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`

## Relationships

- [get asyncpg server settings for](get_asyncpg_server_settings_for.md) (9 shared connections)
- [player disconnect handlers](player_disconnect_handlers.md) (6 shared connections)
- [player presence tracker](player_presence_tracker.md) (3 shared connections)
- [Player](Player.md) (3 shared connections)
- [Enhanced Logging Migration Report](Enhanced_Logging_Migration_Report.md) (1 shared connections)
- [test_resolve_room_id_room_no_id](test_resolve_room_id_room_no_id.md) (1 shared connections)
- [.state()](state%28%29.md) (1 shared connections)
- [real time](real_time.md) (1 shared connections)
- [Any](Any.md) (1 shared connections)
- [test command parser](test_command_parser.md) (1 shared connections)
- [spawn defaults](spawn_defaults.md) (1 shared connections)

## Source Files

- `server/realtime/player_presence_tracker.py`
- `server/tests/unit/game/test_instance_manager.py`
- `server/tests/unit/realtime/test_player_presence_tracker.py`

## Audit Trail

- EXTRACTED: 70 (95%)
- INFERRED: 4 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*