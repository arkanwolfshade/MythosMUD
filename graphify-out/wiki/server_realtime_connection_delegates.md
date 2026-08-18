# server realtime connection delegates

> 80 nodes

## Key Concepts

- **connection_delegates.py** (41 connections) — `server/realtime/connection_delegates.py`
- **connection_manager_health_cleanup.py** (29 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **delegate_error_handler()** (18 connections) — `server/realtime/connection_delegates.py`
- **delegate_connection_cleaner()** (16 connections) — `server/realtime/connection_delegates.py`
- **Any** (15 connections)
- **delegate_health_monitor()** (14 connections) — `server/realtime/connection_delegates.py`
- **validate_token_impl()** (13 connections) — `server/realtime/connection_delegates.py`
- **delegate_connection_cleaner_sync()** (12 connections) — `server/realtime/connection_delegates.py`
- **delegate_health_monitor_sync()** (12 connections) — `server/realtime/connection_delegates.py`
- **delegate_personal_message_sender()** (11 connections) — `server/realtime/connection_delegates.py`
- **CleanupContext** (10 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **UUID** (10 connections)
- **delegate_personal_message_sender_sync()** (9 connections) — `server/realtime/connection_delegates.py`
- **delegate_room_event_handler()** (9 connections) — `server/realtime/connection_delegates.py`
- **_async_callable()** (8 connections) — `server/realtime/connection_delegates.py`
- **UUID** (8 connections)
- **_WebsocketCleanupManager** (7 connections) — `server/realtime/connection_delegates.py`
- **_close_dead_websocket_if_open()** (7 connections) — `server/realtime/connection_delegates.py`
- **check_connection_health_impl()** (6 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **_remove_connection_from_player_list()** (5 connections) — `server/realtime/connection_delegates.py`
- **_sync_callable()** (5 connections) — `server/realtime/connection_delegates.py`
- **check_and_cleanup_impl()** (5 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **cleanup_dead_connections_impl()** (5 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **cleanup_orphaned_data_impl()** (5 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **detect_and_handle_error_state_impl()** (5 connections) — `server/realtime/connection_manager_health_cleanup.py`
- *... and 55 more nodes in this community*

## Relationships

- [server realtime connection delegates cleanup](server_realtime_connection_delegates_cleanup.md) (44 shared connections)
- [server realtime connection manager methods](server_realtime_connection_manager_methods.md) (12 shared connections)
- [server realtime connection cleanup methods](server_realtime_connection_cleanup_methods.md) (11 shared connections)
- [server realtime connection error methods](server_realtime_connection_error_methods.md) (10 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (8 shared connections)
- [server realtime connection models](server_realtime_connection_models.md) (3 shared connections)
- [server tests unit realtime maintenance](server_tests_unit_realtime_maintenance.md) (3 shared connections)
- [server realtime player disconnect handlers](server_realtime_player_disconnect_handlers.md) (3 shared connections)
- [server realtime rate limiter py](server_realtime_rate_limiter_py.md) (2 shared connections)
- [server auth utils](server_auth_utils.md) (2 shared connections)
- [claude rules sqlalchemy](claude_rules_sqlalchemy.md) (2 shared connections)
- [server realtime maintenance connection cleaner](server_realtime_maintenance_connection_cleaner.md) (1 shared connections)

## Source Files

- `server/realtime/connection_delegates.py`
- `server/realtime/connection_manager_health_cleanup.py`
- `server/realtime/maintenance/connection_cleaner.py`

## Audit Trail

- EXTRACTED: 245 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*