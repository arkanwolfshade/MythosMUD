# Room Occupant Events

> 309 nodes

## Key Concepts

- **connection_manager.py** (164 connections) — `server/realtime/connection_manager.py`
- **connection_manager_methods.py** (89 connections) — `server/realtime/connection_manager_methods.py`
- **Any** (60 connections)
- **test_connection_delegates.py** (51 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **UUID** (27 connections)
- **test_connection_statistics.py** (24 connections) — `server/tests/unit/realtime/test_connection_statistics.py`
- **connection_delegates.py** (20 connections) — `server/realtime/connection_delegates.py`
- **canonical_room_id_impl()** (17 connections) — `server/realtime/connection_room_utils.py`
- **test_connection_room_utils.py** (16 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **Any** (13 connections)
- **validate_token_impl()** (13 connections) — `server/realtime/connection_delegates.py`
- **delegate_error_handler()** (12 connections) — `server/realtime/connection_delegates.py`
- **delegate_game_state_provider()** (12 connections) — `server/realtime/connection_delegates.py`
- **cleanup_dead_websocket_impl()** (11 connections) — `server/realtime/connection_delegates.py`
- **delegate_connection_cleaner()** (11 connections) — `server/realtime/connection_delegates.py`
- **delegate_message_broadcaster()** (11 connections) — `server/realtime/connection_delegates.py`
- **connection_statistics.py** (11 connections) — `server/realtime/connection_statistics.py`
- **validate_player_presence_impl()** (11 connections) — `server/realtime/connection_statistics.py`
- **get_online_player_by_display_name_impl()** (10 connections) — `server/realtime/connection_statistics.py`
- **delegate_health_monitor()** (9 connections) — `server/realtime/connection_delegates.py`
- **delegate_connection_cleaner_sync()** (9 connections) — `server/realtime/connection_delegates.py`
- **delegate_personal_message_sender()** (9 connections) — `server/realtime/connection_delegates.py`
- **delegate_room_event_handler()** (9 connections) — `server/realtime/connection_delegates.py`
- **get_player_presence_info_impl()** (9 connections) — `server/realtime/connection_statistics.py`
- **get_session_stats_impl()** (9 connections) — `server/realtime/connection_statistics.py`
- *... and 284 more nodes in this community*

## Relationships

- [Distributed Event Bus](Distributed_Event_Bus.md) (77 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (25 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (19 shared connections)
- [Message Broadcaster Core](Message_Broadcaster_Core.md) (18 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (13 shared connections)
- [NATS Message Broker](NATS_Message_Broker.md) (7 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (5 shared connections)
- [Combat Turn Processor](Combat_Turn_Processor.md) (4 shared connections)
- [Unified Command Handler](Unified_Command_Handler.md) (4 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (3 shared connections)
- [Command Field Validators](Command_Field_Validators.md) (3 shared connections)
- [Auth Token Utilities](Auth_Token_Utilities.md) (2 shared connections)

## Source Files

- `server/realtime/connection_delegates.py`
- `server/realtime/connection_manager.py`
- `server/realtime/connection_manager_methods.py`
- `server/realtime/connection_room_utils.py`
- `server/realtime/connection_statistics.py`
- `server/realtime/maintenance/connection_cleaner.py`
- `server/tests/unit/realtime/test_connection_delegates.py`
- `server/tests/unit/realtime/test_connection_room_utils.py`
- `server/tests/unit/realtime/test_connection_statistics.py`

## Audit Trail

- EXTRACTED: 1403 (100%)
- INFERRED: 7 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*