# Server Realtime (60)

> 30 nodes

## Key Concepts

- **connection_disconnection.py** (17 connections) — `server/realtime/connection_disconnection.py`
- **_DisconnectConnectionManager** (15 connections) — `server/realtime/connection_disconnection.py`
- **disconnect_all_websockets_impl()** (13 connections) — `server/realtime/connection_disconnection.py`
- **_cleanup_room_subscriptions()** (13 connections) — `server/realtime/connection_disconnection.py`
- **cleanup_websocket_disconnect()** (13 connections) — `server/realtime/connection_disconnection.py`
- **disconnect_connection_by_id_impl()** (12 connections) — `server/realtime/connection_disconnection.py`
- **UUID** (11 connections)
- **_cleanup_player_data()** (10 connections) — `server/realtime/connection_disconnection.py`
- **_cleanup_fully_disconnected_player()** (8 connections) — `server/realtime/connection_disconnection.py`
- **.has_websocket_connection()** (7 connections) — `server/realtime/connection_disconnection.py`
- **_is_non_intentional_force_disconnect()** (6 connections) — `server/realtime/connection_disconnection.py`
- **_disconnect_single_websocket()** (6 connections) — `server/realtime/connection_disconnection.py`
- **_disconnect_websocket_by_connection_id()** (5 connections) — `server/realtime/connection_disconnection.py`
- **_cleanup_connection_tracking()** (4 connections) — `server/realtime/connection_disconnection.py`
- **.disconnect_connection_by_id()** (3 connections) — `server/realtime/connection_manager.py`
- **Protocol** (1 connections)
- **Disconnect a specific connection by its ID.** (1 connections) — `server/realtime/connection_manager.py`
- **Connection disconnection management for connection manager.  This module handles** (1 connections) — `server/realtime/connection_disconnection.py`
- **Connection manager surface used by disconnection helpers.** (1 connections) — `server/realtime/connection_disconnection.py`
- **Return True when the player still has at least one WebSocket connection.** (1 connections) — `server/realtime/connection_disconnection.py`
- **True when force-disconnect should skip leave tracking and keep room membership.** (1 connections) — `server/realtime/connection_disconnection.py`
- **Remove connection registry entries; safe when already cleaned up elsewhere.** (1 connections) — `server/realtime/connection_disconnection.py`
- **Close one WebSocket and clean tracking. Idempotent for duplicate disconnect call** (1 connections) — `server/realtime/connection_disconnection.py`
- **Disconnect all WebSocket connections for a player.      Args:         connection** (1 connections) — `server/realtime/connection_disconnection.py`
- **Clean up room subscriptions if needed.      Args:         player_id: The player'** (1 connections) — `server/realtime/connection_disconnection.py`
- *... and 5 more nodes in this community*

## Relationships

- [Server Realtime (51)](Server_Realtime_%2851%29.md) (23 shared connections)
- [Server Realtime (85)](Server_Realtime_%2885%29.md) (8 shared connections)
- [Server Realtime (7)](Server_Realtime_%287%29.md) (3 shared connections)
- [Server Realtime (4)](Server_Realtime_%284%29.md) (2 shared connections)

## Source Files

- `server/realtime/connection_disconnection.py`
- `server/realtime/connection_manager.py`

## Audit Trail

- EXTRACTED: 158 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*