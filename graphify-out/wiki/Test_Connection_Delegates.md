# Test Connection Delegates

> 108 nodes

## Key Concepts

- **test_connection_delegates.py** (52 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **connection_delegates.py** (40 connections) — `server/realtime/connection_delegates.py`
- **asyncio** (27 connections)
- **cleanup_dead_websocket_impl()** (14 connections) — `server/realtime/connection_delegates.py`
- **validate_token_impl()** (13 connections) — `server/realtime/connection_delegates.py`
- **delegate_error_handler()** (12 connections) — `server/realtime/connection_delegates.py`
- **delegate_game_state_provider()** (12 connections) — `server/realtime/connection_delegates.py`
- **delegate_message_broadcaster()** (12 connections) — `server/realtime/connection_delegates.py`
- **delegate_health_monitor()** (11 connections) — `server/realtime/connection_delegates.py`
- **delegate_personal_message_sender()** (11 connections) — `server/realtime/connection_delegates.py`
- **delegate_health_monitor_sync()** (10 connections) — `server/realtime/connection_delegates.py`
- **UUID** (10 connections)
- **delegate_personal_message_sender_sync()** (9 connections) — `server/realtime/connection_delegates.py`
- **delegate_room_event_handler()** (9 connections) — `server/realtime/connection_delegates.py`
- **_async_callable()** (8 connections) — `server/realtime/connection_delegates.py`
- **delegate_game_state_provider_sync()** (8 connections) — `server/realtime/connection_delegates.py`
- **_WebsocketCleanupManager** (7 connections) — `server/realtime/connection_delegates.py`
- **_close_dead_websocket_if_open()** (7 connections) — `server/realtime/connection_delegates.py`
- **_remove_connection_from_player_list()** (5 connections) — `server/realtime/connection_delegates.py`
- **_sync_callable()** (5 connections) — `server/realtime/connection_delegates.py`
- **test_validate_token_impl_database_error()** (5 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **WebSocket** (5 connections)
- **_PlayerIdCarrier** (4 connections) — `server/realtime/connection_delegates.py`
- **_TokenPersistence** (4 connections) — `server/realtime/connection_delegates.py`
- **_TokenValidateManager** (4 connections) — `server/realtime/connection_delegates.py`
- *... and 83 more nodes in this community*

## Relationships

- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (18 shared connections)
- [Connection Manager Methods](Connection_Manager_Methods.md) (15 shared connections)
- [Connection Cleanup Methods](Connection_Cleanup_Methods.md) (11 shared connections)
- [Connection Error Methods](Connection_Error_Methods.md) (7 shared connections)
- [Error Handling & Exceptions](Error_Handling_&_Exceptions.md) (4 shared connections)
- [Test Connection Rate Limiter](Test_Connection_Rate_Limiter.md) (2 shared connections)
- [Connection Manager](Connection_Manager.md) (2 shared connections)
- [Test Auth Utils](Test_Auth_Utils.md) (2 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (2 shared connections)

## Source Files

- `server/realtime/connection_delegates.py`
- `server/tests/unit/realtime/test_connection_delegates.py`

## Audit Trail

- EXTRACTED: 278 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*