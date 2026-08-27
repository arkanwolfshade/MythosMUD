# submitAuth.ts

> 67 nodes

## Key Concepts

- **test_connection_delegates.py** (52 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **asyncio** (27 connections)
- **cleanup_dead_websocket_impl()** (12 connections) — `server/realtime/connection_delegates.py`
- **delegate_message_broadcaster()** (12 connections) — `server/realtime/connection_delegates.py`
- **validate_token_impl()** (11 connections) — `server/realtime/connection_delegates.py`
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
- *... and 42 more nodes in this community*

## Relationships

- [security.ts](security.ts.md) (33 shared connections)
- [MythosTickScheduler](MythosTickScheduler.md) (6 shared connections)
- [BehaviorEngine](BehaviorEngine.md) (3 shared connections)
- [ContainerComponent](ContainerComponent.md) (3 shared connections)
- [test_chat_logger.py](test_chat_logger.py.md) (2 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (1 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (1 shared connections)
- [🚫 Anti-Patterns NOT Found (Good!)](🚫_Anti-Patterns_NOT_Found_Good!.md) (1 shared connections)

## Source Files

- `server/realtime/connection_delegates.py`
- `server/tests/unit/realtime/test_connection_delegates.py`

## Audit Trail

- EXTRACTED: 165 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*