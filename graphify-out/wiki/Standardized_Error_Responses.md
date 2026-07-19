# Standardized Error Responses

> 268 nodes · cohesion 0.02

## Key Concepts

- **RateLimitError** (80 connections) — `server/exceptions.py`
- **MythosMUDError** (67 connections) — `server/exceptions.py`
- **ErrorMessages** (53 connections) — `server/error_types.py`
- **ErrorContext** (51 connections) — `server/exceptions.py`
- **AuthenticationError** (50 connections) — `server/exceptions.py`
- **legacy_error_handlers.py** (48 connections) — `server/legacy_error_handlers.py`
- **ErrorType** (45 connections) — `server/error_types.py`
- **NetworkError** (42 connections) — `server/exceptions.py`
- **test_legacy_error_handlers.py** (41 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **ResourceNotFoundError** (40 connections) — `server/exceptions.py`
- **ConfigurationError** (39 connections) — `server/exceptions.py`
- **CircuitBreaker** (39 connections) — `server/legacy_error_handlers.py`
- **GameLogicError** (37 connections) — `server/exceptions.py`
- **ErrorResponse** (36 connections) — `server/legacy_error_handlers.py`
- **test_exceptions_comprehensive.py** (35 connections) — `server/tests/unit/test_exceptions_comprehensive.py`
- **TestErrorMapping** (35 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **ErrorSeverity** (34 connections) — `server/error_types.py`
- **create_error_context()** (33 connections) — `server/exceptions.py`
- **standardized_responses.py** (31 connections) — `server/error_handlers/standardized_responses.py`
- **TestSanitization** (31 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **TestErrorHandlers** (27 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **TestCircuitBreaker** (22 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **HttpStandardErrorResponse** (21 connections) — `server/error_types.py`
- **JSONResponse** (21 connections) — `server/legacy_error_handlers.py`
- **MythosMUDError** (21 connections) — `server/legacy_error_handlers.py`
- *... and 243 more nodes in this community*

## Relationships

- [[NPC Admin API]] (116 shared connections)
- [[Pydantic Error Handlers]] (47 shared connections)
- [[Container Exception Handlers]] (45 shared connections)
- [[Container API Endpoints]] (36 shared connections)
- [[Enhanced Logging Exceptions]] (35 shared connections)
- [[Legacy Error Sanitization]] (33 shared connections)
- [[Character Creation API]] (8 shared connections)
- [[Database Manager Tests]] (6 shared connections)
- [[NATS Subject Admin API]] (6 shared connections)
- [[WebSocket Message Validation]] (4 shared connections)
- [[Auth Token Utilities]] (4 shared connections)
- [[Combat Messaging Base]] (4 shared connections)

## Source Files

- `server/error_handlers/standardized_responses.py`
- `server/error_types.py`
- `server/exceptions.py`
- `server/legacy_error_handlers.py`
- `server/legacy_error_sanitization.py`
- `server/tests/unit/realtime/test_websocket_handler_error_handling.py`
- `server/tests/unit/test_exceptions.py`
- `server/tests/unit/test_exceptions_comprehensive.py`
- `server/tests/unit/test_legacy_error_handlers.py`
- `tools/room_toolkit/room_validator/rules/base_rule.py`

## Audit Trail

- EXTRACTED: 1224 (63%)
- INFERRED: 733 (37%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
