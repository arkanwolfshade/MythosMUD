# player event state

> 21 nodes

## Key Concepts

- **connection_establishment.py** (24 connections) — `server/realtime/connection_establishment.py`
- **establish_websocket_connection()** (23 connections) — `server/realtime/connection_establishment.py`
- **UUID** (12 connections)
- **Any** (12 connections)
- **_setup_player_and_room()** (10 connections) — `server/realtime/connection_establishment.py`
- **_cleanup_failed_connection()** (10 connections) — `server/realtime/connection_establishment.py`
- **_register_new_connection()** (9 connections) — `server/realtime/connection_establishment.py`
- **_setup_connection_metadata()** (9 connections) — `server/realtime/connection_establishment.py`
- **_setup_session_tracking()** (9 connections) — `server/realtime/connection_establishment.py`
- **_track_player_presence()** (8 connections) — `server/realtime/connection_establishment.py`
- **_cancel_rest_countdown_if_active()** (6 connections) — `server/realtime/connection_establishment.py`
- **WebSocket** (2 connections)
- **Connection establishment management for connection manager.  This module handles** (1 connections) — `server/realtime/connection_establishment.py`
- **Register a new WebSocket connection.      Args:         websocket: The WebSocket** (1 connections) — `server/realtime/connection_establishment.py`
- **Create and store connection metadata.      Args:         connection_id: The conn** (1 connections) — `server/realtime/connection_establishment.py`
- **Track connection in session.      Args:         connection_id: The connection ID** (1 connections) — `server/realtime/connection_establishment.py`
- **Get player and setup room subscription.      Args:         player_id: The player** (1 connections) — `server/realtime/connection_establishment.py`
- **Track player presence and broadcast connection message.      Args:         playe** (1 connections) — `server/realtime/connection_establishment.py`
- **Cleanup connection on failure.      Args:         connection_id: The connection** (1 connections) — `server/realtime/connection_establishment.py`
- **Cancel leftover /rest countdown from a prior session (crashed client / mid-rest** (1 connections) — `server/realtime/connection_establishment.py`
- **Establish a new WebSocket connection.      Args:         websocket: The WebSocke** (1 connections) — `server/realtime/connection_establishment.py`

## Relationships

- [connection establishment realtime](connection_establishment_realtime.md) (18 shared connections)
- [cleanup combat handler](cleanup_combat_handler.md) (6 shared connections)
- [useDraggablePanelInteractions draggableP](useDraggablePanelInteractions_draggableP.md) (4 shared connections)
- [event bus events](event_bus_events.md) (4 shared connections)
- [models npc rationale](models_npc_rationale.md) (3 shared connections)
- [Database Config](Database_Config.md) (3 shared connections)
- [persistence rationale room](persistence_rationale_room.md) (3 shared connections)
- [connection disconnection realtime](connection_disconnection_realtime.md) (3 shared connections)
- [Room Broadcast](Room_Broadcast.md) (3 shared connections)
- [room game service](room_game_service.md) (3 shared connections)
- [rest grace period](rest_grace_period.md) (2 shared connections)
- [chat game service](chat_game_service.md) (2 shared connections)

## Source Files

- `server/realtime/connection_establishment.py`

## Audit Trail

- EXTRACTED: 141 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*