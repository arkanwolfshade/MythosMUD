# time.py

> 490 nodes

## Key Concepts

- **time.py** (89 connections) — `server/container/bundles/time.py`
- **RateLimiter** (51 connections) — `server/realtime/rate_limiter.py`
- **MessageQueue** (50 connections) — `server/realtime/message_queue.py`
- **RoomSubscriptionManager** (43 connections) — `server/realtime/room_subscription_manager.py`
- **connection_initialization.py** (41 connections) — `server/realtime/connection_initialization.py`
- **test_connection_disconnection.py** (34 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_connection_rate_limiter.py** (33 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **connection_disconnection.py** (32 connections) — `server/realtime/connection_disconnection.py`
- **test_message_queue.py** (32 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **HealthMonitor** (22 connections) — `server/realtime/monitoring/health_monitor.py`
- **connection_cleaner.py** (22 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **_DisconnectConnectionManager** (20 connections) — `server/realtime/connection_disconnection.py`
- **statistics_aggregator.py** (19 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **test_connection_disconnection_websockets.py** (19 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **get_global_tracked_manager()** (18 connections) — `server/app/tracked_task_manager.py`
- **PerformanceTracker** (17 connections) — `server/realtime/monitoring/performance_tracker.py`
- **room_subscription_manager.py** (17 connections) — `server/realtime/room_subscription_manager.py`
- **tracked_task_manager.py** (14 connections) — `server/app/tracked_task_manager.py`
- **MemoryMonitor** (13 connections) — `server/realtime/memory_monitor.py`
- **disconnect_all_websockets_impl()** (13 connections) — `server/realtime/connection_disconnection.py`
- **._canonical_room_id()** (13 connections) — `server/realtime/room_subscription_manager.py`
- **message_queue.py** (13 connections) — `server/realtime/message_queue.py`
- **health_monitor.py** (13 connections) — `server/realtime/monitoring/health_monitor.py`
- **Any** (13 connections)
- **test_room_subscription_manager_npcs.py** (13 connections) — `server/tests/unit/realtime/test_room_subscription_manager_npcs.py`
- *... and 465 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (52 shared connections)
- [test_connection_initialization.py](test_connection_initialization.py.md) (15 shared connections)
- [connection_manager.py](connection_manager.py.md) (11 shared connections)
- [deque](deque.md) (9 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (8 shared connections)
- [EventBus](EventBus.md) (8 shared connections)
- [StatisticsAggregator](StatisticsAggregator.md) (7 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (7 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (6 shared connections)
- [test_connection_establishment.py](test_connection_establishment.py.md) (5 shared connections)
- [.add_message](add_message.md) (5 shared connections)
- [test_health_monitor.py](test_health_monitor.py.md) (4 shared connections)

## Source Files

- `server/app/memory_cleanup_service.py`
- `server/app/memory_lifespan_coordinator.py`
- `server/app/tracked_task_manager.py`
- `server/container/bundles/time.py`
- `server/realtime/connection_disconnection.py`
- `server/realtime/connection_initialization.py`
- `server/realtime/maintenance/connection_cleaner.py`
- `server/realtime/memory_monitor.py`
- `server/realtime/message_queue.py`
- `server/realtime/messaging/__init__.py`
- `server/realtime/messaging/personal_message_sender.py`
- `server/realtime/monitoring/__init__.py`
- `server/realtime/monitoring/health_monitor.py`
- `server/realtime/monitoring/performance_tracker.py`
- `server/realtime/monitoring/statistics_aggregator.py`
- `server/realtime/rate_limiter.py`
- `server/realtime/room_subscription_manager.py`
- `server/services/game_tick_service.py`
- `server/tests/unit/realtime/test_connection_disconnection.py`
- `server/tests/unit/realtime/test_connection_disconnection_websockets.py`

## Audit Trail

- EXTRACTED: 1005 (99%)
- INFERRED: 15 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*