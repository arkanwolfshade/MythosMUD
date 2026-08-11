# Game Tick Processing

> 40 nodes

## Key Concepts

- **websocket_handler_commands.py** (32 connections) — `server/realtime/websocket_handler_commands.py`
- **test_websocket_handler_app_state_connection.py** (23 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **resolve_and_setup_app_state_services()** (20 connections) — `server/realtime/websocket_handler_app_state.py`
- **websocket_handler_app_state.py** (11 connections) — `server/realtime/websocket_handler_app_state.py`
- **_websocket_unified_command_result()** (10 connections) — `server/realtime/websocket_handler_commands.py`
- **_services_from_container()** (4 connections) — `server/realtime/websocket_handler_app_state.py`
- **_mirror_service_to_app_state()** (3 connections) — `server/realtime/websocket_handler_app_state.py`
- **test_resolve_and_setup_app_state_services_services_already_set()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **test_resolve_and_setup_app_state_services_missing_services()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **test_resolve_and_setup_app_state_services_no_app_state()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **test_resolve_and_setup_app_state_services_container_no_services()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **test_resolve_and_setup_app_state_services_no_container_attribute()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **test_resolve_and_setup_app_state_services_only_player_service()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **test_resolve_and_setup_app_state_services_only_user_manager()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **test_resolve_and_setup_app_state_services_player_service_already_set()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **test_resolve_and_setup_app_state_services_user_manager_already_set()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **test_resolve_and_setup_app_state_services_player_service_no_hasattr()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **test_resolve_and_setup_app_state_services_user_manager_no_hasattr()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **test_cleanup_connection_mute_cleanup_error()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **test_handle_websocket_message_loop()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **WebSocket app.state / container service wiring for command processing.  Extrac** (1 connections) — `server/realtime/websocket_handler_app_state.py`
- **Read player_service and user_manager from app_state.container.** (1 connections) — `server/realtime/websocket_handler_app_state.py`
- **Copy container service onto app.state if missing.** (1 connections) — `server/realtime/websocket_handler_app_state.py`
- **Resolve player_service and user_manager from container or app.state.      Muta** (1 connections) — `server/realtime/websocket_handler_app_state.py`
- **WebSocket game command processing (parse, unified handler, broadcast).  Extrac** (1 connections) — `server/realtime/websocket_handler_commands.py`
- *... and 15 more nodes in this community*

## Relationships

- [Player Combat XP](Player_Combat_XP.md) (13 shared connections)
- [Container API Endpoints](Container_API_Endpoints.md) (8 shared connections)
- [Client Memory Leak Detector](Client_Memory_Leak_Detector.md) (6 shared connections)
- [Admin Teleport Commands](Admin_Teleport_Commands.md) (5 shared connections)
- [Client Event Store](Client_Event_Store.md) (4 shared connections)
- [WebSocket Auth Integration](WebSocket_Auth_Integration.md) (3 shared connections)
- [Player Schema Converter](Player_Schema_Converter.md) (2 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (2 shared connections)
- [Pylint Unique Findings](Pylint_Unique_Findings.md) (2 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (1 shared connections)
- [Archive Bug Fix](Archive_Bug_Fix.md) (1 shared connections)
- [Async Persistence Layer](Async_Persistence_Layer.md) (1 shared connections)

## Source Files

- `server/realtime/websocket_handler_app_state.py`
- `server/realtime/websocket_handler_commands.py`
- `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`

## Audit Trail

- EXTRACTED: 157 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*