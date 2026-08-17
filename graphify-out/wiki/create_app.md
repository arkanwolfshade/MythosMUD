# create_app

> 15 nodes

## Key Concepts

- **create_app()** (12 connections) — `server/app/factory.py`
- **main()** (4 connections) — `scripts/generate_openapi_spec.py`
- **_register_v1_routers()** (4 connections) — `server/app/factory.py`
- **_create_get_app()** (4 connections) — `server/main.py`
- **main()** (4 connections) — `server/main.py`
- **_sanitize_token_examples()** (3 connections) — `scripts/generate_openapi_spec.py`
- **generate_openapi_spec.py** (3 connections) — `scripts/generate_openapi_spec.py`
- **FastAPI** (3 connections)
- **FastAPI** (3 connections)
- **Replace auth token examples with clearly fake placeholders.** (1 connections) — `scripts/generate_openapi_spec.py`
- **Generate and write OpenAPI spec to docs/openapi/openapi.json.** (1 connections) — `scripts/generate_openapi_spec.py`
- **Mount all versioned API routers under /v1.** (1 connections) — `server/app/factory.py`
- **Create and configure the FastAPI application. This function sets up the FastAPI…** (1 connections) — `server/app/factory.py`
- **Main entry point for the MythosMUD server.** (1 connections) — `server/main.py`
- **Factory function that creates the get_app function with encapsulated cache.…** (1 connections) — `server/main.py`

## Relationships

- [get_logger](get_logger.md) (8 shared connections)
- [test_error_handling_middleware.py](test_error_handling_middleware.py.md) (1 shared connections)
- [test_lifespan_helpers.py](test_lifespan_helpers.py.md) (1 shared connections)

## Source Files

- `scripts/generate_openapi_spec.py`
- `server/app/factory.py`
- `server/main.py`

## Audit Trail

- EXTRACTED: 27 (96%)
- INFERRED: 1 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*