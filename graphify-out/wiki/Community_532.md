# Community 532

> 32 nodes

## Key Concepts

- **test_connection_disconnection.py** (40 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **asyncio** (14 connections)
- **_track_disconnect_if_needed()** (12 connections) — `server/realtime/connection_disconnection.py`
- **force_disconnect_player_impl()** (10 connections) — `server/realtime/connection_disconnection.py`
- **test_cleanup_websocket_disconnect_when_mapping_cleared_during_close()** (5 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_disconnect_all_websockets()** (5 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_cleanup_websocket_disconnect()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_cleanup_websocket_disconnect_intentional_without_sockets()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_disconnect_all_websockets_none_websocket()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_disconnect_connection_by_id_impl()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_force_disconnect_player_impl_intentional_without_sockets()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_force_disconnect_player_impl_with_sockets()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_track_disconnect_if_needed_already_processed()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_track_disconnect_if_needed_force_disconnect()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_track_disconnect_if_needed_has_connection()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_track_disconnect_if_needed_intentional_force_disconnect()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_track_disconnect_if_needed_new()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **Test _track_disconnect_if_needed() when disconnect is new.** (2 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **Track disconnection if needed. Args: player_id: The player's ID manager:…** (1 connections) — `server/realtime/connection_disconnection.py`
- **Force disconnect a player from all connections (WebSocket only).** (1 connections) — `server/realtime/connection_disconnection.py`
- **Unit tests for connection disconnection. Tests the connection disconnection…** (1 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **Intentional logout via force_disconnect must still track leave…** (1 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **Intentional logout with empty player_websockets must still clear rooms and…** (1 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **force_disconnect with no sockets must still track intentional leave.** (1 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **force_disconnect with sockets delegates to disconnect_websocket.** (1 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- *... and 7 more nodes in this community*

## Relationships

- [Community 531](Community_531.md) (17 shared connections)
- [Community 1006](Community_1006.md) (7 shared connections)
- [Community 1189](Community_1189.md) (5 shared connections)
- [Community 42](Community_42.md) (4 shared connections)
- [Community 1248](Community_1248.md) (4 shared connections)
- [Community 38](Community_38.md) (2 shared connections)
- [Community 586](Community_586.md) (2 shared connections)
- [Community 136](Community_136.md) (1 shared connections)

## Source Files

- `server/realtime/connection_disconnection.py`
- `server/tests/unit/realtime/test_connection_disconnection.py`

## Audit Trail

- EXTRACTED: 92 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*