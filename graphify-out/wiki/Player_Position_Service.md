# Player Position Service

> 53 nodes

## Key Concepts

- **StandardizedErrorResponse** (35 connections) — `server/error_handlers/standardized_responses.py`
- **.handle_exception()** (14 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_mythos_error()** (11 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_generic_exception()** (10 connections) — `server/error_handlers/standardized_responses.py`
- **test_standardized_responses_security.py** (10 connections) — `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- **TestStandardizedResponsesSecurity** (10 connections) — `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- **._extract_context_from_request()** (8 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_http_exception()** (8 connections) — `server/error_handlers/standardized_responses.py`
- **._create_fallback_response()** (8 connections) — `server/error_handlers/standardized_responses.py`
- **handle_api_error()** (8 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_pydantic_validation_error()** (7 connections) — `server/error_handlers/standardized_responses.py`
- **_SampleModel** (7 connections) — `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- **Request** (5 connections)
- **._generate_user_friendly_message()** (5 connections) — `server/error_handlers/standardized_responses.py`
- **._create_error_details()** (5 connections) — `server/error_handlers/standardized_responses.py`
- **._sanitize_http_detail()** (5 connections) — `server/error_handlers/standardized_responses.py`
- **._sanitize_exception_message()** (5 connections) — `server/error_handlers/standardized_responses.py`
- **create_standardized_error_response()** (5 connections) — `server/error_handlers/standardized_responses.py`
- **.test_pydantic_validation_error_does_not_expose_str_error_in_message()** (5 connections) — `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- **.__init__()** (4 connections) — `server/error_handlers/standardized_responses.py`
- **._extract_user_id_from_state()** (4 connections) — `server/error_handlers/standardized_responses.py`
- **._extract_request_metadata()** (4 connections) — `server/error_handlers/standardized_responses.py`
- **Exception** (4 connections)
- **_response_message()** (4 connections) — `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- **.test_pydantic_convert_to_mythos_error_does_not_use_str_error_as_message()** (4 connections) — `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- *... and 28 more nodes in this community*

## Relationships

- [Container API Endpoints](Container_API_Endpoints.md) (27 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (13 shared connections)
- [Combat Death Handling](Combat_Death_Handling.md) (9 shared connections)
- [Error Handling Middleware](Error_Handling_Middleware.md) (4 shared connections)
- [Command Parser Helpers](Command_Parser_Helpers.md) (3 shared connections)
- [Active Lucidity Service](Active_Lucidity_Service.md) (2 shared connections)
- [Player Combat XP](Player_Combat_XP.md) (2 shared connections)
- [Combat Feature Flags](Combat_Feature_Flags.md) (2 shared connections)
- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (1 shared connections)

## Source Files

- `server/error_handlers/standardized_responses.py`
- `server/tests/unit/error_handlers/test_standardized_responses_security.py`

## Audit Trail

- EXTRACTED: 213 (92%)
- INFERRED: 18 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*