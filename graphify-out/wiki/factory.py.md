# factory.py

> 73 nodes

## Key Concepts

- **factory.py** (54 connections) — `server/app/factory.py`
- **server/main.py** (19 connections) — `server/main.py`
- **create_app()** (17 connections) — `server/app/factory.py`
- **server/api/__init__.py** (11 connections) — `server/api/__init__.py`
- **CORSConfigDict** (7 connections) — `server/app/factory.py`
- **generate_openapi_spec.py** (7 connections) — `scripts/generate_openapi_spec.py`
- **containers.py** (7 connections) — `server/api/containers.py`
- **_configure_cors()** (6 connections) — `server/app/factory.py`
- **_get_cors_config_from_app_config()** (6 connections) — `server/app/factory.py`
- **_parse_cors_env_vars()** (6 connections) — `server/app/factory.py`
- **test_auth()** (6 connections) — `server/main.py`
- **api/admin/__init__.py** (6 connections) — `server/api/admin/__init__.py`
- **test_openapi_tags.py** (6 connections) — `server/tests/unit/app/test_openapi_tags.py`
- **main()** (5 connections) — `scripts/generate_openapi_spec.py`
- **_render_tag_table()** (5 connections) — `scripts/generate_openapi_spec.py`
- **_apply_cors_env_overrides()** (5 connections) — `server/app/factory.py`
- **CORSConfigOverrides** (4 connections) — `server/app/factory.py`
- **_update_tag_table_doc()** (4 connections) — `scripts/generate_openapi_spec.py`
- **_get_default_cors_config()** (4 connections) — `server/app/factory.py`
- **_parse_cors_origin_list()** (4 connections) — `server/app/factory.py`
- **_register_v1_routers()** (4 connections) — `server/app/factory.py`
- **_create_get_app()** (4 connections) — `server/main.py`
- **main()** (4 connections) — `server/main.py`
- **_openapi_spec()** (4 connections) — `server/tests/unit/app/test_openapi_tags.py`
- **_route_declared_tags()** (4 connections) — `server/tests/unit/app/test_openapi_tags.py`
- *... and 48 more nodes in this community*

## Relationships

- [User](User.md) (12 shared connections)
- [get_logger](get_logger.md) (7 shared connections)
- [get_config](get_config.md) (5 shared connections)
- [test_error_handling_middleware.py](test_error_handling_middleware.py.md) (3 shared connections)
- [auth_rate_limit.py](auth_rate_limit.py.md) (3 shared connections)
- [test_auth_rate_limit.py](test_auth_rate_limit.py.md) (3 shared connections)
- [lifespan.py](lifespan.py.md) (3 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (3 shared connections)
- [api/monitoring.py](api-monitoring.py.md) (2 shared connections)
- [api/player_respawn.py](api-player_respawn.py.md) (2 shared connections)
- [real_time.py](real_time.py.md) (2 shared connections)
- [pydantic.md](pydantic.md.md) (2 shared connections)

## Source Files

- `scripts/generate_openapi_spec.py`
- `server/api/__init__.py`
- `server/api/admin/__init__.py`
- `server/api/containers.py`
- `server/app/factory.py`
- `server/auth/endpoints.py`
- `server/main.py`
- `server/tests/unit/app/test_openapi_tags.py`
- `server/tests/unit/middleware/test_auth_rate_limit.py`

## Audit Trail

- EXTRACTED: 173 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*