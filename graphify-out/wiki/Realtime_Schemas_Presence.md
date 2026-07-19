# Realtime Schemas Presence

> 23 nodes · cohesion 0.19

## Key Concepts

- **realtime.py** (12 connections) — `server/schemas/realtime/realtime.py`
- **ErrorStatistics** (10 connections) — `server/schemas/realtime/presence_data.py`
- **PresenceStatistics** (10 connections) — `server/schemas/realtime/presence_data.py`
- **SessionStatistics** (10 connections) — `server/schemas/realtime/presence_data.py`
- **ConnectionStatisticsResponse** (9 connections) — `server/schemas/realtime/realtime.py`
- **NewGameSessionResponse** (9 connections) — `server/schemas/realtime/realtime.py`
- **PlayerConnectionsResponse** (9 connections) — `server/schemas/realtime/realtime.py`
- **SessionInfo** (9 connections) — `server/schemas/realtime/realtime.py`
- **__init__.py** (8 connections) — `server/schemas/realtime/__init__.py`
- **HealthInfo** (6 connections) — `server/schemas/realtime/realtime.py`
- **PresenceInfo** (6 connections) — `server/schemas/realtime/realtime.py`
- **presence_data.py** (5 connections) — `server/schemas/realtime/presence_data.py`
- **Realtime domain schemas: realtime API, NATS messages, WebSocket messages.** (1 connections) — `server/schemas/realtime/__init__.py`
- **Presence and health statistics schema for MythosMUD.  This module defines Pydant** (1 connections) — `server/schemas/realtime/presence_data.py`
- **Presence statistics for connection monitoring.      This model represents aggreg** (1 connections) — `server/schemas/realtime/presence_data.py`
- **Session statistics for connection monitoring.      This model represents aggrega** (1 connections) — `server/schemas/realtime/presence_data.py`
- **Error statistics for connection monitoring.      This model represents aggregate** (1 connections) — `server/schemas/realtime/presence_data.py`
- **Real-time API response schemas for MythosMUD server.  This module provides Pydan** (1 connections) — `server/schemas/realtime/realtime.py`
- **Presence information for a player connection.** (1 connections) — `server/schemas/realtime/realtime.py`
- **Session information for a player connection.** (1 connections) — `server/schemas/realtime/realtime.py`
- **Health information for a player connection.** (1 connections) — `server/schemas/realtime/realtime.py`
- **Response model for player connection information endpoint.** (1 connections) — `server/schemas/realtime/realtime.py`
- **Response model for new game session endpoint.** (1 connections) — `server/schemas/realtime/realtime.py`

## Relationships

- [[Admin NPC Schemas]] (12 shared connections)
- [[Realtime WebSocket Auth]] (5 shared connections)
- [[NATS Message Schemas]] (2 shared connections)
- [[Monitoring Response Models]] (1 shared connections)

## Source Files

- `server/schemas/realtime/__init__.py`
- `server/schemas/realtime/presence_data.py`
- `server/schemas/realtime/realtime.py`

## Audit Trail

- EXTRACTED: 78 (68%)
- INFERRED: 36 (32%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
