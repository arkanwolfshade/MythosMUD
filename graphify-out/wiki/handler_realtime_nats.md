# handler realtime nats

> 167 nodes

## Key Concepts

- **StandardizedErrorResponse** (46 connections) — `server/error_handlers/standardized_responses.py`
- **error_types.py** (38 connections) — `server/error_types.py`
- **create_websocket_error_response()** (32 connections) — `server/error_types.py`
- **test_standardized_responses.py** (29 connections) — `server/tests/unit/error_handlers/test_standardized_responses.py`
- **create_standard_error_response()** (27 connections) — `server/error_types.py`
- **pydantic_error_handler.py** (25 connections) — `server/error_handlers/pydantic_error_handler.py`
- **PydanticErrorHandler** (23 connections) — `server/error_handlers/pydantic_error_handler.py`
- **test_error_types.py** (21 connections) — `server/tests/unit/test_error_types.py`
- **create_sse_error_response()** (17 connections) — `server/error_types.py`
- **.handle_validation_error()** (14 connections) — `server/error_handlers/pydantic_error_handler.py`
- **.handle_exception()** (14 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_mythos_error()** (11 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_logged_http_exception()** (11 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_generic_exception()** (10 connections) — `server/error_handlers/standardized_responses.py`
- **handle_api_error()** (10 connections) — `server/error_handlers/standardized_responses.py`
- **test_standardized_responses_security.py** (10 connections) — `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- **TestStandardizedResponsesSecurity** (10 connections) — `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- **__init__.py** (9 connections) — `server/error_handlers/__init__.py`
- **handle_pydantic_error()** (9 connections) — `server/error_handlers/pydantic_error_handler.py`
- **convert_pydantic_error()** (9 connections) — `server/error_handlers/pydantic_error_handler.py`
- **ErrorResponseDetails** (9 connections) — `server/error_types.py`
- **_ExtractedErrorInfo** (8 connections) — `server/error_handlers/pydantic_error_handler.py`
- **._create_fallback_error_response()** (8 connections) — `server/error_handlers/pydantic_error_handler.py`
- **.convert_to_mythos_error()** (8 connections) — `server/error_handlers/pydantic_error_handler.py`
- **._extract_context_from_request()** (8 connections) — `server/error_handlers/standardized_responses.py`
- *... and 142 more nodes in this community*

## Relationships

- [Error Handling Core](Error_Handling_Core.md) (79 shared connections)
- [services inventory mutation](services_inventory_mutation.md) (5 shared connections)
- [occupant formatter realtime](occupant_formatter_realtime.md) (5 shared connections)
- [command inventory models](command_inventory_models.md) (4 shared connections)
- [middleware error handling](middleware_error_handling.md) (4 shared connections)
- [alias storage rationale](alias_storage_rationale.md) (4 shared connections)
- [realtime message validator](realtime_message_validator.md) (4 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (3 shared connections)
- [chat logger services](chat_logger_services.md) (3 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (3 shared connections)
- [tsconfig src/**/* spec](tsconfig_src-__-__spec.md) (3 shared connections)
- [command processor rationale](command_processor_rationale.md) (2 shared connections)

## Source Files

- `server/error_handlers/__init__.py`
- `server/error_handlers/pydantic_error_handler.py`
- `server/error_handlers/standardized_responses.py`
- `server/error_types.py`
- `server/exceptions.py`
- `server/tests/unit/error_handlers/test_standardized_responses.py`
- `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- `server/tests/unit/test_error_types.py`

## Audit Trail

- EXTRACTED: 757 (97%)
- INFERRED: 23 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*