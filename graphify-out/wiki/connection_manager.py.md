# connection_manager.py

> 287 nodes

## Key Concepts

- **connection_manager.py** (130 connections) — `server/realtime/connection_manager.py`
- **connection_manager_methods.py** (95 connections) — `server/realtime/connection_manager_methods.py`
- **RateLimiter** (69 connections) — `server/realtime/rate_limiter.py`
- **MessageQueue** (60 connections) — `server/realtime/message_queue.py`
- **RoomSubscriptionManager** (52 connections) — `server/realtime/room_subscription_manager.py`
- **connection_initialization.py** (39 connections) — `server/realtime/connection_initialization.py`
- **test_connection_rate_limiter.py** (33 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **StatisticsAggregator** (31 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **ConnectionMetadata** (30 connections) — `server/realtime/connection_models.py`
- **ConnectionErrorHandler** (28 connections) — `server/realtime/errors/error_handler.py`
- **PerformanceTracker** (28 connections) — `server/realtime/monitoring/performance_tracker.py`
- **statistics_aggregator.py** (26 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **connection_cleaner.py** (22 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **room_subscription_manager.py** (21 connections) — `server/realtime/room_subscription_manager.py`
- **test_connection_initialization.py** (18 connections) — `server/tests/unit/realtime/test_connection_initialization.py`
- **message_queue.py** (17 connections) — `server/realtime/message_queue.py`
- **realtime/rate_limiter.py** (17 connections) — `server/realtime/rate_limiter.py`
- **health_monitor.py** (16 connections) — `server/realtime/monitoring/health_monitor.py`
- **test_connection_error_handler.py** (15 connections) — `server/tests/unit/realtime/test_connection_error_handler.py`
- **performance_tracker.py** (14 connections) — `server/realtime/monitoring/performance_tracker.py`
- **initialize_core_components()** (13 connections) — `server/realtime/connection_initialization.py`
- **connection_models.py** (13 connections) — `server/realtime/connection_models.py`
- **error_handler.py** (13 connections) — `server/realtime/errors/error_handler.py`
- **.__init__()** (12 connections) — `server/realtime/connection_manager.py`
- **._build_connection_stats()** (10 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- *... and 262 more nodes in this community*

## Relationships

- [ConnectionManager](ConnectionManager.md) (66 shared connections)
- [get_logger](get_logger.md) (40 shared connections)
- [test_message_queue.py](test_message_queue.py.md) (38 shared connections)
- [test_connection_disconnection.py](test_connection_disconnection.py.md) (35 shared connections)
- [test_connection_establishment.py](test_connection_establishment.py.md) (21 shared connections)
- [Any](Any.md) (20 shared connections)
- [test_connection_session_management.py](test_connection_session_management.py.md) (19 shared connections)
- [test_connection_delegates.py](test_connection_delegates.py.md) (19 shared connections)
- [MemoryMonitor](MemoryMonitor.md) (12 shared connections)
- [.detect_and_handle_error_state](detect_and_handle_error_state.md) (9 shared connections)
- [connection_cleanup_methods.py](connection_cleanup_methods.py.md) (9 shared connections)
- [test_health_monitor.py](test_health_monitor.py.md) (8 shared connections)

## Source Files

- `server/realtime/__init__.py`
- `server/realtime/connection_initialization.py`
- `server/realtime/connection_manager.py`
- `server/realtime/connection_manager_methods.py`
- `server/realtime/connection_models.py`
- `server/realtime/errors/__init__.py`
- `server/realtime/errors/error_handler.py`
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
- `server/tests/unit/realtime/test_connection_error_handler.py`
- `server/tests/unit/realtime/test_connection_initialization.py`
- `server/tests/unit/realtime/test_connection_models.py`

## Audit Trail

- EXTRACTED: 867 (94%)
- INFERRED: 57 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*