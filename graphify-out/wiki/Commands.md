# Commands

> 14 nodes

## Key Concepts

- **RateLimiter** (14 connections) — `server/utils/rate_limiter.py`
- **test_auth_rate_limit_response_returns_429_when_exceeded()** (4 connections) — `server/tests/unit/middleware/test_auth_rate_limit.py`
- **.enforce_rate_limit()** (4 connections) — `server/utils/rate_limiter.py`
- **.get_rate_limit_info()** (4 connections) — `server/utils/rate_limiter.py`
- **.check_rate_limit()** (3 connections) — `server/utils/rate_limiter.py`
- **server/utils/__init__.py** (3 connections) — `server/utils/__init__.py`
- **.__init__()** (2 connections) — `server/utils/rate_limiter.py`
- **Any** (1 connections)
- **Utility modules for MythosMUD server. This package contains various utility…** (1 connections) — `server/utils/__init__.py`
- **Enforce rate limiting for a user. Args: user_id: The user's ID Raises:…** (1 connections) — `server/utils/rate_limiter.py`
- **Simple in-memory rate limiter for API endpoints. This rate limiter tracks…** (1 connections) — `server/utils/rate_limiter.py`
- **Initialize the rate limiter. Args: max_requests: Maximum number of requests…** (1 connections) — `server/utils/rate_limiter.py`
- **Check if a user has exceeded the rate limit. Args: user_id: The user's ID…** (1 connections) — `server/utils/rate_limiter.py`
- **Get rate limit information for a user. Args: user_id: The user's ID Returns:…** (1 connections) — `server/utils/rate_limiter.py`

## Relationships

- [Execution Steps](Execution_Steps.md) (4 shared connections)
- [fastapi_integration.py](fastapi_integration.py.md) (3 shared connections)
- [ChatService](ChatService.md) (1 shared connections)
- [InventoryMutationGuard](InventoryMutationGuard.md) (1 shared connections)
- [FeatureFlagService](FeatureFlagService.md) (1 shared connections)
- [npc_schedules.schema.json](npc_schedules.schema.json.md) (1 shared connections)

## Source Files

- `server/tests/unit/middleware/test_auth_rate_limit.py`
- `server/utils/__init__.py`
- `server/utils/rate_limiter.py`

## Audit Trail

- EXTRACTED: 23 (88%)
- INFERRED: 3 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*