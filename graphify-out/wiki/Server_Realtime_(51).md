# Server Realtime (51)

> 42 nodes

## Key Concepts

- **test_connection_disconnection.py** (31 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **_track_disconnect_if_needed()** (13 connections) — `server/realtime/connection_disconnection.py`
- **test_track_disconnect_if_needed_new()** (3 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_track_disconnect_if_needed_already_processed()** (3 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_track_disconnect_if_needed_force_disconnect()** (3 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_track_disconnect_if_needed_intentional_force_disconnect()** (3 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_cleanup_room_subscriptions()** (3 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_cleanup_room_subscriptions_force_disconnect()** (3 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_cleanup_room_subscriptions_intentional_force_disconnect()** (3 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_cleanup_room_subscriptions_has_connection()** (3 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_cleanup_player_data()** (3 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_cleanup_player_data_has_connection()** (3 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_disconnect_all_websockets()** (3 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_disconnect_all_websockets_none_websocket()** (3 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_track_disconnect_if_needed_has_connection()** (3 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_cleanup_websocket_disconnect()** (3 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_cleanup_websocket_disconnect_when_mapping_cleared_during_close()** (3 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_disconnect_connection_by_id_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **remove_player_data_mock()** (2 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **remove_player_messages_mock()** (2 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **remove_player_from_all_rooms_mock()** (2 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **mock_manager()** (2 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **Test _track_disconnect_if_needed() when disconnect is new.** (2 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **Test _cleanup_room_subscriptions() preserves rooms on force disconnect.** (2 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **Track disconnection if needed.      Args:         player_id: The player's ID** (1 connections) — `server/realtime/connection_disconnection.py`
- *... and 17 more nodes in this community*

## Relationships

- [Server Realtime (60)](Server_Realtime_%2860%29.md) (23 shared connections)
- [Server Commands](Server_Commands.md) (2 shared connections)
- [Server Realtime (14)](Server_Realtime_%2814%29.md) (1 shared connections)

## Source Files

- `server/realtime/connection_disconnection.py`
- `server/tests/unit/realtime/test_connection_disconnection.py`

## Audit Trail

- EXTRACTED: 122 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*