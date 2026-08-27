# canonical_room_id_impl

> 137 nodes

## Key Concepts

- **ErrorType** (52 connections) — `server/error_types.py`
- **StandardizedErrorResponse** (46 connections) — `server/error_handlers/standardized_responses.py`
- **error_types.py** (35 connections) — `server/error_types.py`
- **create_websocket_error_response()** (30 connections) — `server/error_types.py`
- **test_standardized_responses.py** (30 connections) — `server/tests/unit/error_handlers/test_standardized_responses.py`
- **standardized_responses.py** (23 connections) — `server/error_handlers/standardized_responses.py`
- **create_standard_error_response()** (22 connections) — `server/error_types.py`
- **pydantic_error_handler.py** (21 connections) — `server/error_handlers/pydantic_error_handler.py`
- **test_error_types.py** (18 connections) — `server/tests/unit/test_error_types.py`
- **test_standardized_responses_security.py** (13 connections) — `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- **ErrorSeverity** (10 connections) — `server/error_types.py`
- **TestStandardizedResponsesSecurity** (10 connections) — `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- **.handle_exception()** (10 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_generic_exception()** (10 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_logged_http_exception()** (10 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_mythos_error()** (10 connections) — `server/error_handlers/standardized_responses.py`
- **handle_api_error()** (9 connections) — `server/error_handlers/standardized_responses.py`
- **error_handlers/__init__.py** (9 connections) — `server/error_handlers/__init__.py`
- **._handle_http_exception()** (8 connections) — `server/error_handlers/standardized_responses.py`
- **JSONResponse** (8 connections)
- **create_standardized_error_response()** (7 connections) — `server/error_handlers/standardized_responses.py`
- **._create_fallback_response()** (7 connections) — `server/error_handlers/standardized_responses.py`
- **._extract_context_from_request()** (7 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_pydantic_validation_error()** (7 connections) — `server/error_handlers/standardized_responses.py`
- **ErrorResponseDetails** (6 connections) — `server/error_types.py`
- *... and 112 more nodes in this community*

## Relationships

- [test_config_model_helpers.py](test_config_model_helpers.py.md) (21 shared connections)
- [test_logging_processors.py](test_logging_processors.py.md) (21 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (13 shared connections)
- [test_error_logging.py](test_error_logging.py.md) (8 shared connections)
- [ExceptionTracker](ExceptionTracker.md) (7 shared connections)
- [CatatoniaRegistry](CatatoniaRegistry.md) (7 shared connections)
- [register_user](register_user.md) (5 shared connections)
- [test_goto_helpers.py](test_goto_helpers.py.md) (5 shared connections)
- [UUID](UUID.md) (5 shared connections)
- [player_combat_service_support.py](player_combat_service_support.py.md) (4 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (4 shared connections)
- [ContainerComponent](ContainerComponent.md) (3 shared connections)

## Source Files

- `server/error_handlers/__init__.py`
- `server/error_handlers/pydantic_error_handler.py`
- `server/error_handlers/standardized_responses.py`
- `server/error_types.py`
- `server/tests/unit/error_handlers/test_standardized_responses.py`
- `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- `server/tests/unit/test_error_types.py`

## Audit Trail

- EXTRACTED: 360 (90%)
- INFERRED: 39 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*