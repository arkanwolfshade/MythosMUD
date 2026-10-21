# EventBus

> 256 nodes · cohesion 0.02

## Key Concepts

- **ErrorType** (52 connections) — `server/error_types.py`
- **StandardizedErrorResponse** (46 connections) — `server/error_handlers/standardized_responses.py`
- **error_types.py** (36 connections) — `server/error_types.py`
- **test_websocket_handler_helpers_extended.py** (34 connections) — `server/tests/unit/realtime/test_websocket_handler_helpers_extended.py`
- **ErrorMessages** (33 connections) — `server/error_types.py`
- **standardized_responses.py** (32 connections) — `server/error_handlers/standardized_responses.py`
- **create_websocket_error_response()** (30 connections) — `server/error_types.py`
- **test_standardized_responses.py** (29 connections) — `server/tests/unit/error_handlers/test_standardized_responses.py`
- **pydantic_error_handler.py** (24 connections) — `server/error_handlers/pydantic_error_handler.py`
- **PydanticErrorHandler** (22 connections) — `server/error_handlers/pydantic_error_handler.py`
- **create_standard_error_response()** (22 connections) — `server/error_types.py`
- **asyncio** (21 connections)
- **test_error_types.py** (18 connections) — `server/tests/unit/test_error_types.py`
- **JSONResponse** (15 connections) — `docs/examples/logging/fastapi_integration.py`
- **.handle_validation_error()** (12 connections) — `server/error_handlers/pydantic_error_handler.py`
- **.handle_exception()** (10 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_generic_exception()** (10 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_logged_http_exception()** (10 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_mythos_error()** (10 connections) — `server/error_handlers/standardized_responses.py`
- **ErrorSeverity** (10 connections) — `server/error_types.py`
- **test_standardized_responses_security.py** (10 connections) — `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- **TestStandardizedResponsesSecurity** (10 connections) — `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- **error_handlers/__init__.py** (9 connections) — `server/error_handlers/__init__.py`
- **handle_api_error()** (9 connections) — `server/error_handlers/standardized_responses.py`
- **test_websocket_handler_error_handling.py** (9 connections) — `server/tests/unit/realtime/test_websocket_handler_error_handling.py`
- *... and 231 more nodes in this community*

## Relationships

- [AttributeError](AttributeError.md) (26 shared connections)
- [resolve_weapon_attack_from_equipped](resolve_weapon_attack_from_equipped.md) (12 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (10 shared connections)
- [NATSService](NATSService.md) (10 shared connections)
- [test_security_validator.py](test_security_validator.py.md) (9 shared connections)
- [useAsciiMapState.ts](useAsciiMapState.ts.md) (9 shared connections)
- [Alias](Alias.md) (8 shared connections)
- [Room](Room.md) (5 shared connections)
- [apiTypeGuards.ts](apiTypeGuards.ts.md) (5 shared connections)
- [test_look_player.py](test_look_player.py.md) (5 shared connections)
- [test_npc_startup_service.py](test_npc_startup_service.py.md) (5 shared connections)
- [look_container.py](look_container.py.md) (5 shared connections)

## Source Files

- `docs/examples/logging/fastapi_integration.py`
- `monitoring/webhook-receiver.py`
- `server/error_handlers/__init__.py`
- `server/error_handlers/pydantic_error_handler.py`
- `server/error_handlers/standardized_responses.py`
- `server/error_types.py`
- `server/exceptions.py`
- `server/tests/unit/error_handlers/test_standardized_responses.py`
- `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- `server/tests/unit/realtime/test_websocket_handler_error_handling.py`
- `server/tests/unit/realtime/test_websocket_handler_helpers_extended.py`
- `server/tests/unit/test_error_types.py`

## Audit Trail

- EXTRACTED: 573 (91%)
- INFERRED: 55 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*