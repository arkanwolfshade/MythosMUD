# connection_establishment.py

> 40 nodes

## Key Concepts

- **connection_establishment.py** (42 connections) — `server/realtime/connection_establishment.py`
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
- *... and 15 more nodes in this community*

## Relationships

- [test_connection_establishment.py](test_connection_establishment.py.md) (38 shared connections)
- [test_connection_establishment_ws.py](test_connection_establishment_ws.py.md) (17 shared connections)
- [get_logger](get_logger.md) (11 shared connections)
- [connection_manager_methods.py](connection_manager_methods.py.md) (10 shared connections)
- [disconnect_grace_period.py](disconnect_grace_period.py.md) (3 shared connections)
- [test_connection_session_management.py](test_connection_session_management.py.md) (2 shared connections)
- [test_rest_command.py](test_rest_command.py.md) (2 shared connections)
- [sqlalchemy.md](sqlalchemy.md.md) (2 shared connections)
- [.connect_websocket](connect_websocket.md) (1 shared connections)
- [DatabaseError](DatabaseError.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (1 shared connections)

## Source Files

- `server/realtime/connection_establishment.py`

## Audit Trail

- EXTRACTED: 170 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*