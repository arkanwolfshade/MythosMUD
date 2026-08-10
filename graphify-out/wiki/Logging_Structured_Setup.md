# Logging Structured Setup

> 19 nodes

## Key Concepts

- **connection_establishment.py** (22 connections) — `server/realtime/connection_establishment.py`
- **establish_websocket_connection()** (21 connections) — `server/realtime/connection_establishment.py`
- **UUID** (11 connections)
- **Any** (11 connections)
- **_cleanup_dead_connections()** (10 connections) — `server/realtime/connection_establishment.py`
- **_update_player_connection_list()** (9 connections) — `server/realtime/connection_establishment.py`
- **_register_new_connection()** (9 connections) — `server/realtime/connection_establishment.py`
- **_setup_connection_metadata()** (9 connections) — `server/realtime/connection_establishment.py`
- **_track_player_presence()** (8 connections) — `server/realtime/connection_establishment.py`
- **_remove_dead_connection()** (7 connections) — `server/realtime/connection_establishment.py`
- **WebSocket** (2 connections)
- **Connection establishment management for connection manager.  This module handles** (1 connections) — `server/realtime/connection_establishment.py`
- **Remove a single dead connection from tracking structures.      Args:         con** (1 connections) — `server/realtime/connection_establishment.py`
- **Update player's connection list to only include active connections.      Args:** (1 connections) — `server/realtime/connection_establishment.py`
- **Clean up dead connections under lock.      Args:         dead_connection_ids: Li** (1 connections) — `server/realtime/connection_establishment.py`
- **Register a new WebSocket connection.      Args:         websocket: The WebSocket** (1 connections) — `server/realtime/connection_establishment.py`
- **Create and store connection metadata.      Args:         connection_id: The conn** (1 connections) — `server/realtime/connection_establishment.py`
- **Track player presence and broadcast connection message.      Args:         playe** (1 connections) — `server/realtime/connection_establishment.py`
- **Establish a new WebSocket connection.      Args:         websocket: The WebSocke** (1 connections) — `server/realtime/connection_establishment.py`

## Relationships

- [WebSocket Connection Setup](WebSocket_Connection_Setup.md) (18 shared connections)
- [Services Npc Startup](Services_Npc_Startup.md) (4 shared connections)
- [App Game Tick](App_Game_Tick.md) (4 shared connections)
- [Components Ui Designtokens](Components_Ui_Designtokens.md) (4 shared connections)
- [Realtime Connection Impl](Realtime_Connection_Impl.md) (4 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (3 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (3 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (2 shared connections)
- [Room Occupant Events](Room_Occupant_Events.md) (2 shared connections)
- [Level and XP Curve](Level_and_XP_Curve.md) (1 shared connections)
- [test_validate_combat_state_in_combat_required](test_validate_combat_state_in_combat_required.md) (1 shared connections)
- [test_update_player_connection_list_with_active](test_update_player_connection_list_with_active.md) (1 shared connections)

## Source Files

- `server/realtime/connection_establishment.py`

## Audit Trail

- EXTRACTED: 126 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*