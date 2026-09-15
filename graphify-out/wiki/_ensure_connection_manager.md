# _ensure_connection_manager

> 11 nodes

## Key Concepts

- **_ensure_connection_manager()** (11 connections) — `server/api/real_time.py`
- **get_player_connections()** (10 connections) — `server/api/real_time.py`
- **_app_state_from_request()** (5 connections) — `server/api/real_time.py`
- **Request** (5 connections)
- **test_ensure_connection_manager_missing()** (4 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_get_player_connections()** (3 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **_request_with_connection_manager()** (2 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **get** (2 connections)
- **Read Starlette app.state without treating Request.app as Any.** (1 connections) — `server/api/real_time.py`
- **Ensure connection manager is available. Raises LoggedHTTPException with proper…** (1 connections) — `server/api/real_time.py`
- **Get connection information for a player. Returns detailed connection metadata…** (1 connections) — `server/api/real_time.py`

## Relationships

- [test_real_time_helpers.py](test_real_time_helpers.py.md) (6 shared connections)
- [realtime/realtime.py](realtime-realtime.py.md) (5 shared connections)
- [real_time.py](real_time.py.md) (4 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (2 shared connections)
- [_RealtimeConnectionManager](_RealtimeConnectionManager.md) (2 shared connections)
- [.state](state.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/api/real_time.py`
- `server/tests/unit/api/test_real_time_helpers.py`

## Audit Trail

- EXTRACTED: 31 (94%)
- INFERRED: 2 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*