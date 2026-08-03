# app factory rationale

> 45 nodes

## Key Concepts

- **main.py** (15 connections) — `server/main.py`
- **create_app()** (14 connections) — `server/app/factory.py`
- **correlation_middleware.py** (9 connections) — `server/middleware/correlation_middleware.py`
- **.__call__()** (8 connections) — `server/middleware/correlation_middleware.py`
- **CorrelationMiddleware** (6 connections) — `server/middleware/correlation_middleware.py`
- **WebSocketCorrelationMiddleware** (5 connections) — `server/middleware/correlation_middleware.py`
- **.__call__()** (5 connections) — `server/middleware/correlation_middleware.py`
- **main()** (4 connections) — `scripts/generate_openapi_spec.py`
- **main()** (4 connections) — `server/main.py`
- **_create_get_app()** (4 connections) — `server/main.py`
- **_get_header()** (4 connections) — `server/middleware/correlation_middleware.py`
- **create_correlation_middleware()** (4 connections) — `server/middleware/correlation_middleware.py`
- **generate_openapi_spec.py** (3 connections) — `scripts/generate_openapi_spec.py`
- **_sanitize_token_examples()** (3 connections) — `scripts/generate_openapi_spec.py`
- **FastAPI** (3 connections)
- **FastAPI** (3 connections)
- **test_auth()** (3 connections) — `server/main.py`
- **.__init__()** (3 connections) — `server/middleware/correlation_middleware.py`
- **create_websocket_correlation_middleware()** (3 connections) — `server/middleware/correlation_middleware.py`
- **read_root()** (2 connections) — `server/main.py`
- **Scope** (2 connections)
- **.__init__()** (2 connections) — `server/middleware/correlation_middleware.py`
- **Any** (2 connections)
- **Replace auth token examples with clearly fake placeholders.** (1 connections) — `scripts/generate_openapi_spec.py`
- **Generate and write OpenAPI spec to docs/openapi/openapi.json.** (1 connections) — `scripts/generate_openapi_spec.py`
- *... and 20 more nodes in this community*

## Relationships

- [command inventory factories](command_inventory_factories.md) (9 shared connections)
- [middleware correlation rationale](middleware_correlation_rationale.md) (4 shared connections)
- [auth users rationale](auth_users_rationale.md) (3 shared connections)
- [time service rationale](time_service_rationale.md) (1 shared connections)
- [middleware comprehensive logging](middleware_comprehensive_logging.md) (1 shared connections)
- [middleware error handling](middleware_error_handling.md) (1 shared connections)
- [security headers middleware](security_headers_middleware.md) (1 shared connections)
- [Item Instances](Item_Instances.md) (1 shared connections)

## Source Files

- `scripts/generate_openapi_spec.py`
- `server/app/factory.py`
- `server/main.py`
- `server/middleware/correlation_middleware.py`

## Audit Trail

- EXTRACTED: 126 (95%)
- INFERRED: 7 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*