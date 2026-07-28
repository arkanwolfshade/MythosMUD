# Realtime Event Delegation

> 57 nodes · cohesion 0.04

## Key Concepts

- **test_connection_disconnection.py** (34 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **connection_disconnection.py** (31 connections) — `server/realtime/connection_disconnection.py`
- **_DisconnectConnectionManager** (19 connections) — `server/realtime/connection_disconnection.py`
- **test_connection_disconnection_websockets.py** (15 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **cleanup_websocket_disconnect()** (14 connections) — `server/realtime/connection_disconnection.py`
- **_cleanup_room_subscriptions()** (13 connections) — `server/realtime/connection_disconnection.py`
- **disconnect_all_websockets_impl()** (13 connections) — `server/realtime/connection_disconnection.py`
- **disconnect_connection_by_id_impl()** (13 connections) — `server/realtime/connection_disconnection.py`
- **_track_disconnect_if_needed()** (13 connections) — `server/realtime/connection_disconnection.py`
- **rate_limiter.py** (12 connections) — `server/realtime/rate_limiter.py`
- **UUID** (11 connections)
- **_cleanup_player_data()** (10 connections) — `server/realtime/connection_disconnection.py`
- **_cleanup_fully_disconnected_player()** (8 connections) — `server/realtime/connection_disconnection.py`
- **_disconnect_single_websocket()** (7 connections) — `server/realtime/connection_disconnection.py`
- **.has_websocket_connection()** (7 connections) — `server/realtime/connection_disconnection.py`
- **_disconnect_websocket_by_connection_id()** (6 connections) — `server/realtime/connection_disconnection.py`
- **_cleanup_connection_tracking()** (4 connections) — `server/realtime/connection_disconnection.py`
- **test_cleanup_player_data_has_connection()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_disconnect_connection_by_id_impl_websocket()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **.disconnect_connection_by_id()** (3 connections) — `server/realtime/connection_manager.py`
- **test_cleanup_player_data()** (3 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_cleanup_room_subscriptions()** (3 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_cleanup_room_subscriptions_force_disconnect()** (3 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_cleanup_room_subscriptions_has_connection()** (3 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_cleanup_websocket_disconnect()** (3 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- *... and 32 more nodes in this community*

## Relationships

- [Distributed Event Bus](Distributed_Event_Bus.md) (12 shared connections)
- [Room Occupant Events](Room_Occupant_Events.md) (8 shared connections)
- [WebSocket Connection Setup](WebSocket_Connection_Setup.md) (8 shared connections)
- [Message Queue Cleanup](Message_Queue_Cleanup.md) (5 shared connections)
- [Realtime Messaging Message](Realtime_Messaging_Message.md) (4 shared connections)
- [Realtime Connection Impl](Realtime_Connection_Impl.md) (3 shared connections)
- [AnyIO Code Review](AnyIO_Code_Review.md) (3 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (1 shared connections)
- [Restart Invalidating JWT](Restart_Invalidating_JWT.md) (1 shared connections)
- [Connection Disconnection Cleanup](Connection_Disconnection_Cleanup.md) (1 shared connections)

## Source Files

- `server/realtime/connection_disconnection.py`
- `server/realtime/connection_manager.py`
- `server/realtime/rate_limiter.py`
- `server/tests/unit/realtime/test_connection_disconnection.py`
- `server/tests/unit/realtime/test_connection_disconnection_websockets.py`

## Audit Trail

- EXTRACTED: 308 (97%)
- INFERRED: 8 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*