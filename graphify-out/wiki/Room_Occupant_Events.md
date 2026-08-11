# Room Occupant Events

> 132 nodes

## Key Concepts

- **test_connection_delegates.py** (51 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **connection_manager_health_cleanup.py** (30 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **connection_delegates.py** (21 connections) — `server/realtime/connection_delegates.py`
- **Any** (15 connections)
- **Any** (13 connections)
- **delegate_error_handler()** (12 connections) — `server/realtime/connection_delegates.py`
- **cleanup_dead_websocket_impl()** (11 connections) — `server/realtime/connection_delegates.py`
- **delegate_connection_cleaner()** (11 connections) — `server/realtime/connection_delegates.py`
- **delegate_message_broadcaster()** (11 connections) — `server/realtime/connection_delegates.py`
- **delegate_health_monitor()** (9 connections) — `server/realtime/connection_delegates.py`
- **delegate_connection_cleaner_sync()** (9 connections) — `server/realtime/connection_delegates.py`
- **delegate_personal_message_sender()** (9 connections) — `server/realtime/connection_delegates.py`
- **delegate_room_event_handler()** (9 connections) — `server/realtime/connection_delegates.py`
- **delegate_health_monitor_sync()** (8 connections) — `server/realtime/connection_delegates.py`
- **delegate_game_state_provider_sync()** (8 connections) — `server/realtime/connection_delegates.py`
- **delegate_personal_message_sender_sync()** (8 connections) — `server/realtime/connection_delegates.py`
- **check_connection_health_impl()** (8 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **UUID** (8 connections)
- **CleanupContext** (8 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **detect_and_handle_error_state_impl()** (7 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **handle_websocket_error_impl()** (7 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **handle_authentication_error_impl()** (7 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **handle_security_violation_impl()** (7 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **recover_from_error_impl()** (7 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **cleanup_dead_connections_impl()** (7 connections) — `server/realtime/connection_manager_health_cleanup.py`
- *... and 107 more nodes in this community*

## Relationships

- [Playwright E2E Specs](Playwright_E2E_Specs.md) (45 shared connections)
- [Archive Bug Fix](Archive_Bug_Fix.md) (16 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (4 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (3 shared connections)
- [NATS Message Broker](NATS_Message_Broker.md) (3 shared connections)
- [Unified Command Handler](Unified_Command_Handler.md) (2 shared connections)
- [Auth Token Utilities](Auth_Token_Utilities.md) (1 shared connections)
- [Deprecated Logging Patterns](Deprecated_Logging_Patterns.md) (1 shared connections)

## Source Files

- `server/realtime/connection_delegates.py`
- `server/realtime/connection_manager_health_cleanup.py`
- `server/realtime/maintenance/connection_cleaner.py`
- `server/tests/unit/realtime/test_connection_delegates.py`

## Audit Trail

- EXTRACTED: 516 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*