# Game State Provider Tests

> 41 nodes

## Key Concepts

- **connection_initialization.py** (41 connections) — `server/realtime/connection_initialization.py`
- **test_connection_initialization.py** (16 connections) — `server/tests/unit/realtime/test_connection_initialization.py`
- **Any** (11 connections)
- **initialize_connection_manager()** (11 connections) — `server/realtime/connection_initialization.py`
- **initialize_core_components()** (10 connections) — `server/realtime/connection_initialization.py`
- **initialize_specialized_components()** (10 connections) — `server/realtime/connection_initialization.py`
- **initialize_messaging()** (8 connections) — `server/realtime/connection_initialization.py`
- **initialize_health_monitor()** (7 connections) — `server/realtime/connection_initialization.py`
- **initialize_error_handler()** (7 connections) — `server/realtime/connection_initialization.py`
- **initialize_connection_cleaner()** (7 connections) — `server/realtime/connection_initialization.py`
- **initialize_game_state_provider()** (7 connections) — `server/realtime/connection_initialization.py`
- **initialize_room_event_handler()** (7 connections) — `server/realtime/connection_initialization.py`
- **initialize_connection_maps()** (5 connections) — `server/realtime/connection_initialization.py`
- **initialize_session_and_health_config()** (5 connections) — `server/realtime/connection_initialization.py`
- **test_initialize_connection_manager_wires_core_state()** (3 connections) — `server/tests/unit/realtime/test_connection_initialization.py`
- **test_initialize_health_monitor()** (3 connections) — `server/tests/unit/realtime/test_connection_initialization.py`
- **test_initialize_error_handler()** (3 connections) — `server/tests/unit/realtime/test_connection_initialization.py`
- **test_initialize_connection_cleaner()** (3 connections) — `server/tests/unit/realtime/test_connection_initialization.py`
- **test_initialize_game_state_provider()** (3 connections) — `server/tests/unit/realtime/test_connection_initialization.py`
- **test_initialize_messaging()** (3 connections) — `server/tests/unit/realtime/test_connection_initialization.py`
- **test_initialize_room_event_handler()** (3 connections) — `server/tests/unit/realtime/test_connection_initialization.py`
- **Initialization helpers for connection manager.  This module provides helper func** (1 connections) — `server/realtime/connection_initialization.py`
- **Initialize connection maps, presence tracking, and service references.** (1 connections) — `server/realtime/connection_initialization.py`
- **Initialize cleanup stats, modular services, and specialized placeholders.** (1 connections) — `server/realtime/connection_initialization.py`
- **Initialize session maps, closed-socket tracking, and health-check config.** (1 connections) — `server/realtime/connection_initialization.py`
- *... and 16 more nodes in this community*

## Relationships

- [Client Event Store](Client_Event_Store.md) (11 shared connections)
- [Commands Look Item](Commands_Look_Item.md) (3 shared connections)
- [E2E Playwright Conversion Plan](E2E_Playwright_Conversion_Plan.md) (3 shared connections)
- [Commands Command Handler](Commands_Command_Handler.md) (2 shared connections)
- [Game State Provider](Game_State_Provider.md) (2 shared connections)
- [Deprecated Logging Patterns](Deprecated_Logging_Patterns.md) (2 shared connections)
- [Game Magic Spell](Game_Magic_Spell.md) (2 shared connections)
- [Investigations Sessions Session](Investigations_Sessions_Session.md) (2 shared connections)
- [Realtime Health Monitor](Realtime_Health_Monitor.md) (2 shared connections)
- [Typography Layout Spec](Typography_Layout_Spec.md) (2 shared connections)
- [Validate Calendar](Validate_Calendar.md) (2 shared connections)
- [Connection Statistics Aggregator](Connection_Statistics_Aggregator.md) (2 shared connections)

## Source Files

- `server/realtime/connection_initialization.py`
- `server/tests/unit/realtime/test_connection_initialization.py`

## Audit Trail

- EXTRACTED: 191 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*