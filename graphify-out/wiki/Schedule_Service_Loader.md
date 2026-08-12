# Schedule Service Loader

> 35 nodes

## Key Concepts

- **realtime.py** (13 connections) — `server/schemas/realtime/realtime.py`
- **PresenceStatistics** (10 connections) — `server/schemas/realtime/presence_data.py`
- **SessionStatistics** (10 connections) — `server/schemas/realtime/presence_data.py`
- **ErrorStatistics** (10 connections) — `server/schemas/realtime/presence_data.py`
- **PlayerConnectionsResponse** (10 connections) — `server/schemas/realtime/realtime.py`
- **NewGameSessionResponse** (10 connections) — `server/schemas/realtime/realtime.py`
- **ConnectionStatisticsResponse** (10 connections) — `server/schemas/realtime/realtime.py`
- **_ensure_connection_manager()** (9 connections) — `server/api/real_time.py`
- **__init__.py** (9 connections) — `server/schemas/realtime/__init__.py`
- **SessionInfo** (9 connections) — `server/schemas/realtime/realtime.py`
- **get_player_connections()** (8 connections) — `server/api/real_time.py`
- **handle_new_game_session()** (8 connections) — `server/api/real_time.py`
- **get_connection_statistics()** (6 connections) — `server/api/real_time.py`
- **PresenceInfo** (6 connections) — `server/schemas/realtime/realtime.py`
- **BaseModel** (6 connections)
- **HealthInfo** (6 connections) — `server/schemas/realtime/realtime.py`
- **presence_data.py** (5 connections) — `server/schemas/realtime/presence_data.py`
- **Request** (4 connections)
- **BaseModel** (3 connections)
- **Ensure connection manager is available.     Raises LoggedHTTPException with prop** (1 connections) — `server/api/real_time.py`
- **Get connection information for a player.     Returns detailed connection metadat** (1 connections) — `server/api/real_time.py`
- **Handle a new game session for a player.     This will disconnect existing connec** (1 connections) — `server/api/real_time.py`
- **Get comprehensive connection statistics.     Returns detailed statistics about a** (1 connections) — `server/api/real_time.py`
- **Realtime domain schemas: realtime API, NATS messages, WebSocket messages.** (1 connections) — `server/schemas/realtime/__init__.py`
- **Presence and health statistics schema for MythosMUD.  This module defines Pydant** (1 connections) — `server/schemas/realtime/presence_data.py`
- *... and 10 more nodes in this community*

## Relationships

- [Memory Threshold Monitor](Memory_Threshold_Monitor.md) (12 shared connections)
- [Client Event Store](Client_Event_Store.md) (4 shared connections)
- [Game Terminal Panels](Game_Terminal_Panels.md) (4 shared connections)
- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (2 shared connections)
- [NATS Message Schemas](NATS_Message_Schemas.md) (2 shared connections)

## Source Files

- `server/api/real_time.py`
- `server/schemas/realtime/__init__.py`
- `server/schemas/realtime/presence_data.py`
- `server/schemas/realtime/realtime.py`

## Audit Trail

- EXTRACTED: 132 (79%)
- INFERRED: 36 (21%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*