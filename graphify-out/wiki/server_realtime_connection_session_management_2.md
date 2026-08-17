# server realtime connection session management

> 19 nodes

## Key Concepts

- **connection_session_management.py** (26 connections) — `server/realtime/connection_session_management.py`
- **_SessionConnectionManager** (14 connections) — `server/realtime/connection_session_management.py`
- **_disconnect_connection_for_session()** (13 connections) — `server/realtime/connection_session_management.py`
- **handle_new_game_session_impl()** (13 connections) — `server/realtime/connection_session_management.py`
- **_disconnect_all_connections_for_session()** (10 connections) — `server/realtime/connection_session_management.py`
- **_cleanup_old_session_tracking()** (9 connections) — `server/realtime/connection_session_management.py`
- **_cleanup_player_data_for_session()** (8 connections) — `server/realtime/connection_session_management.py`
- **UUID** (6 connections)
- **NewGameSessionResult** (4 connections) — `server/realtime/connection_session_management.py`
- **Protocol** (1 connections)
- **TypedDict** (1 connections)
- **Connection session management for connection manager. This module handles…** (1 connections) — `server/realtime/connection_session_management.py`
- **Disconnect all connections for a new game session. Args: connection_ids: List…** (1 connections) — `server/realtime/connection_session_management.py`
- **Clean up old session tracking on reconnect. When a player reconnects, purge…** (1 connections) — `server/realtime/connection_session_management.py`
- **Clean up player data for a new session. Args: player_id: The player's ID…** (1 connections) — `server/realtime/connection_session_management.py`
- **Handle a new game session by disconnecting existing connections. Args:…** (1 connections) — `server/realtime/connection_session_management.py`
- **Result payload from handle_new_game_session_impl.** (1 connections) — `server/realtime/connection_session_management.py`
- **Connection manager surface used by session-replacement helpers.** (1 connections) — `server/realtime/connection_session_management.py`
- **Disconnect a single connection for a new game session. Args: connection_id: The…** (1 connections) — `server/realtime/connection_session_management.py`

## Relationships

- [server realtime connection session management](server_realtime_connection_session_management.md) (28 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (8 shared connections)
- [server realtime connection models connectionmetadata](server_realtime_connection_models_connectionmetadata.md) (2 shared connections)
- [server realtime rate limiter ratelimiter](server_realtime_rate_limiter_ratelimiter.md) (2 shared connections)
- [deque](deque.md) (2 shared connections)
- [server realtime room subscription manager](server_realtime_room_subscription_manager.md) (2 shared connections)
- [scripts populate test npc databases](scripts_populate_test_npc_databases.md) (1 shared connections)
- [server realtime connection establishment](server_realtime_connection_establishment.md) (1 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (1 shared connections)

## Source Files

- `server/realtime/connection_session_management.py`

## Audit Trail

- EXTRACTED: 76 (95%)
- INFERRED: 4 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*