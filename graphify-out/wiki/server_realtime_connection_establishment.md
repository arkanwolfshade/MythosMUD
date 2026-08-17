# server realtime connection establishment

> 32 nodes

## Key Concepts

- **connection_establishment.py** (32 connections) — `server/realtime/connection_establishment.py`
- **_EstablishmentConnectionManager** (21 connections) — `server/realtime/connection_establishment.py`
- **UUID** (16 connections)
- **_setup_player_and_room()** (11 connections) — `server/realtime/connection_establishment.py`
- **_track_player_presence()** (11 connections) — `server/realtime/connection_establishment.py`
- **_bind_accepted_websocket()** (9 connections) — `server/realtime/connection_establishment.py`
- **_cleanup_failed_connection()** (9 connections) — `server/realtime/connection_establishment.py`
- **_register_new_connection()** (9 connections) — `server/realtime/connection_establishment.py`
- **_setup_connection_metadata()** (9 connections) — `server/realtime/connection_establishment.py`
- **_setup_session_tracking()** (9 connections) — `server/realtime/connection_establishment.py`
- **_update_player_connection_list()** (9 connections) — `server/realtime/connection_establishment.py`
- **_reconcile_prior_session()** (5 connections) — `server/realtime/connection_establishment.py`
- **Player** (5 connections)
- **.broadcast_connection_message()** (4 connections) — `server/realtime/connection_establishment.py`
- **.get_player()** (4 connections) — `server/realtime/connection_establishment.py`
- **.track_player_connected()** (4 connections) — `server/realtime/connection_establishment.py`
- **WebSocket** (3 connections)
- **Protocol** (1 connections)
- **Connection establishment management for connection manager. This module handles…** (1 connections) — `server/realtime/connection_establishment.py`
- **Update player's connection list to only include active connections. Args:…** (1 connections) — `server/realtime/connection_establishment.py`
- **Register a new WebSocket connection. Args: websocket: The WebSocket connection…** (1 connections) — `server/realtime/connection_establishment.py`
- **Create and store connection metadata. Args: connection_id: The connection ID…** (1 connections) — `server/realtime/connection_establishment.py`
- **Track connection in session. Args: connection_id: The connection ID player_id:…** (1 connections) — `server/realtime/connection_establishment.py`
- **Register an accepted socket and attach session metadata.** (1 connections) — `server/realtime/connection_establishment.py`
- **Get player and setup room subscription. Args: player_id: The player's ID…** (1 connections) — `server/realtime/connection_establishment.py`
- *... and 7 more nodes in this community*

## Relationships

- [connectionmetadata](connectionmetadata.md) (38 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (11 shared connections)
- [server realtime connection establishment establish](server_realtime_connection_establishment_establish.md) (10 shared connections)
- [server realtime connection establishment find](server_realtime_connection_establishment_find.md) (3 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (1 shared connections)
- [server game skill service](server_game_skill_service.md) (1 shared connections)
- [server realtime connection session management](server_realtime_connection_session_management.md) (1 shared connections)

## Source Files

- `server/realtime/connection_establishment.py`

## Audit Trail

- EXTRACTED: 124 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*