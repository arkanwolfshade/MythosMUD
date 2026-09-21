# connection_manager.py

> 579 nodes

## Key Concepts

- **connection_manager.py** (130 connections) — `server/realtime/connection_manager.py`
- **time.py** (107 connections) — `server/container/bundles/time.py`
- **connection_manager_methods.py** (95 connections) — `server/realtime/connection_manager_methods.py`
- **RateLimiter** (69 connections) — `server/realtime/rate_limiter.py`
- **MessageQueue** (60 connections) — `server/realtime/message_queue.py`
- **RoomSubscriptionManager** (52 connections) — `server/realtime/room_subscription_manager.py`
- **connection_initialization.py** (39 connections) — `server/realtime/connection_initialization.py`
- **memory_monitor.py** (37 connections) — `server/realtime/memory_monitor.py`
- **test_connection_rate_limiter.py** (33 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **test_message_queue.py** (32 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **ConnectionMetadata** (30 connections) — `server/realtime/connection_models.py`
- **PerformanceTracker** (28 connections) — `server/realtime/monitoring/performance_tracker.py`
- **player_disconnect_handlers.py** (28 connections) — `server/realtime/player_disconnect_handlers.py`
- **deque** (27 connections)
- **connection_session_management.py** (26 connections) — `server/realtime/connection_session_management.py`
- **statistics_aggregator.py** (26 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **test_connection_cleaner.py** (26 connections) — `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- **HealthMonitor** (25 connections) — `server/realtime/monitoring/health_monitor.py`
- **test_connection_statistics.py** (24 connections) — `server/tests/unit/realtime/test_connection_statistics.py`
- **connection_cleaner.py** (22 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **room_subscription_manager.py** (21 connections) — `server/realtime/room_subscription_manager.py`
- **connection_cleanup_methods.py** (19 connections) — `server/realtime/connection_cleanup_methods.py`
- **test_connection_initialization.py** (18 connections) — `server/tests/unit/realtime/test_connection_initialization.py`
- **message_queue.py** (17 connections) — `server/realtime/message_queue.py`
- **realtime/rate_limiter.py** (17 connections) — `server/realtime/rate_limiter.py`
- *... and 554 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (70 shared connections)
- [ConnectionManager](ConnectionManager.md) (69 shared connections)
- [test_connection_disconnection.py](test_connection_disconnection.py.md) (35 shared connections)
- [test_connection_delegates.py](test_connection_delegates.py.md) (25 shared connections)
- [test_connection_session_management.py](test_connection_session_management.py.md) (21 shared connections)
- [connection_establishment.py](connection_establishment.py.md) (18 shared connections)
- [event_types.py](event_types.py.md) (13 shared connections)
- [test_player_disconnect_handlers.py](test_player_disconnect_handlers.py.md) (12 shared connections)
- [asyncio](asyncio.md) (11 shared connections)
- [ConnectionCleaner](ConnectionCleaner.md) (10 shared connections)
- [MemoryMonitor](MemoryMonitor.md) (10 shared connections)
- [collect_idle_memory_sample](collect_idle_memory_sample.md) (10 shared connections)

## Source Files

- `server/container/bundles/time.py`
- `server/realtime/connection_cleanup_methods.py`
- `server/realtime/connection_initialization.py`
- `server/realtime/connection_manager.py`
- `server/realtime/connection_manager_methods.py`
- `server/realtime/connection_models.py`
- `server/realtime/connection_room_utils.py`
- `server/realtime/connection_session_management.py`
- `server/realtime/connection_statistics.py`
- `server/realtime/integration/room_event_handler.py`
- `server/realtime/maintenance/connection_cleaner.py`
- `server/realtime/memory_monitor.py`
- `server/realtime/message_queue.py`
- `server/realtime/messaging/personal_message_sender.py`
- `server/realtime/monitoring/__init__.py`
- `server/realtime/monitoring/health_monitor.py`
- `server/realtime/monitoring/performance_tracker.py`
- `server/realtime/monitoring/statistics_aggregator.py`
- `server/realtime/player_disconnect_handlers.py`
- `server/realtime/rate_limiter.py`

## Audit Trail

- EXTRACTED: 1447 (95%)
- INFERRED: 73 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*