# _PlayerLookupPersistence

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

- [real_time.py](real_time.py.md) (3 shared connections)
- [_RealtimeConnectionManager](_RealtimeConnectionManager.md) (2 shared connections)
- [test_real_time_helpers.py](test_real_time_helpers.py.md) (1 shared connections)

## Source Files

- `server/api/real_time.py`

## Audit Trail

- EXTRACTED: 16 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*