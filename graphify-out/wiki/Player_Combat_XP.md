# Player Combat XP

> 190 nodes

## Key Concepts

- **test_websocket_handler_core.py** (42 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_websocket_handler_validation_errors.py** (39 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_websocket_handler_coverage_gaps.py** (24 connections) — `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- **test_websocket_handler_app_state_connection.py** (23 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **handle_websocket_connection()** (21 connections) — `server/realtime/websocket_handler.py`
- **resolve_and_setup_app_state_services()** (20 connections) — `server/realtime/websocket_handler_app_state.py`
- **handle_chat_message()** (18 connections) — `server/realtime/websocket_handler.py`
- **send_system_message()** (13 connections) — `server/realtime/websocket_handler.py`
- **websocket_handler_app_state.py** (11 connections) — `server/realtime/websocket_handler_app_state.py`
- **handle_websocket_message()** (10 connections) — `server/realtime/websocket_handler.py`
- **test_websocket_handler_system_message.py** (8 connections) — `server/tests/unit/realtime/test_websocket_handler_system_message.py`
- **WebSocket** (4 connections)
- **_services_from_container()** (4 connections) — `server/realtime/websocket_handler_app_state.py`
- **UUID** (3 connections)
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
- *... and 165 more nodes in this community*

## Relationships

- [Logout and Quit Commands](Logout_and_Quit_Commands.md) (25 shared connections)
- [Combat Command Helpers](Combat_Command_Helpers.md) (12 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (6 shared connections)
- [Client Event Store](Client_Event_Store.md) (4 shared connections)
- [Database Helper Tests](Database_Helper_Tests.md) (4 shared connections)
- [Client Memory Leak Detector](Client_Memory_Leak_Detector.md) (3 shared connections)
- [Combat Aggro Threat](Combat_Aggro_Threat.md) (2 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (2 shared connections)
- [Database Error Handling](Database_Error_Handling.md) (2 shared connections)
- [WebSocket Auth Integration](WebSocket_Auth_Integration.md) (2 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (2 shared connections)
- [Cursor Skills Harden](Cursor_Skills_Harden.md) (2 shared connections)

## Source Files

- `server/realtime/websocket_handler.py`
- `server/realtime/websocket_handler_app_state.py`
- `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- `server/tests/unit/realtime/test_websocket_handler_core.py`
- `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- `server/tests/unit/realtime/test_websocket_handler_system_message.py`
- `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`

## Audit Trail

- EXTRACTED: 536 (100%)
- INFERRED: 2 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*