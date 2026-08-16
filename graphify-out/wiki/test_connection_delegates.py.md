# test_connection_delegates.py

> 159 nodes

## Key Concepts

- **test_connection_delegates.py** (52 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **connection_delegates.py** (41 connections) — `server/realtime/connection_delegates.py`
- **connection_manager_health_cleanup.py** (29 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **asyncio** (27 connections)
- **delegate_error_handler()** (18 connections) — `server/realtime/connection_delegates.py`
- **delegate_connection_cleaner()** (16 connections) — `server/realtime/connection_delegates.py`
- **Any** (15 connections)
- **cleanup_dead_websocket_impl()** (14 connections) — `server/realtime/connection_delegates.py`
- **delegate_health_monitor()** (14 connections) — `server/realtime/connection_delegates.py`
- **validate_token_impl()** (13 connections) — `server/realtime/connection_delegates.py`
- **delegate_connection_cleaner_sync()** (12 connections) — `server/realtime/connection_delegates.py`
- **delegate_health_monitor_sync()** (12 connections) — `server/realtime/connection_delegates.py`
- **delegate_message_broadcaster()** (12 connections) — `server/realtime/connection_delegates.py`
- **delegate_personal_message_sender()** (11 connections) — `server/realtime/connection_delegates.py`
- **CleanupContext** (10 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **UUID** (10 connections)
- **delegate_personal_message_sender_sync()** (9 connections) — `server/realtime/connection_delegates.py`
- **delegate_room_event_handler()** (9 connections) — `server/realtime/connection_delegates.py`
- **_async_callable()** (8 connections) — `server/realtime/connection_delegates.py`
- **delegate_game_state_provider_sync()** (8 connections) — `server/realtime/connection_delegates.py`
- **UUID** (8 connections)
- **_WebsocketCleanupManager** (7 connections) — `server/realtime/connection_delegates.py`
- **_close_dead_websocket_if_open()** (7 connections) — `server/realtime/connection_delegates.py`
- **check_connection_health_impl()** (6 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **_remove_connection_from_player_list()** (5 connections) — `server/realtime/connection_delegates.py`
- *... and 134 more nodes in this community*

## Relationships

- [connection_manager.py](connection_manager.py.md) (26 shared connections)
- [connection_cleanup_methods.py](connection_cleanup_methods.py.md) (11 shared connections)
- [UUID](UUID.md) (9 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [test_connection_session_management.py](test_connection_session_management.py.md) (3 shared connections)
- [test_connection_cleaner.py](test_connection_cleaner.py.md) (3 shared connections)
- [test_player_disconnect_handlers.py](test_player_disconnect_handlers.py.md) (3 shared connections)
- [DatabaseError](DatabaseError.md) (3 shared connections)
- [RateLimiter](RateLimiter.md) (2 shared connections)
- [RoomSubscriptionManager](RoomSubscriptionManager.md) (2 shared connections)
- [test_auth_utils.py](test_auth_utils.py.md) (2 shared connections)
- [ConnectionCleaner](ConnectionCleaner.md) (1 shared connections)

## Source Files

- `server/realtime/connection_delegates.py`
- `server/realtime/connection_manager_health_cleanup.py`
- `server/realtime/maintenance/connection_cleaner.py`
- `server/tests/unit/realtime/test_connection_delegates.py`

## Audit Trail

- EXTRACTED: 372 (99%)
- INFERRED: 5 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*