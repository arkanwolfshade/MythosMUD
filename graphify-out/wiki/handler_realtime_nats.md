# handler realtime nats

> 98 nodes

## Key Concepts

- **StandardizedErrorResponse** (46 connections) — `server/error_handlers/standardized_responses.py`
- **JSONResponse** (31 connections) — `docs/examples/logging/fastapi_integration.py`
- **test_standardized_responses.py** (29 connections) — `server/tests/unit/error_handlers/test_standardized_responses.py`
- **.handle_exception()** (14 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_logged_http_exception()** (11 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_generic_exception()** (10 connections) — `server/error_handlers/standardized_responses.py`
- **handle_api_error()** (10 connections) — `server/error_handlers/standardized_responses.py`
- **test_standardized_responses_security.py** (10 connections) — `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- **TestStandardizedResponsesSecurity** (10 connections) — `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- **._extract_context_from_request()** (8 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_http_exception()** (8 connections) — `server/error_handlers/standardized_responses.py`
- **._create_fallback_response()** (8 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_pydantic_validation_error()** (7 connections) — `server/error_handlers/standardized_responses.py`
- **create_standardized_error_response()** (7 connections) — `server/error_handlers/standardized_responses.py`
- **_SampleModel** (7 connections) — `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- **Request** (5 connections)
- **._extract_user_id_from_state()** (5 connections) — `server/error_handlers/standardized_responses.py`
- **._get_logged_http_user_friendly_message()** (5 connections) — `server/error_handlers/standardized_responses.py`
- **._map_status_code_to_error_type()** (5 connections) — `server/error_handlers/standardized_responses.py`
- **._create_error_details()** (5 connections) — `server/error_handlers/standardized_responses.py`
- **._sanitize_http_detail()** (5 connections) — `server/error_handlers/standardized_responses.py`
- **._sanitize_exception_message()** (5 connections) — `server/error_handlers/standardized_responses.py`
- **.test_pydantic_validation_error_does_not_expose_str_error_in_message()** (5 connections) — `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- **.test_mythos_exception_handler()** (5 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_mythos_exception_handler_with_debug()** (5 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- *... and 73 more nodes in this community*

## Relationships

- [Error Handling Core](Error_Handling_Core.md) (63 shared connections)
- [game weapon player](game_weapon_player.md) (9 shared connections)
- [Exception Containers](Exception_Containers.md) (9 shared connections)
- [middleware error handling](middleware_error_handling.md) (5 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (5 shared connections)
- [middleware correlation rationale](middleware_correlation_rationale.md) (3 shared connections)
- [Spell Validation](Spell_Validation.md) (2 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (2 shared connections)
- [Database Config](Database_Config.md) (2 shared connections)
- [combat schemas schema](combat_schemas_schema.md) (2 shared connections)
- [webhook receiver monitoring](webhook_receiver_monitoring.md) (1 shared connections)
- [grace period login](grace_period_login.md) (1 shared connections)

## Source Files

- `docs/examples/logging/fastapi_integration.py`
- `server/error_handlers/standardized_responses.py`
- `server/tests/unit/error_handlers/test_standardized_responses.py`
- `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- `server/tests/unit/realtime/test_websocket_handler_core.py`
- `server/tests/unit/test_legacy_error_handlers.py`

## Audit Trail

- EXTRACTED: 377 (90%)
- INFERRED: 44 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*