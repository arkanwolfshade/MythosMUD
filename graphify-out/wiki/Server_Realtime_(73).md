# Server Realtime (73)

> 21 nodes

## Key Concepts

- **connection_establishment.py** (22 connections) — `server/realtime/connection_establishment.py`
- **establish_websocket_connection()** (21 connections) — `server/realtime/connection_establishment.py`
- **_find_dead_connections()** (11 connections) — `server/realtime/connection_establishment.py`
- **UUID** (11 connections)
- **Any** (11 connections)
- **_setup_player_and_room()** (10 connections) — `server/realtime/connection_establishment.py`
- **_cleanup_failed_connection()** (10 connections) — `server/realtime/connection_establishment.py`
- **_register_new_connection()** (9 connections) — `server/realtime/connection_establishment.py`
- **_setup_connection_metadata()** (9 connections) — `server/realtime/connection_establishment.py`
- **_setup_session_tracking()** (9 connections) — `server/realtime/connection_establishment.py`
- **_track_player_presence()** (8 connections) — `server/realtime/connection_establishment.py`
- **WebSocket** (2 connections)
- **Connection establishment management for connection manager.  This module handles** (1 connections) — `server/realtime/connection_establishment.py`
- **Find dead WebSocket connections for a player before acquiring lock.      Args:** (1 connections) — `server/realtime/connection_establishment.py`
- **Register a new WebSocket connection.      Args:         websocket: The WebSocket** (1 connections) — `server/realtime/connection_establishment.py`
- **Create and store connection metadata.      Args:         connection_id: The conn** (1 connections) — `server/realtime/connection_establishment.py`
- **Track connection in session.      Args:         connection_id: The connection ID** (1 connections) — `server/realtime/connection_establishment.py`
- **Get player and setup room subscription.      Args:         player_id: The player** (1 connections) — `server/realtime/connection_establishment.py`
- **Track player presence and broadcast connection message.      Args:         playe** (1 connections) — `server/realtime/connection_establishment.py`
- **Cleanup connection on failure.      Args:         connection_id: The connection** (1 connections) — `server/realtime/connection_establishment.py`
- **Establish a new WebSocket connection.      Args:         websocket: The WebSocke** (1 connections) — `server/realtime/connection_establishment.py`

## Relationships

- [Server Realtime (63)](Server_Realtime_%2863%29.md) (22 shared connections)
- [Server Realtime (74)](Server_Realtime_%2874%29.md) (9 shared connections)
- [Server Commands](Server_Commands.md) (3 shared connections)
- [Server Persistence](Server_Persistence.md) (3 shared connections)
- [Server Realtime (88)](Server_Realtime_%2888%29.md) (3 shared connections)
- [Server Realtime (7)](Server_Realtime_%287%29.md) (2 shared connections)
- [Server Admin](Server_Admin.md) (1 shared connections)
- [Server Realtime (153)](Server_Realtime_%28153%29.md) (1 shared connections)
- [Server Realtime (142)](Server_Realtime_%28142%29.md) (1 shared connections)
- [Server Realtime (143)](Server_Realtime_%28143%29.md) (1 shared connections)
- [Server Realtime (145)](Server_Realtime_%28145%29.md) (1 shared connections)
- [Server Realtime (144)](Server_Realtime_%28144%29.md) (1 shared connections)

## Source Files

- `server/realtime/connection_establishment.py`

## Audit Trail

- EXTRACTED: 140 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*