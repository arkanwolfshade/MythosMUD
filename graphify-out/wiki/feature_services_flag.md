# feature services flag

> 40 nodes

## Key Concepts

- **main.py** (15 connections) — `server/main.py`
- **create_app()** (14 connections) — `server/app/factory.py`
- **CORSConfigDict** (7 connections) — `server/app/factory.py`
- **_get_cors_config_from_app_config()** (6 connections) — `server/app/factory.py`
- **_parse_cors_env_vars()** (6 connections) — `server/app/factory.py`
- **_configure_cors()** (6 connections) — `server/app/factory.py`
- **_apply_cors_env_overrides()** (5 connections) — `server/app/factory.py`
- **main()** (4 connections) — `scripts/generate_openapi_spec.py`
- **CORSConfigOverrides** (4 connections) — `server/app/factory.py`
- **_get_default_cors_config()** (4 connections) — `server/app/factory.py`
- **_parse_cors_origin_list()** (4 connections) — `server/app/factory.py`
- **main()** (4 connections) — `server/main.py`
- **_create_get_app()** (4 connections) — `server/main.py`
- **generate_openapi_spec.py** (3 connections) — `scripts/generate_openapi_spec.py`
- **_sanitize_token_examples()** (3 connections) — `scripts/generate_openapi_spec.py`
- **_first_set_env()** (3 connections) — `server/app/factory.py`
- **_try_json_str_list()** (3 connections) — `server/app/factory.py`
- **FastAPI** (3 connections)
- **test_auth()** (3 connections) — `server/main.py`
- **TypedDict** (2 connections)
- **read_root()** (2 connections) — `server/main.py`
- **Replace auth token examples with clearly fake placeholders.** (1 connections) — `scripts/generate_openapi_spec.py`
- **Generate and write OpenAPI spec to docs/openapi/openapi.json.** (1 connections) — `scripts/generate_openapi_spec.py`
- **Type definition for CORS configuration dictionary.** (1 connections) — `server/app/factory.py`
- **Partial CORS overrides from environment variables.** (1 connections) — `server/app/factory.py`
- *... and 15 more nodes in this community*

## Relationships

- [player requests schemas](player_requests_schemas.md) (14 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (3 shared connections)
- [circuit breaker realtime](circuit_breaker_realtime.md) (2 shared connections)
- [app factory rationale](app_factory_rationale.md) (2 shared connections)
- [aggro threat services](aggro_threat_services.md) (1 shared connections)
- [middleware comprehensive logging](middleware_comprehensive_logging.md) (1 shared connections)
- [middleware error handling](middleware_error_handling.md) (1 shared connections)
- [security headers middleware](security_headers_middleware.md) (1 shared connections)
- [websocket handler realtime](websocket_handler_realtime.md) (1 shared connections)

## Source Files

- `scripts/generate_openapi_spec.py`
- `server/app/factory.py`
- `server/main.py`

## Audit Trail

- EXTRACTED: 121 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*