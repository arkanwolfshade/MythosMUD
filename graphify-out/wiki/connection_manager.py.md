# connection_manager.py

> 227 nodes

## Key Concepts

- **connection_manager.py** (127 connections) — `server/realtime/connection_manager.py`
- **time.py** (99 connections) — `server/container/bundles/time.py`
- **MessageQueue** (60 connections) — `server/realtime/message_queue.py`
- **MemoryMonitor** (39 connections) — `server/realtime/memory_monitor.py`
- **connection_initialization.py** (38 connections) — `server/realtime/connection_initialization.py`
- **memory_monitor.py** (37 connections) — `server/realtime/memory_monitor.py`
- **test_memory_monitor.py** (32 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **PerformanceTracker** (26 connections) — `server/realtime/monitoring/performance_tracker.py`
- **statistics_aggregator.py** (26 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **connection_cleaner.py** (24 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **HealthMonitor** (23 connections) — `server/realtime/monitoring/health_monitor.py`
- **health_monitor.py** (18 connections) — `server/realtime/monitoring/health_monitor.py`
- **test_connection_initialization.py** (18 connections) — `server/tests/unit/realtime/test_connection_initialization.py`
- **message_queue.py** (17 connections) — `server/realtime/message_queue.py`
- **realtime/rate_limiter.py** (17 connections) — `server/realtime/rate_limiter.py`
- **performance_tracker.py** (14 connections) — `server/realtime/monitoring/performance_tracker.py`
- **initialize_core_components()** (13 connections) — `server/realtime/connection_initialization.py`
- **collect_idle_memory_sample()** (13 connections) — `server/realtime/memory_monitor.py`
- **.__init__()** (12 connections) — `server/realtime/connection_manager.py`
- **initialize_connection_state()** (9 connections) — `server/realtime/connection_initialization.py`
- **initialize_messaging()** (9 connections) — `server/realtime/connection_initialization.py`
- **UUID** (9 connections)
- **test_performance_tracker.py** (9 connections) — `server/tests/unit/realtime/monitoring/test_performance_tracker.py`
- **initialize_connection_cleaner()** (8 connections) — `server/realtime/connection_initialization.py`
- **initialize_error_handler()** (8 connections) — `server/realtime/connection_initialization.py`
- *... and 202 more nodes in this community*

## Relationships

- [test_message_queue.py](test_message_queue.py.md) (39 shared connections)
- [get_logger](get_logger.md) (32 shared connections)
- [RoomSubscriptionManager](RoomSubscriptionManager.md) (24 shared connections)
- [test_connection_disconnection.py](test_connection_disconnection.py.md) (20 shared connections)
- [connection_manager_methods.py](connection_manager_methods.py.md) (19 shared connections)
- [RateLimiter](RateLimiter.md) (10 shared connections)
- [StatisticsAggregator](StatisticsAggregator.md) (9 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (9 shared connections)
- [connection_establishment.py](connection_establishment.py.md) (8 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (8 shared connections)
- [connection_cleanup_methods.py](connection_cleanup_methods.py.md) (8 shared connections)
- [EventBus](EventBus.md) (7 shared connections)

## Source Files

- `server/container/bundles/time.py`
- `server/realtime/__init__.py`
- `server/realtime/connection_initialization.py`
- `server/realtime/connection_manager.py`
- `server/realtime/maintenance/connection_cleaner.py`
- `server/realtime/memory_monitor.py`
- `server/realtime/message_queue.py`
- `server/realtime/monitoring/__init__.py`
- `server/realtime/monitoring/health_monitor.py`
- `server/realtime/monitoring/performance_tracker.py`
- `server/realtime/monitoring/statistics_aggregator.py`
- `server/realtime/rate_limiter.py`
- `server/structured_logging/log_aggregator.py`
- `server/tests/unit/realtime/monitoring/test_performance_tracker.py`
- `server/tests/unit/realtime/test_connection_disconnection.py`
- `server/tests/unit/realtime/test_connection_initialization.py`
- `server/tests/unit/realtime/test_memory_monitor.py`

## Audit Trail

- EXTRACTED: 757 (97%)
- INFERRED: 20 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*