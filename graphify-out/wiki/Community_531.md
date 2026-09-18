# Community 531

> 32 nodes

## Key Concepts

- **connection_disconnection.py** (28 connections) — `server/realtime/connection_disconnection.py`
- **_DisconnectConnectionManager** (22 connections) — `server/realtime/connection_disconnection.py`
- **UUID** (16 connections)
- **cleanup_websocket_disconnect()** (15 connections) — `server/realtime/connection_disconnection.py`
- **disconnect_all_websockets_impl()** (13 connections) — `server/realtime/connection_disconnection.py`
- **_apply_disconnect_side_effects()** (9 connections) — `server/realtime/connection_disconnection.py`
- **_close_and_untrack_websockets()** (6 connections) — `server/realtime/connection_disconnection.py`
- **_disconnect_single_websocket()** (6 connections) — `server/realtime/connection_disconnection.py`
- **_is_non_intentional_force_disconnect()** (6 connections) — `server/realtime/connection_disconnection.py`
- **_disconnect_websocket_by_connection_id()** (5 connections) — `server/realtime/connection_disconnection.py`
- **_cleanup_connection_tracking()** (4 connections) — `server/realtime/connection_disconnection.py`
- **.disconnect_websocket()** (3 connections) — `server/realtime/connection_disconnection.py`
- **.has_websocket_connection()** (3 connections) — `server/realtime/connection_disconnection.py`
- **.track_player_disconnected()** (3 connections) — `server/realtime/connection_disconnection.py`
- **.is_websocket_closed()** (2 connections) — `server/realtime/connection_disconnection.py`
- **.mark_websocket_closed()** (2 connections) — `server/realtime/connection_disconnection.py`
- **Protocol** (1 connections)
- **Connection disconnection management for connection manager. This module handles…** (1 connections) — `server/realtime/connection_disconnection.py`
- **Disconnect all WebSocket connections for a player. Args: connection_ids: List…** (1 connections) — `server/realtime/connection_disconnection.py`
- **Track leave if needed, then clear room subscriptions and player-scoped data.** (1 connections) — `server/realtime/connection_disconnection.py`
- **Close every tracked WebSocket for the player and drop player_websockets entry.** (1 connections) — `server/realtime/connection_disconnection.py`
- **Clean up WebSocket connections for a player. Args: player_id: The player's ID…** (1 connections) — `server/realtime/connection_disconnection.py`
- **Connection manager surface used by disconnection helpers.** (1 connections) — `server/realtime/connection_disconnection.py`
- **Close one WebSocket by connection ID and update player_websockets tracking.** (1 connections) — `server/realtime/connection_disconnection.py`
- **Return True when the player still has at least one WebSocket connection.** (1 connections) — `server/realtime/connection_disconnection.py`
- *... and 7 more nodes in this community*

## Relationships

- [Community 532](Community_532.md) (17 shared connections)
- [Community 586](Community_586.md) (14 shared connections)
- [Community 1189](Community_1189.md) (5 shared connections)
- [Community 42](Community_42.md) (5 shared connections)
- [Community 1006](Community_1006.md) (4 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (3 shared connections)
- [Community 136](Community_136.md) (1 shared connections)
- [Community 966](Community_966.md) (1 shared connections)
- [Community 1044](Community_1044.md) (1 shared connections)

## Source Files

- `server/realtime/connection_disconnection.py`

## Audit Trail

- EXTRACTED: 105 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*