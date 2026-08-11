# Plan Cursor Plans

> 29 nodes

## Key Concepts

- **create_app()** (16 connections) — `server/app/factory.py`
- **CORSConfigDict** (6 connections) — `server/app/factory.py`
- **_get_cors_config_from_app_config()** (6 connections) — `server/app/factory.py`
- **_configure_cors()** (6 connections) — `server/app/factory.py`
- **UserRead** (6 connections) — `server/auth/endpoints.py`
- **UserUpdate** (6 connections) — `server/auth/endpoints.py`
- **main()** (4 connections) — `scripts/generate_openapi_spec.py`
- **_get_default_cors_config()** (4 connections) — `server/app/factory.py`
- **_parse_cors_env_vars()** (4 connections) — `server/app/factory.py`
- **main()** (4 connections) — `server/main.py`
- **_create_get_app()** (4 connections) — `server/main.py`
- **generate_openapi_spec.py** (3 connections) — `scripts/generate_openapi_spec.py`
- **_sanitize_token_examples()** (3 connections) — `scripts/generate_openapi_spec.py`
- **FastAPI** (3 connections)
- **FastAPI** (2 connections)
- **Replace auth token examples with clearly fake placeholders.** (1 connections) — `scripts/generate_openapi_spec.py`
- **Generate and write OpenAPI spec to docs/openapi/openapi.json.** (1 connections) — `scripts/generate_openapi_spec.py`
- **TypedDict** (1 connections)
- **Any** (1 connections)
- **Type definition for CORS configuration dictionary.** (1 connections) — `server/app/factory.py`
- **Get default CORS configuration values.      Returns:         CORSConfigDict: Dic** (1 connections) — `server/app/factory.py`
- **Get CORS configuration from AppConfig, with fallback to defaults.      Returns:** (1 connections) — `server/app/factory.py`
- **Parse CORS-related environment variables and return overrides.      Environment** (1 connections) — `server/app/factory.py`
- **Configure CORS settings from config file and environment variables.      Precede** (1 connections) — `server/app/factory.py`
- **Create and configure the FastAPI application.      This function sets up the Fas** (1 connections) — `server/app/factory.py`
- *... and 4 more nodes in this community*

## Relationships

- [Room Occupancy Class](Room_Occupancy_Class.md) (14 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (3 shared connections)
- [Who Command Helpers](Who_Command_Helpers.md) (2 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (2 shared connections)
- [Command Parser](Command_Parser.md) (1 shared connections)
- [Docker PostgreSQL Typo Bug](Docker_PostgreSQL_Typo_Bug.md) (1 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (1 shared connections)
- [Graceful Degradation Plan](Graceful_Degradation_Plan.md) (1 shared connections)

## Source Files

- `scripts/generate_openapi_spec.py`
- `server/app/factory.py`
- `server/auth/endpoints.py`
- `server/main.py`

## Audit Trail

- EXTRACTED: 79 (87%)
- INFERRED: 12 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*