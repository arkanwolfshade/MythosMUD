# Connection Disconnection Cleanup

> 80 nodes · cohesion 0.04

## Key Concepts

- **connection_disconnection.py** (28 connections) — `server/realtime/connection_disconnection.py`
- **test_connection_disconnection.py** (28 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **_DisconnectConnectionManager** (18 connections) — `server/realtime/connection_disconnection.py`
- **UUID** (14 connections) — `server/realtime/connection_disconnection.py`
- **cleanup_websocket_disconnect()** (13 connections) — `server/realtime/connection_disconnection.py`
- **disconnect_all_websockets_impl()** (13 connections) — `server/realtime/connection_disconnection.py`
- **disconnect_connection_by_id_impl()** (12 connections) — `server/realtime/connection_disconnection.py`
- **test_connection_disconnection_websockets.py** (12 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **_cleanup_room_subscriptions()** (11 connections) — `server/realtime/connection_disconnection.py`
- **_track_disconnect_if_needed()** (11 connections) — `server/realtime/connection_disconnection.py`
- **_cleanup_player_data()** (10 connections) — `server/realtime/connection_disconnection.py`
- **_cleanup_fully_disconnected_player()** (8 connections) — `server/realtime/connection_disconnection.py`
- **_disconnect_single_websocket()** (7 connections) — `server/realtime/connection_disconnection.py`
- **.has_websocket_connection()** (7 connections) — `server/realtime/connection_disconnection.py`
- **_disconnect_websocket_by_connection_id()** (6 connections) — `server/realtime/connection_disconnection.py`
- **_cleanup_connection_tracking()** (4 connections) — `server/realtime/connection_disconnection.py`
- **.disconnect_connection_by_id()** (3 connections) — `server/realtime/connection_manager.py`
- **test_cleanup_player_data()** (3 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_cleanup_player_data_has_connection()** (3 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_cleanup_room_subscriptions()** (3 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_cleanup_room_subscriptions_force_disconnect()** (3 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_cleanup_room_subscriptions_has_connection()** (3 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_cleanup_websocket_disconnect()** (3 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_cleanup_websocket_disconnect_when_mapping_cleared_during_close()** (3 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_disconnect_all_websockets()** (3 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- *... and 55 more nodes in this community*

## Relationships

- [[Room Occupant Events]] (15 shared connections)
- [[NPC Admin API]] (5 shared connections)
- [[Message Queue Cleanup]] (5 shared connections)
- [[Rate Limiter Service]] (5 shared connections)
- [[Realtime Connection]] (4 shared connections)
- [[Player Combat XP]] (1 shared connections)

## Source Files

- `server/realtime/connection_disconnection.py`
- `server/realtime/connection_manager.py`
- `server/tests/unit/realtime/test_connection_disconnection.py`
- `server/tests/unit/realtime/test_connection_disconnection_websockets.py`

## Audit Trail

- EXTRACTED: 307 (97%)
- INFERRED: 8 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
