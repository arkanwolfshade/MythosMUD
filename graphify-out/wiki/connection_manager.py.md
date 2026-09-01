# connection_manager.py

> 335 nodes

## Key Concepts

- **connection_manager.py** (129 connections) — `server/realtime/connection_manager.py`
- **RateLimiter** (69 connections) — `server/realtime/rate_limiter.py`
- **MessageQueue** (60 connections) — `server/realtime/message_queue.py`
- **RoomSubscriptionManager** (52 connections) — `server/realtime/room_subscription_manager.py`
- **test_connection_disconnection.py** (42 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **connection_initialization.py** (38 connections) — `server/realtime/connection_initialization.py`
- **connection_disconnection.py** (35 connections) — `server/realtime/connection_disconnection.py`
- **test_connection_rate_limiter.py** (33 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **_DisconnectConnectionManager** (26 connections) — `server/realtime/connection_disconnection.py`
- **PerformanceTracker** (26 connections) — `server/realtime/monitoring/performance_tracker.py`
- **statistics_aggregator.py** (26 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **test_connection_disconnection_websockets.py** (26 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **connection_cleaner.py** (23 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **room_subscription_manager.py** (21 connections) — `server/realtime/room_subscription_manager.py`
- **health_monitor.py** (18 connections) — `server/realtime/monitoring/health_monitor.py`
- **test_connection_initialization.py** (18 connections) — `server/tests/unit/realtime/test_connection_initialization.py`
- **message_queue.py** (17 connections) — `server/realtime/message_queue.py`
- **realtime/rate_limiter.py** (17 connections) — `server/realtime/rate_limiter.py`
- **UUID** (16 connections)
- **cleanup_websocket_disconnect()** (15 connections) — `server/realtime/connection_disconnection.py`
- **performance_tracker.py** (14 connections) — `server/realtime/monitoring/performance_tracker.py`
- **asyncio** (14 connections)
- **disconnect_all_websockets_impl()** (13 connections) — `server/realtime/connection_disconnection.py`
- **disconnect_connection_by_id_impl()** (13 connections) — `server/realtime/connection_disconnection.py`
- **initialize_core_components()** (13 connections) — `server/realtime/connection_initialization.py`
- *... and 310 more nodes in this community*

## Relationships

- [test_message_queue.py](test_message_queue.py.md) (38 shared connections)
- [get_logger](get_logger.md) (27 shared connections)
- [Any](Any.md) (23 shared connections)
- [test_connection_session_management.py](test_connection_session_management.py.md) (22 shared connections)
- [connection_manager_methods.py](connection_manager_methods.py.md) (22 shared connections)
- [test_connection_establishment.py](test_connection_establishment.py.md) (13 shared connections)
- [ConnectionManager](ConnectionManager.md) (12 shared connections)
- [MemoryMonitor](MemoryMonitor.md) (10 shared connections)
- [StatisticsAggregator](StatisticsAggregator.md) (9 shared connections)
- [time.py](time.py.md) (8 shared connections)
- [connection_cleanup_methods.py](connection_cleanup_methods.py.md) (8 shared connections)
- [test_health_monitor.py](test_health_monitor.py.md) (7 shared connections)

## Source Files

- `server/realtime/__init__.py`
- `server/realtime/connection_disconnection.py`
- `server/realtime/connection_initialization.py`
- `server/realtime/connection_manager.py`
- `server/realtime/connection_websocket_close.py`
- `server/realtime/integration/room_event_handler.py`
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
- `server/tests/unit/realtime/test_connection_initialization.py`
- `server/tests/unit/realtime/test_connection_manager_methods.py`
- `server/tests/unit/realtime/test_connection_rate_limiter.py`

## Audit Trail

- EXTRACTED: 906 (96%)
- INFERRED: 38 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*