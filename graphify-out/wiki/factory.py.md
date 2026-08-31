# factory.py

> 39 nodes

## Key Concepts

- **factory.py** (54 connections) — `server/app/factory.py`
- **create_app()** (17 connections) — `server/app/factory.py`
- **CORSConfigDict** (7 connections) — `server/app/factory.py`
- **_configure_cors()** (6 connections) — `server/app/factory.py`
- **_get_cors_config_from_app_config()** (6 connections) — `server/app/factory.py`
- **_parse_cors_env_vars()** (6 connections) — `server/app/factory.py`
- **test_openapi_tags.py** (6 connections) — `server/tests/unit/app/test_openapi_tags.py`
- **_apply_cors_env_overrides()** (5 connections) — `server/app/factory.py`
- **CORSConfigOverrides** (4 connections) — `server/app/factory.py`
- **_get_default_cors_config()** (4 connections) — `server/app/factory.py`
- **_parse_cors_origin_list()** (4 connections) — `server/app/factory.py`
- **_register_v1_routers()** (4 connections) — `server/app/factory.py`
- **_openapi_spec()** (4 connections) — `server/tests/unit/app/test_openapi_tags.py`
- **_route_declared_tags()** (4 connections) — `server/tests/unit/app/test_openapi_tags.py`
- **UserRead** (3 connections) — `server/auth/endpoints.py`
- **UserUpdate** (3 connections) — `server/auth/endpoints.py`
- **_first_set_env()** (3 connections) — `server/app/factory.py`
- **_try_json_str_list()** (3 connections) — `server/app/factory.py`
- **FastAPI** (3 connections)
- **test_openapi_tags_matches_route_declared_tags()** (2 connections) — `server/tests/unit/app/test_openapi_tags.py`
- **TypedDict** (2 connections)
- **FastAPI application factory for MythosMUD server. This module handles FastAPI…** (1 connections) — `server/app/factory.py`
- **Get CORS configuration from AppConfig, with fallback to defaults. Returns:…** (1 connections) — `server/app/factory.py`
- **Return the first non-empty environment value among keys.** (1 connections) — `server/app/factory.py`
- **Parse candidate as a JSON string list, or None on failure.** (1 connections) — `server/app/factory.py`
- *... and 14 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (8 shared connections)
- [test_auth_rate_limit.py](test_auth_rate_limit.py.md) (6 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (4 shared connections)
- [server/main.py](server-main.py.md) (4 shared connections)
- [error_handling_middleware.py](error_handling_middleware.py.md) (3 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (3 shared connections)
- [PlayerService](PlayerService.md) (3 shared connections)
- [generate_openapi_spec.py](generate_openapi_spec.py.md) (2 shared connections)
- [CORSConfig](CORSConfig.md) (2 shared connections)
- [pytest.md](pytest.md.md) (2 shared connections)
- [AuthRateLimitMiddleware](AuthRateLimitMiddleware.md) (1 shared connections)
- [ComprehensiveLoggingMiddleware](ComprehensiveLoggingMiddleware.md) (1 shared connections)

## Source Files

- `server/app/factory.py`
- `server/auth/endpoints.py`
- `server/tests/unit/app/test_openapi_tags.py`

## Audit Trail

- EXTRACTED: 108 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*