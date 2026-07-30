# init

> 26 nodes

## Key Concepts

- **factory.py** (37 connections) — `server/app/factory.py`
- **create_app()** (16 connections) — `server/app/factory.py`
- **CORSConfigDict** (6 connections) — `server/app/factory.py`
- **_get_cors_config_from_app_config()** (6 connections) — `server/app/factory.py`
- **_configure_cors()** (6 connections) — `server/app/factory.py`
- **UserRead** (6 connections) — `server/auth/endpoints.py`
- **UserUpdate** (6 connections) — `server/auth/endpoints.py`
- **main()** (4 connections) — `scripts/generate_openapi_spec.py`
- **_get_default_cors_config()** (4 connections) — `server/app/factory.py`
- **_parse_cors_env_vars()** (4 connections) — `server/app/factory.py`
- **generate_openapi_spec.py** (3 connections) — `scripts/generate_openapi_spec.py`
- **_sanitize_token_examples()** (3 connections) — `scripts/generate_openapi_spec.py`
- **FastAPI** (2 connections)
- **Replace auth token examples with clearly fake placeholders.** (1 connections) — `scripts/generate_openapi_spec.py`
- **Generate and write OpenAPI spec to docs/openapi/openapi.json.** (1 connections) — `scripts/generate_openapi_spec.py`
- **TypedDict** (1 connections)
- **Any** (1 connections)
- **FastAPI application factory for MythosMUD server.  This module handles FastAPI a** (1 connections) — `server/app/factory.py`
- **Type definition for CORS configuration dictionary.** (1 connections) — `server/app/factory.py`
- **Get default CORS configuration values.      Returns:         CORSConfigDict: Dic** (1 connections) — `server/app/factory.py`
- **Get CORS configuration from AppConfig, with fallback to defaults.      Returns:** (1 connections) — `server/app/factory.py`
- **Parse CORS-related environment variables and return overrides.      Environment** (1 connections) — `server/app/factory.py`
- **Configure CORS settings from config file and environment variables.      Precede** (1 connections) — `server/app/factory.py`
- **Create and configure the FastAPI application.      This function sets up the Fas** (1 connections) — `server/app/factory.py`
- **Schema for user read operations.** (1 connections) — `server/auth/endpoints.py`
- *... and 1 more nodes in this community*

## Relationships

- [Connection Manager](Connection_Manager.md) (7 shared connections)
- [close db()](close_db%28%29.md) (4 shared connections)
- [Tests for get container dependency](Tests_for_get_container_dependency.md) (4 shared connections)
- [.shutdown()](shutdown%28%29.md) (3 shared connections)
- [CombatDPSync](CombatDPSync.md) (3 shared connections)
- [Response](Response.md) (3 shared connections)
- [Remove sensitive data from log](Remove_sensitive_data_from_log.md) (3 shared connections)
- [world](world.md) (2 shared connections)
- [equipment helpers](equipment_helpers.md) (2 shared connections)
- [APIRouter](APIRouter.md) (1 shared connections)
- [AsyncSessionFactory](AsyncSessionFactory.md) (1 shared connections)
- [ExitStack](ExitStack.md) (1 shared connections)

## Source Files

- `scripts/generate_openapi_spec.py`
- `server/app/factory.py`
- `server/auth/endpoints.py`

## Audit Trail

- EXTRACTED: 104 (90%)
- INFERRED: 12 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*