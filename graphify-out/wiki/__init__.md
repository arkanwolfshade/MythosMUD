# .__init__

> 27 nodes · cohesion 0.11

## Key Concepts

- **.__init__()** (17 connections) — `server/realtime/connection_manager.py`
- **test_connection_initialization.py** (14 connections) — `server/tests/unit/realtime/test_connection_initialization.py`
- **initialize_messaging()** (9 connections) — `server/realtime/connection_initialization.py`
- **initialize_connection_cleaner()** (8 connections) — `server/realtime/connection_initialization.py`
- **initialize_error_handler()** (8 connections) — `server/realtime/connection_initialization.py`
- **initialize_game_state_provider()** (8 connections) — `server/realtime/connection_initialization.py`
- **initialize_health_monitor()** (8 connections) — `server/realtime/connection_initialization.py`
- **Any** (6 connections)
- **test_initialize_connection_cleaner()** (3 connections) — `server/tests/unit/realtime/test_connection_initialization.py`
- **test_initialize_error_handler()** (3 connections) — `server/tests/unit/realtime/test_connection_initialization.py`
- **test_initialize_game_state_provider()** (3 connections) — `server/tests/unit/realtime/test_connection_initialization.py`
- **test_initialize_health_monitor()** (3 connections) — `server/tests/unit/realtime/test_connection_initialization.py`
- **test_initialize_messaging()** (3 connections) — `server/tests/unit/realtime/test_connection_initialization.py`
- **test_initialize_room_event_handler()** (3 connections) — `server/tests/unit/realtime/test_connection_initialization.py`
- **Initialize the health monitor with required callbacks.** (1 connections) — `server/realtime/connection_initialization.py`
- **Initialize the error handler with required callbacks.** (1 connections) — `server/realtime/connection_initialization.py`
- **Initialize the connection cleaner with required callbacks.** (1 connections) — `server/realtime/connection_initialization.py`
- **Initialize the game state provider with required callbacks.** (1 connections) — `server/realtime/connection_initialization.py`
- **Initialize messaging components with required callbacks.** (1 connections) — `server/realtime/connection_initialization.py`
- **Initialize the connection manager with modular components.** (1 connections) — `server/realtime/connection_manager.py`
- **Unit tests for connection initialization.  Tests the connection_initialization m** (1 connections) — `server/tests/unit/realtime/test_connection_initialization.py`
- **Test initialize_room_event_handler() initializes room event handler.** (1 connections) — `server/tests/unit/realtime/test_connection_initialization.py`
- **Test initialize_health_monitor() initializes health monitor.** (1 connections) — `server/tests/unit/realtime/test_connection_initialization.py`
- **Test initialize_error_handler() initializes error handler.** (1 connections) — `server/tests/unit/realtime/test_connection_initialization.py`
- **Test initialize_connection_cleaner() initializes connection cleaner.** (1 connections) — `server/tests/unit/realtime/test_connection_initialization.py`
- *... and 2 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (11 shared connections)
- [connection_manager.py](connection_manager.py.md) (5 shared connections)
- [ConnectionCleaner](ConnectionCleaner.md) (1 shared connections)
- [ConnectionErrorHandler](ConnectionErrorHandler.md) (1 shared connections)
- [.state](state.md) (1 shared connections)
- [HealthMonitor](HealthMonitor.md) (1 shared connections)
- [MessageBroadcaster](MessageBroadcaster.md) (1 shared connections)
- [PersonalMessageSender](PersonalMessageSender.md) (1 shared connections)
- [deque](deque.md) (1 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)
- [InventoryMutationGuard](InventoryMutationGuard.md) (1 shared connections)
- [UUID](UUID.md) (1 shared connections)

## Source Files

- `server/realtime/connection_initialization.py`
- `server/realtime/connection_manager.py`
- `server/tests/unit/realtime/test_connection_initialization.py`

## Audit Trail

- EXTRACTED: 107 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*