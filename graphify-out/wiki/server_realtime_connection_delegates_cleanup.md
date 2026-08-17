# server realtime connection delegates cleanup

> 63 nodes

## Key Concepts

- **test_connection_delegates.py** (52 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **asyncio** (27 connections)
- **cleanup_dead_websocket_impl()** (12 connections) — `server/realtime/connection_delegates.py`
- **delegate_message_broadcaster()** (9 connections) — `server/realtime/connection_delegates.py`
- **delegate_game_state_provider()** (6 connections) — `server/realtime/connection_delegates.py`
- **test_validate_token_impl_database_error()** (5 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_cleanup_dead_websocket_impl_close_timeout()** (4 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_cleanup_dead_websocket_impl_error()** (4 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_cleanup_dead_websocket_impl_none_websocket()** (4 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_cleanup_dead_websocket_impl_not_in_active()** (4 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_cleanup_dead_websocket_impl_success()** (4 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_delegate_connection_cleaner_none()** (4 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_delegate_connection_cleaner_success()** (4 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_delegate_error_handler_none()** (4 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_delegate_error_handler_success()** (4 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_delegate_game_state_provider_none()** (4 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_delegate_game_state_provider_success()** (4 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_delegate_health_monitor_none()** (4 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_delegate_health_monitor_success()** (4 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_delegate_message_broadcaster_broadcast_global()** (4 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_delegate_message_broadcaster_broadcast_to_room()** (4 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_delegate_message_broadcaster_none()** (4 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_delegate_message_broadcaster_success()** (4 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_delegate_personal_message_sender_none()** (4 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_delegate_personal_message_sender_send_message()** (4 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- *... and 38 more nodes in this community*

## Relationships

- [server realtime connection delegates](server_realtime_connection_delegates.md) (37 shared connections)
- [server realtime connection delegates delegate](server_realtime_connection_delegates_delegate.md) (9 shared connections)
- [scripts populate test npc databases](scripts_populate_test_npc_databases.md) (2 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/realtime/connection_delegates.py`
- `server/tests/unit/realtime/test_connection_delegates.py`

## Audit Trail

- EXTRACTED: 154 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*