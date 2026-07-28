# Whisper Reply Command Tests

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

- [Distributed Event Bus](Distributed_Event_Bus.md) (11 shared connections)
- [Room Occupant Events](Room_Occupant_Events.md) (5 shared connections)
- [Realtime Maintenance Connection](Realtime_Maintenance_Connection.md) (1 shared connections)
- [Command Parser Helpers](Command_Parser_Helpers.md) (1 shared connections)
- [Look Command Helpers](Look_Command_Helpers.md) (1 shared connections)
- [System Audit Status](System_Audit_Status.md) (1 shared connections)
- [Npc Communication](Npc_Communication.md) (1 shared connections)
- [Whisper Work Remaining](Whisper_Work_Remaining.md) (1 shared connections)
- [Mythos Map Builder](Mythos_Map_Builder.md) (1 shared connections)
- [Connection Disconnection Cleanup](Connection_Disconnection_Cleanup.md) (1 shared connections)
- [Services Inventory Mutation](Services_Inventory_Mutation.md) (1 shared connections)
- [Restart Invalidating JWT](Restart_Invalidating_JWT.md) (1 shared connections)

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