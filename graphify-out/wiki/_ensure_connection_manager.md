# _ensure_connection_manager

> 10 nodes

## Key Concepts

- **_ensure_connection_manager()** (10 connections) — `server/api/real_time.py`
- **get_player_connections()** (10 connections) — `server/api/real_time.py`
- **get_connection_statistics()** (8 connections) — `server/api/real_time.py`
- **Request** (4 connections)
- **test_ensure_connection_manager_missing()** (3 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_get_player_connections()** (3 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **get** (2 connections)
- **Get connection information for a player. Returns detailed connection metadata…** (1 connections) — `server/api/real_time.py`
- **Get comprehensive connection statistics. Returns detailed statistics about all…** (1 connections) — `server/api/real_time.py`
- **Ensure connection manager is available. Raises LoggedHTTPException with proper…** (1 connections) — `server/api/real_time.py`

## Relationships

- [asyncio](asyncio.md) (6 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [realtime/realtime.py](realtime-realtime.py.md) (4 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (2 shared connections)
- [test_real_time_helpers.py](test_real_time_helpers.py.md) (2 shared connections)

## Source Files

- `server/api/real_time.py`
- `server/tests/unit/api/test_real_time_helpers.py`

## Audit Trail

- EXTRACTED: 30 (97%)
- INFERRED: 1 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*