# Connection Session Management

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

- [Test Connection Session Management](Test_Connection_Session_Management.md) (26 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (11 shared connections)
- [Connection Manager](Connection_Manager.md) (2 shared connections)
- [Test Connection Rate Limiter](Test_Connection_Rate_Limiter.md) (1 shared connections)
- [Test Message Queue](Test_Message_Queue.md) (1 shared connections)
- [Connection Establishment](Connection_Establishment.md) (1 shared connections)

## Source Files

- `server/realtime/connection_session_management.py`

## Audit Trail

- EXTRACTED: 59 (94%)
- INFERRED: 4 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*