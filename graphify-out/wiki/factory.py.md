# factory.py

> 38 nodes · cohesion 0.07

## Key Concepts

- **factory.py** (37 connections) — `server/app/factory.py`
- **create_app()** (16 connections) — `server/app/factory.py`
- **SecurityHeadersMiddleware** (13 connections) — `server/middleware/security_headers.py`
- **ComprehensiveLoggingMiddleware** (10 connections) — `server/middleware/comprehensive_logging.py`
- **_configure_cors()** (6 connections) — `server/app/factory.py`
- **CORSConfigDict** (6 connections) — `server/app/factory.py`
- **_get_cors_config_from_app_config()** (6 connections) — `server/app/factory.py`
- **UserRead** (6 connections) — `server/auth/endpoints.py`
- **UserUpdate** (6 connections) — `server/auth/endpoints.py`
- **security_headers.py** (6 connections) — `server/middleware/security_headers.py`
- **main()** (4 connections) — `scripts/generate_openapi_spec.py`
- **_get_default_cors_config()** (4 connections) — `server/app/factory.py`
- **_parse_cors_env_vars()** (4 connections) — `server/app/factory.py`
- **generate_openapi_spec.py** (3 connections) — `scripts/generate_openapi_spec.py`
- **_sanitize_token_examples()** (3 connections) — `scripts/generate_openapi_spec.py`
- **.__init__()** (3 connections) — `server/middleware/comprehensive_logging.py`
- **.__init__()** (3 connections) — `server/middleware/security_headers.py`
- **FastAPI** (2 connections)
- **Replace auth token examples with clearly fake placeholders.** (1 connections) — `scripts/generate_openapi_spec.py`
- **Generate and write OpenAPI spec to docs/openapi/openapi.json.** (1 connections) — `scripts/generate_openapi_spec.py`
- **Any** (1 connections)
- **TypedDict** (1 connections)
- **FastAPI application factory for MythosMUD server.  This module handles FastAPI a** (1 connections) — `server/app/factory.py`
- **Parse CORS-related environment variables and return overrides.      Environment** (1 connections) — `server/app/factory.py`
- **Configure CORS settings from config file and environment variables.      Precede** (1 connections) — `server/app/factory.py`
- *... and 13 more nodes in this community*

## Relationships

- [User](User.md) (11 shared connections)
- [get_logger](get_logger.md) (7 shared connections)
- [.__call__](__call__.md) (6 shared connections)
- [test_security_headers.py](test_security_headers.py.md) (6 shared connections)
- [lifespan.py](lifespan.py.md) (4 shared connections)
- [main.py](main.py.md) (4 shared connections)
- [error_handling_middleware.py](error_handling_middleware.py.md) (3 shared connections)
- [exceptions.py](exceptions.py.md) (2 shared connections)
- [CombatService](CombatService.md) (2 shared connections)
- [.dispatch](dispatch.md) (2 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (1 shared connections)
- [ExplorationService](ExplorationService.md) (1 shared connections)

## Source Files

- `scripts/generate_openapi_spec.py`
- `server/app/factory.py`
- `server/auth/endpoints.py`
- `server/middleware/comprehensive_logging.py`
- `server/middleware/security_headers.py`

## Audit Trail

- EXTRACTED: 144 (91%)
- INFERRED: 14 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*