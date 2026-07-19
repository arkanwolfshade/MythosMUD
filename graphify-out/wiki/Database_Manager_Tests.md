# Database Manager Tests

> 91 nodes · cohesion 0.02

## Key Concepts

- **RuntimeError** (208 connections) — `server/realtime/websocket_handler_message_loop.py`
- **test_websocket_handler_helpers_extended.py** (32 connections) — `server/tests/unit/realtime/test_websocket_handler_helpers_extended.py`
- **_not_configured_async()** (4 connections) — `server/realtime/nats_message_handler.py`
- **test_handle_generic_exception_disconnected()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_helpers_extended.py`
- **test_close_handles_no_running_loop()** (3 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_initialize_database_config_runtime_error()** (3 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_database_manager_close_dispose_error()** (3 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_get_engine_no_running_loop()** (3 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_engine_handles_no_running_loop()** (3 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_initialize_database_config_runtime_error()** (3 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_connection_manager_property_resolution_error()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_handle_runtime_error()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_message_loop_should_raise_exception()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- **test_send_welcome_event_cannot_call_error()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- **test_send_welcome_event_close_message_sent()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- **Test _send_error_response() handles WebSocket disconnection.** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_error_handling.py`
- **test_handle_runtime_error_disconnected()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_error_handling.py`
- **test_handle_runtime_error_other()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_error_handling.py`
- **test_send_error_response_disconnected()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_error_handling.py`
- **test_handle_generic_exception_success()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_helpers_extended.py`
- **test_handle_message_loop_exception_runtime_error()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_helpers_extended.py`
- **test_handle_runtime_error_disconnected()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_helpers_extended.py`
- **test_handle_runtime_error_other()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_helpers_extended.py`
- **test_process_message_validation_failed()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_helpers_extended.py`
- **test_send_error_response_other_error()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_helpers_extended.py`
- *... and 66 more nodes in this community*

## Relationships

- [[Dependency Injection Tests]] (18 shared connections)
- [[NPC Admin API]] (14 shared connections)
- [[NATS Chat Broadcasting]] (9 shared connections)
- [[WebSocket Handler Helpers]] (8 shared connections)
- [[Dependencies Infrastructure]] (8 shared connections)
- [[NATS Message Handler Tests]] (6 shared connections)
- [[Standardized Error Responses]] (6 shared connections)
- [[Lifespan Startup Hooks]] (6 shared connections)
- [[WebSocket Coverage Gaps]] (5 shared connections)
- [[Pydantic Error Handlers]] (5 shared connections)
- [[Database Helper Tests]] (5 shared connections)
- [[Database Error Handling]] (4 shared connections)

## Source Files

- `server/database.py`
- `server/realtime/nats_message_handler.py`
- `server/realtime/websocket_handler_message_loop.py`
- `server/tests/unit/infrastructure/test_database_error_handling.py`
- `server/tests/unit/infrastructure/test_database_extended.py`
- `server/tests/unit/infrastructure/test_database_init.py`
- `server/tests/unit/realtime/test_nats_message_handler.py`
- `server/tests/unit/realtime/test_websocket_handler_core.py`
- `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- `server/tests/unit/realtime/test_websocket_handler_error_handling.py`
- `server/tests/unit/realtime/test_websocket_handler_helpers_extended.py`
- `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- `server/tests/unit/services/test_rate_limiter.py`

## Audit Trail

- EXTRACTED: 186 (44%)
- INFERRED: 232 (56%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
