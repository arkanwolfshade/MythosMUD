# test_connection_initialization.py

> 39 nodes

## Key Concepts

- **test_connection_initialization.py** (16 connections) — `server/tests/unit/realtime/test_connection_initialization.py`
- **initialize_connection_manager()** (11 connections) — `server/realtime/connection_initialization.py`
- **Any** (11 connections)
- **initialize_specialized_components()** (10 connections) — `server/realtime/connection_initialization.py`
- **initialize_messaging()** (8 connections) — `server/realtime/connection_initialization.py`
- **initialize_connection_cleaner()** (7 connections) — `server/realtime/connection_initialization.py`
- **initialize_error_handler()** (7 connections) — `server/realtime/connection_initialization.py`
- **initialize_game_state_provider()** (7 connections) — `server/realtime/connection_initialization.py`
- **initialize_health_monitor()** (7 connections) — `server/realtime/connection_initialization.py`
- **initialize_room_event_handler()** (7 connections) — `server/realtime/connection_initialization.py`
- **initialize_connection_maps()** (5 connections) — `server/realtime/connection_initialization.py`
- **initialize_session_and_health_config()** (5 connections) — `server/realtime/connection_initialization.py`
- **.__init__()** (4 connections) — `server/realtime/connection_manager.py`
- **test_initialize_connection_cleaner()** (3 connections) — `server/tests/unit/realtime/test_connection_initialization.py`
- **test_initialize_connection_manager_wires_core_state()** (3 connections) — `server/tests/unit/realtime/test_connection_initialization.py`
- **test_initialize_error_handler()** (3 connections) — `server/tests/unit/realtime/test_connection_initialization.py`
- **test_initialize_game_state_provider()** (3 connections) — `server/tests/unit/realtime/test_connection_initialization.py`
- **test_initialize_health_monitor()** (3 connections) — `server/tests/unit/realtime/test_connection_initialization.py`
- **test_initialize_messaging()** (3 connections) — `server/tests/unit/realtime/test_connection_initialization.py`
- **test_initialize_room_event_handler()** (3 connections) — `server/tests/unit/realtime/test_connection_initialization.py`
- **Wire specialized components that need manager callbacks.** (1 connections) — `server/realtime/connection_initialization.py`
- **Fully initialize a ConnectionManager instance.** (1 connections) — `server/realtime/connection_initialization.py`
- **Initialize the health monitor with required callbacks.** (1 connections) — `server/realtime/connection_initialization.py`
- **Initialize the error handler with required callbacks.** (1 connections) — `server/realtime/connection_initialization.py`
- **Initialize the connection cleaner with required callbacks.** (1 connections) — `server/realtime/connection_initialization.py`
- *... and 14 more nodes in this community*

## Relationships

- [time.py](time.py.md) (15 shared connections)
- [ConnectionCleaner](ConnectionCleaner.md) (1 shared connections)
- [connection_manager.py](connection_manager.py.md) (1 shared connections)
- [MetricsCollector](MetricsCollector.md) (1 shared connections)
- [ConnectionErrorHandler](ConnectionErrorHandler.md) (1 shared connections)
- [GameStateProvider](GameStateProvider.md) (1 shared connections)
- [MessageBroadcaster](MessageBroadcaster.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [deque](deque.md) (1 shared connections)
- [UUID](UUID.md) (1 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)

## Source Files

- `server/realtime/connection_initialization.py`
- `server/realtime/connection_manager.py`
- `server/tests/unit/realtime/test_connection_initialization.py`

## Audit Trail

- EXTRACTED: 83 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*