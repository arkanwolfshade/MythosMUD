# connection delegates

> 86 nodes

## Key Concepts

- **test_connection_delegates.py** (51 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **connection_delegates.py** (29 connections) — `server/realtime/connection_delegates.py`
- **cleanup_dead_websocket_impl()** (14 connections) — `server/realtime/connection_delegates.py`
- **UUID** (10 connections)
- **delegate_message_broadcaster()** (10 connections) — `server/realtime/connection_delegates.py`
- **delegate_personal_message_sender()** (10 connections) — `server/realtime/connection_delegates.py`
- **delegate_health_monitor()** (9 connections) — `server/realtime/connection_delegates.py`
- **delegate_health_monitor_sync()** (9 connections) — `server/realtime/connection_delegates.py`
- **delegate_connection_cleaner_sync()** (9 connections) — `server/realtime/connection_delegates.py`
- **_async_callable()** (8 connections) — `server/realtime/connection_delegates.py`
- **delegate_personal_message_sender_sync()** (8 connections) — `server/realtime/connection_delegates.py`
- **_close_dead_websocket_if_open()** (7 connections) — `server/realtime/connection_delegates.py`
- **delegate_game_state_provider()** (7 connections) — `server/realtime/connection_delegates.py`
- **delegate_game_state_provider_sync()** (7 connections) — `server/realtime/connection_delegates.py`
- **delegate_room_event_handler()** (7 connections) — `server/realtime/connection_delegates.py`
- **WebSocket** (5 connections)
- **_WebsocketCleanupManager** (5 connections) — `server/realtime/connection_delegates.py`
- **_sync_callable()** (5 connections) — `server/realtime/connection_delegates.py`
- **_remove_connection_from_player_list()** (5 connections) — `server/realtime/connection_delegates.py`
- **_websocket_client_connected()** (4 connections) — `server/realtime/connection_delegates.py`
- **test_delegate_error_handler_success()** (3 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_delegate_error_handler_none()** (3 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_cleanup_dead_websocket_impl_success()** (3 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_cleanup_dead_websocket_impl_none_websocket()** (3 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_cleanup_dead_websocket_impl_not_in_active()** (3 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- *... and 61 more nodes in this community*

## Relationships

- [PlayerIdCarrier](PlayerIdCarrier.md) (12 shared connections)
- [Periodically check for cleanup conditions](Periodically_check_for_cleanup_conditions.md) (9 shared connections)
- [Any](Any.md) (8 shared connections)
- [ConnectionManager](ConnectionManager.md) (8 shared connections)
- [main()](main%28%29.md) (1 shared connections)
- [Player](Player.md) (1 shared connections)

## Source Files

- `server/realtime/connection_delegates.py`
- `server/tests/unit/realtime/test_connection_delegates.py`

## Audit Trail

- EXTRACTED: 355 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*