# Container API Endpoints

> 104 nodes

## Key Concepts

- **StandardizedErrorResponse** (35 connections) — `server/error_handlers/standardized_responses.py`
- **pydantic_error_handler.py** (25 connections) — `server/error_handlers/pydantic_error_handler.py`
- **PydanticErrorHandler** (23 connections) — `server/error_handlers/pydantic_error_handler.py`
- **.handle_validation_error()** (14 connections) — `server/error_handlers/pydantic_error_handler.py`
- **.handle_exception()** (14 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_generic_exception()** (10 connections) — `server/error_handlers/standardized_responses.py`
- **test_standardized_responses_security.py** (10 connections) — `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- **TestStandardizedResponsesSecurity** (10 connections) — `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- **__init__.py** (9 connections) — `server/error_handlers/__init__.py`
- **handle_pydantic_error()** (9 connections) — `server/error_handlers/pydantic_error_handler.py`
- **convert_pydantic_error()** (9 connections) — `server/error_handlers/pydantic_error_handler.py`
- **_ExtractedErrorInfo** (8 connections) — `server/error_handlers/pydantic_error_handler.py`
- **._create_fallback_error_response()** (8 connections) — `server/error_handlers/pydantic_error_handler.py`
- **.convert_to_mythos_error()** (8 connections) — `server/error_handlers/pydantic_error_handler.py`
- **._extract_context_from_request()** (8 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_http_exception()** (8 connections) — `server/error_handlers/standardized_responses.py`
- **._create_fallback_response()** (8 connections) — `server/error_handlers/standardized_responses.py`
- **handle_api_error()** (8 connections) — `server/error_handlers/standardized_responses.py`
- **ErrorContextInitKwargs** (8 connections) — `server/exceptions.py`
- **ValidationError** (7 connections)
- **._extract_error_info()** (7 connections) — `server/error_handlers/pydantic_error_handler.py`
- **._generate_user_friendly_message()** (7 connections) — `server/error_handlers/pydantic_error_handler.py`
- **._create_error_details()** (7 connections) — `server/error_handlers/pydantic_error_handler.py`
- **.create_handler()** (7 connections) — `server/error_handlers/pydantic_error_handler.py`
- **._handle_pydantic_validation_error()** (7 connections) — `server/error_handlers/standardized_responses.py`
- *... and 79 more nodes in this community*

## Relationships

- [Standardized Error Responses](Standardized_Error_Responses.md) (58 shared connections)
- [Active Lucidity Service](Active_Lucidity_Service.md) (8 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (4 shared connections)
- [Room Service Tests](Room_Service_Tests.md) (4 shared connections)
- [Error Handling Middleware](Error_Handling_Middleware.md) (4 shared connections)
- [Cursor Skills Delight](Cursor_Skills_Delight.md) (2 shared connections)
- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (2 shared connections)
- [Combat Feature Flags](Combat_Feature_Flags.md) (2 shared connections)
- [Player Combat XP](Player_Combat_XP.md) (2 shared connections)

## Source Files

- `server/error_handlers/__init__.py`
- `server/error_handlers/pydantic_error_handler.py`
- `server/error_handlers/standardized_responses.py`
- `server/error_types.py`
- `server/exceptions.py`
- `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- `server/tests/unit/realtime/test_websocket_handler_core.py`

## Audit Trail

- EXTRACTED: 427 (95%)
- INFERRED: 23 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*