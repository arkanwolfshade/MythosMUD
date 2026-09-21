# handle_new_game_session

> 24 nodes

## Key Concepts

- **handle_new_game_session()** (12 connections) — `server/api/real_time.py`
- **_ensure_connection_manager()** (11 connections) — `server/api/real_time.py`
- **get_player_connections()** (10 connections) — `server/api/real_time.py`
- **get_connection_statistics()** (8 connections) — `server/api/real_time.py`
- **NewGameSessionResponse** (7 connections) — `server/schemas/realtime/realtime.py`
- **PlayerConnectionsResponse** (7 connections) — `server/schemas/realtime/realtime.py`
- **SessionInfo** (6 connections) — `server/schemas/realtime/realtime.py`
- **BaseModel** (6 connections)
- **_app_state_from_request()** (5 connections) — `server/api/real_time.py`
- **Request** (5 connections)
- **HealthInfo** (4 connections) — `server/schemas/realtime/realtime.py`
- **PresenceInfo** (4 connections) — `server/schemas/realtime/realtime.py`
- **get** (2 connections)
- **post** (1 connections)
- **Read Starlette app.state without treating Request.app as Any.** (1 connections) — `server/api/real_time.py`
- **Ensure connection manager is available. Raises LoggedHTTPException with proper…** (1 connections) — `server/api/real_time.py`
- **Get connection information for a player. Returns detailed connection metadata…** (1 connections) — `server/api/real_time.py`
- **Handle a new game session for a player. This will disconnect existing…** (1 connections) — `server/api/real_time.py`
- **Get comprehensive connection statistics. Returns detailed statistics about all…** (1 connections) — `server/api/real_time.py`
- **Presence information for a player connection.** (1 connections) — `server/schemas/realtime/realtime.py`
- **Session information for a player connection.** (1 connections) — `server/schemas/realtime/realtime.py`
- **Health information for a player connection.** (1 connections) — `server/schemas/realtime/realtime.py`
- **Response model for player connection information endpoint.** (1 connections) — `server/schemas/realtime/realtime.py`
- **Response model for new game session endpoint.** (1 connections) — `server/schemas/realtime/realtime.py`

## Relationships

- [real_time.py](real_time.py.md) (14 shared connections)
- [test_real_time_helpers.py](test_real_time_helpers.py.md) (13 shared connections)
- [test_websocket_handler_core.py](test_websocket_handler_core.py.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (2 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (2 shared connections)
- [test_admin_setlucidity_command.py](test_admin_setlucidity_command.py.md) (1 shared connections)

## Source Files

- `server/api/real_time.py`
- `server/schemas/realtime/realtime.py`

## Audit Trail

- EXTRACTED: 67 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*