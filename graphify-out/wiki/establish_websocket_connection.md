# establish_websocket_connection

> 36 nodes

## Key Concepts

- **_EstablishmentConnectionManager** (25 connections) — `server/realtime/connection_establishment.py`
- **establish_websocket_connection()** (25 connections) — `server/realtime/connection_establishment.py`
- **UUID** (16 connections)
- **_track_player_presence()** (13 connections) — `server/realtime/connection_establishment.py`
- **_find_dead_connections()** (11 connections) — `server/realtime/connection_establishment.py`
- **_setup_player_and_room()** (11 connections) — `server/realtime/connection_establishment.py`
- **_cleanup_dead_connections()** (10 connections) — `server/realtime/connection_establishment.py`
- **_bind_accepted_websocket()** (9 connections) — `server/realtime/connection_establishment.py`
- **_cleanup_failed_connection()** (9 connections) — `server/realtime/connection_establishment.py`
- **_register_new_connection()** (9 connections) — `server/realtime/connection_establishment.py`
- **_setup_connection_metadata()** (9 connections) — `server/realtime/connection_establishment.py`
- **_setup_session_tracking()** (9 connections) — `server/realtime/connection_establishment.py`
- **_update_player_connection_list()** (9 connections) — `server/realtime/connection_establishment.py`
- **_reconcile_prior_session()** (6 connections) — `server/realtime/connection_establishment.py`
- **Player** (5 connections)
- **.broadcast_connection_message()** (4 connections) — `server/realtime/connection_establishment.py`
- **.get_player()** (4 connections) — `server/realtime/connection_establishment.py`
- **.track_player_connected()** (4 connections) — `server/realtime/connection_establishment.py`
- **WebSocket** (3 connections)
- **Protocol** (1 connections)
- **Update player's connection list to only include active connections. Args:…** (1 connections) — `server/realtime/connection_establishment.py`
- **Clean up dead connections under lock. Args: dead_connection_ids: List of dead…** (1 connections) — `server/realtime/connection_establishment.py`
- **Register a new WebSocket connection. Args: websocket: The WebSocket connection…** (1 connections) — `server/realtime/connection_establishment.py`
- **Create and store connection metadata. Args: connection_id: The connection ID…** (1 connections) — `server/realtime/connection_establishment.py`
- **Track connection in session. Args: connection_id: The connection ID player_id:…** (1 connections) — `server/realtime/connection_establishment.py`
- *... and 11 more nodes in this community*

## Relationships

- [test_connection_establishment.py](test_connection_establishment.py.md) (36 shared connections)
- [test_connection_establishment_ws.py](test_connection_establishment_ws.py.md) (16 shared connections)
- [get_logger](get_logger.md) (15 shared connections)
- [connection_manager_methods.py](connection_manager_methods.py.md) (2 shared connections)
- [RateLimiter](RateLimiter.md) (2 shared connections)
- [build_event](build_event.md) (1 shared connections)
- [.connect_websocket](connect_websocket.md) (1 shared connections)
- [test_connection_session_management.py](test_connection_session_management.py.md) (1 shared connections)
- [test_rest_command.py](test_rest_command.py.md) (1 shared connections)
- [start_grace_period](start_grace_period.md) (1 shared connections)

## Source Files

- `server/realtime/connection_establishment.py`

## Audit Trail

- EXTRACTED: 138 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*