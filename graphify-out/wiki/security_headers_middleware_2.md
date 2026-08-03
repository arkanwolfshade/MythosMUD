# security headers middleware

> 53 nodes

## Key Concepts

- **test_security_headers.py** (20 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **SecurityHeadersMiddleware** (13 connections) — `server/middleware/security_headers.py`
- **MutableHeaders** (6 connections)
- **.__call__()** (5 connections) — `server/middleware/security_headers.py`
- **.dispatch()** (5 connections) — `server/middleware/security_headers.py`
- **._add_security_headers_to_response()** (4 connections) — `server/middleware/security_headers.py`
- **.__init__()** (3 connections) — `server/middleware/security_headers.py`
- **._add_security_headers()** (3 connections) — `server/middleware/security_headers.py`
- **test_security_headers_middleware_init()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_security_headers_middleware_init_with_env_vars()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_security_headers_middleware_non_http_scope()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_security_headers_middleware_adds_headers()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_security_headers_middleware_error_handling()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_add_security_headers()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_add_security_headers_hsts_value()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_add_security_headers_permissions_policy()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_add_security_headers_csp_policy()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_add_security_headers_referrer_policy()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Any** (2 connections)
- **mock_app()** (2 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_add_security_headers_to_response()** (2 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_add_security_headers_to_response_hsts_with_subdomains()** (2 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_add_security_headers_to_response_hsts_without_subdomains()** (2 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_dispatch_method()** (2 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_dispatch_method_error_handling()** (2 connections) — `server/tests/unit/middleware/test_security_headers.py`
- *... and 28 more nodes in this community*

## Relationships

- [app factory rationale](app_factory_rationale.md) (5 shared connections)
- [player service game](player_service_game.md) (2 shared connections)
- [models npc rationale](models_npc_rationale.md) (2 shared connections)

## Source Files

- `server/middleware/security_headers.py`
- `server/tests/unit/middleware/test_security_headers.py`

## Audit Trail

- EXTRACTED: 120 (92%)
- INFERRED: 11 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*