# factory.py

> 98 nodes

## Key Concepts

- **factory.py** (55 connections) — `server/app/factory.py`
- **server/main.py** (19 connections) — `server/main.py`
- **create_app()** (17 connections) — `server/app/factory.py`
- **ComprehensiveLoggingMiddleware** (16 connections) — `server/middleware/comprehensive_logging.py`
- **test_comprehensive_logging.py** (9 connections) — `server/tests/unit/middleware/test_comprehensive_logging.py`
- **.__call__()** (8 connections) — `server/middleware/comprehensive_logging.py`
- **CORSConfigDict** (7 connections) — `server/app/factory.py`
- **.dispatch()** (7 connections) — `server/middleware/comprehensive_logging.py`
- **generate_openapi_spec.py** (7 connections) — `scripts/generate_openapi_spec.py`
- **comprehensive_logging.py** (7 connections) — `server/middleware/comprehensive_logging.py`
- **UserUpdate** (6 connections) — `server/auth/endpoints.py`
- **_configure_cors()** (6 connections) — `server/app/factory.py`
- **_get_cors_config_from_app_config()** (6 connections) — `server/app/factory.py`
- **_parse_cors_env_vars()** (6 connections) — `server/app/factory.py`
- **test_auth()** (6 connections) — `server/main.py`
- **test_openapi_tags.py** (6 connections) — `server/tests/unit/app/test_openapi_tags.py`
- **main()** (5 connections) — `scripts/generate_openapi_spec.py`
- **_render_tag_table()** (5 connections) — `scripts/generate_openapi_spec.py`
- **_apply_cors_env_overrides()** (5 connections) — `server/app/factory.py`
- **._log_request_error()** (5 connections) — `server/middleware/comprehensive_logging.py`
- **._log_request_start()** (5 connections) — `server/middleware/comprehensive_logging.py`
- **._log_request_success_with_status()** (5 connections) — `server/middleware/comprehensive_logging.py`
- **asyncio** (5 connections)
- **CORSConfigOverrides** (4 connections) — `server/app/factory.py`
- **_update_tag_table_doc()** (4 connections) — `scripts/generate_openapi_spec.py`
- *... and 73 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (9 shared connections)
- [test_security_headers.py](test_security_headers.py.md) (7 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (6 shared connections)
- [get_config](get_config.md) (5 shared connections)
- [User](User.md) (4 shared connections)
- [test_error_handling_middleware.py](test_error_handling_middleware.py.md) (3 shared connections)
- [auth_rate_limit.py](auth_rate_limit.py.md) (3 shared connections)
- [test_auth_rate_limit.py](test_auth_rate_limit.py.md) (3 shared connections)
- [lifespan.py](lifespan.py.md) (3 shared connections)
- [CORSConfig](CORSConfig.md) (2 shared connections)
- [system_monitoring.py](system_monitoring.py.md) (2 shared connections)
- [players.py](players.py.md) (2 shared connections)

## Source Files

- `scripts/generate_openapi_spec.py`
- `server/app/factory.py`
- `server/auth/endpoints.py`
- `server/main.py`
- `server/middleware/comprehensive_logging.py`
- `server/realtime/envelope.py`
- `server/tests/unit/app/test_openapi_tags.py`
- `server/tests/unit/middleware/test_auth_rate_limit.py`
- `server/tests/unit/middleware/test_comprehensive_logging.py`

## Audit Trail

- EXTRACTED: 206 (95%)
- INFERRED: 11 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*