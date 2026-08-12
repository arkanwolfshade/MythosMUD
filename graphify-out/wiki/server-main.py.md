# server/main.py

> 33 nodes

## Key Concepts

- **server/main.py** (15 connections) — `server/main.py`
- **create_app()** (11 connections) — `server/app/factory.py`
- **CORSConfigDict** (6 connections) — `server/app/factory.py`
- **_configure_cors()** (6 connections) — `server/app/factory.py`
- **_get_cors_config_from_app_config()** (6 connections) — `server/app/factory.py`
- **main()** (4 connections) — `scripts/generate_openapi_spec.py`
- **_get_default_cors_config()** (4 connections) — `server/app/factory.py`
- **_parse_cors_env_vars()** (4 connections) — `server/app/factory.py`
- **_create_get_app()** (4 connections) — `server/main.py`
- **main()** (4 connections) — `server/main.py`
- **test_auth()** (4 connections) — `server/main.py`
- **_sanitize_token_examples()** (3 connections) — `scripts/generate_openapi_spec.py`
- **read_root()** (3 connections) — `server/main.py`
- **generate_openapi_spec.py** (3 connections) — `scripts/generate_openapi_spec.py`
- **FastAPI** (3 connections)
- **FastAPI** (2 connections)
- **get** (2 connections)
- **Any** (1 connections)
- **TypedDict** (1 connections)
- **Any** (1 connections)
- **Replace auth token examples with clearly fake placeholders.** (1 connections) — `scripts/generate_openapi_spec.py`
- **Generate and write OpenAPI spec to docs/openapi/openapi.json.** (1 connections) — `scripts/generate_openapi_spec.py`
- **Parse CORS-related environment variables and return overrides. Environment…** (1 connections) — `server/app/factory.py`
- **Configure CORS settings from config file and environment variables. Precedence:…** (1 connections) — `server/app/factory.py`
- **Create and configure the FastAPI application. This function sets up the FastAPI…** (1 connections) — `server/app/factory.py`
- *... and 8 more nodes in this community*

## Relationships

- [lifespan.py](lifespan.py.md) (9 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [get_config](get_config.md) (2 shared connections)
- [fastapi_integration.py](fastapi_integration.py.md) (2 shared connections)
- [error_handling_middleware.py](error_handling_middleware.py.md) (1 shared connections)
- [database.py](database.py.md) (1 shared connections)

## Source Files

- `scripts/generate_openapi_spec.py`
- `server/app/factory.py`
- `server/main.py`

## Audit Trail

- EXTRACTED: 99 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*