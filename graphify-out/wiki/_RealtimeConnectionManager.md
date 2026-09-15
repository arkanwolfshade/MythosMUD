# _RealtimeConnectionManager

> 12 nodes

## Key Concepts

- **_RealtimeConnectionManager** (16 connections) — `server/api/real_time.py`
- **UUID** (14 connections)
- **.check_connection_health()** (2 connections) — `server/api/real_time.py`
- **.get_player_presence_info()** (2 connections) — `server/api/real_time.py`
- **.get_player_session()** (2 connections) — `server/api/real_time.py`
- **.handle_new_game_session()** (2 connections) — `server/api/real_time.py`
- **.validate_session()** (2 connections) — `server/api/real_time.py`
- **.get_error_statistics()** (1 connections) — `server/api/real_time.py`
- **.get_presence_statistics()** (1 connections) — `server/api/real_time.py`
- **.get_session_connections()** (1 connections) — `server/api/real_time.py`
- **.get_session_stats()** (1 connections) — `server/api/real_time.py`
- **Connection manager API used by realtime HTTP/WebSocket routes.** (1 connections) — `server/api/real_time.py`

## Relationships

- [real_time.py](real_time.py.md) (7 shared connections)
- [test_real_time_helpers.py](test_real_time_helpers.py.md) (4 shared connections)
- [_ensure_connection_manager](_ensure_connection_manager.md) (2 shared connections)
- [_PlayerLookupPersistence](_PlayerLookupPersistence.md) (2 shared connections)

## Source Files

- `server/api/real_time.py`

## Audit Trail

- EXTRACTED: 30 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*