# _RealtimeConnectionManager

> 22 nodes

## Key Concepts

- **_RealtimeConnectionManager** (16 connections) — `server/api/real_time.py`
- **UUID** (14 connections)
- **_PlayerLookupPersistence** (6 connections) — `server/api/real_time.py`
- **Protocol** (4 connections)
- **_ConnectionManagerUtilsModule** (3 connections) — `server/api/real_time.py`
- **.get_player_by_id()** (3 connections) — `server/api/real_time.py`
- **_WebSocketHandlerModule** (2 connections) — `server/api/real_time.py`
- **.resolve_connection_manager()** (2 connections) — `server/api/real_time.py`
- **.get_player_by_user_id()** (2 connections) — `server/api/real_time.py`
- **.check_connection_health()** (2 connections) — `server/api/real_time.py`
- **.get_player_presence_info()** (2 connections) — `server/api/real_time.py`
- **.get_player_session()** (2 connections) — `server/api/real_time.py`
- **.handle_new_game_session()** (2 connections) — `server/api/real_time.py`
- **.validate_session()** (2 connections) — `server/api/real_time.py`
- **Player** (2 connections)
- **.get_error_statistics()** (1 connections) — `server/api/real_time.py`
- **.get_presence_statistics()** (1 connections) — `server/api/real_time.py`
- **.get_session_connections()** (1 connections) — `server/api/real_time.py`
- **.get_session_stats()** (1 connections) — `server/api/real_time.py`
- **Resolve the connection manager singleton (or optional candidate).** (1 connections) — `server/api/real_time.py`
- **Minimal async persistence surface for WebSocket player resolution.** (1 connections) — `server/api/real_time.py`
- **Connection manager API used by realtime HTTP/WebSocket routes.** (1 connections) — `server/api/real_time.py`

## Relationships

- [real_time.py](real_time.py.md) (12 shared connections)
- [handle_new_game_session](handle_new_game_session.md) (3 shared connections)
- [test_real_time_helpers.py](test_real_time_helpers.py.md) (2 shared connections)

## Source Files

- `server/api/real_time.py`

## Audit Trail

- EXTRACTED: 44 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*