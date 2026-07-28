# Server Realtime (12)

> 88 nodes

## Key Concepts

- **test_connection_delegates.py** (51 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **connection_delegates.py** (20 connections) — `server/realtime/connection_delegates.py`
- **Any** (13 connections)
- **validate_token_impl()** (13 connections) — `server/realtime/connection_delegates.py`
- **delegate_game_state_provider()** (12 connections) — `server/realtime/connection_delegates.py`
- **cleanup_dead_websocket_impl()** (11 connections) — `server/realtime/connection_delegates.py`
- **delegate_connection_cleaner()** (11 connections) — `server/realtime/connection_delegates.py`
- **delegate_message_broadcaster()** (11 connections) — `server/realtime/connection_delegates.py`
- **delegate_health_monitor()** (9 connections) — `server/realtime/connection_delegates.py`
- **delegate_connection_cleaner_sync()** (9 connections) — `server/realtime/connection_delegates.py`
- **delegate_personal_message_sender()** (9 connections) — `server/realtime/connection_delegates.py`
- **delegate_room_event_handler()** (9 connections) — `server/realtime/connection_delegates.py`
- **delegate_health_monitor_sync()** (8 connections) — `server/realtime/connection_delegates.py`
- **delegate_game_state_provider_sync()** (8 connections) — `server/realtime/connection_delegates.py`
- **delegate_personal_message_sender_sync()** (8 connections) — `server/realtime/connection_delegates.py`
- **test_validate_token_impl_database_error()** (4 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_delegate_error_handler_success()** (3 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_delegate_error_handler_none()** (3 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_cleanup_dead_websocket_impl_success()** (3 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_cleanup_dead_websocket_impl_none_websocket()** (3 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_cleanup_dead_websocket_impl_not_in_active()** (3 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_cleanup_dead_websocket_impl_close_timeout()** (3 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_cleanup_dead_websocket_impl_error()** (3 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_validate_token_impl_success()** (3 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_validate_token_impl_invalid_payload()** (3 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- *... and 63 more nodes in this community*

## Relationships

- [Server Realtime (7)](Server_Realtime_%287%29.md) (39 shared connections)
- [Server Persistence](Server_Persistence.md) (4 shared connections)
- [Server Auth (3)](Server_Auth_%283%29.md) (2 shared connections)
- [Server Commands](Server_Commands.md) (2 shared connections)
- [Server Realtime (4)](Server_Realtime_%284%29.md) (2 shared connections)

## Source Files

- `server/realtime/connection_delegates.py`
- `server/tests/unit/realtime/test_connection_delegates.py`

## Audit Trail

- EXTRACTED: 356 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*