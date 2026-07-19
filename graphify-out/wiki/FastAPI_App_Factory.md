# FastAPI App Factory

> 77 nodes · cohesion 0.03

## Key Concepts

- **factory.py** (36 connections) — `server/app/factory.py`
- **main.py** (15 connections) — `server/main.py`
- **SecurityHeadersMiddleware** (12 connections) — `server/middleware/security_headers.py`
- **create_app()** (10 connections) — `server/app/factory.py`
- **ComprehensiveLoggingMiddleware** (9 connections) — `server/middleware/comprehensive_logging.py`
- **.__call__()** (8 connections) — `server/middleware/comprehensive_logging.py`
- **.dispatch()** (7 connections) — `server/middleware/comprehensive_logging.py`
- **_configure_cors()** (6 connections) — `server/app/factory.py`
- **CORSConfigDict** (6 connections) — `server/app/factory.py`
- **_get_cors_config_from_app_config()** (6 connections) — `server/app/factory.py`
- **CorrelationMiddleware** (6 connections) — `server/middleware/correlation_middleware.py`
- **._log_request_error()** (5 connections) — `server/middleware/comprehensive_logging.py`
- **._log_request_start()** (5 connections) — `server/middleware/comprehensive_logging.py`
- **._log_request_success_with_status()** (5 connections) — `server/middleware/comprehensive_logging.py`
- **.__call__()** (5 connections) — `server/middleware/security_headers.py`
- **.dispatch()** (5 connections) — `server/middleware/security_headers.py`
- **_get_default_cors_config()** (4 connections) — `server/app/factory.py`
- **_parse_cors_env_vars()** (4 connections) — `server/app/factory.py`
- **create_correlation_middleware()** (4 connections) — `server/middleware/correlation_middleware.py`
- **._add_security_headers_to_response()** (4 connections) — `server/middleware/security_headers.py`
- **main()** (4 connections) — `scripts/generate_openapi_spec.py`
- **_create_get_app()** (4 connections) — `server/main.py`
- **main()** (4 connections) — `server/main.py`
- **Request** (4 connections) — `server/middleware/comprehensive_logging.py`
- **.__init__()** (3 connections) — `server/middleware/comprehensive_logging.py`
- *... and 52 more nodes in this community*

## Relationships

- [[NPC Admin API]] (22 shared connections)
- [[Security Headers Middleware]] (5 shared connections)
- [[Argon2 Password Hashing]] (4 shared connections)
- [[Error Handling Middleware]] (3 shared connections)
- [[App Lifespan Management]] (2 shared connections)
- [[Logging Correct Patterns]] (2 shared connections)
- [[NATS Metrics API]] (1 shared connections)
- [[Monitoring API Endpoints]] (1 shared connections)
- [[Players API Endpoints]] (1 shared connections)
- [[Realtime WebSocket Auth]] (1 shared connections)
- [[System Monitoring API]] (1 shared connections)
- [[Alias Expansion Logic]] (1 shared connections)

## Source Files

- `scripts/generate_openapi_spec.py`
- `server/app/factory.py`
- `server/main.py`
- `server/middleware/comprehensive_logging.py`
- `server/middleware/correlation_middleware.py`
- `server/middleware/security_headers.py`

## Audit Trail

- EXTRACTED: 249 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
