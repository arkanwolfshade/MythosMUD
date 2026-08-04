# connection realtime delegates

> 141 nodes

## Key Concepts

- **connection_manager_methods.py** (80 connections) — `server/realtime/connection_manager_methods.py`
- **test_connection_delegates.py** (51 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **connection_delegates.py** (38 connections) — `server/realtime/connection_delegates.py`
- **validate_token_impl()** (15 connections) — `server/realtime/connection_delegates.py`
- **cleanup_dead_websocket_impl()** (14 connections) — `server/realtime/connection_delegates.py`
- **delegate_game_state_provider()** (12 connections) — `server/realtime/connection_delegates.py`
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
- **broadcast_global_event_impl()** (8 connections) — `server/realtime/connection_manager_methods.py`
- **_WebsocketCleanupManager** (7 connections) — `server/realtime/connection_delegates.py`
- **_close_dead_websocket_if_open()** (7 connections) — `server/realtime/connection_delegates.py`
- **get_message_delivery_stats_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **broadcast_global_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **_PlayerIdCarrier** (6 connections) — `server/realtime/connection_delegates.py`
- **_TokenPersistence** (6 connections) — `server/realtime/connection_delegates.py`
- **_TokenValidateManager** (6 connections) — `server/realtime/connection_delegates.py`
- *... and 116 more nodes in this community*

## Relationships

- [Room Broadcast](Room_Broadcast.md) (52 shared connections)
- [realtime monitoring statistics](realtime_monitoring_statistics.md) (27 shared connections)
- [connection disconnection realtime](connection_disconnection_realtime.md) (10 shared connections)
- [container service services](container_service_services.md) (9 shared connections)
- [Loot Generation](Loot_Generation.md) (6 shared connections)
- [Database Config](Database_Config.md) (6 shared connections)
- [connection realtime error](connection_realtime_error.md) (6 shared connections)
- [persistence rationale room](persistence_rationale_room.md) (6 shared connections)
- [game chat service](game_chat_service.md) (5 shared connections)
- [services inventory mutation](services_inventory_mutation.md) (3 shared connections)
- [auth rationale access](auth_rationale_access.md) (2 shared connections)
- [realtime message filtering](realtime_message_filtering.md) (2 shared connections)

## Source Files

- `server/realtime/connection_delegates.py`
- `server/realtime/connection_manager_methods.py`
- `server/tests/unit/realtime/test_connection_delegates.py`

## Audit Trail

- EXTRACTED: 608 (98%)
- INFERRED: 10 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*