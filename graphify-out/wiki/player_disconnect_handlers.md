# player disconnect handlers

> 71 nodes

## Key Concepts

- **test_player_disconnect_handlers.py** (34 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **player_disconnect_handlers.py** (25 connections) — `server/realtime/player_disconnect_handlers.py`
- **_collect_disconnect_keys()** (17 connections) — `server/realtime/player_disconnect_handlers.py`
- **handle_player_disconnect_broadcast()** (15 connections) — `server/realtime/player_disconnect_handlers.py`
- **_cleanup_player_references()** (9 connections) — `server/realtime/player_disconnect_handlers.py`
- **age_off_disconnected_sessions()** (9 connections) — `server/realtime/player_disconnect_handlers.py`
- **_remove_player_from_online_tracking()** (8 connections) — `server/realtime/player_disconnect_handlers.py`
- **UUID** (7 connections)
- **_get_session_maps_for_age_off()** (4 connections) — `server/realtime/player_disconnect_handlers.py`
- **_purge_expired_sessions_from_maps()** (4 connections) — `server/realtime/player_disconnect_handlers.py`
- **_session_ids_past_age_off()** (3 connections) — `server/realtime/player_disconnect_handlers.py`
- **test_handle_player_disconnect_broadcast_with_room()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_handle_player_disconnect_broadcast_no_room()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_handle_player_disconnect_broadcast_empty_player_name()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_collect_disconnect_keys_with_player()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_collect_disconnect_keys_no_player()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_remove_player_from_online_tracking()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_handle_player_disconnect_broadcast_room_no_player()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_handle_player_disconnect_broadcast_no_persistence()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_handle_player_disconnect_broadcast_no_room_found()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_collect_disconnect_keys_with_user_id()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_collect_disconnect_keys_with_string_user_id()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_collect_disconnect_keys_with_player_name()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_collect_disconnect_keys_no_name()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_remove_player_from_online_tracking_not_in_online_players()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- *... and 46 more nodes in this community*

## Relationships

- [disconnect grace period](disconnect_grace_period.md) (9 shared connections)
- [main()](main%28%29.md) (5 shared connections)
- [Any](Any.md) (3 shared connections)
- [spawn defaults](spawn_defaults.md) (2 shared connections)
- [UUID](UUID.md) (2 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (1 shared connections)
- [. init ()](_init_%28%29.md) (1 shared connections)
- [Player](Player.md) (1 shared connections)

## Source Files

- `server/realtime/player_disconnect_handlers.py`
- `server/tests/unit/realtime/test_player_disconnect_handlers.py`

## Audit Trail

- EXTRACTED: 244 (98%)
- INFERRED: 6 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*