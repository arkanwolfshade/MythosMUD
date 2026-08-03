# player disconnect handlers

> 46 nodes

## Key Concepts

- **test_player_disconnect_handlers.py** (34 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **_collect_disconnect_keys()** (19 connections) — `server/realtime/player_disconnect_handlers.py`
- **handle_player_disconnect_broadcast()** (17 connections) — `server/realtime/player_disconnect_handlers.py`
- **test_handle_player_disconnect_broadcast_with_room()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_handle_player_disconnect_broadcast_no_room()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_handle_player_disconnect_broadcast_empty_player_name()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_collect_disconnect_keys_with_player()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_collect_disconnect_keys_no_player()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_handle_player_disconnect_broadcast_room_no_player()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_handle_player_disconnect_broadcast_no_persistence()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_handle_player_disconnect_broadcast_no_room_found()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_collect_disconnect_keys_with_user_id()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_collect_disconnect_keys_with_string_user_id()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_collect_disconnect_keys_with_player_name()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_collect_disconnect_keys_no_name()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_age_off_disconnected_sessions_missing_attrs_returns_zero()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_handle_player_disconnect_broadcast_room_player_left_called()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_handle_player_disconnect_broadcast_no_player_name()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_collect_disconnect_keys_with_string_canonical_id()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_collect_disconnect_keys_with_uuid_canonical_id()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_collect_disconnect_keys_no_canonical_id()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **mock_connection_manager()** (2 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **Player** (1 connections)
- **Handle broadcasting disconnect events when a player disconnects.      Args:** (1 connections) — `server/realtime/player_disconnect_handlers.py`
- **Collect all keys (UUID and string) that need to be removed for player disconnect** (1 connections) — `server/realtime/player_disconnect_handlers.py`
- *... and 21 more nodes in this community*

## Relationships

- [emote game service](emote_game_service.md) (16 shared connections)
- [look helpers commands](look_helpers_commands.md) (4 shared connections)
- [player presence tracker](player_presence_tracker.md) (4 shared connections)
- [combat services messaging](combat_services_messaging.md) (1 shared connections)
- [help content websocket](help_content_websocket.md) (1 shared connections)

## Source Files

- `server/realtime/player_disconnect_handlers.py`
- `server/tests/unit/realtime/test_player_disconnect_handlers.py`

## Audit Trail

- EXTRACTED: 149 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*