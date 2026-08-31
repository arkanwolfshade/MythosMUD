# RateLimiter

> 17 nodes

## Key Concepts

- **RateLimiter** (12 connections) — `server/utils/rate_limiter.py`
- **test_auth_rate_limit_response_returns_429_when_exceeded()** (5 connections) — `server/tests/unit/middleware/test_auth_rate_limit.py`
- **rate_limiter()** (5 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **.enforce_rate_limit()** (5 connections) — `server/utils/rate_limiter.py`
- **.get_rate_limit_info()** (4 connections) — `server/utils/rate_limiter.py`
- **.check_rate_limit()** (3 connections) — `server/utils/rate_limiter.py`
- **server/utils/__init__.py** (3 connections) — `server/utils/__init__.py`
- **.__init__()** (2 connections) — `server/utils/rate_limiter.py`
- **fixture** (1 connections)
- **Any** (1 connections)
- **Create a RateLimiter instance for testing.** (1 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **Utility modules for MythosMUD server. This package contains various utility…** (1 connections) — `server/utils/__init__.py`
- **Enforce rate limiting for a user. Args: user_id: The user's ID Raises:…** (1 connections) — `server/utils/rate_limiter.py`
- **Simple in-memory rate limiter for API endpoints. This rate limiter tracks…** (1 connections) — `server/utils/rate_limiter.py`
- **Initialize the rate limiter. Args: max_requests: Maximum number of requests…** (1 connections) — `server/utils/rate_limiter.py`
- **Check if a user has exceeded the rate limit. Args: user_id: The user's ID…** (1 connections) — `server/utils/rate_limiter.py`
- **Get rate limit information for a user. Args: user_id: The user's ID Returns:…** (1 connections) — `server/utils/rate_limiter.py`

## Relationships

- [test_auth_rate_limit.py](test_auth_rate_limit.py.md) (4 shared connections)
- [test_rate_limiter_utils.py](test_rate_limiter_utils.py.md) (4 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (2 shared connections)
- [connection_manager.py](connection_manager.py.md) (2 shared connections)

## Source Files

- `server/tests/unit/middleware/test_auth_rate_limit.py`
- `server/tests/unit/utils/test_rate_limiter_utils.py`
- `server/utils/__init__.py`
- `server/utils/rate_limiter.py`

## Audit Trail

- EXTRACTED: 28 (93%)
- INFERRED: 2 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*