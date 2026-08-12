# test_connection_delegates.py

> 137 nodes

## Key Concepts

- **test_connection_delegates.py** (51 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **connection_manager_health_cleanup.py** (30 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **asyncio** (27 connections)
- **connection_delegates.py** (21 connections) — `server/realtime/connection_delegates.py`
- **Any** (15 connections)
- **Any** (13 connections)
- **delegate_error_handler()** (12 connections) — `server/realtime/connection_delegates.py`
- **validate_token_impl()** (12 connections) — `server/realtime/connection_delegates.py`
- **cleanup_dead_websocket_impl()** (11 connections) — `server/realtime/connection_delegates.py`
- **delegate_connection_cleaner()** (11 connections) — `server/realtime/connection_delegates.py`
- **delegate_message_broadcaster()** (11 connections) — `server/realtime/connection_delegates.py`
- **delegate_connection_cleaner_sync()** (9 connections) — `server/realtime/connection_delegates.py`
- **delegate_health_monitor()** (9 connections) — `server/realtime/connection_delegates.py`
- **delegate_personal_message_sender()** (9 connections) — `server/realtime/connection_delegates.py`
- **delegate_room_event_handler()** (9 connections) — `server/realtime/connection_delegates.py`
- **CleanupContext** (8 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **delegate_game_state_provider_sync()** (8 connections) — `server/realtime/connection_delegates.py`
- **delegate_health_monitor_sync()** (8 connections) — `server/realtime/connection_delegates.py`
- **delegate_personal_message_sender_sync()** (8 connections) — `server/realtime/connection_delegates.py`
- **check_connection_health_impl()** (8 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **UUID** (8 connections)
- **check_and_cleanup_impl()** (7 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **cleanup_dead_connections_impl()** (7 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **cleanup_orphaned_data_impl()** (7 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **detect_and_handle_error_state_impl()** (7 connections) — `server/realtime/connection_manager_health_cleanup.py`
- *... and 112 more nodes in this community*

## Relationships

- [connection_manager.py](connection_manager.py.md) (36 shared connections)
- [ConnectionManager](ConnectionManager.md) (17 shared connections)
- [DatabaseError](DatabaseError.md) (4 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [test_player_disconnect_handlers.py](test_player_disconnect_handlers.py.md) (3 shared connections)
- [RateLimiter](RateLimiter.md) (2 shared connections)
- [test_auth_utils.py](test_auth_utils.py.md) (2 shared connections)
- [asyncio](asyncio.md) (1 shared connections)
- [test_connection_cleaner.py](test_connection_cleaner.py.md) (1 shared connections)
- [.check_and_cleanup](check_and_cleanup.md) (1 shared connections)

## Source Files

- `server/realtime/connection_delegates.py`
- `server/realtime/connection_manager_health_cleanup.py`
- `server/realtime/maintenance/connection_cleaner.py`
- `server/tests/unit/realtime/test_connection_delegates.py`

## Audit Trail

- EXTRACTED: 588 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*