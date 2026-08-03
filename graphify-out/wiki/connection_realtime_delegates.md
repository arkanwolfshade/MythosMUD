# connection realtime delegates

> 74 nodes

## Key Concepts

- **test_connection_delegates.py** (51 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **connection_delegates.py** (38 connections) — `server/realtime/connection_delegates.py`
- **delegate_game_state_provider()** (12 connections) — `server/realtime/connection_delegates.py`
- **delegate_message_broadcaster()** (12 connections) — `server/realtime/connection_delegates.py`
- **delegate_health_monitor()** (11 connections) — `server/realtime/connection_delegates.py`
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
- **test_delegate_connection_cleaner_sync_success()** (3 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_delegate_connection_cleaner_sync_none()** (3 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_delegate_game_state_provider_success()** (3 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- *... and 49 more nodes in this community*

## Relationships

- [Room Broadcast](Room_Broadcast.md) (28 shared connections)
- [combat npc mixin](combat_npc_mixin.md) (12 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (11 shared connections)
- [container service services](container_service_services.md) (9 shared connections)
- [connection realtime error](connection_realtime_error.md) (6 shared connections)
- [Database Config](Database_Config.md) (3 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)
- [auth rationale access](auth_rationale_access.md) (1 shared connections)

## Source Files

- `server/realtime/connection_delegates.py`
- `server/tests/unit/realtime/test_connection_delegates.py`

## Audit Trail

- EXTRACTED: 320 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*