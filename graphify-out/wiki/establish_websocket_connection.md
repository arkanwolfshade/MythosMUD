# establish_websocket_connection

> 34 nodes

## Key Concepts

- **establish_websocket_connection()** (26 connections) — `server/realtime/connection_establishment.py`
- **_EstablishmentConnectionManager** (23 connections) — `server/realtime/connection_establishment.py`
- **UUID** (14 connections)
- **_track_player_presence()** (13 connections) — `server/realtime/connection_establishment.py`
- **_find_dead_connections()** (11 connections) — `server/realtime/connection_establishment.py`
- **_setup_player_and_room()** (11 connections) — `server/realtime/connection_establishment.py`
- **_cleanup_dead_connections()** (10 connections) — `server/realtime/connection_establishment.py`
- **_cleanup_failed_connection()** (9 connections) — `server/realtime/connection_establishment.py`
- **_register_new_connection()** (9 connections) — `server/realtime/connection_establishment.py`
- **_setup_connection_metadata()** (9 connections) — `server/realtime/connection_establishment.py`
- **_setup_session_tracking()** (9 connections) — `server/realtime/connection_establishment.py`
- **_update_player_connection_list()** (9 connections) — `server/realtime/connection_establishment.py`
- **_remove_dead_connection()** (7 connections) — `server/realtime/connection_establishment.py`
- **.get_player()** (5 connections) — `server/realtime/connection_establishment.py`
- **Player** (5 connections)
- **.broadcast_connection_message()** (4 connections) — `server/realtime/connection_establishment.py`
- **.track_player_connected()** (4 connections) — `server/realtime/connection_establishment.py`
- **WebSocket** (2 connections)
- **Protocol** (1 connections)
- **Remove a single dead connection from tracking structures. Args: conn_id: The…** (1 connections) — `server/realtime/connection_establishment.py`
- **Update player's connection list to only include active connections. Args:…** (1 connections) — `server/realtime/connection_establishment.py`
- **Clean up dead connections under lock. Args: dead_connection_ids: List of dead…** (1 connections) — `server/realtime/connection_establishment.py`
- **Register a new WebSocket connection. Args: websocket: The WebSocket connection…** (1 connections) — `server/realtime/connection_establishment.py`
- **Create and store connection metadata. Args: connection_id: The connection ID…** (1 connections) — `server/realtime/connection_establishment.py`
- **Track connection in session. Args: connection_id: The connection ID player_id:…** (1 connections) — `server/realtime/connection_establishment.py`
- *... and 9 more nodes in this community*

## Relationships

- [test_connection_establishment.py](test_connection_establishment.py.md) (36 shared connections)
- [get_logger](get_logger.md) (18 shared connections)
- [_FakeWebSocket](_FakeWebSocket.md) (11 shared connections)
- [_meta](_meta.md) (5 shared connections)
- [RateLimiter](RateLimiter.md) (1 shared connections)
- [handle_new_game_session_impl](handle_new_game_session_impl.md) (1 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)
- [websocket_helpers.py](websocket_helpers.py.md) (1 shared connections)
- [start_grace_period](start_grace_period.md) (1 shared connections)
- [test_rest_command.py](test_rest_command.py.md) (1 shared connections)

## Source Files

- `server/realtime/connection_establishment.py`

## Audit Trail

- EXTRACTED: 130 (96%)
- INFERRED: 6 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*