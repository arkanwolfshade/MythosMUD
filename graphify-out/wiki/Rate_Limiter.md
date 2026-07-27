# Rate Limiter

> 15 nodes · cohesion 0.16

## Key Concepts

- **RateLimiter** (10 connections) — `server/utils/rate_limiter.py`
- **rate_limiter.py** (7 connections) — `server/utils/rate_limiter.py`
- **.enforce_rate_limit()** (5 connections) — `server/utils/rate_limiter.py`
- **.get_rate_limit_info()** (4 connections) — `server/utils/rate_limiter.py`
- **__init__.py** (3 connections) — `server/utils/__init__.py`
- **.check_rate_limit()** (3 connections) — `server/utils/rate_limiter.py`
- **.__init__()** (2 connections) — `server/utils/rate_limiter.py`
- **Utility modules for MythosMUD server.  This package contains various utility mod** (1 connections) — `server/utils/__init__.py`
- **Any** (1 connections) — `server/utils/rate_limiter.py`
- **Rate limiting utilities for MythosMUD API endpoints.  This module provides rate** (1 connections) — `server/utils/rate_limiter.py`
- **Simple in-memory rate limiter for API endpoints.      This rate limiter tracks r** (1 connections) — `server/utils/rate_limiter.py`
- **Initialize the rate limiter.          Args:             max_requests: Maximum nu** (1 connections) — `server/utils/rate_limiter.py`
- **Check if a user has exceeded the rate limit.          Args:             user_id:** (1 connections) — `server/utils/rate_limiter.py`
- **Get rate limit information for a user.          Args:             user_id: The u** (1 connections) — `server/utils/rate_limiter.py`
- **Enforce rate limiting for a user.          Args:             user_id: The user's** (1 connections) — `server/utils/rate_limiter.py`

## Relationships

- [[Container API Endpoints]] (2 shared connections)
- [[Standardized Error Responses]] (2 shared connections)
- [[Rate Limiter Utilities]] (2 shared connections)
- [[Character Creation API]] (1 shared connections)
- [[NPC Admin API]] (1 shared connections)

## Source Files

- `server/utils/__init__.py`
- `server/utils/rate_limiter.py`

## Audit Trail

- EXTRACTED: 42 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
