# Test Websocket Handler Validation Errors

> 86 nodes

## Key Concepts

- **RuntimeError** (46 connections)
- **test_websocket_handler_validation_errors.py** (42 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **asyncio** (25 connections)
- **handle_chat_message()** (14 connections) — `server/realtime/websocket_handler.py`
- **send_system_message()** (12 connections) — `server/realtime/websocket_handler.py`
- **test_websocket_handler_system_message.py** (9 connections) — `server/tests/unit/realtime/test_websocket_handler_system_message.py`
- **test_handle_websocket_message_error()** (7 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_send_system_message_disconnected()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_system_message.py`
- **test_send_system_message_error()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_system_message.py`
- **test_send_system_message_success()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_system_message.py`
- **test_send_system_message_warning()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_system_message.py`
- **test_cleanup_connection_runtime_error()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_handle_chat_message_error()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_handle_chat_message_no_player()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_send_error_response_runtime_error_close_message()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_send_error_response_runtime_error_disconnected()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_send_error_response_runtime_error_other()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_send_system_message_error()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_validate_message_restores_csrf_from_message_jwt_when_metadata_token_missing()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_validate_message_validation_error()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **WebSocket** (4 connections)
- **asyncio** (4 connections)
- **.__init__()** (3 connections) — `server/database.py`
- **test_handle_runtime_error()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **mock_websocket()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_system_message.py`
- *... and 61 more nodes in this community*

## Relationships

- [WebSocket Message Handlers](WebSocket_Message_Handlers.md) (15 shared connections)
- [Test Websocket Helpers](Test_Websocket_Helpers.md) (8 shared connections)
- [Test Websocket Handler Helpers Extended](Test_Websocket_Handler_Helpers_Extended.md) (7 shared connections)
- [Test Websocket Handler Coverage Gaps](Test_Websocket_Handler_Coverage_Gaps.md) (4 shared connections)
- [Test Message Validator](Test_Message_Validator.md) (4 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (4 shared connections)
- [Test Combat Service Modules](Test_Combat_Service_Modules.md) (4 shared connections)
- [Test Database Error Handling](Test_Database_Error_Handling.md) (3 shared connections)
- [Test Websocket Initial State](Test_Websocket_Initial_State.md) (3 shared connections)
- [NPC Definitions API](NPC_Definitions_API.md) (3 shared connections)
- [Test Lifespan Helpers](Test_Lifespan_Helpers.md) (2 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (2 shared connections)

## Source Files

- `server/database.py`
- `server/realtime/websocket_handler.py`
- `server/tests/unit/realtime/test_websocket_handler_core.py`
- `server/tests/unit/realtime/test_websocket_handler_system_message.py`
- `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`

## Audit Trail

- EXTRACTED: 147 (75%)
- INFERRED: 49 (25%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*