# handle_new_game_session_impl

> 14 nodes

## Key Concepts

- **handle_new_game_session_impl()** (17 connections) — `server/realtime/connection_session_management.py`
- **_SessionConnectionManager** (14 connections) — `server/realtime/connection_session_management.py`
- **_disconnect_connection_for_session()** (13 connections) — `server/realtime/connection_session_management.py`
- **_disconnect_all_connections_for_session()** (10 connections) — `server/realtime/connection_session_management.py`
- **_cleanup_old_session_tracking()** (9 connections) — `server/realtime/connection_session_management.py`
- **_cleanup_player_data_for_session()** (8 connections) — `server/realtime/connection_session_management.py`
- **UUID** (6 connections)
- **Protocol** (1 connections)
- **Disconnect all connections for a new game session. Args: connection_ids: List…** (1 connections) — `server/realtime/connection_session_management.py`
- **Clean up old session tracking on reconnect. When a player reconnects, purge…** (1 connections) — `server/realtime/connection_session_management.py`
- **Clean up player data for a new session. Args: player_id: The player's ID…** (1 connections) — `server/realtime/connection_session_management.py`
- **Handle a new game session by disconnecting existing connections. Args:…** (1 connections) — `server/realtime/connection_session_management.py`
- **Connection manager surface used by session-replacement helpers.** (1 connections) — `server/realtime/connection_session_management.py`
- **Disconnect a single connection for a new game session. Args: connection_id: The…** (1 connections) — `server/realtime/connection_session_management.py`

## Relationships

- [get_logger](get_logger.md) (12 shared connections)
- [_as_mgr](_as_mgr.md) (11 shared connections)
- [test_connection_session_management.py](test_connection_session_management.py.md) (9 shared connections)
- [_as_ws](_as_ws.md) (4 shared connections)
- [ConnectionManager](ConnectionManager.md) (2 shared connections)
- [RateLimiter](RateLimiter.md) (1 shared connections)
- [_is_websocket_connected](_is_websocket_connected.md) (1 shared connections)
- [test_disconnect_connection_for_session_key_error](test_disconnect_connection_for_session_key_error.md) (1 shared connections)
- [establish_websocket_connection](establish_websocket_connection.md) (1 shared connections)

## Source Files

- `server/realtime/connection_session_management.py`

## Audit Trail

- EXTRACTED: 59 (94%)
- INFERRED: 4 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*