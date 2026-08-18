# scripts generate openapi spec

> 23 nodes

## Key Concepts

- **server/main.py** (17 connections) — `server/main.py`
- **create_app()** (12 connections) — `server/app/factory.py`
- **main()** (4 connections) — `scripts/generate_openapi_spec.py`
- **_register_v1_routers()** (4 connections) — `server/app/factory.py`
- **_create_get_app()** (4 connections) — `server/main.py`
- **main()** (4 connections) — `server/main.py`
- **test_auth()** (4 connections) — `server/main.py`
- **_sanitize_token_examples()** (3 connections) — `scripts/generate_openapi_spec.py`
- **read_root()** (3 connections) — `server/main.py`
- **generate_openapi_spec.py** (3 connections) — `scripts/generate_openapi_spec.py`
- **FastAPI** (3 connections)
- **FastAPI** (3 connections)
- **get** (2 connections)
- **Any** (1 connections)
- **Replace auth token examples with clearly fake placeholders.** (1 connections) — `scripts/generate_openapi_spec.py`
- **Generate and write OpenAPI spec to docs/openapi/openapi.json.** (1 connections) — `scripts/generate_openapi_spec.py`
- **Mount all versioned API routers under /v1.** (1 connections) — `server/app/factory.py`
- **Create and configure the FastAPI application. This function sets up the FastAPI…** (1 connections) — `server/app/factory.py`
- **MythosMUD Server - Main Application Entry Point This module serves as the…** (1 connections) — `server/main.py`
- **Root endpoint providing basic server information.** (1 connections) — `server/main.py`
- **Test endpoint to verify JWT authentication is working.** (1 connections) — `server/main.py`
- **Main entry point for the MythosMUD server.** (1 connections) — `server/main.py`
- **Factory function that creates the get_app function with encapsulated cache.…** (1 connections) — `server/main.py`

## Relationships

- [claude rules fastapi](claude_rules_fastapi.md) (6 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (3 shared connections)
- [server config init](server_config_init.md) (2 shared connections)
- [server middleware correlation middleware](server_middleware_correlation_middleware.md) (2 shared connections)
- [server middleware error handling middleware](server_middleware_error_handling_middleware.md) (1 shared connections)
- [server app lifespan](server_app_lifespan.md) (1 shared connections)
- [claude rules uvicorn](claude_rules_uvicorn.md) (1 shared connections)

## Source Files

- `scripts/generate_openapi_spec.py`
- `server/app/factory.py`
- `server/main.py`

## Audit Trail

- EXTRACTED: 45 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*