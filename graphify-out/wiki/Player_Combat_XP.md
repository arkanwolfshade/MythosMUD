# Player Combat XP

> 106 nodes

## Key Concepts

- **websocket_handler.py** (64 connections) — `server/realtime/websocket_handler.py`
- **test_websocket_handler_core.py** (42 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_websocket_handler_coverage_gaps.py** (24 connections) — `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- **handle_websocket_connection()** (21 connections) — `server/realtime/websocket_handler.py`
- **handle_chat_message()** (18 connections) — `server/realtime/websocket_handler.py`
- **send_system_message()** (13 connections) — `server/realtime/websocket_handler.py`
- **handle_websocket_message()** (10 connections) — `server/realtime/websocket_handler.py`
- **test_websocket_handler_system_message.py** (8 connections) — `server/tests/unit/realtime/test_websocket_handler_system_message.py`
- **load_player_mute_data()** (7 connections) — `server/realtime/websocket_helpers.py`
- **WebSocket** (4 connections)
- **UUID** (3 connections)
- **test_handle_generic_exception()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_generic_exception_should_break()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_get_help_content()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_get_help_content_with_command()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_send_system_message()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_chat_message()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_websocket_message()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_websocket_message_chat()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_websocket_message_command()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_websocket_connection_full_flow()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- **test_handle_chat_message_resolve_connection_manager_from_app()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- **test_handle_chat_message_exception_handling()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- **test_handle_chat_message_runtime_error_handling()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- **test_handle_websocket_connection_no_connection_manager()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- *... and 81 more nodes in this community*

## Relationships

- [Pre-commit Hook Analysis](Pre-commit_Hook_Analysis.md) (21 shared connections)
- [Look Item Commands](Look_Item_Commands.md) (11 shared connections)
- [Container API Endpoints](Container_API_Endpoints.md) (10 shared connections)
- [WebSocket Auth Integration](WebSocket_Auth_Integration.md) (8 shared connections)
- [Scenario Conversion Guide](Scenario_Conversion_Guide.md) (8 shared connections)
- [Party Service Management](Party_Service_Management.md) (6 shared connections)
- [Archive Bug Fix](Archive_Bug_Fix.md) (5 shared connections)
- [Memory Threshold Monitor](Memory_Threshold_Monitor.md) (4 shared connections)
- [Pylint Unique Findings](Pylint_Unique_Findings.md) (4 shared connections)
- [Client Event Store](Client_Event_Store.md) (4 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (4 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (3 shared connections)

## Source Files

- `server/realtime/websocket_handler.py`
- `server/realtime/websocket_helpers.py`
- `server/tests/unit/realtime/test_websocket_handler_core.py`
- `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- `server/tests/unit/realtime/test_websocket_handler_system_message.py`

## Audit Trail

- EXTRACTED: 371 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*