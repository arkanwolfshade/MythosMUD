# connection_establishment.py

> 36 nodes

## Key Concepts

- **connection_establishment.py** (42 connections) — `server/realtime/connection_establishment.py`
- **_EstablishmentConnectionManager** (25 connections) — `server/realtime/connection_establishment.py`
- **UUID** (16 connections)
- **_track_player_presence()** (13 connections) — `server/realtime/connection_establishment.py`
- **_setup_player_and_room()** (11 connections) — `server/realtime/connection_establishment.py`
- **_cleanup_dead_connections()** (10 connections) — `server/realtime/connection_establishment.py`
- **_bind_accepted_websocket()** (9 connections) — `server/realtime/connection_establishment.py`
- **_cleanup_failed_connection()** (9 connections) — `server/realtime/connection_establishment.py`
- **_register_new_connection()** (9 connections) — `server/realtime/connection_establishment.py`
- **_setup_connection_metadata()** (9 connections) — `server/realtime/connection_establishment.py`
- **_setup_session_tracking()** (9 connections) — `server/realtime/connection_establishment.py`
- **_update_player_connection_list()** (9 connections) — `server/realtime/connection_establishment.py`
- **_remove_dead_connection()** (7 connections) — `server/realtime/connection_establishment.py`
- **_reconcile_prior_session()** (6 connections) — `server/realtime/connection_establishment.py`
- **Player** (5 connections)
- **.broadcast_connection_message()** (4 connections) — `server/realtime/connection_establishment.py`
- **.get_player()** (4 connections) — `server/realtime/connection_establishment.py`
- **.track_player_connected()** (4 connections) — `server/realtime/connection_establishment.py`
- **WebSocket** (3 connections)
- **Protocol** (1 connections)
- **Connection establishment management for connection manager. This module handles…** (1 connections) — `server/realtime/connection_establishment.py`
- **Remove a single dead connection from tracking structures. Args: conn_id: The…** (1 connections) — `server/realtime/connection_establishment.py`
- **Update player's connection list to only include active connections. Args:…** (1 connections) — `server/realtime/connection_establishment.py`
- **Clean up dead connections under lock. Args: dead_connection_ids: List of dead…** (1 connections) — `server/realtime/connection_establishment.py`
- **Register a new WebSocket connection. Args: websocket: The WebSocket connection…** (1 connections) — `server/realtime/connection_establishment.py`
- *... and 11 more nodes in this community*

## Relationships

- [test_connection_establishment.py](test_connection_establishment.py.md) (40 shared connections)
- [establish_websocket_connection](establish_websocket_connection.md) (11 shared connections)
- [get_logger](get_logger.md) (11 shared connections)
- [test_connection_session_management.py](test_connection_session_management.py.md) (7 shared connections)
- [MessageQueue](MessageQueue.md) (4 shared connections)
- [RateLimiter](RateLimiter.md) (2 shared connections)
- [test_rest_command.py](test_rest_command.py.md) (2 shared connections)
- [start_grace_period](start_grace_period.md) (2 shared connections)
- [pytest.md](pytest.md.md) (2 shared connections)
- [PerformanceTracker](PerformanceTracker.md) (1 shared connections)
- [test_player_disconnect_handlers.py](test_player_disconnect_handlers.py.md) (1 shared connections)

## Source Files

- `server/realtime/connection_establishment.py`

## Audit Trail

- EXTRACTED: 147 (97%)
- INFERRED: 5 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*