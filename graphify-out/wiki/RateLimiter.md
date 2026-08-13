# RateLimiter

> 9 nodes

## Key Concepts

- **RateLimiter** (10 connections) — `server/utils/rate_limiter.py`
- **rate_limiter()** (4 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **server/utils/__init__.py** (3 connections) — `server/utils/__init__.py`
- **.__init__()** (2 connections) — `server/utils/rate_limiter.py`
- **fixture** (1 connections)
- **Create a RateLimiter instance for testing.** (1 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **Utility modules for MythosMUD server. This package contains various utility…** (1 connections) — `server/utils/__init__.py`
- **Simple in-memory rate limiter for API endpoints. This rate limiter tracks…** (1 connections) — `server/utils/rate_limiter.py`
- **Initialize the rate limiter. Args: max_requests: Maximum number of requests…** (1 connections) — `server/utils/rate_limiter.py`

## Relationships

- [.enforce_rate_limit](enforce_rate_limit.md) (3 shared connections)
- [test_rate_limiter_utils.py](test_rate_limiter_utils.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [ContainerServiceError](ContainerServiceError.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_rate_limiter_utils.py`
- `server/utils/__init__.py`
- `server/utils/rate_limiter.py`

## Audit Trail

- EXTRACTED: 16 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*