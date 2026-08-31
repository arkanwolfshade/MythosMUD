# handle_new_game_session

> 13 nodes

## Key Concepts

- **handle_new_game_session()** (12 connections) — `server/api/real_time.py`
- **_ensure_connection_manager()** (10 connections) — `server/api/real_time.py`
- **get_player_connections()** (10 connections) — `server/api/real_time.py`
- **get_connection_statistics()** (8 connections) — `server/api/real_time.py`
- **test_get_connection_statistics()** (6 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **Request** (4 connections)
- **test_ensure_connection_manager_missing()** (3 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **get** (2 connections)
- **post** (1 connections)
- **Get connection information for a player. Returns detailed connection metadata…** (1 connections) — `server/api/real_time.py`
- **Handle a new game session for a player. This will disconnect existing…** (1 connections) — `server/api/real_time.py`
- **Get comprehensive connection statistics. Returns detailed statistics about all…** (1 connections) — `server/api/real_time.py`
- **Ensure connection manager is available. Raises LoggedHTTPException with proper…** (1 connections) — `server/api/real_time.py`

## Relationships

- [real_time.py](real_time.py.md) (8 shared connections)
- [realtime/realtime.py](realtime-realtime.py.md) (7 shared connections)
- [test_real_time_helpers.py](test_real_time_helpers.py.md) (7 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)

## Source Files

- `server/api/real_time.py`
- `server/tests/unit/api/test_real_time_helpers.py`

## Audit Trail

- EXTRACTED: 40 (91%)
- INFERRED: 4 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*