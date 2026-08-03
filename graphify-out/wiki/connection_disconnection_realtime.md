# connection disconnection realtime

> 399 nodes

## Key Concepts

- **RateLimiter** (61 connections) — `server/realtime/rate_limiter.py`
- **MessageQueue** (54 connections) — `server/realtime/message_queue.py`
- **RoomSubscriptionManager** (46 connections) — `server/realtime/room_subscription_manager.py`
- **connection_initialization.py** (38 connections) — `server/realtime/connection_initialization.py`
- **test_connection_disconnection.py** (37 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_connection_rate_limiter.py** (33 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **test_message_queue.py** (32 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **connection_disconnection.py** (31 connections) — `server/realtime/connection_disconnection.py`
- **deque** (26 connections)
- **connection_cleaner.py** (22 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **statistics_aggregator.py** (22 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **ConnectionMetadata** (21 connections) — `server/realtime/connection_models.py`
- **_DisconnectConnectionManager** (19 connections) — `server/realtime/connection_disconnection.py`
- **room_subscription_manager.py** (18 connections) — `server/realtime/room_subscription_manager.py`
- **test_connection_initialization.py** (18 connections) — `server/tests/unit/realtime/test_connection_initialization.py`
- **_track_disconnect_if_needed()** (15 connections) — `server/realtime/connection_disconnection.py`
- **_cleanup_room_subscriptions()** (15 connections) — `server/realtime/connection_disconnection.py`
- **cleanup_websocket_disconnect()** (15 connections) — `server/realtime/connection_disconnection.py`
- **personal_message_sender.py** (15 connections) — `server/realtime/messaging/personal_message_sender.py`
- **test_connection_disconnection_websockets.py** (15 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **message_queue.py** (14 connections) — `server/realtime/message_queue.py`
- **rate_limiter.py** (14 connections) — `server/realtime/rate_limiter.py`
- **disconnect_all_websockets_impl()** (13 connections) — `server/realtime/connection_disconnection.py`
- **disconnect_connection_by_id_impl()** (13 connections) — `server/realtime/connection_disconnection.py`
- **initialize_core_components()** (13 connections) — `server/realtime/connection_initialization.py`
- *... and 374 more nodes in this community*

## Relationships

- [Room Broadcast](Room_Broadcast.md) (39 shared connections)
- [models npc rationale](models_npc_rationale.md) (25 shared connections)
- [event realtime publisher](event_realtime_publisher.md) (17 shared connections)
- [realtime maintenance connection](realtime_maintenance_connection.md) (8 shared connections)
- [commands communication channels](commands_communication_channels.md) (7 shared connections)
- [realtime messaging message](realtime_messaging_message.md) (6 shared connections)
- [connection realtime delegates](connection_realtime_delegates.md) (6 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (6 shared connections)
- [mythos mud mapbuilder](mythos_mud_mapbuilder.md) (5 shared connections)
- [services npc startup](services_npc_startup.md) (5 shared connections)
- [Database Config](Database_Config.md) (5 shared connections)
- [command utility models](command_utility_models.md) (5 shared connections)

## Source Files

- `server/realtime/connection_disconnection.py`
- `server/realtime/connection_initialization.py`
- `server/realtime/connection_manager.py`
- `server/realtime/connection_models.py`
- `server/realtime/maintenance/connection_cleaner.py`
- `server/realtime/memory_monitor.py`
- `server/realtime/message_queue.py`
- `server/realtime/messaging/personal_message_sender.py`
- `server/realtime/monitoring/statistics_aggregator.py`
- `server/realtime/rate_limiter.py`
- `server/realtime/room_subscription_manager.py`
- `server/tests/unit/realtime/test_connection_disconnection.py`
- `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- `server/tests/unit/realtime/test_connection_initialization.py`
- `server/tests/unit/realtime/test_connection_models.py`
- `server/tests/unit/realtime/test_connection_rate_limiter.py`
- `server/tests/unit/realtime/test_message_queue.py`
- `server/tests/unit/realtime/test_room_subscription_manager_npcs.py`

## Audit Trail

- EXTRACTED: 1426 (95%)
- INFERRED: 68 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*