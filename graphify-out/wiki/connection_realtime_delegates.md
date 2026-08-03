# connection realtime delegates

> 125 nodes

## Key Concepts

- **test_connection_delegates.py** (51 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **connection_delegates.py** (38 connections) — `server/realtime/connection_delegates.py`
- **ConnectionMetadata** (21 connections) — `server/realtime/connection_models.py`
- **validate_token_impl()** (15 connections) — `server/realtime/connection_delegates.py`
- **cleanup_dead_websocket_impl()** (14 connections) — `server/realtime/connection_delegates.py`
- **delegate_message_broadcaster()** (12 connections) — `server/realtime/connection_delegates.py`
- **delegate_health_monitor()** (11 connections) — `server/realtime/connection_delegates.py`
- **delegate_personal_message_sender()** (11 connections) — `server/realtime/connection_delegates.py`
- **UUID** (10 connections)
- **delegate_health_monitor_sync()** (10 connections) — `server/realtime/connection_delegates.py`
- **delegate_connection_cleaner_sync()** (9 connections) — `server/realtime/connection_delegates.py`
- **delegate_personal_message_sender_sync()** (9 connections) — `server/realtime/connection_delegates.py`
- **delegate_room_event_handler()** (9 connections) — `server/realtime/connection_delegates.py`
- **connection_models.py** (9 connections) — `server/realtime/connection_models.py`
- **test_connection_models.py** (9 connections) — `server/tests/unit/realtime/test_connection_models.py`
- **_async_callable()** (8 connections) — `server/realtime/connection_delegates.py`
- **delegate_game_state_provider_sync()** (8 connections) — `server/realtime/connection_delegates.py`
- **_WebsocketCleanupManager** (7 connections) — `server/realtime/connection_delegates.py`
- **_close_dead_websocket_if_open()** (7 connections) — `server/realtime/connection_delegates.py`
- **_PlayerIdCarrier** (6 connections) — `server/realtime/connection_delegates.py`
- **_TokenPersistence** (6 connections) — `server/realtime/connection_delegates.py`
- **_TokenValidateManager** (6 connections) — `server/realtime/connection_delegates.py`
- **_sync_callable()** (5 connections) — `server/realtime/connection_delegates.py`
- **WebSocket** (5 connections)
- **_remove_connection_from_player_list()** (5 connections) — `server/realtime/connection_delegates.py`
- *... and 100 more nodes in this community*

## Relationships

- [Room Broadcast](Room_Broadcast.md) (30 shared connections)
- [container service services](container_service_services.md) (9 shared connections)
- [NATS Messaging](NATS_Messaging.md) (8 shared connections)
- [connection disconnection realtime](connection_disconnection_realtime.md) (8 shared connections)
- [connection realtime error](connection_realtime_error.md) (6 shared connections)
- [npc populate databases](npc_populate_databases.md) (4 shared connections)
- [player event state](player_event_state.md) (3 shared connections)
- [auth rationale access](auth_rationale_access.md) (2 shared connections)
- [command inventory factories](command_inventory_factories.md) (1 shared connections)

## Source Files

- `server/realtime/connection_delegates.py`
- `server/realtime/connection_models.py`
- `server/tests/unit/realtime/test_connection_delegates.py`
- `server/tests/unit/realtime/test_connection_models.py`

## Audit Trail

- EXTRACTED: 470 (97%)
- INFERRED: 15 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*