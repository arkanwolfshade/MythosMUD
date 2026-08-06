# websocket handler realtime

> 68 nodes

## Key Concepts

- **StandardizedErrorResponse** (46 connections) — `server/error_handlers/standardized_responses.py`
- **test_standardized_responses.py** (29 connections) — `server/tests/unit/error_handlers/test_standardized_responses.py`
- **.handle_exception()** (14 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_generic_exception()** (10 connections) — `server/error_handlers/standardized_responses.py`
- **handle_api_error()** (10 connections) — `server/error_handlers/standardized_responses.py`
- **TestStandardizedResponsesSecurity** (10 connections) — `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- **._extract_context_from_request()** (8 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_http_exception()** (8 connections) — `server/error_handlers/standardized_responses.py`
- **._create_fallback_response()** (8 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_pydantic_validation_error()** (7 connections) — `server/error_handlers/standardized_responses.py`
- **create_standardized_error_response()** (7 connections) — `server/error_handlers/standardized_responses.py`
- **_SampleModel** (7 connections) — `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- **Request** (5 connections)
- **._extract_user_id_from_state()** (5 connections) — `server/error_handlers/standardized_responses.py`
- **._create_error_details()** (5 connections) — `server/error_handlers/standardized_responses.py`
- **._sanitize_http_detail()** (5 connections) — `server/error_handlers/standardized_responses.py`
- **._sanitize_exception_message()** (5 connections) — `server/error_handlers/standardized_responses.py`
- **.test_pydantic_validation_error_does_not_expose_str_error_in_message()** (5 connections) — `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- **_contains_sensitive_exception_pattern()** (4 connections) — `server/error_handlers/standardized_responses.py`
- **_contains_file_path_in_exception()** (4 connections) — `server/error_handlers/standardized_responses.py`
- **.__init__()** (4 connections) — `server/error_handlers/standardized_responses.py`
- **._extract_request_metadata()** (4 connections) — `server/error_handlers/standardized_responses.py`
- **Exception** (4 connections)
- **test_handle_mythos_error_response()** (4 connections) — `server/tests/unit/error_handlers/test_standardized_responses.py`
- **test_handle_logged_http_exception()** (4 connections) — `server/tests/unit/error_handlers/test_standardized_responses.py`
- *... and 43 more nodes in this community*

## Relationships

- [handler realtime nats](handler_realtime_nats.md) (38 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (13 shared connections)
- [middleware error handling](middleware_error_handling.md) (4 shared connections)
- [services inventory mutation](services_inventory_mutation.md) (3 shared connections)
- [add used user](add_used_user.md) (3 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (3 shared connections)
- [Async Query Helpers](Async_Query_Helpers.md) (2 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (2 shared connections)
- [command commands aliases](command_commands_aliases.md) (2 shared connections)

## Source Files

- `server/error_handlers/standardized_responses.py`
- `server/tests/unit/error_handlers/test_standardized_responses.py`
- `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- `server/tests/unit/realtime/test_websocket_handler_core.py`

## Audit Trail

- EXTRACTED: 276 (93%)
- INFERRED: 22 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*