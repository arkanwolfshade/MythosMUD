# connection_manager.py

> 217 nodes

## Key Concepts

- **connection_manager.py** (163 connections) — `server/realtime/connection_manager.py`
- **time.py** (96 connections) — `server/container/bundles/time.py`
- **connection_initialization.py** (38 connections) — `server/realtime/connection_initialization.py`
- **test_connection_disconnection.py** (37 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **connection_disconnection.py** (31 connections) — `server/realtime/connection_disconnection.py`
- **MemoryMonitor** (27 connections) — `server/realtime/memory_monitor.py`
- **PerformanceTracker** (25 connections) — `server/realtime/monitoring/performance_tracker.py`
- **connection_cleaner.py** (23 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **HealthMonitor** (22 connections) — `server/realtime/monitoring/health_monitor.py`
- **statistics_aggregator.py** (22 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **ConnectionMetadata** (21 connections) — `server/realtime/connection_models.py`
- **test_memory_monitor.py** (21 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **_DisconnectConnectionManager** (19 connections) — `server/realtime/connection_disconnection.py`
- **test_connection_disconnection_websockets.py** (19 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **room_subscription_manager.py** (18 connections) — `server/realtime/room_subscription_manager.py`
- **test_connection_initialization.py** (18 connections) — `server/tests/unit/realtime/test_connection_initialization.py`
- **cleanup_websocket_disconnect()** (16 connections) — `server/realtime/connection_disconnection.py`
- **_cleanup_room_subscriptions()** (14 connections) — `server/realtime/connection_disconnection.py`
- **_track_disconnect_if_needed()** (14 connections) — `server/realtime/connection_disconnection.py`
- **message_queue.py** (14 connections) — `server/realtime/message_queue.py`
- **health_monitor.py** (14 connections) — `server/realtime/monitoring/health_monitor.py`
- **realtime/rate_limiter.py** (14 connections) — `server/realtime/rate_limiter.py`
- **disconnect_all_websockets_impl()** (13 connections) — `server/realtime/connection_disconnection.py`
- **initialize_core_components()** (13 connections) — `server/realtime/connection_initialization.py`
- **safe_close_websocket_impl()** (13 connections) — `server/realtime/connection_manager_methods.py`
- *... and 192 more nodes in this community*

## Relationships

- [connection_manager_methods.py](connection_manager_methods.py.md) (53 shared connections)
- [get_logger](get_logger.md) (46 shared connections)
- [ConnectionManager](ConnectionManager.md) (26 shared connections)
- [UUID](UUID.md) (14 shared connections)
- [MessageQueue](MessageQueue.md) (12 shared connections)
- [RateLimiter](RateLimiter.md) (12 shared connections)
- [RoomSubscriptionManager](RoomSubscriptionManager.md) (9 shared connections)
- [StatisticsAggregator](StatisticsAggregator.md) (8 shared connections)
- [broadcast_game_event](broadcast_game_event.md) (8 shared connections)
- [connection_cleanup_methods.py](connection_cleanup_methods.py.md) (8 shared connections)
- [EventBus](EventBus.md) (7 shared connections)
- [test_player_presence_tracker.py](test_player_presence_tracker.py.md) (7 shared connections)

## Source Files

- `server/container/bundles/time.py`
- `server/realtime/connection_disconnection.py`
- `server/realtime/connection_initialization.py`
- `server/realtime/connection_manager.py`
- `server/realtime/connection_manager_methods.py`
- `server/realtime/connection_models.py`
- `server/realtime/maintenance/connection_cleaner.py`
- `server/realtime/memory_monitor.py`
- `server/realtime/message_queue.py`
- `server/realtime/monitoring/__init__.py`
- `server/realtime/monitoring/health_monitor.py`
- `server/realtime/monitoring/performance_tracker.py`
- `server/realtime/monitoring/statistics_aggregator.py`
- `server/realtime/rate_limiter.py`
- `server/realtime/room_subscription_manager.py`
- `server/tests/unit/realtime/monitoring/test_performance_tracker.py`
- `server/tests/unit/realtime/test_connection_disconnection.py`
- `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- `server/tests/unit/realtime/test_connection_initialization.py`
- `server/tests/unit/realtime/test_connection_models.py`

## Audit Trail

- EXTRACTED: 808 (98%)
- INFERRED: 16 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*