# Player Combat XP

> 306 nodes

## Key Concepts

- **websocket_handler.py** (64 connections) — `server/realtime/websocket_handler.py`
- **test_websocket_handler_core.py** (42 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_websocket_handler_validation_errors.py** (39 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **websocket_handler_commands.py** (32 connections) — `server/realtime/websocket_handler_commands.py`
- **handle_game_command()** (29 connections) — `server/realtime/websocket_handler_commands.py`
- **websocket_handler_message_loop.py** (25 connections) — `server/realtime/websocket_handler_message_loop.py`
- **test_websocket_handler_coverage_gaps.py** (24 connections) — `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- **test_websocket_handler_app_state_connection.py** (23 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **websocket_handler_validation.py** (21 connections) — `server/realtime/websocket_handler_validation.py`
- **resolve_and_setup_app_state_services()** (20 connections) — `server/realtime/websocket_handler_app_state.py`
- **process_websocket_command()** (19 connections) — `server/realtime/websocket_handler_commands.py`
- **handle_chat_message()** (18 connections) — `server/realtime/websocket_handler.py`
- **send_system_message()** (13 connections) — `server/realtime/websocket_handler.py`
- **websocket_handler_app_state.py** (11 connections) — `server/realtime/websocket_handler_app_state.py`
- **resolve_websocket_connection_manager()** (11 connections) — `server/realtime/websocket_handler_commands.py`
- **handle_websocket_message()** (10 connections) — `server/realtime/websocket_handler.py`
- **_websocket_unified_command_result()** (10 connections) — `server/realtime/websocket_handler_commands.py`
- **handle_message_loop_exception()** (10 connections) — `server/realtime/websocket_handler_message_loop.py`
- **is_client_disconnected_exception()** (10 connections) — `server/realtime/websocket_helpers.py`
- **create_websocket_request_context()** (9 connections) — `server/realtime/request_context.py`
- **test_websocket_handler_error_handling.py** (9 connections) — `server/tests/unit/realtime/test_websocket_handler_error_handling.py`
- **test_websocket_handler_system_message.py** (8 connections) — `server/tests/unit/realtime/test_websocket_handler_system_message.py`
- **send_websocket_error_response()** (7 connections) — `server/realtime/websocket_handler_message_loop.py`
- **WebSocket** (7 connections)
- **handle_json_decode_error()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- *... and 281 more nodes in this community*

## Relationships

- [Standardized Error Responses](Standardized_Error_Responses.md) (32 shared connections)
- [Pre-commit Hook Analysis](Pre-commit_Hook_Analysis.md) (20 shared connections)
- [Auth Token Utilities](Auth_Token_Utilities.md) (16 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (13 shared connections)
- [Pylint Unique Findings](Pylint_Unique_Findings.md) (8 shared connections)
- [Config Model Tests](Config_Model_Tests.md) (6 shared connections)
- [Playwright E2E Specs](Playwright_E2E_Specs.md) (6 shared connections)
- [Character Creation Service](Character_Creation_Service.md) (5 shared connections)
- [Archive Bug Fix](Archive_Bug_Fix.md) (4 shared connections)
- [Real-Time Architecture Docs](Real-Time_Architecture_Docs.md) (4 shared connections)
- [Party Service Management](Party_Service_Management.md) (4 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (4 shared connections)

## Source Files

- `server/realtime/request_context.py`
- `server/realtime/websocket_handler.py`
- `server/realtime/websocket_handler_app_state.py`
- `server/realtime/websocket_handler_commands.py`
- `server/realtime/websocket_handler_message_loop.py`
- `server/realtime/websocket_handler_validation.py`
- `server/realtime/websocket_helpers.py`
- `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- `server/tests/unit/realtime/test_websocket_handler_commands.py`
- `server/tests/unit/realtime/test_websocket_handler_core.py`
- `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- `server/tests/unit/realtime/test_websocket_handler_error_handling.py`
- `server/tests/unit/realtime/test_websocket_handler_system_message.py`
- `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`

## Audit Trail

- EXTRACTED: 960 (95%)
- INFERRED: 50 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*