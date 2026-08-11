# Room Occupant Events

> 154 nodes

## Key Concepts

- **test_connection_delegates.py** (51 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **connection_manager_health_cleanup.py** (30 connections) — `server/realtime/connection_manager_health_cleanup.py`
- **connection_delegates.py** (21 connections) — `server/realtime/connection_delegates.py`
- **Any** (15 connections)
- **Any** (13 connections)
- **validate_token_impl()** (13 connections) — `server/realtime/connection_delegates.py`
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
- *... and 129 more nodes in this community*

## Relationships

- [Distributed Event Bus](Distributed_Event_Bus.md) (36 shared connections)
- [Archive Bug Fix](Archive_Bug_Fix.md) (17 shared connections)
- [Schemas Maps Map](Schemas_Maps_Map.md) (5 shared connections)
- [Unified Command Handler](Unified_Command_Handler.md) (5 shared connections)
- [Client Event Store](Client_Event_Store.md) (4 shared connections)
- [NATS Message Broker](NATS_Message_Broker.md) (3 shared connections)
- [Auth Token Utilities](Auth_Token_Utilities.md) (2 shared connections)

## Source Files

- `server/realtime/connection_delegates.py`
- `server/realtime/connection_manager.py`
- `server/realtime/connection_manager_health_cleanup.py`
- `server/realtime/maintenance/connection_cleaner.py`
- `server/tests/unit/realtime/maintenance/test_connection_cleaner.py`
- `server/tests/unit/realtime/test_connection_delegates.py`

## Audit Trail

- EXTRACTED: 570 (100%)
- INFERRED: 2 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*