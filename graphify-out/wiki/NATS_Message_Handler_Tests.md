# NATS Message Handler Tests

> 103 nodes · cohesion 0.03

## Key Concepts

- **test_connection_delegates.py** (51 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **connection_delegates.py** (20 connections) — `server/realtime/connection_delegates.py`
- **Any** (13 connections)
- **validate_token_impl()** (13 connections) — `server/realtime/connection_delegates.py`
- **delegate_error_handler()** (12 connections) — `server/realtime/connection_delegates.py`
- **delegate_game_state_provider()** (12 connections) — `server/realtime/connection_delegates.py`
- **cleanup_dead_websocket_impl()** (11 connections) — `server/realtime/connection_delegates.py`
- **delegate_connection_cleaner()** (11 connections) — `server/realtime/connection_delegates.py`
- **delegate_message_broadcaster()** (11 connections) — `server/realtime/connection_delegates.py`
- **delegate_connection_cleaner_sync()** (9 connections) — `server/realtime/connection_delegates.py`
- **delegate_health_monitor()** (9 connections) — `server/realtime/connection_delegates.py`
- **delegate_personal_message_sender()** (9 connections) — `server/realtime/connection_delegates.py`
- **delegate_room_event_handler()** (9 connections) — `server/realtime/connection_delegates.py`
- **delegate_game_state_provider_sync()** (8 connections) — `server/realtime/connection_delegates.py`
- **delegate_health_monitor_sync()** (8 connections) — `server/realtime/connection_delegates.py`
- **delegate_personal_message_sender_sync()** (8 connections) — `server/realtime/connection_delegates.py`
- **._cleanup_dead_websocket()** (4 connections) — `server/realtime/connection_manager.py`
- **test_validate_token_impl_database_error()** (4 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_cleanup_dead_websocket_impl_close_timeout()** (3 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_cleanup_dead_websocket_impl_error()** (3 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_cleanup_dead_websocket_impl_none_websocket()** (3 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_cleanup_dead_websocket_impl_not_in_active()** (3 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_cleanup_dead_websocket_impl_success()** (3 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_delegate_connection_cleaner_none()** (3 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_delegate_connection_cleaner_success()** (3 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- *... and 78 more nodes in this community*

## Relationships

- [Room Occupant Events](Room_Occupant_Events.md) (40 shared connections)
- [Realtime Connection Impl](Realtime_Connection_Impl.md) (4 shared connections)
- [Auth Token Utilities](Auth_Token_Utilities.md) (2 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (2 shared connections)
- [Restart Invalidating JWT](Restart_Invalidating_JWT.md) (2 shared connections)
- [Connection Disconnection Cleanup](Connection_Disconnection_Cleanup.md) (1 shared connections)

## Source Files

- `server/realtime/connection_delegates.py`
- `server/realtime/connection_manager.py`
- `server/tests/unit/realtime/test_connection_delegates.py`

## Audit Trail

- EXTRACTED: 374 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*