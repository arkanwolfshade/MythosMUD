# Room Broadcast

> 808 nodes

## Key Concepts

- **ConnectionManager** (221 connections) — `server/realtime/connection_manager.py`
- **connection_manager.py** (160 connections) — `server/realtime/connection_manager.py`
- **connection_manager_methods.py** (79 connections) — `server/realtime/connection_manager_methods.py`
- **RateLimiter** (61 connections) — `server/realtime/rate_limiter.py`
- **MessageQueue** (54 connections) — `server/realtime/message_queue.py`
- **RoomSubscriptionManager** (46 connections) — `server/realtime/room_subscription_manager.py`
- **UUID** (41 connections)
- **connection_initialization.py** (38 connections) — `server/realtime/connection_initialization.py`
- **test_connection_disconnection.py** (37 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_connection_helpers_impl.py** (35 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_connection_rate_limiter.py** (33 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **connection_disconnection.py** (31 connections) — `server/realtime/connection_disconnection.py`
- **test_connection_statistics.py** (24 connections) — `server/tests/unit/realtime/test_connection_statistics.py`
- **connection_cleaner.py** (22 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **HealthMonitor** (22 connections) — `server/realtime/monitoring/health_monitor.py`
- **statistics_aggregator.py** (22 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **connection_helpers.py** (21 connections) — `server/realtime/connection_helpers.py`
- **UUID** (21 connections)
- **ConnectionMetadata** (21 connections) — `server/realtime/connection_models.py`
- **game_state_provider.py** (21 connections) — `server/realtime/integration/game_state_provider.py`
- **_DisconnectConnectionManager** (19 connections) — `server/realtime/connection_disconnection.py`
- **convert_uuids_to_strings()** (18 connections) — `server/realtime/connection_helpers.py`
- **PerformanceTracker** (18 connections) — `server/realtime/monitoring/performance_tracker.py`
- **room_subscription_manager.py** (18 connections) — `server/realtime/room_subscription_manager.py`
- **test_connection_initialization.py** (18 connections) — `server/tests/unit/realtime/test_connection_initialization.py`
- *... and 783 more nodes in this community*

## Relationships

- [command inventory factories](command_inventory_factories.md) (42 shared connections)
- [Database Config](Database_Config.md) (33 shared connections)
- [connection realtime delegates](connection_realtime_delegates.md) (28 shared connections)
- [connection disconnection realtime](connection_disconnection_realtime.md) (23 shared connections)
- [room realtime subscription](room_realtime_subscription.md) (20 shared connections)
- [combat services messaging](combat_services_messaging.md) (15 shared connections)
- [NPC Combat](NPC_Combat.md) (15 shared connections)
- [container service services](container_service_services.md) (15 shared connections)
- [event realtime publisher](event_realtime_publisher.md) (14 shared connections)
- [item models rationale](item_models_rationale.md) (13 shared connections)
- [realtime websocket initial](realtime_websocket_initial.md) (12 shared connections)
- [time service rationale](time_service_rationale.md) (11 shared connections)

## Source Files

- `server/realtime/connection_disconnection.py`
- `server/realtime/connection_event_helpers.py`
- `server/realtime/connection_helpers.py`
- `server/realtime/connection_initialization.py`
- `server/realtime/connection_manager.py`
- `server/realtime/connection_manager_methods.py`
- `server/realtime/connection_models.py`
- `server/realtime/connection_room_utils.py`
- `server/realtime/connection_statistics.py`
- `server/realtime/errors/__init__.py`
- `server/realtime/errors/error_handler.py`
- `server/realtime/integration/__init__.py`
- `server/realtime/integration/game_state_provider.py`
- `server/realtime/integration/room_event_handler.py`
- `server/realtime/maintenance/connection_cleaner.py`
- `server/realtime/memory_monitor.py`
- `server/realtime/message_queue.py`
- `server/realtime/messaging/personal_message_sender.py`
- `server/realtime/monitoring/__init__.py`
- `server/realtime/monitoring/health_monitor.py`

## Audit Trail

- EXTRACTED: 3265 (97%)
- INFERRED: 96 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*