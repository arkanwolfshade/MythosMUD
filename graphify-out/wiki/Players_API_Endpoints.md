# Players API Endpoints

> 375 nodes

## Key Concepts

- **RateLimiter** (55 connections) — `server/realtime/rate_limiter.py`
- **MessageQueue** (53 connections) — `server/realtime/message_queue.py`
- **RoomSubscriptionManager** (45 connections) — `server/realtime/room_subscription_manager.py`
- **test_connection_disconnection.py** (34 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_connection_rate_limiter.py** (33 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **test_message_queue.py** (32 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **connection_disconnection.py** (31 connections) — `server/realtime/connection_disconnection.py`
- **connection_cleaner.py** (22 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **_DisconnectConnectionManager** (19 connections) — `server/realtime/connection_disconnection.py`
- **statistics_aggregator.py** (19 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **room_subscription_manager.py** (17 connections) — `server/realtime/room_subscription_manager.py`
- **test_connection_disconnection_websockets.py** (15 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **cleanup_websocket_disconnect()** (14 connections) — `server/realtime/connection_disconnection.py`
- **ConnectionMetadata** (14 connections) — `server/realtime/connection_models.py`
- **MemoryMonitor** (14 connections) — `server/realtime/memory_monitor.py`
- **disconnect_all_websockets_impl()** (13 connections) — `server/realtime/connection_disconnection.py`
- **_track_disconnect_if_needed()** (13 connections) — `server/realtime/connection_disconnection.py`
- **_cleanup_room_subscriptions()** (13 connections) — `server/realtime/connection_disconnection.py`
- **disconnect_connection_by_id_impl()** (13 connections) — `server/realtime/connection_disconnection.py`
- **room_event_handler.py** (13 connections) — `server/realtime/integration/room_event_handler.py`
- **message_queue.py** (13 connections) — `server/realtime/message_queue.py`
- **Any** (13 connections)
- **._canonical_room_id()** (13 connections) — `server/realtime/room_subscription_manager.py`
- **test_room_subscription_manager_npcs.py** (13 connections) — `server/tests/unit/realtime/test_room_subscription_manager_npcs.py`
- **rate_limiter.py** (12 connections) — `server/realtime/rate_limiter.py`
- *... and 350 more nodes in this community*

## Relationships

- [Room Occupant Events](Room_Occupant_Events.md) (25 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (18 shared connections)
- [Message Broadcaster Core](Message_Broadcaster_Core.md) (16 shared connections)
- [Level and XP Curve](Level_and_XP_Curve.md) (11 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (10 shared connections)
- [Architecture Decisions Adr](Architecture_Decisions_Adr.md) (9 shared connections)
- [Unified Command Handler](Unified_Command_Handler.md) (5 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (4 shared connections)
- [Logging Structured Setup](Logging_Structured_Setup.md) (3 shared connections)
- [Realtime WebSocket Auth](Realtime_WebSocket_Auth.md) (3 shared connections)
- [Connection Statistics Aggregator](Connection_Statistics_Aggregator.md) (3 shared connections)
- [App Router Integration](App_Router_Integration.md) (3 shared connections)

## Source Files

- `server/realtime/connection_disconnection.py`
- `server/realtime/connection_manager_methods.py`
- `server/realtime/connection_models.py`
- `server/realtime/integration/room_event_handler.py`
- `server/realtime/maintenance/connection_cleaner.py`
- `server/realtime/memory_monitor.py`
- `server/realtime/message_queue.py`
- `server/realtime/monitoring/statistics_aggregator.py`
- `server/realtime/rate_limiter.py`
- `server/realtime/room_subscription_manager.py`
- `server/tests/unit/realtime/test_connection_disconnection.py`
- `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- `server/tests/unit/realtime/test_connection_models.py`
- `server/tests/unit/realtime/test_connection_rate_limiter.py`
- `server/tests/unit/realtime/test_message_queue.py`
- `server/tests/unit/realtime/test_room_subscription_manager_npcs.py`

## Audit Trail

- EXTRACTED: 1259 (97%)
- INFERRED: 36 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*