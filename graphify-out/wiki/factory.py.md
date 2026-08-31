# factory.py

> 78 nodes

## Key Concepts

- **factory.py** (54 connections) — `server/app/factory.py`
- **create_app()** (17 connections) — `server/app/factory.py`
- **server/main.py** (17 connections) — `server/main.py`
- **SecurityHeadersMiddleware** (12 connections) — `server/middleware/security_headers.py`
- **CORSConfigDict** (7 connections) — `server/app/factory.py`
- **webhook-receiver.py** (7 connections) — `monitoring/webhook-receiver.py`
- **containers.py** (7 connections) — `server/api/containers.py`
- **_configure_cors()** (6 connections) — `server/app/factory.py`
- **_get_cors_config_from_app_config()** (6 connections) — `server/app/factory.py`
- **_parse_cors_env_vars()** (6 connections) — `server/app/factory.py`
- **test_openapi_tags.py** (6 connections) — `server/tests/unit/app/test_openapi_tags.py`
- **webhook()** (5 connections) — `monitoring/webhook-receiver.py`
- **_apply_cors_env_overrides()** (5 connections) — `server/app/factory.py`
- **.dispatch()** (5 connections) — `server/middleware/security_headers.py`
- **CORSConfigOverrides** (4 connections) — `server/app/factory.py`
- **_get_default_cors_config()** (4 connections) — `server/app/factory.py`
- **_parse_cors_origin_list()** (4 connections) — `server/app/factory.py`
- **_register_v1_routers()** (4 connections) — `server/app/factory.py`
- **_create_get_app()** (4 connections) — `server/main.py`
- **main()** (4 connections) — `server/main.py`
- **test_auth()** (4 connections) — `server/main.py`
- **._add_security_headers_to_response()** (4 connections) — `server/middleware/security_headers.py`
- **_openapi_spec()** (4 connections) — `server/tests/unit/app/test_openapi_tags.py`
- **_route_declared_tags()** (4 connections) — `server/tests/unit/app/test_openapi_tags.py`
- **UserRead** (3 connections) — `server/auth/endpoints.py`
- *... and 53 more nodes in this community*

## Relationships

- [LoggedHTTPException](LoggedHTTPException.md) (14 shared connections)
- [get_logger](get_logger.md) (12 shared connections)
- [test_security_headers.py](test_security_headers.py.md) (4 shared connections)
- [AppConfig](AppConfig.md) (4 shared connections)
- [middleware](middleware.md) (3 shared connections)
- [auth_rate_limit.py](auth_rate_limit.py.md) (3 shared connections)
- [test_auth_rate_limit.py](test_auth_rate_limit.py.md) (3 shared connections)
- [lifespan.py](lifespan.py.md) (3 shared connections)
- [get_config](get_config.md) (3 shared connections)
- [generate_openapi_spec.py](generate_openapi_spec.py.md) (2 shared connections)
- [test_error_handling_middleware.py](test_error_handling_middleware.py.md) (2 shared connections)
- [ComprehensiveLoggingMiddleware](ComprehensiveLoggingMiddleware.md) (2 shared connections)

## Source Files

- `.claude/rules/uvicorn.md`
- `monitoring/webhook-receiver.py`
- `server/api/containers.py`
- `server/app/factory.py`
- `server/auth/endpoints.py`
- `server/main.py`
- `server/middleware/security_headers.py`
- `server/tests/unit/app/test_openapi_tags.py`
- `server/tests/unit/middleware/test_auth_rate_limit.py`

## Audit Trail

- EXTRACTED: 172 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*