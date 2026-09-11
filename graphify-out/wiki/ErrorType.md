# ErrorType

> 160 nodes

## Key Concepts

- **ErrorType** (52 connections) — `server/error_types.py`
- **StandardizedErrorResponse** (46 connections) — `server/error_handlers/standardized_responses.py`
- **create_websocket_error_response()** (30 connections) — `server/error_types.py`
- **test_standardized_responses.py** (29 connections) — `server/tests/unit/error_handlers/test_standardized_responses.py`
- **PydanticErrorHandler** (22 connections) — `server/error_handlers/pydantic_error_handler.py`
- **create_standard_error_response()** (22 connections) — `server/error_types.py`
- **test_error_types.py** (18 connections) — `server/tests/unit/test_error_types.py`
- **JSONResponse** (15 connections) — `docs/examples/logging/fastapi_integration.py`
- **.handle_validation_error()** (12 connections) — `server/error_handlers/pydantic_error_handler.py`
- **TestStandardizedResponsesSecurity** (10 connections) — `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- **.handle_exception()** (10 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_generic_exception()** (10 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_logged_http_exception()** (10 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_mythos_error()** (10 connections) — `server/error_handlers/standardized_responses.py`
- **handle_api_error()** (9 connections) — `server/error_handlers/standardized_responses.py`
- **error_handlers/__init__.py** (9 connections) — `server/error_handlers/__init__.py`
- **_ExtractedErrorInfo** (8 connections) — `server/error_handlers/pydantic_error_handler.py`
- **ErrorContextInitKwargs** (8 connections) — `server/exceptions.py`
- **convert_pydantic_error()** (8 connections) — `server/error_handlers/pydantic_error_handler.py`
- **handle_pydantic_error()** (8 connections) — `server/error_handlers/pydantic_error_handler.py`
- **._extract_context_from_request()** (8 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_http_exception()** (8 connections) — `server/error_handlers/standardized_responses.py`
- **.convert_to_mythos_error()** (7 connections) — `server/error_handlers/pydantic_error_handler.py`
- **._create_error_details()** (7 connections) — `server/error_handlers/pydantic_error_handler.py`
- **._create_fallback_error_response()** (7 connections) — `server/error_handlers/pydantic_error_handler.py`
- *... and 135 more nodes in this community*

## Relationships

- [api/character_creation.py](api-character_creation.py.md) (31 shared connections)
- [get_logger](get_logger.md) (30 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (13 shared connections)
- [test_websocket_handler_helpers_extended.py](test_websocket_handler_helpers_extended.py.md) (10 shared connections)
- [test_websocket_handler_validation_errors.py](test_websocket_handler_validation_errors.py.md) (6 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (5 shared connections)
- [test_websocket_handler_core.py](test_websocket_handler_core.py.md) (5 shared connections)
- [websocket_handler_commands.py](websocket_handler_commands.py.md) (4 shared connections)
- [websocket_handler_validation.py](websocket_handler_validation.py.md) (4 shared connections)
- [ExceptionTracker](ExceptionTracker.md) (3 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (3 shared connections)
- [._handle_exception](_handle_exception.md) (2 shared connections)

## Source Files

- `docs/examples/logging/fastapi_integration.py`
- `monitoring/webhook-receiver.py`
- `server/error_handlers/__init__.py`
- `server/error_handlers/pydantic_error_handler.py`
- `server/error_handlers/standardized_responses.py`
- `server/error_types.py`
- `server/exceptions.py`
- `server/realtime/websocket_handler_message_loop.py`
- `server/tests/unit/error_handlers/test_standardized_responses.py`
- `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- `server/tests/unit/test_error_types.py`

## Audit Trail

- EXTRACTED: 383 (90%)
- INFERRED: 42 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*