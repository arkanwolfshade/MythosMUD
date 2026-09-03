# Test Request Schema Security

> 24 nodes

## Key Concepts

- **test_request_schema_security.py** (15 connections) — `server/tests/integration/test_request_schema_security.py`
- **_all_route_reachable_models()** (7 connections) — `server/tests/integration/test_request_schema_security.py`
- **_iter_body_models()** (6 connections) — `server/tests/integration/test_request_schema_security.py`
- **_iter_api_routes()** (5 connections) — `server/tests/integration/test_request_schema_security.py`
- **_iter_nested_models()** (4 connections) — `server/tests/integration/test_request_schema_security.py`
- **_resolve_hints()** (4 connections) — `server/tests/integration/test_request_schema_security.py`
- **test_every_request_body_schema_is_secure_base_model()** (4 connections) — `server/tests/integration/test_request_schema_security.py`
- **_RouteContainer** (3 connections) — `server/tests/integration/test_request_schema_security.py`
- **_RouterHolder** (3 connections) — `server/tests/integration/test_request_schema_security.py`
- **test_secure_base_model_config_survives_subclass_json_schema_extra()** (3 connections) — `server/tests/integration/test_request_schema_security.py`
- **BaseModel** (3 connections)
- **APIRoute** (2 connections)
- **Protocol** (2 connections)
- **BaseRoute** (1 connections)
- **Guard: every FastAPI request-body schema must inherit SecureBaseModel. #755…** (1 connections) — `server/tests/integration/test_request_schema_security.py`
- **Yield model and every BaseModel subclass reachable through its fields, once…** (1 connections) — `server/tests/integration/test_request_schema_security.py`
- **Map each request-body-reachable model to the route path(s) that reach it.** (1 connections) — `server/tests/integration/test_request_schema_security.py`
- **Every schema reachable from a request body must inherit SecureBaseModel.** (1 connections) — `server/tests/integration/test_request_schema_security.py`
- **A subclass that redeclares model_config only for json_schema_extra must still…** (1 connections) — `server/tests/integration/test_request_schema_security.py`
- **Structural shape of fastapi.routing's internal include-router wrapper.** (1 connections) — `server/tests/integration/test_request_schema_security.py`
- **Structural shape shared by Router/APIRouter/Mount: something with .routes.** (1 connections) — `server/tests/integration/test_request_schema_security.py`
- **Recursively descend into every route grouping to find leaf APIRoutes.…** (1 connections) — `server/tests/integration/test_request_schema_security.py`
- **Best-effort get_type_hints: resolves every annotation get_type_hints can, even…** (1 connections) — `server/tests/integration/test_request_schema_security.py`
- **Yield each BaseModel subclass bound as a body parameter on this route.** (1 connections) — `server/tests/integration/test_request_schema_security.py`

## Relationships

- [NPC Definitions API](NPC_Definitions_API.md) (4 shared connections)
- [Test Websocket Handler Validation Errors](Test_Websocket_Handler_Validation_Errors.md) (1 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)
- [Command Aliases](Command_Aliases.md) (1 shared connections)
- [Correlation Middleware](Correlation_Middleware.md) (1 shared connections)

## Source Files

- `server/tests/integration/test_request_schema_security.py`

## Audit Trail

- EXTRACTED: 37 (92%)
- INFERRED: 3 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*