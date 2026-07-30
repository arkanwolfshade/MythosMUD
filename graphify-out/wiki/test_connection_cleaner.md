# test connection cleaner

> 37 nodes

## Key Concepts

- **test_connection_initialization.py** (18 connections) — `server/tests/unit/realtime/test_connection_initialization.py`
- **initialize_core_components()** (13 connections) — `server/realtime/connection_initialization.py`
- **.__init__()** (12 connections) — `server/realtime/connection_manager.py`
- **initialize_connection_state()** (9 connections) — `server/realtime/connection_initialization.py`
- **initialize_messaging()** (9 connections) — `server/realtime/connection_initialization.py`
- **Any** (8 connections)
- **initialize_health_monitor()** (8 connections) — `server/realtime/connection_initialization.py`
- **initialize_error_handler()** (8 connections) — `server/realtime/connection_initialization.py`
- **initialize_connection_cleaner()** (8 connections) — `server/realtime/connection_initialization.py`
- **initialize_game_state_provider()** (8 connections) — `server/realtime/connection_initialization.py`
- **initialize_room_event_handler()** (8 connections) — `server/realtime/connection_initialization.py`
- **test_initialize_connection_state()** (3 connections) — `server/tests/unit/realtime/test_connection_initialization.py`
- **test_initialize_core_components()** (3 connections) — `server/tests/unit/realtime/test_connection_initialization.py`
- **test_initialize_health_monitor()** (3 connections) — `server/tests/unit/realtime/test_connection_initialization.py`
- **test_initialize_error_handler()** (3 connections) — `server/tests/unit/realtime/test_connection_initialization.py`
- **test_initialize_connection_cleaner()** (3 connections) — `server/tests/unit/realtime/test_connection_initialization.py`
- **test_initialize_game_state_provider()** (3 connections) — `server/tests/unit/realtime/test_connection_initialization.py`
- **test_initialize_messaging()** (3 connections) — `server/tests/unit/realtime/test_connection_initialization.py`
- **test_initialize_room_event_handler()** (3 connections) — `server/tests/unit/realtime/test_connection_initialization.py`
- **Initialize websocket, presence, session, and health-check state attributes.** (1 connections) — `server/realtime/connection_initialization.py`
- **Initialize modular components and nullable specialized-component stubs.** (1 connections) — `server/realtime/connection_initialization.py`
- **Initialize the health monitor with required callbacks.** (1 connections) — `server/realtime/connection_initialization.py`
- **Initialize the error handler with required callbacks.** (1 connections) — `server/realtime/connection_initialization.py`
- **Initialize the connection cleaner with required callbacks.** (1 connections) — `server/realtime/connection_initialization.py`
- **Initialize the game state provider with required callbacks.** (1 connections) — `server/realtime/connection_initialization.py`
- *... and 12 more nodes in this community*

## Relationships

- [test statistics aggregator](test_statistics_aggregator.md) (11 shared connections)
- [Player](Player.md) (9 shared connections)
- [Coord](Coord.md) (2 shared connections)
- [world](world.md) (2 shared connections)
- [Any](Any.md) (2 shared connections)
- [get current tick()](get_current_tick%28%29.md) (1 shared connections)
- [nats config()](nats_config%28%29.md) (1 shared connections)
- [Custom user manager for MythosMUD.](Custom_user_manager_for_MythosMUD.md) (1 shared connections)
- [GameTerminalContext](GameTerminalContext.md) (1 shared connections)
- [NPCDefinitionCRUDMixin](NPCDefinitionCRUDMixin.md) (1 shared connections)
- [.state()](state%28%29.md) (1 shared connections)
- [SendPersonalMessage](SendPersonalMessage.md) (1 shared connections)

## Source Files

- `server/realtime/connection_initialization.py`
- `server/realtime/connection_manager.py`
- `server/tests/unit/realtime/test_connection_initialization.py`

## Audit Trail

- EXTRACTED: 148 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*