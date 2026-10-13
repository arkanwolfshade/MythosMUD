# Community 1020

> 14 nodes

## Key Concepts

- **_RealtimeConnectionManager** (16 connections) — `server/api/real_time.py`
- **UUID** (14 connections)
- **_resolve_player_id_from_token()** (8 connections) — `server/api/real_time.py`
- **.check_connection_health()** (2 connections) — `server/api/real_time.py`
- **.get_player_presence_info()** (2 connections) — `server/api/real_time.py`
- **.get_player_session()** (2 connections) — `server/api/real_time.py`
- **.handle_new_game_session()** (2 connections) — `server/api/real_time.py`
- **.validate_session()** (2 connections) — `server/api/real_time.py`
- **.get_error_statistics()** (1 connections) — `server/api/real_time.py`
- **.get_presence_statistics()** (1 connections) — `server/api/real_time.py`
- **.get_session_connections()** (1 connections) — `server/api/real_time.py`
- **.get_session_stats()** (1 connections) — `server/api/real_time.py`
- **Resolve player ID from JWT token payload. Validates that the user has a player…** (1 connections) — `server/api/real_time.py`
- **Connection manager API used by realtime HTTP/WebSocket routes.** (1 connections) — `server/api/real_time.py`

## Relationships

- [Community 643](Community_643.md) (8 shared connections)
- [Container API Models](Container_API_Models.md) (3 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (3 shared connections)
- [Community 586](Community_586.md) (3 shared connections)
- [Community 1219](Community_1219.md) (2 shared connections)
- [API Response Models](API_Response_Models.md) (1 shared connections)

## Source Files

- `server/api/real_time.py`

## Audit Trail

- EXTRACTED: 37 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*