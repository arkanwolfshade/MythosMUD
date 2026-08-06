# schedule services service

> 27 nodes

## Key Concepts

- **realtime.py** (13 connections) — `server/schemas/realtime/realtime.py`
- **PresenceStatistics** (12 connections) — `server/schemas/realtime/presence_data.py`
- **SessionStatistics** (12 connections) — `server/schemas/realtime/presence_data.py`
- **ErrorStatistics** (12 connections) — `server/schemas/realtime/presence_data.py`
- **PlayerConnectionsResponse** (10 connections) — `server/schemas/realtime/realtime.py`
- **NewGameSessionResponse** (10 connections) — `server/schemas/realtime/realtime.py`
- **ConnectionStatisticsResponse** (10 connections) — `server/schemas/realtime/realtime.py`
- **__init__.py** (9 connections) — `server/schemas/realtime/__init__.py`
- **SessionInfo** (9 connections) — `server/schemas/realtime/realtime.py`
- **PresenceInfo** (6 connections) — `server/schemas/realtime/realtime.py`
- **BaseModel** (6 connections)
- **HealthInfo** (6 connections) — `server/schemas/realtime/realtime.py`
- **presence_data.py** (5 connections) — `server/schemas/realtime/presence_data.py`
- **test_get_connection_statistics()** (5 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **BaseModel** (3 connections)
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
- *... and 2 more nodes in this community*

## Relationships

- [fixtures mock helpers](fixtures_mock_helpers.md) (5 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (4 shared connections)
- [cleanup combat handler](cleanup_combat_handler.md) (4 shared connections)
- [nats services metrics](nats_services_metrics.md) (4 shared connections)
- [schemas nats messages](schemas_nats_messages.md) (2 shared connections)
- [Error Conversion](Error_Conversion.md) (1 shared connections)

## Source Files

- `server/schemas/realtime/__init__.py`
- `server/schemas/realtime/presence_data.py`
- `server/schemas/realtime/realtime.py`
- `server/tests/unit/api/test_real_time_helpers.py`

## Audit Trail

- EXTRACTED: 104 (74%)
- INFERRED: 36 (26%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*