# test_auth_rate_limit.py

> 36 nodes

## Key Concepts

- **test_auth_rate_limit.py** (27 connections) — `server/tests/unit/middleware/test_auth_rate_limit.py`
- **auth_rate_limit.py** (19 connections) — `server/middleware/auth_rate_limit.py`
- **auth_client_key()** (11 connections) — `server/middleware/auth_rate_limit.py`
- **auth_rate_limit_response()** (11 connections) — `server/middleware/auth_rate_limit.py`
- **assert_auth_rate_limit_paths_registered()** (9 connections) — `server/middleware/auth_rate_limit.py`
- **_post_request()** (9 connections) — `server/tests/unit/middleware/test_auth_rate_limit.py`
- **is_auth_rate_limited_path()** (5 connections) — `server/middleware/auth_rate_limit.py`
- **test_auth_rate_limit_response_returns_429_when_exceeded()** (5 connections) — `server/tests/unit/middleware/test_auth_rate_limit.py`
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
- **test_create_app_auth_rate_limit_paths_match()** (2 connections) — `server/tests/unit/middleware/test_auth_rate_limit.py`
- *... and 11 more nodes in this community*

## Relationships

- [factory.py](factory.py.md) (6 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (5 shared connections)
- [test_rate_limiter_utils.py](test_rate_limiter_utils.py.md) (4 shared connections)
- [PlayerGuidFormatter](PlayerGuidFormatter.md) (2 shared connections)
- [AuthRateLimitMiddleware](AuthRateLimitMiddleware.md) (2 shared connections)
- [pytest.md](pytest.md.md) (2 shared connections)
- [StandardizedErrorResponse](StandardizedErrorResponse.md) (1 shared connections)
- [connection_manager_methods.py](connection_manager_methods.py.md) (1 shared connections)

## Source Files

- `server/middleware/auth_rate_limit.py`
- `server/tests/unit/middleware/test_auth_rate_limit.py`

## Audit Trail

- EXTRACTED: 88 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*