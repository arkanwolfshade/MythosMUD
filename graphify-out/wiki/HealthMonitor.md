# HealthMonitor

> 82 nodes

## Key Concepts

- **HealthMonitor** (21 connections) — `server/realtime/monitoring/health_monitor.py`
- **test_connection_initialization.py** (18 connections) — `server/tests/unit/realtime/test_connection_initialization.py`
- **.__init__()** (12 connections) — `server/realtime/connection_manager.py`
- **initialize_connection_state()** (9 connections) — `server/realtime/connection_initialization.py`
- **initialize_messaging()** (9 connections) — `server/realtime/connection_initialization.py`
- **UUID** (9 connections)
- **initialize_connection_cleaner()** (8 connections) — `server/realtime/connection_initialization.py`
- **initialize_error_handler()** (8 connections) — `server/realtime/connection_initialization.py`
- **initialize_game_state_provider()** (8 connections) — `server/realtime/connection_initialization.py`
- **initialize_health_monitor()** (8 connections) — `server/realtime/connection_initialization.py`
- **initialize_room_event_handler()** (8 connections) — `server/realtime/connection_initialization.py`
- **._process_single_connection()** (8 connections) — `server/realtime/monitoring/health_monitor.py`
- **.acquire_async()** (8 connections) — `server/services/inventory_mutation_guard.py`
- **Lock** (8 connections)
- **Any** (8 connections)
- **_AsyncPlayerGuardState** (6 connections) — `server/services/inventory_mutation_guard.py`
- **.check_all_connections_health()** (6 connections) — `server/realtime/monitoring/health_monitor.py`
- **.periodic_health_check_task()** (5 connections) — `server/realtime/monitoring/health_monitor.py`
- **.start_periodic_checks()** (5 connections) — `server/realtime/monitoring/health_monitor.py`
- **._get_async_global_lock()** (5 connections) — `server/services/inventory_mutation_guard.py`
- **._get_async_state()** (5 connections) — `server/services/inventory_mutation_guard.py`
- **.check_player_connection_health()** (4 connections) — `server/realtime/monitoring/health_monitor.py`
- **._cleanup_stale_connections()** (4 connections) — `server/realtime/monitoring/health_monitor.py`
- **._find_player_id_for_cleanup()** (4 connections) — `server/realtime/monitoring/health_monitor.py`
- **._wait_for_task_cancellation()** (4 connections) — `server/realtime/monitoring/health_monitor.py`
- *... and 57 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (25 shared connections)
- [ContainerServiceError](ContainerServiceError.md) (7 shared connections)
- [test_health_monitor.py](test_health_monitor.py.md) (3 shared connections)
- [deque](deque.md) (2 shared connections)
- [NPCThreadManager](NPCThreadManager.md) (2 shared connections)
- [ConnectionCleaner](ConnectionCleaner.md) (1 shared connections)
- [ConnectionErrorHandler](ConnectionErrorHandler.md) (1 shared connections)
- [.state](state.md) (1 shared connections)
- [PersonalMessageSender](PersonalMessageSender.md) (1 shared connections)
- [MessageBroadcaster](MessageBroadcaster.md) (1 shared connections)
- [RoomEventHandler](RoomEventHandler.md) (1 shared connections)
- [EventPublisher](EventPublisher.md) (1 shared connections)

## Source Files

- `server/realtime/connection_initialization.py`
- `server/realtime/connection_manager.py`
- `server/realtime/monitoring/health_monitor.py`
- `server/services/inventory_mutation_guard.py`
- `server/tests/unit/realtime/test_connection_initialization.py`

## Audit Trail

- EXTRACTED: 162 (94%)
- INFERRED: 10 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*