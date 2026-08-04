# taunt combat commands

> 262 nodes

## Key Concepts

- **time.py** (96 connections) — `server/container/bundles/time.py`
- **MessageQueue** (54 connections) — `server/realtime/message_queue.py`
- **RoomSubscriptionManager** (46 connections) — `server/realtime/room_subscription_manager.py`
- **connection_initialization.py** (38 connections) — `server/realtime/connection_initialization.py`
- **test_message_queue.py** (32 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **MemoryMonitor** (27 connections) — `server/realtime/memory_monitor.py`
- **deque** (26 connections)
- **PerformanceTracker** (25 connections) — `server/realtime/monitoring/performance_tracker.py`
- **connection_cleaner.py** (22 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **HealthMonitor** (22 connections) — `server/realtime/monitoring/health_monitor.py`
- **statistics_aggregator.py** (22 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **test_memory_monitor.py** (21 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **room_subscription_manager.py** (18 connections) — `server/realtime/room_subscription_manager.py`
- **test_connection_initialization.py** (18 connections) — `server/tests/unit/realtime/test_connection_initialization.py`
- **test_connection_disconnection_websockets.py** (15 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **message_queue.py** (14 connections) — `server/realtime/message_queue.py`
- **health_monitor.py** (14 connections) — `server/realtime/monitoring/health_monitor.py`
- **rate_limiter.py** (14 connections) — `server/realtime/rate_limiter.py`
- **initialize_core_components()** (13 connections) — `server/realtime/connection_initialization.py`
- **.__init__()** (12 connections) — `server/realtime/connection_manager.py`
- **performance_tracker.py** (11 connections) — `server/realtime/monitoring/performance_tracker.py`
- **memory_monitor.py** (10 connections) — `server/realtime/memory_monitor.py`
- **initialize_connection_state()** (9 connections) — `server/realtime/connection_initialization.py`
- **initialize_messaging()** (9 connections) — `server/realtime/connection_initialization.py`
- **connection_models.py** (9 connections) — `server/realtime/connection_models.py`
- *... and 237 more nodes in this community*

## Relationships

- [persistence rationale room](persistence_rationale_room.md) (27 shared connections)
- [NPC Combat](NPC_Combat.md) (23 shared connections)
- [Room Broadcast](Room_Broadcast.md) (20 shared connections)
- [spell models rationale](spell_models_rationale.md) (20 shared connections)
- [connection disconnection realtime](connection_disconnection_realtime.md) (10 shared connections)
- [event realtime publisher](event_realtime_publisher.md) (9 shared connections)
- [services npc startup](services_npc_startup.md) (7 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (6 shared connections)
- [realtime maintenance connection](realtime_maintenance_connection.md) (6 shared connections)
- [combat configuration service](combat_configuration_service.md) (6 shared connections)
- [room subscription manager](room_subscription_manager.md) (6 shared connections)
- [mythos mud mapbuilder](mythos_mud_mapbuilder.md) (5 shared connections)

## Source Files

- `server/container/bundles/time.py`
- `server/realtime/connection_initialization.py`
- `server/realtime/connection_manager.py`
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
- `server/tests/unit/realtime/test_memory_monitor.py`
- `server/tests/unit/realtime/test_message_queue.py`

## Audit Trail

- EXTRACTED: 1074 (96%)
- INFERRED: 50 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*