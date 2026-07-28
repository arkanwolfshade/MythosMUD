# Server Middleware

> 62 nodes

## Key Concepts

- **factory.py** (37 connections) — `server/app/factory.py`
- **create_app()** (16 connections) — `server/app/factory.py`
- **SecurityHeadersMiddleware** (13 connections) — `server/middleware/security_headers.py`
- **ComprehensiveLoggingMiddleware** (10 connections) — `server/middleware/comprehensive_logging.py`
- **.__call__()** (8 connections) — `server/middleware/comprehensive_logging.py`
- **.dispatch()** (7 connections) — `server/middleware/comprehensive_logging.py`
- **CORSConfigDict** (6 connections) — `server/app/factory.py`
- **_get_cors_config_from_app_config()** (6 connections) — `server/app/factory.py`
- **_configure_cors()** (6 connections) — `server/app/factory.py`
- **UserRead** (6 connections) — `server/auth/endpoints.py`
- **UserUpdate** (6 connections) — `server/auth/endpoints.py`
- **._log_request_start()** (5 connections) — `server/middleware/comprehensive_logging.py`
- **._log_request_success_with_status()** (5 connections) — `server/middleware/comprehensive_logging.py`
- **._log_request_error()** (5 connections) — `server/middleware/comprehensive_logging.py`
- **.__call__()** (5 connections) — `server/middleware/security_headers.py`
- **.dispatch()** (5 connections) — `server/middleware/security_headers.py`
- **main()** (4 connections) — `scripts/generate_openapi_spec.py`
- **_get_default_cors_config()** (4 connections) — `server/app/factory.py`
- **_parse_cors_env_vars()** (4 connections) — `server/app/factory.py`
- **Request** (4 connections)
- **._add_security_headers_to_response()** (4 connections) — `server/middleware/security_headers.py`
- **generate_openapi_spec.py** (3 connections) — `scripts/generate_openapi_spec.py`
- **_sanitize_token_examples()** (3 connections) — `scripts/generate_openapi_spec.py`
- **.__init__()** (3 connections) — `server/middleware/comprehensive_logging.py`
- **.__init__()** (3 connections) — `server/middleware/security_headers.py`
- *... and 37 more nodes in this community*

## Relationships

- [Server Admin](Server_Admin.md) (8 shared connections)
- [Server Commands](Server_Commands.md) (6 shared connections)
- [Server Middleware (3)](Server_Middleware_%283%29.md) (5 shared connections)
- [Server Middleware (4)](Server_Middleware_%284%29.md) (4 shared connections)
- [Server Monitoring](Server_Monitoring.md) (3 shared connections)
- [Server Middleware (2)](Server_Middleware_%282%29.md) (3 shared connections)
- [Server Api (5)](Server_Api_%285%29.md) (2 shared connections)
- [Server Auth (2)](Server_Auth_%282%29.md) (2 shared connections)
- [Server Config (2)](Server_Config_%282%29.md) (2 shared connections)
- [Server Auth](Server_Auth.md) (2 shared connections)
- [Server Api (2)](Server_Api_%282%29.md) (1 shared connections)
- [Server Infrastructure](Server_Infrastructure.md) (1 shared connections)

## Source Files

- `scripts/generate_openapi_spec.py`
- `server/app/factory.py`
- `server/auth/endpoints.py`
- `server/middleware/comprehensive_logging.py`
- `server/middleware/security_headers.py`

## Audit Trail

- EXTRACTED: 203 (94%)
- INFERRED: 14 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*