# connection_manager.py

> 340 nodes

## Key Concepts

- **connection_manager.py** (130 connections) — `server/realtime/connection_manager.py`
- **time.py** (106 connections) — `server/container/bundles/time.py`
- **RateLimiter** (69 connections) — `server/realtime/rate_limiter.py`
- **MessageQueue** (60 connections) — `server/realtime/message_queue.py`
- **RoomSubscriptionManager** (52 connections) — `server/realtime/room_subscription_manager.py`
- **test_connection_disconnection.py** (43 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **connection_initialization.py** (38 connections) — `server/realtime/connection_initialization.py`
- **connection_disconnection.py** (34 connections) — `server/realtime/connection_disconnection.py`
- **test_connection_rate_limiter.py** (33 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **ConnectionMetadata** (30 connections) — `server/realtime/connection_models.py`
- **_DisconnectConnectionManager** (26 connections) — `server/realtime/connection_disconnection.py`
- **PerformanceTracker** (26 connections) — `server/realtime/monitoring/performance_tracker.py`
- **connection_session_management.py** (25 connections) — `server/realtime/connection_session_management.py`
- **statistics_aggregator.py** (25 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **test_connection_disconnection_websockets.py** (25 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **connection_cleaner.py** (22 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **room_subscription_manager.py** (21 connections) — `server/realtime/room_subscription_manager.py`
- **handle_new_game_session_impl()** (17 connections) — `server/realtime/connection_session_management.py`
- **message_queue.py** (17 connections) — `server/realtime/message_queue.py`
- **realtime/rate_limiter.py** (17 connections) — `server/realtime/rate_limiter.py`
- **UUID** (16 connections)
- **health_monitor.py** (16 connections) — `server/realtime/monitoring/health_monitor.py`
- **cleanup_websocket_disconnect()** (15 connections) — `server/realtime/connection_disconnection.py`
- **_SessionConnectionManager** (14 connections) — `server/realtime/connection_session_management.py`
- **performance_tracker.py** (14 connections) — `server/realtime/monitoring/performance_tracker.py`
- *... and 315 more nodes in this community*

## Relationships

- [test_message_queue.py](test_message_queue.py.md) (37 shared connections)
- [get_logger](get_logger.md) (35 shared connections)
- [test_connection_session_management.py](test_connection_session_management.py.md) (27 shared connections)
- [test_connection_establishment.py](test_connection_establishment.py.md) (25 shared connections)
- [connection_manager_methods.py](connection_manager_methods.py.md) (24 shared connections)
- [RoomEventHandler](RoomEventHandler.md) (23 shared connections)
- [ConnectionManager](ConnectionManager.md) (21 shared connections)
- [Any](Any.md) (20 shared connections)
- [MemoryMonitor](MemoryMonitor.md) (12 shared connections)
- [test_connection_delegates.py](test_connection_delegates.py.md) (9 shared connections)
- [StatisticsAggregator](StatisticsAggregator.md) (9 shared connections)
- [connection_cleanup_methods.py](connection_cleanup_methods.py.md) (9 shared connections)

## Source Files

- `server/container/bundles/time.py`
- `server/realtime/connection_disconnection.py`
- `server/realtime/connection_initialization.py`
- `server/realtime/connection_manager.py`
- `server/realtime/connection_models.py`
- `server/realtime/connection_session_management.py`
- `server/realtime/connection_websocket_close.py`
- `server/realtime/maintenance/connection_cleaner.py`
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
- `server/tests/unit/realtime/test_connection_manager_methods.py`
- `server/tests/unit/realtime/test_connection_models.py`

## Audit Trail

- EXTRACTED: 1025 (96%)
- INFERRED: 43 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*