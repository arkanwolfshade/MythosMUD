# test_auth_rate_limit.py

> 23 nodes

## Key Concepts

- **test_auth_rate_limit.py** (27 connections) — `server/tests/unit/middleware/test_auth_rate_limit.py`
- **auth_client_key()** (11 connections) — `server/middleware/auth_rate_limit.py`
- **auth_rate_limit_response()** (11 connections) — `server/middleware/auth_rate_limit.py`
- **_post_request()** (9 connections) — `server/tests/unit/middleware/test_auth_rate_limit.py`
- **is_auth_rate_limited_path()** (5 connections) — `server/middleware/auth_rate_limit.py`
- **test_auth_client_key_rejects_non_ip_xff()** (4 connections) — `server/tests/unit/middleware/test_auth_rate_limit.py`
- **test_auth_client_key_uses_xff_when_trusted()** (4 connections) — `server/tests/unit/middleware/test_auth_rate_limit.py`
- **test_auth_rate_limit_response_maps_rate_limit_error()** (4 connections) — `server/tests/unit/middleware/test_auth_rate_limit.py`
- **test_assert_auth_rate_limit_paths_registered_ok()** (3 connections) — `server/tests/unit/middleware/test_auth_rate_limit.py`
- **test_auth_client_key_ignores_xff_by_default()** (3 connections) — `server/tests/unit/middleware/test_auth_rate_limit.py`
- **test_auth_client_key_uses_ip()** (3 connections) — `server/tests/unit/middleware/test_auth_rate_limit.py`
- **test_auth_rate_limit_response_skips_other_paths()** (3 connections) — `server/tests/unit/middleware/test_auth_rate_limit.py`
- **_auth_bucket()** (2 connections) — `server/middleware/auth_rate_limit.py`
- **_ok_post()** (2 connections) — `server/tests/unit/middleware/test_auth_rate_limit.py`
- **test_create_app_auth_rate_limit_paths_match()** (2 connections) — `server/tests/unit/middleware/test_auth_rate_limit.py`
- **test_is_auth_rate_limited_path()** (2 connections) — `server/tests/unit/middleware/test_auth_rate_limit.py`
- **Request** (2 connections)
- **MonkeyPatch** (2 connections)
- **Request** (1 connections)
- **Return 429 when an auth POST exceeds the limiter; otherwise None.** (1 connections) — `server/middleware/auth_rate_limit.py`
- **Return True if path is an unauthenticated auth POST covered by the limiter.** (1 connections) — `server/middleware/auth_rate_limit.py`
- **Key the limiter by client IP. Default uses the TCP peer (request.client.host).…** (1 connections) — `server/middleware/auth_rate_limit.py`
- **Unit tests for auth HTTP rate limiting.** (1 connections) — `server/tests/unit/middleware/test_auth_rate_limit.py`

## Relationships

- [auth_rate_limit.py](auth_rate_limit.py.md) (8 shared connections)
- [RateLimiter](RateLimiter.md) (4 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (2 shared connections)
- [create_app](create_app.md) (2 shared connections)
- [.format](format.md) (1 shared connections)
- [ErrorType](ErrorType.md) (1 shared connections)
- [AuthRateLimitMiddleware](AuthRateLimitMiddleware.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [DatabaseError](DatabaseError.md) (1 shared connections)
- [test_rate_limiter_utils.py](test_rate_limiter_utils.py.md) (1 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (1 shared connections)
- [factory.py](factory.py.md) (1 shared connections)

## Source Files

- `server/middleware/auth_rate_limit.py`
- `server/tests/unit/middleware/test_auth_rate_limit.py`

## Audit Trail

- EXTRACTED: 63 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*