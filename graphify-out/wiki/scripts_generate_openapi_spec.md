# scripts generate openapi spec

> 50 nodes

## Key Concepts

- **factory.py** (49 connections) — `server/app/factory.py`
- **server/main.py** (17 connections) — `server/main.py`
- **create_app()** (12 connections) — `server/app/factory.py`
- **CORSConfigDict** (7 connections) — `server/app/factory.py`
- **_configure_cors()** (6 connections) — `server/app/factory.py`
- **_get_cors_config_from_app_config()** (6 connections) — `server/app/factory.py`
- **_parse_cors_env_vars()** (6 connections) — `server/app/factory.py`
- **_apply_cors_env_overrides()** (5 connections) — `server/app/factory.py`
- **CORSConfigOverrides** (4 connections) — `server/app/factory.py`
- **main()** (4 connections) — `scripts/generate_openapi_spec.py`
- **_get_default_cors_config()** (4 connections) — `server/app/factory.py`
- **_parse_cors_origin_list()** (4 connections) — `server/app/factory.py`
- **_register_v1_routers()** (4 connections) — `server/app/factory.py`
- **_create_get_app()** (4 connections) — `server/main.py`
- **main()** (4 connections) — `server/main.py`
- **test_auth()** (4 connections) — `server/main.py`
- **UserRead** (3 connections) — `server/auth/endpoints.py`
- **UserUpdate** (3 connections) — `server/auth/endpoints.py`
- **_sanitize_token_examples()** (3 connections) — `scripts/generate_openapi_spec.py`
- **_first_set_env()** (3 connections) — `server/app/factory.py`
- **_try_json_str_list()** (3 connections) — `server/app/factory.py`
- **read_root()** (3 connections) — `server/main.py`
- **generate_openapi_spec.py** (3 connections) — `scripts/generate_openapi_spec.py`
- **FastAPI** (3 connections)
- **FastAPI** (3 connections)
- *... and 25 more nodes in this community*

## Relationships

- [claude rules fastapi](claude_rules_fastapi.md) (9 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (8 shared connections)
- [characterinfo](characterinfo.md) (4 shared connections)
- [server middleware error handling middleware](server_middleware_error_handling_middleware.md) (3 shared connections)
- [server app lifespan](server_app_lifespan.md) (3 shared connections)
- [server app game tick counter](server_app_game_tick_counter.md) (3 shared connections)
- [server config init create config](server_config_init_create_config.md) (2 shared connections)
- [server middleware comprehensive logging](server_middleware_comprehensive_logging.md) (2 shared connections)
- [server middleware correlation middleware](server_middleware_correlation_middleware.md) (2 shared connections)
- [mutableheaders](mutableheaders.md) (1 shared connections)
- [maprooms](maprooms.md) (1 shared connections)
- [server api metrics](server_api_metrics.md) (1 shared connections)

## Source Files

- `scripts/generate_openapi_spec.py`
- `server/app/factory.py`
- `server/auth/endpoints.py`
- `server/main.py`

## Audit Trail

- EXTRACTED: 119 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*