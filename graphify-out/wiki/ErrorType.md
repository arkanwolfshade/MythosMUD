# ErrorType

> 121 nodes

## Key Concepts

- **ErrorType** (65 connections) — `server/error_types.py`
- **legacy_error_handlers.py** (44 connections) — `server/legacy_error_handlers.py`
- **test_legacy_error_handlers.py** (43 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **error_types.py** (38 connections) — `server/error_types.py`
- **standardized_responses.py** (35 connections) — `server/error_handlers/standardized_responses.py`
- **create_websocket_error_response()** (31 connections) — `server/error_types.py`
- **create_standard_error_response()** (26 connections) — `server/error_types.py`
- **pydantic_error_handler.py** (26 connections) — `server/error_handlers/pydantic_error_handler.py`
- **test_error_types.py** (21 connections) — `server/tests/unit/test_error_types.py`
- **ErrorSeverity** (19 connections) — `server/error_types.py`
- **logged_http_exception_handler()** (17 connections) — `server/legacy_error_handlers.py`
- **ErrorResponse** (16 connections) — `server/legacy_error_handlers.py`
- **create_sse_error_response()** (16 connections) — `server/error_types.py`
- **create_error_response()** (15 connections) — `server/legacy_error_handlers.py`
- **http_exception_handler()** (15 connections) — `server/legacy_error_handlers.py`
- **general_exception_handler()** (12 connections) — `server/legacy_error_handlers.py`
- **mythos_exception_handler()** (12 connections) — `server/legacy_error_handlers.py`
- **._handle_logged_http_exception()** (11 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_mythos_error()** (11 connections) — `server/error_handlers/standardized_responses.py`
- **register_error_handlers()** (11 connections) — `server/legacy_error_handlers.py`
- **TestErrorResponse** (9 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **TestCreateErrorResponse** (8 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **HttpStandardErrorResponse** (7 connections) — `server/error_types.py`
- **_normalize_error_response_details()** (7 connections) — `server/error_types.py`
- **ErrorResponseDetails** (6 connections) — `server/error_types.py`
- *... and 96 more nodes in this community*

## Relationships

- [StandardizedErrorResponse](StandardizedErrorResponse.md) (41 shared connections)
- [AuthenticationError](AuthenticationError.md) (25 shared connections)
- [PydanticErrorHandler](PydanticErrorHandler.md) (18 shared connections)
- [TestErrorHandlers](TestErrorHandlers.md) (15 shared connections)
- [legacy_error_sanitization.py](legacy_error_sanitization.py.md) (12 shared connections)
- [PlayerService](PlayerService.md) (12 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (11 shared connections)
- [get_logger](get_logger.md) (11 shared connections)
- [test_websocket_handler_helpers_extended.py](test_websocket_handler_helpers_extended.py.md) (9 shared connections)
- [MythosMUDError](MythosMUDError.md) (9 shared connections)
- [test_exceptions.py](test_exceptions.py.md) (9 shared connections)
- [ValidationError](ValidationError.md) (8 shared connections)

## Source Files

- `server/error_handlers/pydantic_error_handler.py`
- `server/error_handlers/standardized_responses.py`
- `server/error_types.py`
- `server/legacy_error_handlers.py`
- `server/tests/unit/test_error_types.py`
- `server/tests/unit/test_legacy_error_handlers.py`

## Audit Trail

- EXTRACTED: 423 (87%)
- INFERRED: 61 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*