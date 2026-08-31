# auth_rate_limit.py

> 12 nodes

## Key Concepts

- **auth_rate_limit.py** (19 connections) — `server/middleware/auth_rate_limit.py`
- **assert_auth_rate_limit_paths_registered()** (9 connections) — `server/middleware/auth_rate_limit.py`
- **_collect_post_paths()** (3 connections) — `server/middleware/auth_rate_limit.py`
- **Protocol** (3 connections)
- **_HasPrefix** (2 connections) — `server/middleware/auth_rate_limit.py`
- **_HasRoutes** (2 connections) — `server/middleware/auth_rate_limit.py`
- **_IncludedRouterLike** (2 connections) — `server/middleware/auth_rate_limit.py`
- **_join_route_path()** (2 connections) — `server/middleware/auth_rate_limit.py`
- **test_assert_auth_rate_limit_paths_registered_missing()** (2 connections) — `server/tests/unit/middleware/test_auth_rate_limit.py`
- **FastAPI** (2 connections)
- **IP-based rate limiting for unauthenticated auth HTTP endpoints.** (1 connections) — `server/middleware/auth_rate_limit.py`
- **Fail startup if AUTH_RATE_LIMITED_PATHS do not match mounted POST routes.** (1 connections) — `server/middleware/auth_rate_limit.py`

## Relationships

- [test_auth_rate_limit.py](test_auth_rate_limit.py.md) (8 shared connections)
- [factory.py](factory.py.md) (3 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [test_rate_limiter_utils.py](test_rate_limiter_utils.py.md) (1 shared connections)
- [AuthRateLimitMiddleware](AuthRateLimitMiddleware.md) (1 shared connections)
- [.format](format.md) (1 shared connections)

## Source Files

- `server/middleware/auth_rate_limit.py`
- `server/tests/unit/middleware/test_auth_rate_limit.py`

## Audit Trail

- EXTRACTED: 32 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*