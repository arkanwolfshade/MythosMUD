# ErrorType

> 122 nodes

## Key Concepts

- **ErrorType** (42 connections) — `server/error_types.py`
- **error_types.py** (38 connections) — `server/error_types.py`
- **standardized_responses.py** (33 connections) — `server/error_handlers/standardized_responses.py`
- **create_websocket_error_response()** (31 connections) — `server/error_types.py`
- **create_standard_error_response()** (26 connections) — `server/error_types.py`
- **pydantic_error_handler.py** (25 connections) — `server/error_handlers/pydantic_error_handler.py`
- **ErrorSeverity** (24 connections) — `server/error_types.py`
- **PydanticErrorHandler** (23 connections) — `server/error_handlers/pydantic_error_handler.py`
- **test_error_types.py** (21 connections) — `server/tests/unit/test_error_types.py`
- **create_sse_error_response()** (16 connections) — `server/error_types.py`
- **.handle_validation_error()** (13 connections) — `server/error_handlers/pydantic_error_handler.py`
- **._handle_logged_http_exception()** (11 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_mythos_error()** (11 connections) — `server/error_handlers/standardized_responses.py`
- **HttpStandardErrorResponse** (10 connections) — `server/error_types.py`
- **test_standardized_responses_security.py** (10 connections) — `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- **error_handlers/__init__.py** (9 connections) — `server/error_handlers/__init__.py`
- **_ExtractedErrorInfo** (8 connections) — `server/error_handlers/pydantic_error_handler.py`
- **ErrorContextInitKwargs** (8 connections) — `server/exceptions.py`
- **convert_pydantic_error()** (8 connections) — `server/error_handlers/pydantic_error_handler.py`
- **handle_pydantic_error()** (8 connections) — `server/error_handlers/pydantic_error_handler.py`
- **._create_fallback_error_response()** (8 connections) — `server/error_handlers/pydantic_error_handler.py`
- **.convert_to_mythos_error()** (7 connections) — `server/error_handlers/pydantic_error_handler.py`
- **._create_error_details()** (7 connections) — `server/error_handlers/pydantic_error_handler.py`
- **.create_handler()** (7 connections) — `server/error_handlers/pydantic_error_handler.py`
- **._extract_error_info()** (7 connections) — `server/error_handlers/pydantic_error_handler.py`
- *... and 97 more nodes in this community*

## Relationships

- [MythosMUDError](MythosMUDError.md) (51 shared connections)
- [StandardizedErrorResponse](StandardizedErrorResponse.md) (40 shared connections)
- [get_logger](get_logger.md) (12 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (8 shared connections)
- [LootAllRequest](LootAllRequest.md) (7 shared connections)
- [.state](state.md) (6 shared connections)
- [create_error_context](create_error_context.md) (5 shared connections)
- [WebSocketMessageValidator](WebSocketMessageValidator.md) (5 shared connections)
- [message_handler_factory.py](message_handler_factory.py.md) (4 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (4 shared connections)
- [test_websocket_handler_core.py](test_websocket_handler_core.py.md) (3 shared connections)
- [test_websocket_handler_helpers_extended.py](test_websocket_handler_helpers_extended.py.md) (2 shared connections)

## Source Files

- `server/error_handlers/__init__.py`
- `server/error_handlers/pydantic_error_handler.py`
- `server/error_handlers/standardized_responses.py`
- `server/error_types.py`
- `server/exceptions.py`
- `server/legacy_error_handlers.py`
- `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- `server/tests/unit/test_error_types.py`

## Audit Trail

- EXTRACTED: 360 (92%)
- INFERRED: 31 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*