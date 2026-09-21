# test_connection_delegates.py

> 105 nodes

## Key Concepts

- **test_connection_delegates.py** (51 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **connection_delegates.py** (38 connections) — `server/realtime/connection_delegates.py`
- **asyncio** (27 connections)
- **cleanup_dead_websocket_impl()** (14 connections) — `server/realtime/connection_delegates.py`
- **validate_token_impl()** (13 connections) — `server/realtime/connection_delegates.py`
- **delegate_message_broadcaster()** (12 connections) — `server/realtime/connection_delegates.py`
- **delegate_connection_cleaner()** (11 connections) — `server/realtime/connection_delegates.py`
- **delegate_health_monitor()** (11 connections) — `server/realtime/connection_delegates.py`
- **delegate_personal_message_sender()** (11 connections) — `server/realtime/connection_delegates.py`
- **delegate_health_monitor_sync()** (10 connections) — `server/realtime/connection_delegates.py`
- **UUID** (10 connections)
- **delegate_connection_cleaner_sync()** (9 connections) — `server/realtime/connection_delegates.py`
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
- **_TokenValidateManager** (4 connections) — `server/realtime/connection_delegates.py`
- **_websocket_client_connected()** (4 connections) — `server/realtime/connection_delegates.py`
- **test_cleanup_dead_websocket_impl_close_timeout()** (4 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- *... and 80 more nodes in this community*

## Relationships

- [connection_manager.py](connection_manager.py.md) (25 shared connections)
- [test_connection_error_methods.py](test_connection_error_methods.py.md) (8 shared connections)
- [delegate_game_state_provider](delegate_game_state_provider.md) (7 shared connections)
- [ConnectionManager](ConnectionManager.md) (6 shared connections)
- [asyncio](asyncio.md) (6 shared connections)
- [_PlayerIdCarrier](_PlayerIdCarrier.md) (4 shared connections)
- [DatabaseError](DatabaseError.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [test_auth_utils.py](test_auth_utils.py.md) (2 shared connections)

## Source Files

- `server/realtime/connection_delegates.py`
- `server/tests/unit/realtime/test_connection_delegates.py`

## Audit Trail

- EXTRACTED: 258 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*