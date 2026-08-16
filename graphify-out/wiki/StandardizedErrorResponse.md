# StandardizedErrorResponse

> 59 nodes

## Key Concepts

- **StandardizedErrorResponse** (46 connections) — `server/error_handlers/standardized_responses.py`
- **ErrorMessages** (35 connections) — `server/error_types.py`
- **standardized_responses.py** (35 connections) — `server/error_handlers/standardized_responses.py`
- **test_standardized_responses.py** (30 connections) — `server/tests/unit/error_handlers/test_standardized_responses.py`
- **test_standardized_responses_security.py** (13 connections) — `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- **TestStandardizedResponsesSecurity** (10 connections) — `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- **handle_api_error()** (9 connections) — `server/error_handlers/standardized_responses.py`
- **error_handlers/__init__.py** (9 connections) — `server/error_handlers/__init__.py`
- **._extract_context_from_request()** (8 connections) — `server/error_handlers/standardized_responses.py`
- **create_standardized_error_response()** (7 connections) — `server/error_handlers/standardized_responses.py`
- **._create_error_details()** (5 connections) — `server/error_handlers/standardized_responses.py`
- **._extract_user_id_from_state()** (5 connections) — `server/error_handlers/standardized_responses.py`
- **._sanitize_exception_message()** (5 connections) — `server/error_handlers/standardized_responses.py`
- **._sanitize_http_detail()** (5 connections) — `server/error_handlers/standardized_responses.py`
- **test_handle_mythos_error_response()** (5 connections) — `server/tests/unit/error_handlers/test_standardized_responses.py`
- **Request** (5 connections)
- **_SampleModel** (4 connections) — `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- **_contains_file_path_in_exception()** (4 connections) — `server/error_handlers/standardized_responses.py`
- **_contains_sensitive_exception_pattern()** (4 connections) — `server/error_handlers/standardized_responses.py`
- **._extract_request_metadata()** (4 connections) — `server/error_handlers/standardized_responses.py`
- **.__init__()** (4 connections) — `server/error_handlers/standardized_responses.py`
- **_response_message()** (4 connections) — `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- **.test_pydantic_validation_error_does_not_expose_str_error_in_message()** (4 connections) — `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- **test_determine_error_type_from_exception_uses_attr()** (4 connections) — `server/tests/unit/error_handlers/test_standardized_responses.py`
- **test_handle_logged_http_exception()** (4 connections) — `server/tests/unit/error_handlers/test_standardized_responses.py`
- *... and 34 more nodes in this community*

## Relationships

- [ErrorType](ErrorType.md) (34 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (20 shared connections)
- [PydanticErrorHandler](PydanticErrorHandler.md) (8 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (8 shared connections)
- [test_websocket_handler_helpers_extended.py](test_websocket_handler_helpers_extended.py.md) (6 shared connections)
- [test_error_handling_middleware.py](test_error_handling_middleware.py.md) (5 shared connections)
- [LootAllRequest](LootAllRequest.md) (3 shared connections)
- [api/player_effects.py](api-player_effects.py.md) (3 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (3 shared connections)
- [test_websocket_handler_error_handling.py](test_websocket_handler_error_handling.py.md) (3 shared connections)
- [DatabaseError](DatabaseError.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)

## Source Files

- `server/error_handlers/__init__.py`
- `server/error_handlers/standardized_responses.py`
- `server/error_types.py`
- `server/tests/unit/error_handlers/test_standardized_responses.py`
- `server/tests/unit/error_handlers/test_standardized_responses_security.py`

## Audit Trail

- EXTRACTED: 183 (84%)
- INFERRED: 34 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*