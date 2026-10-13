# Community 538

> 32 nodes

## Key Concepts

- **connection_establishment.py** (41 connections) — `server/realtime/connection_establishment.py`
- **_EstablishmentConnectionManager** (25 connections) — `server/realtime/connection_establishment.py`
- **UUID** (16 connections)
- **_track_player_presence()** (13 connections) — `server/realtime/connection_establishment.py`
- **_cleanup_dead_connections()** (10 connections) — `server/realtime/connection_establishment.py`
- **_bind_accepted_websocket()** (9 connections) — `server/realtime/connection_establishment.py`
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
- **Create and store connection metadata. Args: connection_id: The connection ID…** (1 connections) — `server/realtime/connection_establishment.py`
- **Track connection in session. Args: connection_id: The connection ID player_id:…** (1 connections) — `server/realtime/connection_establishment.py`
- *... and 7 more nodes in this community*

## Relationships

- [Community 81](Community_81.md) (47 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (12 shared connections)
- [Community 980](Community_980.md) (4 shared connections)
- [Community 119](Community_119.md) (3 shared connections)
- [Community 155](Community_155.md) (2 shared connections)
- [Community 169](Community_169.md) (2 shared connections)
- [Community 146](Community_146.md) (2 shared connections)
- [Community 76](Community_76.md) (2 shared connections)
- [Community 139](Community_139.md) (2 shared connections)
- [Invite & NPC DB Scripts](Invite_&_NPC_DB_Scripts.md) (2 shared connections)

## Source Files

- `server/realtime/connection_establishment.py`

## Audit Trail

- EXTRACTED: 134 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*