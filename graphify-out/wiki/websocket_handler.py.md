# websocket_handler.py

> 97 nodes

## Key Concepts

- **websocket_handler.py** (69 connections) — `server/realtime/websocket_handler.py`
- **AttributeError** (46 connections)
- **ErrorMessages** (32 connections) — `server/error_types.py`
- **websocket_handler_message_loop.py** (29 connections) — `server/realtime/websocket_handler_message_loop.py`
- **bind_request_context()** (21 connections) — `server/structured_logging/logging_context.py`
- **clear_request_context()** (16 connections) — `server/structured_logging/logging_context.py`
- **test_websocket_correlation_context.py** (12 connections) — `server/tests/unit/realtime/test_websocket_correlation_context.py`
- **test_logging_context.py** (12 connections) — `server/tests/unit/structured_logging/test_logging_context.py`
- **handle_message_loop_exception()** (10 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_websocket_message_loop()** (10 connections) — `server/realtime/websocket_handler_message_loop.py`
- **get_current_context()** (10 connections) — `server/structured_logging/logging_context.py`
- **logging_context.py** (10 connections) — `server/structured_logging/logging_context.py`
- **test_websocket_handler_error_handling.py** (9 connections) — `server/tests/unit/realtime/test_websocket_handler_error_handling.py`
- **handle_websocket_runtime_error()** (8 connections) — `server/realtime/websocket_handler_message_loop.py`
- **WebSocket** (7 connections)
- **add_request_context()** (6 connections) — `docs/examples/logging/fastapi_integration.py`
- **websocket_endpoint()** (6 connections) — `docs/examples/logging/fastapi_integration.py`
- **handle_json_decode_error()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_websocket_generic_exception()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **process_exception_in_message_loop()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **process_websocket_inbound_message()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **UUID** (6 connections)
- **correct_async_logging()** (5 connections) — `docs/examples/logging/correct_patterns.py`
- **_cleanup_connection_and_clear_context()** (5 connections) — `server/realtime/websocket_handler.py`
- **test_connection_binds_context_fields_before_message_loop()** (5 connections) — `server/tests/unit/realtime/test_websocket_correlation_context.py`
- *... and 72 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (19 shared connections)
- [websocket_handler_commands.py](websocket_handler_commands.py.md) (14 shared connections)
- [ErrorType](ErrorType.md) (13 shared connections)
- [build_event](build_event.md) (11 shared connections)
- [test_websocket_helpers.py](test_websocket_helpers.py.md) (9 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (7 shared connections)
- [test_websocket_handler_helpers_extended.py](test_websocket_handler_helpers_extended.py.md) (7 shared connections)
- [ExceptionTracker](ExceptionTracker.md) (6 shared connections)
- [test_websocket_handler_core.py](test_websocket_handler_core.py.md) (5 shared connections)
- [PlayerService](PlayerService.md) (4 shared connections)
- [websocket_handler_validation.py](websocket_handler_validation.py.md) (4 shared connections)
- [WebSocketMessageValidator](WebSocketMessageValidator.md) (4 shared connections)

## Source Files

- `docs/examples/logging/correct_patterns.py`
- `docs/examples/logging/fastapi_integration.py`
- `server/error_types.py`
- `server/realtime/websocket_handler.py`
- `server/realtime/websocket_handler_message_loop.py`
- `server/structured_logging/logging_context.py`
- `server/tests/unit/realtime/test_websocket_correlation_context.py`
- `server/tests/unit/realtime/test_websocket_handler_error_handling.py`
- `server/tests/unit/realtime/test_websocket_handler_helpers.py`
- `server/tests/unit/services/test_room_sync_service.py`
- `server/tests/unit/structured_logging/test_logging_context.py`
- `server/tests/unit/utils/test_command_processor.py`

## Audit Trail

- EXTRACTED: 238 (72%)
- INFERRED: 93 (28%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*