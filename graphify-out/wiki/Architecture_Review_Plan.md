# Architecture Review Plan

> 18 nodes

## Key Concepts

- **connection_establishment.py** (22 connections) — `server/realtime/connection_establishment.py`
- **establish_websocket_connection()** (21 connections) — `server/realtime/connection_establishment.py`
- **_find_dead_connections()** (11 connections) — `server/realtime/connection_establishment.py`
- **UUID** (11 connections)
- **Any** (11 connections)
- **_setup_player_and_room()** (10 connections) — `server/realtime/connection_establishment.py`
- **_cleanup_failed_connection()** (10 connections) — `server/realtime/connection_establishment.py`
- **_setup_connection_metadata()** (9 connections) — `server/realtime/connection_establishment.py`
- **_setup_session_tracking()** (9 connections) — `server/realtime/connection_establishment.py`
- **_track_player_presence()** (8 connections) — `server/realtime/connection_establishment.py`
- **Connection establishment management for connection manager.  This module handles** (1 connections) — `server/realtime/connection_establishment.py`
- **Find dead WebSocket connections for a player before acquiring lock.      Args:** (1 connections) — `server/realtime/connection_establishment.py`
- **Create and store connection metadata.      Args:         connection_id: The conn** (1 connections) — `server/realtime/connection_establishment.py`
- **Track connection in session.      Args:         connection_id: The connection ID** (1 connections) — `server/realtime/connection_establishment.py`
- **Get player and setup room subscription.      Args:         player_id: The player** (1 connections) — `server/realtime/connection_establishment.py`
- **Track player presence and broadcast connection message.      Args:         playe** (1 connections) — `server/realtime/connection_establishment.py`
- **Cleanup connection on failure.      Args:         connection_id: The connection** (1 connections) — `server/realtime/connection_establishment.py`
- **Establish a new WebSocket connection.      Args:         websocket: The WebSocke** (1 connections) — `server/realtime/connection_establishment.py`

## Relationships

- [WebSocket Connection Setup](WebSocket_Connection_Setup.md) (22 shared connections)
- [Archive Npc Population](Archive_Npc_Population.md) (6 shared connections)
- [Archive Optimization Summary](Archive_Optimization_Summary.md) (5 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (3 shared connections)
- [Investigations Sessions Session](Investigations_Sessions_Session.md) (3 shared connections)
- [Combat Client Crash Report](Combat_Client_Crash_Report.md) (3 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (2 shared connections)
- [Playwright E2E Specs](Playwright_E2E_Specs.md) (2 shared connections)
- [Realtime Service Bundle](Realtime_Service_Bundle.md) (1 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (1 shared connections)
- [Persistence Item Repositories](Persistence_Item_Repositories.md) (1 shared connections)
- [Realtime Payload Optimizer](Realtime_Payload_Optimizer.md) (1 shared connections)

## Source Files

- `server/realtime/connection_establishment.py`

## Audit Trail

- EXTRACTED: 128 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*