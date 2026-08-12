# RateLimiter

> 530 nodes

## Key Concepts

- **RateLimiter** (51 connections) — `server/realtime/rate_limiter.py`
- **MessageQueue** (50 connections) — `server/realtime/message_queue.py`
- **RoomSubscriptionManager** (43 connections) — `server/realtime/room_subscription_manager.py`
- **connection_initialization.py** (41 connections) — `server/realtime/connection_initialization.py`
- **test_connection_disconnection.py** (34 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_connection_rate_limiter.py** (33 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **connection_disconnection.py** (32 connections) — `server/realtime/connection_disconnection.py`
- **test_message_queue.py** (32 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **deque** (24 connections)
- **HealthMonitor** (22 connections) — `server/realtime/monitoring/health_monitor.py`
- **connection_cleaner.py** (22 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **_DisconnectConnectionManager** (20 connections) — `server/realtime/connection_disconnection.py`
- **statistics_aggregator.py** (19 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **test_connection_disconnection_websockets.py** (19 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **PerformanceTracker** (17 connections) — `server/realtime/monitoring/performance_tracker.py`
- **room_subscription_manager.py** (17 connections) — `server/realtime/room_subscription_manager.py`
- **test_health_monitor.py** (16 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **test_connection_initialization.py** (16 connections) — `server/tests/unit/realtime/test_connection_initialization.py`
- **MemoryMonitor** (13 connections) — `server/realtime/memory_monitor.py`
- **disconnect_all_websockets_impl()** (13 connections) — `server/realtime/connection_disconnection.py`
- **._canonical_room_id()** (13 connections) — `server/realtime/room_subscription_manager.py`
- **message_queue.py** (13 connections) — `server/realtime/message_queue.py`
- **health_monitor.py** (13 connections) — `server/realtime/monitoring/health_monitor.py`
- **Any** (13 connections)
- **test_room_subscription_manager_npcs.py** (13 connections) — `server/tests/unit/realtime/test_room_subscription_manager_npcs.py`
- *... and 505 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (38 shared connections)
- [connection_manager.py](connection_manager.py.md) (12 shared connections)
- [StatisticsAggregator](StatisticsAggregator.md) (7 shared connections)
- [MessageBroadcaster](MessageBroadcaster.md) (5 shared connections)
- [mythos_mud_mapbuilder.py](mythos_mud_mapbuilder.py.md) (5 shared connections)
- [GameStateProvider](GameStateProvider.md) (4 shared connections)
- [ConnectionCleaner](ConnectionCleaner.md) (4 shared connections)
- [test_connection_establishment.py](test_connection_establishment.py.md) (3 shared connections)
- [test_room_subscription_manager_helpers.py](test_room_subscription_manager_helpers.py.md) (3 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (3 shared connections)
- [message_broadcaster.py](message_broadcaster.py.md) (3 shared connections)
- [ConnectionManager](ConnectionManager.md) (3 shared connections)

## Source Files

- `server/realtime/connection_disconnection.py`
- `server/realtime/connection_initialization.py`
- `server/realtime/integration/room_event_handler.py`
- `server/realtime/maintenance/connection_cleaner.py`
- `server/realtime/memory_monitor.py`
- `server/realtime/message_queue.py`
- `server/realtime/messaging/personal_message_sender.py`
- `server/realtime/monitoring/__init__.py`
- `server/realtime/monitoring/health_monitor.py`
- `server/realtime/monitoring/performance_tracker.py`
- `server/realtime/monitoring/statistics_aggregator.py`
- `server/realtime/rate_limiter.py`
- `server/realtime/room_subscription_manager.py`
- `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- `server/tests/unit/realtime/test_connection_disconnection.py`
- `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- `server/tests/unit/realtime/test_connection_initialization.py`
- `server/tests/unit/realtime/test_connection_rate_limiter.py`
- `server/tests/unit/realtime/test_message_queue.py`
- `server/tests/unit/realtime/test_room_subscription_manager_npcs.py`

## Audit Trail

- EXTRACTED: 1836 (98%)
- INFERRED: 42 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*