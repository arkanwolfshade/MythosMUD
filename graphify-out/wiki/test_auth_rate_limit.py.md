# test_auth_rate_limit.py

> 34 nodes

## Key Concepts

- **test_auth_rate_limit.py** (25 connections) — `server/tests/unit/middleware/test_auth_rate_limit.py`
- **auth_rate_limit.py** (19 connections) — `server/middleware/auth_rate_limit.py`
- **auth_client_key()** (11 connections) — `server/middleware/auth_rate_limit.py`
- **auth_rate_limit_response()** (11 connections) — `server/middleware/auth_rate_limit.py`
- **assert_auth_rate_limit_paths_registered()** (9 connections) — `server/middleware/auth_rate_limit.py`
- **_post_request()** (9 connections) — `server/tests/unit/middleware/test_auth_rate_limit.py`
- **is_auth_rate_limited_path()** (5 connections) — `server/middleware/auth_rate_limit.py`
- **test_auth_client_key_rejects_non_ip_xff()** (4 connections) — `server/tests/unit/middleware/test_auth_rate_limit.py`
- **test_auth_client_key_uses_xff_when_trusted()** (4 connections) — `server/tests/unit/middleware/test_auth_rate_limit.py`
- **test_auth_rate_limit_response_maps_rate_limit_error()** (4 connections) — `server/tests/unit/middleware/test_auth_rate_limit.py`
- **_collect_post_paths()** (3 connections) — `server/middleware/auth_rate_limit.py`
- **test_assert_auth_rate_limit_paths_registered_ok()** (3 connections) — `server/tests/unit/middleware/test_auth_rate_limit.py`
- **test_auth_client_key_ignores_xff_by_default()** (3 connections) — `server/tests/unit/middleware/test_auth_rate_limit.py`
- **test_auth_client_key_uses_ip()** (3 connections) — `server/tests/unit/middleware/test_auth_rate_limit.py`
- **test_auth_rate_limit_response_skips_other_paths()** (3 connections) — `server/tests/unit/middleware/test_auth_rate_limit.py`
- **Protocol** (3 connections)
- **_HasPrefix** (2 connections) — `server/middleware/auth_rate_limit.py`
- **_HasRoutes** (2 connections) — `server/middleware/auth_rate_limit.py`
- **_IncludedRouterLike** (2 connections) — `server/middleware/auth_rate_limit.py`
- **_auth_bucket()** (2 connections) — `server/middleware/auth_rate_limit.py`
- **_join_route_path()** (2 connections) — `server/middleware/auth_rate_limit.py`
- **_ok_post()** (2 connections) — `server/tests/unit/middleware/test_auth_rate_limit.py`
- **test_assert_auth_rate_limit_paths_registered_missing()** (2 connections) — `server/tests/unit/middleware/test_auth_rate_limit.py`
- **test_is_auth_rate_limited_path()** (2 connections) — `server/tests/unit/middleware/test_auth_rate_limit.py`
- **FastAPI** (2 connections)
- *... and 9 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (5 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (5 shared connections)
- [RateLimiter](RateLimiter.md) (4 shared connections)
- [create_app](create_app.md) (3 shared connections)
- [.format](format.md) (2 shared connections)
- [AuthRateLimitMiddleware](AuthRateLimitMiddleware.md) (2 shared connections)
- [ErrorType](ErrorType.md) (1 shared connections)

## Source Files

- `server/middleware/auth_rate_limit.py`
- `server/tests/unit/middleware/test_auth_rate_limit.py`

## Audit Trail

- EXTRACTED: 84 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*