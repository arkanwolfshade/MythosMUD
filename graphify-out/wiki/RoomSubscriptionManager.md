# RoomSubscriptionManager

> 217 nodes

## Key Concepts

- **RoomSubscriptionManager** (50 connections) — `server/realtime/room_subscription_manager.py`
- **connection_initialization.py** (38 connections) — `server/realtime/connection_initialization.py`
- **connection_cleaner.py** (24 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **test_room_subscription_manager_helpers.py** (23 connections) — `server/tests/unit/realtime/test_room_subscription_manager_helpers.py`
- **RoomEventHandler** (21 connections) — `server/realtime/integration/room_event_handler.py`
- **HealthMonitor** (21 connections) — `server/realtime/monitoring/health_monitor.py`
- **room_subscription_manager.py** (20 connections) — `server/realtime/room_subscription_manager.py`
- **test_connection_initialization.py** (18 connections) — `server/tests/unit/realtime/test_connection_initialization.py`
- **test_room_event_handler.py** (14 connections) — `server/tests/unit/realtime/integration/test_room_event_handler.py`
- **test_room_subscription_manager_npcs.py** (14 connections) — `server/tests/unit/realtime/test_room_subscription_manager_npcs.py`
- **initialize_core_components()** (13 connections) — `server/realtime/connection_initialization.py`
- **._canonical_room_id()** (13 connections) — `server/realtime/room_subscription_manager.py`
- **room_event_handler.py** (13 connections) — `server/realtime/integration/room_event_handler.py`
- **Any** (13 connections)
- **.__init__()** (12 connections) — `server/realtime/connection_manager.py`
- **initialize_connection_state()** (9 connections) — `server/realtime/connection_initialization.py`
- **initialize_messaging()** (9 connections) — `server/realtime/connection_initialization.py`
- **UUID** (9 connections)
- **asyncio** (9 connections)
- **initialize_connection_cleaner()** (8 connections) — `server/realtime/connection_initialization.py`
- **initialize_error_handler()** (8 connections) — `server/realtime/connection_initialization.py`
- **initialize_game_state_provider()** (8 connections) — `server/realtime/connection_initialization.py`
- **initialize_health_monitor()** (8 connections) — `server/realtime/connection_initialization.py`
- **initialize_room_event_handler()** (8 connections) — `server/realtime/connection_initialization.py`
- **._process_single_connection()** (8 connections) — `server/realtime/monitoring/health_monitor.py`
- *... and 192 more nodes in this community*

## Relationships

- [connection_manager.py](connection_manager.py.md) (20 shared connections)
- [get_logger](get_logger.md) (13 shared connections)
- [StatisticsAggregator](StatisticsAggregator.md) (12 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (7 shared connections)
- [build_event](build_event.md) (6 shared connections)
- [ConnectionCleaner](ConnectionCleaner.md) (6 shared connections)
- [MessageQueue](MessageQueue.md) (5 shared connections)
- [test_health_monitor.py](test_health_monitor.py.md) (3 shared connections)
- [test_connection_establishment.py](test_connection_establishment.py.md) (3 shared connections)
- [test_connection_session_management.py](test_connection_session_management.py.md) (3 shared connections)
- [test_room_subscription_manager.py](test_room_subscription_manager.py.md) (3 shared connections)
- [test_room_subscription_manager_drops.py](test_room_subscription_manager_drops.py.md) (3 shared connections)

## Source Files

- `server/realtime/connection_initialization.py`
- `server/realtime/connection_manager.py`
- `server/realtime/integration/__init__.py`
- `server/realtime/integration/room_event_handler.py`
- `server/realtime/maintenance/connection_cleaner.py`
- `server/realtime/monitoring/health_monitor.py`
- `server/realtime/room_subscription_manager.py`
- `server/tests/unit/realtime/integration/test_room_event_handler.py`
- `server/tests/unit/realtime/test_connection_initialization.py`
- `server/tests/unit/realtime/test_room_subscription_manager_helpers.py`
- `server/tests/unit/realtime/test_room_subscription_manager_npcs.py`

## Audit Trail

- EXTRACTED: 419 (94%)
- INFERRED: 28 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*