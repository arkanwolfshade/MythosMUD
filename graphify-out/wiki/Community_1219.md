# Community 1219

> 10 nodes

## Key Concepts

- **_PlayerLookupPersistence** (6 connections) — `server/api/real_time.py`
- **Protocol** (4 connections)
- **_ConnectionManagerUtilsModule** (3 connections) — `server/api/real_time.py`
- **.get_player_by_id()** (3 connections) — `server/api/real_time.py`
- **_WebSocketHandlerModule** (2 connections) — `server/api/real_time.py`
- **.resolve_connection_manager()** (2 connections) — `server/api/real_time.py`
- **.get_player_by_user_id()** (2 connections) — `server/api/real_time.py`
- **Player** (2 connections)
- **Resolve the connection manager singleton (or optional candidate).** (1 connections) — `server/api/real_time.py`
- **Minimal async persistence surface for WebSocket player resolution.** (1 connections) — `server/api/real_time.py`

## Relationships

- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (3 shared connections)
- [Community 1020](Community_1020.md) (2 shared connections)
- [Community 586](Community_586.md) (1 shared connections)

## Source Files

- `server/api/real_time.py`

## Audit Trail

- EXTRACTED: 16 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*