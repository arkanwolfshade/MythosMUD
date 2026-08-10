# Command Testing Guide

> 20 nodes

## Key Concepts

- **realtime.py** (13 connections) — `server/schemas/realtime/realtime.py`
- **PresenceStatistics** (10 connections) — `server/schemas/realtime/presence_data.py`
- **SessionStatistics** (10 connections) — `server/schemas/realtime/presence_data.py`
- **ErrorStatistics** (10 connections) — `server/schemas/realtime/presence_data.py`
- **NewGameSessionResponse** (10 connections) — `server/schemas/realtime/realtime.py`
- **ConnectionStatisticsResponse** (10 connections) — `server/schemas/realtime/realtime.py`
- **PresenceInfo** (6 connections) — `server/schemas/realtime/realtime.py`
- **BaseModel** (6 connections)
- **HealthInfo** (6 connections) — `server/schemas/realtime/realtime.py`
- **presence_data.py** (5 connections) — `server/schemas/realtime/presence_data.py`
- **BaseModel** (3 connections)
- **Presence and health statistics schema for MythosMUD.  This module defines Pydant** (1 connections) — `server/schemas/realtime/presence_data.py`
- **Presence statistics for connection monitoring.      This model represents aggreg** (1 connections) — `server/schemas/realtime/presence_data.py`
- **Session statistics for connection monitoring.      This model represents aggrega** (1 connections) — `server/schemas/realtime/presence_data.py`
- **Error statistics for connection monitoring.      This model represents aggregate** (1 connections) — `server/schemas/realtime/presence_data.py`
- **Real-time API response schemas for MythosMUD server.  This module provides Pydan** (1 connections) — `server/schemas/realtime/realtime.py`
- **Presence information for a player connection.** (1 connections) — `server/schemas/realtime/realtime.py`
- **Health information for a player connection.** (1 connections) — `server/schemas/realtime/realtime.py`
- **Response model for new game session endpoint.** (1 connections) — `server/schemas/realtime/realtime.py`
- **Response model for connection statistics endpoint.** (1 connections) — `server/schemas/realtime/realtime.py`

## Relationships

- [Client Memory Leak Detector](Client_Memory_Leak_Detector.md) (14 shared connections)
- [NATS Message Schemas](NATS_Message_Schemas.md) (3 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (2 shared connections)
- [Level and XP Curve](Level_and_XP_Curve.md) (1 shared connections)

## Source Files

- `server/schemas/realtime/presence_data.py`
- `server/schemas/realtime/realtime.py`

## Audit Trail

- EXTRACTED: 68 (69%)
- INFERRED: 30 (31%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*