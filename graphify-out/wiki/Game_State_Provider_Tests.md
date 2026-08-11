# Game State Provider Tests

> 80 nodes

## Key Concepts

- **connection_initialization.py** (41 connections) — `server/realtime/connection_initialization.py`
- **GameStateProvider** (26 connections) — `server/realtime/integration/game_state_provider.py`
- **game_state_provider.py** (21 connections) — `server/realtime/integration/game_state_provider.py`
- **test_connection_initialization.py** (16 connections) — `server/tests/unit/realtime/test_connection_initialization.py`
- **MemoryMonitor** (13 connections) — `server/realtime/memory_monitor.py`
- **ConnectionErrorHandler** (12 connections) — `server/realtime/errors/error_handler.py`
- **room_event_handler.py** (12 connections) — `server/realtime/integration/room_event_handler.py`
- **Any** (11 connections)
- **initialize_connection_manager()** (11 connections) — `server/realtime/connection_initialization.py`
- **initialize_core_components()** (10 connections) — `server/realtime/connection_initialization.py`
- **initialize_specialized_components()** (10 connections) — `server/realtime/connection_initialization.py`
- **RoomEventHandler** (10 connections) — `server/realtime/integration/room_event_handler.py`
- **initialize_messaging()** (8 connections) — `server/realtime/connection_initialization.py`
- **error_handler.py** (8 connections) — `server/realtime/errors/error_handler.py`
- **initialize_health_monitor()** (7 connections) — `server/realtime/connection_initialization.py`
- **initialize_error_handler()** (7 connections) — `server/realtime/connection_initialization.py`
- **initialize_connection_cleaner()** (7 connections) — `server/realtime/connection_initialization.py`
- **initialize_game_state_provider()** (7 connections) — `server/realtime/connection_initialization.py`
- **initialize_room_event_handler()** (7 connections) — `server/realtime/connection_initialization.py`
- **initialize_connection_maps()** (5 connections) — `server/realtime/connection_initialization.py`
- **initialize_session_and_health_config()** (5 connections) — `server/realtime/connection_initialization.py`
- **__init__.py** (5 connections) — `server/realtime/integration/__init__.py`
- **.__init__()** (4 connections) — `server/realtime/integration/room_event_handler.py`
- **.handle_player_entered_room()** (4 connections) — `server/realtime/integration/room_event_handler.py`
- **.handle_player_left_room()** (4 connections) — `server/realtime/integration/room_event_handler.py`
- *... and 55 more nodes in this community*

## Relationships

- [Playwright E2E Specs](Playwright_E2E_Specs.md) (18 shared connections)
- [Game State Provider](Game_State_Provider.md) (18 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (8 shared connections)
- [Commands Command Handler](Commands_Command_Handler.md) (8 shared connections)
- [Pylint Unique Findings](Pylint_Unique_Findings.md) (5 shared connections)
- [Validate Calendar](Validate_Calendar.md) (4 shared connections)
- [JSONB Column Parsing](JSONB_Column_Parsing.md) (4 shared connections)
- [Player Respawn Events](Player_Respawn_Events.md) (4 shared connections)
- [E2E Playwright Conversion Plan](E2E_Playwright_Conversion_Plan.md) (3 shared connections)
- [WebSocket Helper Utilities](WebSocket_Helper_Utilities.md) (3 shared connections)
- [Character Creation E2E](Character_Creation_E2E.md) (3 shared connections)
- [Deprecated Logging Patterns](Deprecated_Logging_Patterns.md) (2 shared connections)

## Source Files

- `server/realtime/connection_initialization.py`
- `server/realtime/errors/__init__.py`
- `server/realtime/errors/error_handler.py`
- `server/realtime/integration/__init__.py`
- `server/realtime/integration/game_state_provider.py`
- `server/realtime/integration/room_event_handler.py`
- `server/realtime/memory_monitor.py`
- `server/tests/unit/realtime/test_connection_initialization.py`

## Audit Trail

- EXTRACTED: 356 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*