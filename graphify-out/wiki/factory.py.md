# factory.py

> 50 nodes

## Key Concepts

- **factory.py** (55 connections) — `server/app/factory.py`
- **server/main.py** (19 connections) — `server/main.py`
- **create_app()** (17 connections) — `server/app/factory.py`
- **CORSConfigDict** (7 connections) — `server/app/factory.py`
- **_configure_cors()** (6 connections) — `server/app/factory.py`
- **_get_cors_config_from_app_config()** (6 connections) — `server/app/factory.py`
- **_parse_cors_env_vars()** (6 connections) — `server/app/factory.py`
- **test_auth()** (6 connections) — `server/main.py`
- **test_openapi_tags.py** (6 connections) — `server/tests/unit/app/test_openapi_tags.py`
- **_apply_cors_env_overrides()** (5 connections) — `server/app/factory.py`
- **CORSConfigOverrides** (4 connections) — `server/app/factory.py`
- **_get_default_cors_config()** (4 connections) — `server/app/factory.py`
- **_parse_cors_origin_list()** (4 connections) — `server/app/factory.py`
- **_register_v1_routers()** (4 connections) — `server/app/factory.py`
- **_create_get_app()** (4 connections) — `server/main.py`
- **main()** (4 connections) — `server/main.py`
- **_openapi_spec()** (4 connections) — `server/tests/unit/app/test_openapi_tags.py`
- **_route_declared_tags()** (4 connections) — `server/tests/unit/app/test_openapi_tags.py`
- **UserRead** (3 connections) — `server/auth/endpoints.py`
- **_first_set_env()** (3 connections) — `server/app/factory.py`
- **_try_json_str_list()** (3 connections) — `server/app/factory.py`
- **read_root()** (3 connections) — `server/main.py`
- **FastAPI** (3 connections)
- **FastAPI** (3 connections)
- **test_openapi_tags_matches_route_declared_tags()** (2 connections) — `server/tests/unit/app/test_openapi_tags.py`
- *... and 25 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (8 shared connections)
- [User](User.md) (6 shared connections)
- [test_auth_rate_limit.py](test_auth_rate_limit.py.md) (6 shared connections)
- [test_error_handling_middleware.py](test_error_handling_middleware.py.md) (3 shared connections)
- [lifespan.py](lifespan.py.md) (3 shared connections)
- [get_config](get_config.md) (3 shared connections)
- [generate_openapi_spec.py](generate_openapi_spec.py.md) (2 shared connections)
- [register_user](register_user.md) (2 shared connections)
- [system_monitoring.py](system_monitoring.py.md) (2 shared connections)
- [AppConfig](AppConfig.md) (2 shared connections)
- [middleware](middleware.md) (2 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (1 shared connections)

## Source Files

- `server/app/factory.py`
- `server/auth/endpoints.py`
- `server/main.py`
- `server/tests/unit/app/test_openapi_tags.py`

## Audit Trail

- EXTRACTED: 135 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*