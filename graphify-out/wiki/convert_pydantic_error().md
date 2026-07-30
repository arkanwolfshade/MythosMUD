# convert pydantic error()

> 207 nodes

## Key Concepts

- **error_types.py** (37 connections) — `server/error_types.py`
- **StandardizedErrorResponse** (35 connections) — `server/error_handlers/standardized_responses.py`
- **test_websocket_handler_helpers_extended.py** (33 connections) — `server/tests/unit/realtime/test_websocket_handler_helpers_extended.py`
- **create_websocket_error_response()** (32 connections) — `server/error_types.py`
- **create_standard_error_response()** (27 connections) — `server/error_types.py`
- **pydantic_error_handler.py** (25 connections) — `server/error_handlers/pydantic_error_handler.py`
- **PydanticErrorHandler** (23 connections) — `server/error_handlers/pydantic_error_handler.py`
- **message_handler_factory.py** (23 connections) — `server/realtime/message_handler_factory.py`
- **test_error_types.py** (21 connections) — `server/tests/unit/test_error_types.py`
- **create_sse_error_response()** (17 connections) — `server/error_types.py`
- **.handle_validation_error()** (14 connections) — `server/error_handlers/pydantic_error_handler.py`
- **.handle_exception()** (14 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_mythos_error()** (11 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_logged_http_exception()** (11 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_generic_exception()** (10 connections) — `server/error_handlers/standardized_responses.py`
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
- *... and 182 more nodes in this community*

## Relationships

- [. init ()](_init_%28%29.md) (89 shared connections)
- [.reset instance()](reset_instance%28%29.md) (6 shared connections)
- [nudgeStandBothPlayers()](nudgeStandBothPlayers%28%29.md) (6 shared connections)
- [.initialize()](initialize%28%29.md) (4 shared connections)
- [world](world.md) (4 shared connections)
- [help content](help_content.md) (4 shared connections)
- [.is required()](is_required%28%29.md) (4 shared connections)
- [real time](real_time.md) (3 shared connections)
- [AbstractContextManager](AbstractContextManager.md) (3 shared connections)
- [MessageHandlerFactory](MessageHandlerFactory.md) (3 shared connections)
- [NATS](NATS.md) (2 shared connections)
- [generate invites db](generate_invites_db.md) (2 shared connections)

## Source Files

- `server/error_handlers/__init__.py`
- `server/error_handlers/pydantic_error_handler.py`
- `server/error_handlers/standardized_responses.py`
- `server/error_types.py`
- `server/exceptions.py`
- `server/realtime/message_handler_factory.py`
- `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- `server/tests/unit/realtime/test_websocket_handler_helpers_extended.py`
- `server/tests/unit/test_error_types.py`

## Audit Trail

- EXTRACTED: 811 (97%)
- INFERRED: 23 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*