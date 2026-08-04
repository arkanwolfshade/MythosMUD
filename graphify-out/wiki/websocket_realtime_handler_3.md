# websocket realtime handler

> 56 nodes

## Key Concepts

- **test_websocket_handler_helpers_extended.py** (33 connections) — `server/tests/unit/realtime/test_websocket_handler_helpers_extended.py`
- **test_validate_message_failure()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_helpers_extended.py`
- **test_handle_generic_exception_success()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_helpers_extended.py`
- **test_handle_generic_exception_disconnected()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_helpers_extended.py`
- **test_process_message_validation_failed()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_helpers_extended.py`
- **mock_websocket()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_helpers_extended.py`
- **mock_connection_manager()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_helpers_extended.py`
- **mock_validator()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_helpers_extended.py`
- **test_check_rate_limit_no_connection_id()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_helpers_extended.py`
- **test_check_rate_limit_passed()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_helpers_extended.py`
- **test_check_rate_limit_exceeded()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_helpers_extended.py`
- **test_validate_message_success()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_helpers_extended.py`
- **test_send_error_response_success()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_helpers_extended.py`
- **test_send_error_response_websocket_disconnect()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_helpers_extended.py`
- **test_send_error_response_runtime_error_disconnected()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_helpers_extended.py`
- **test_send_error_response_runtime_error_close_message()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_helpers_extended.py`
- **test_send_error_response_other_error()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_helpers_extended.py`
- **test_handle_json_decode_error()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_helpers_extended.py`
- **test_handle_websocket_disconnect()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_helpers_extended.py`
- **test_handle_websocket_disconnect_no_connection_id()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_helpers_extended.py`
- **test_handle_runtime_error_disconnected()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_helpers_extended.py`
- **test_handle_runtime_error_other()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_helpers_extended.py`
- **test_process_message_rate_limit_exceeded()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_helpers_extended.py`
- **test_process_message_success()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_helpers_extended.py`
- **test_handle_message_loop_exception_json_decode_error()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_helpers_extended.py`
- *... and 31 more nodes in this community*

## Relationships

- [Error Handling Core](Error_Handling_Core.md) (3 shared connections)
- [realtime message validator](realtime_message_validator.md) (3 shared connections)
- [handler realtime nats](handler_realtime_nats.md) (2 shared connections)
- [combat schemas schema](combat_schemas_schema.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_websocket_handler_helpers_extended.py`

## Audit Trail

- EXTRACTED: 117 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*