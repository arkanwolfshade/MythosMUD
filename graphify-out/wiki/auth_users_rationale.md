# auth users rationale

> 27 nodes

## Key Concepts

- **realtime.py** (13 connections) — `server/schemas/realtime/realtime.py`
- **PresenceStatistics** (12 connections) — `server/schemas/realtime/presence_data.py`
- **SessionStatistics** (12 connections) — `server/schemas/realtime/presence_data.py`
- **ErrorStatistics** (12 connections) — `server/schemas/realtime/presence_data.py`
- **PlayerConnectionsResponse** (10 connections) — `server/schemas/realtime/realtime.py`
- **NewGameSessionResponse** (10 connections) — `server/schemas/realtime/realtime.py`
- **ConnectionStatisticsResponse** (10 connections) — `server/schemas/realtime/realtime.py`
- **SessionInfo** (9 connections) — `server/schemas/realtime/realtime.py`
- **get_connection_statistics()** (7 connections) — `server/api/real_time.py`
- **PresenceInfo** (6 connections) — `server/schemas/realtime/realtime.py`
- **BaseModel** (6 connections)
- **HealthInfo** (6 connections) — `server/schemas/realtime/realtime.py`
- **presence_data.py** (5 connections) — `server/schemas/realtime/presence_data.py`
- **test_get_connection_statistics()** (5 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **BaseModel** (3 connections)
- **Get comprehensive connection statistics.     Returns detailed statistics about a** (1 connections) — `server/api/real_time.py`
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

- [combat commands handler](combat_commands_handler.md) (14 shared connections)
- [schemas nats messages](schemas_nats_messages.md) (5 shared connections)
- [profession game service](profession_game_service.md) (3 shared connections)
- [models npc rationale](models_npc_rationale.md) (2 shared connections)

## Source Files

- `server/api/real_time.py`
- `server/schemas/realtime/presence_data.py`
- `server/schemas/realtime/realtime.py`
- `server/tests/unit/api/test_real_time_helpers.py`

## Audit Trail

- EXTRACTED: 102 (74%)
- INFERRED: 36 (26%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*