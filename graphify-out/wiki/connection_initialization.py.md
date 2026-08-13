# connection_initialization.py

> 88 nodes

## Key Concepts

- **connection_initialization.py** (41 connections) — `server/realtime/connection_initialization.py`
- **GameStateProvider** (26 connections) — `server/realtime/integration/game_state_provider.py`
- **game_state_provider.py** (21 connections) — `server/realtime/integration/game_state_provider.py`
- **PerformanceTracker** (17 connections) — `server/realtime/monitoring/performance_tracker.py`
- **room_subscription_manager.py** (17 connections) — `server/realtime/room_subscription_manager.py`
- **test_connection_initialization.py** (16 connections) — `server/tests/unit/realtime/test_connection_initialization.py`
- **ConnectionErrorHandler** (12 connections) — `server/realtime/errors/error_handler.py`
- **room_event_handler.py** (12 connections) — `server/realtime/integration/room_event_handler.py`
- **initialize_connection_manager()** (11 connections) — `server/realtime/connection_initialization.py`
- **Any** (11 connections)
- **RoomEventHandler** (10 connections) — `server/realtime/integration/room_event_handler.py`
- **initialize_core_components()** (10 connections) — `server/realtime/connection_initialization.py`
- **initialize_specialized_components()** (10 connections) — `server/realtime/connection_initialization.py`
- **initialize_messaging()** (8 connections) — `server/realtime/connection_initialization.py`
- **initialize_connection_cleaner()** (7 connections) — `server/realtime/connection_initialization.py`
- **initialize_error_handler()** (7 connections) — `server/realtime/connection_initialization.py`
- **initialize_game_state_provider()** (7 connections) — `server/realtime/connection_initialization.py`
- **initialize_health_monitor()** (7 connections) — `server/realtime/connection_initialization.py`
- **initialize_room_event_handler()** (7 connections) — `server/realtime/connection_initialization.py`
- **._trim_samples()** (7 connections) — `server/realtime/monitoring/performance_tracker.py`
- **initialize_connection_maps()** (5 connections) — `server/realtime/connection_initialization.py`
- **initialize_session_and_health_config()** (5 connections) — `server/realtime/connection_initialization.py`
- **server/realtime/integration/__init__.py** (5 connections) — `server/realtime/integration/__init__.py`
- **.handle_player_entered_room()** (4 connections) — `server/realtime/integration/room_event_handler.py`
- **.handle_player_left_room()** (4 connections) — `server/realtime/integration/room_event_handler.py`
- *... and 63 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (23 shared connections)
- [UUID](UUID.md) (18 shared connections)
- [.detect_and_handle_error_state](detect_and_handle_error_state.md) (7 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (5 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (5 shared connections)
- [RoomSubscriptionManager](RoomSubscriptionManager.md) (5 shared connections)
- [build_event](build_event.md) (5 shared connections)
- [MessageBroadcaster](MessageBroadcaster.md) (4 shared connections)
- [test_game_state_provider.py](test_game_state_provider.py.md) (3 shared connections)
- [HealthMonitor](HealthMonitor.md) (3 shared connections)
- [StatisticsAggregator](StatisticsAggregator.md) (3 shared connections)
- [test_login_grace_period_visual_indicator.py](test_login_grace_period_visual_indicator.py.md) (2 shared connections)

## Source Files

- `server/realtime/connection_initialization.py`
- `server/realtime/errors/__init__.py`
- `server/realtime/errors/error_handler.py`
- `server/realtime/integration/__init__.py`
- `server/realtime/integration/game_state_provider.py`
- `server/realtime/integration/room_event_handler.py`
- `server/realtime/monitoring/performance_tracker.py`
- `server/realtime/room_subscription_manager.py`
- `server/tests/unit/realtime/test_connection_initialization.py`

## Audit Trail

- EXTRACTED: 243 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*