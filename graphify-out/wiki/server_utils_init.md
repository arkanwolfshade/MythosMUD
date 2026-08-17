# server utils init

> 13 nodes

## Key Concepts

- **RateLimiter** (10 connections) — `server/utils/rate_limiter.py`
- **.enforce_rate_limit()** (5 connections) — `server/utils/rate_limiter.py`
- **.get_rate_limit_info()** (4 connections) — `server/utils/rate_limiter.py`
- **.check_rate_limit()** (3 connections) — `server/utils/rate_limiter.py`
- **server/utils/__init__.py** (3 connections) — `server/utils/__init__.py`
- **.__init__()** (2 connections) — `server/utils/rate_limiter.py`
- **Any** (1 connections)
- **Utility modules for MythosMUD server. This package contains various utility…** (1 connections) — `server/utils/__init__.py`
- **Simple in-memory rate limiter for API endpoints. This rate limiter tracks…** (1 connections) — `server/utils/rate_limiter.py`
- **Initialize the rate limiter. Args: max_requests: Maximum number of requests…** (1 connections) — `server/utils/rate_limiter.py`
- **Check if a user has exceeded the rate limit. Args: user_id: The user's ID…** (1 connections) — `server/utils/rate_limiter.py`
- **Get rate limit information for a user. Args: user_id: The user's ID Returns:…** (1 connections) — `server/utils/rate_limiter.py`
- **Enforce rate limiting for a user. Args: user_id: The user's ID Raises:…** (1 connections) — `server/utils/rate_limiter.py`

## Relationships

- [server tests unit utils test](server_tests_unit_utils_test.md) (2 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [docs examples logging fastapi integration](docs_examples_logging_fastapi_integration.md) (1 shared connections)
- [server error handlers pydantic error](server_error_handlers_pydantic_error.md) (1 shared connections)

## Source Files

- `server/utils/__init__.py`
- `server/utils/rate_limiter.py`

## Audit Trail

- EXTRACTED: 20 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*