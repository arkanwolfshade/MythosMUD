# connection_initialization.py

> 141 nodes

## Key Concepts

- **MemoryMonitor** (39 connections) — `server/realtime/memory_monitor.py`
- **connection_initialization.py** (39 connections) — `server/realtime/connection_initialization.py`
- **memory_monitor.py** (37 connections) — `server/realtime/memory_monitor.py`
- **test_memory_monitor.py** (35 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **statistics_aggregator.py** (26 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **room_subscription_manager.py** (23 connections) — `server/realtime/room_subscription_manager.py`
- **test_connection_initialization.py** (18 connections) — `server/tests/unit/realtime/test_connection_initialization.py`
- **collect_idle_memory_sample()** (15 connections) — `server/realtime/memory_monitor.py`
- **initialize_core_components()** (13 connections) — `server/realtime/connection_initialization.py`
- **.__init__()** (12 connections) — `server/realtime/connection_manager.py`
- **initialize_connection_state()** (9 connections) — `server/realtime/connection_initialization.py`
- **initialize_messaging()** (9 connections) — `server/realtime/connection_initialization.py`
- **initialize_connection_cleaner()** (8 connections) — `server/realtime/connection_initialization.py`
- **initialize_game_state_provider()** (8 connections) — `server/realtime/connection_initialization.py`
- **initialize_health_monitor()** (8 connections) — `server/realtime/connection_initialization.py`
- **initialize_room_event_handler()** (8 connections) — `server/realtime/connection_initialization.py`
- **Any** (8 connections)
- **idle_sampler_path()** (7 connections) — `server/realtime/memory_monitor.py`
- **_max_connection_age_seconds()** (7 connections) — `server/realtime/memory_monitor.py`
- **._run_idle_sampler()** (7 connections) — `server/realtime/memory_monitor.py`
- **.start_idle_sampler()** (7 connections) — `server/realtime/memory_monitor.py`
- **_container_instance()** (6 connections) — `server/realtime/memory_monitor.py`
- **idle_sampler_interval_seconds()** (6 connections) — `server/realtime/memory_monitor.py`
- **_task_qualname()** (6 connections) — `server/realtime/memory_monitor.py`
- **ConnectionStatsSnapshot** (5 connections) — `server/realtime/memory_monitor.py`
- *... and 116 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (26 shared connections)
- [MessageQueue](MessageQueue.md) (9 shared connections)
- [ConnectionErrorHandler](ConnectionErrorHandler.md) (7 shared connections)
- [ConnectionCleaner](ConnectionCleaner.md) (6 shared connections)
- [StatisticsAggregator](StatisticsAggregator.md) (6 shared connections)
- [connection_manager_methods.py](connection_manager_methods.py.md) (5 shared connections)
- [RoomSubscriptionManager](RoomSubscriptionManager.md) (5 shared connections)
- [PerformanceTracker](PerformanceTracker.md) (4 shared connections)
- [test_message_broadcaster.py](test_message_broadcaster.py.md) (4 shared connections)
- [RoomEventHandler](RoomEventHandler.md) (4 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (3 shared connections)
- [RateLimiter](RateLimiter.md) (3 shared connections)

## Source Files

- `server/container/main.py`
- `server/realtime/connection_initialization.py`
- `server/realtime/connection_manager.py`
- `server/realtime/memory_monitor.py`
- `server/realtime/monitoring/statistics_aggregator.py`
- `server/realtime/room_subscription_manager.py`
- `server/tests/unit/realtime/test_connection_initialization.py`
- `server/tests/unit/realtime/test_memory_monitor.py`

## Audit Trail

- EXTRACTED: 357 (98%)
- INFERRED: 7 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*