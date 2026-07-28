# Server Error Handlers

> 169 nodes

## Key Concepts

- **MythosMUDError** (79 connections) — `server/exceptions.py`
- **AuthenticationError** (63 connections) — `server/exceptions.py`
- **legacy_error_handlers.py** (48 connections) — `server/legacy_error_handlers.py`
- **ErrorType** (44 connections) — `server/error_types.py`
- **test_legacy_error_handlers.py** (41 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **CircuitBreaker** (38 connections) — `server/legacy_error_handlers.py`
- **NetworkError** (37 connections) — `server/exceptions.py`
- **ErrorResponse** (37 connections) — `server/legacy_error_handlers.py`
- **ResourceNotFoundError** (34 connections) — `server/exceptions.py`
- **ConfigurationError** (32 connections) — `server/exceptions.py`
- **GameLogicError** (31 connections) — `server/exceptions.py`
- **JSONResponse** (30 connections) — `docs/examples/logging/fastapi_integration.py`
- **ErrorSeverity** (30 connections) — `server/error_types.py`
- **TestErrorHandlers** (27 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **TestCircuitBreaker** (22 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **Request** (21 connections)
- **_AppWithLegacyConfigState** (20 connections) — `server/legacy_error_handlers.py`
- **TestErrorResponse** (20 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **_AppStateWithLegacyConfig** (19 connections) — `server/legacy_error_handlers.py`
- **TestCreateErrorResponse** (19 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **TestLegacyHandlerSecurity** (19 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **ErrorResponseDetailsInput** (18 connections)
- **FastAPI** (18 connections)
- **legacy_error_sanitization.py** (18 connections) — `server/legacy_error_sanitization.py`
- **TestGracefulDegradation** (18 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- *... and 144 more nodes in this community*

## Relationships

- [Server Utils (3)](Server_Utils_%283%29.md) (62 shared connections)
- [Server Error Handlers (2)](Server_Error_Handlers_%282%29.md) (51 shared connections)
- [Server (2)](Server_%282%29.md) (34 shared connections)
- [Server (4)](Server_%284%29.md) (33 shared connections)
- [Server Api (2)](Server_Api_%282%29.md) (31 shared connections)
- [Server Api](Server_Api.md) (29 shared connections)
- [Server Utils](Server_Utils.md) (26 shared connections)
- [Server Persistence](Server_Persistence.md) (20 shared connections)
- [Server Auth (3)](Server_Auth_%283%29.md) (19 shared connections)
- [Server Admin](Server_Admin.md) (11 shared connections)
- [Server Auth (4)](Server_Auth_%284%29.md) (9 shared connections)
- [Server Game](Server_Game.md) (5 shared connections)

## Source Files

- `docs/examples/logging/fastapi_integration.py`
- `server/error_handlers/standardized_responses.py`
- `server/error_types.py`
- `server/exceptions.py`
- `server/legacy_error_handlers.py`
- `server/legacy_error_sanitization.py`
- `server/services/combat_messaging_service.py`
- `server/tests/unit/test_exceptions_comprehensive.py`
- `server/tests/unit/test_legacy_error_handlers.py`

## Audit Trail

- EXTRACTED: 782 (61%)
- INFERRED: 504 (39%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*