# connection delegates

> 78 nodes

## Key Concepts

- **test_connection_delegates.py** (51 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **connection_delegates.py** (38 connections) — `server/realtime/connection_delegates.py`
- **delegate_message_broadcaster()** (12 connections) — `server/realtime/connection_delegates.py`
- **delegate_health_monitor()** (11 connections) — `server/realtime/connection_delegates.py`
- **delegate_connection_cleaner()** (11 connections) — `server/realtime/connection_delegates.py`
- **delegate_personal_message_sender()** (11 connections) — `server/realtime/connection_delegates.py`
- **UUID** (10 connections)
- **delegate_health_monitor_sync()** (10 connections) — `server/realtime/connection_delegates.py`
- **delegate_connection_cleaner_sync()** (9 connections) — `server/realtime/connection_delegates.py`
- **delegate_personal_message_sender_sync()** (9 connections) — `server/realtime/connection_delegates.py`
- **delegate_room_event_handler()** (9 connections) — `server/realtime/connection_delegates.py`
- **_async_callable()** (8 connections) — `server/realtime/connection_delegates.py`
- **delegate_game_state_provider_sync()** (8 connections) — `server/realtime/connection_delegates.py`
- **_close_dead_websocket_if_open()** (7 connections) — `server/realtime/connection_delegates.py`
- **_sync_callable()** (5 connections) — `server/realtime/connection_delegates.py`
- **WebSocket** (5 connections)
- **_websocket_client_connected()** (4 connections) — `server/realtime/connection_delegates.py`
- **_is_benign_websocket_close_error()** (3 connections) — `server/realtime/connection_delegates.py`
- **test_delegate_health_monitor_success()** (3 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_delegate_health_monitor_none()** (3 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_delegate_health_monitor_sync_success()** (3 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_delegate_health_monitor_sync_none()** (3 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_delegate_connection_cleaner_success()** (3 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_delegate_connection_cleaner_none()** (3 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_delegate_connection_cleaner_sync_success()** (3 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- *... and 53 more nodes in this community*

## Relationships

- [Player](Player.md) (32 shared connections)
- [command processor()](command_processor%28%29.md) (12 shared connections)
- [.store npc xp mapping for](store_npc_xp_mapping_for.md) (11 shared connections)
- [test player event handlers room](test_player_event_handlers_room.md) (6 shared connections)
- [real time](real_time.md) (3 shared connections)
- [AttributeError](AttributeError.md) (2 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (2 shared connections)
- [create access token()](create_access_token%28%29.md) (1 shared connections)
- [connection disconnection](connection_disconnection.md) (1 shared connections)
- [Custom user manager for MythosMUD.](Custom_user_manager_for_MythosMUD.md) (1 shared connections)

## Source Files

- `server/realtime/connection_delegates.py`
- `server/tests/unit/realtime/test_connection_delegates.py`

## Audit Trail

- EXTRACTED: 327 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*