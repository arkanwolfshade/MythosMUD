# Game Quest Service

> 7 nodes

## Key Concepts

- **.enforce_rate_limit()** (5 connections) — `server/utils/rate_limiter.py`
- **.get_rate_limit_info()** (4 connections) — `server/utils/rate_limiter.py`
- **.check_rate_limit()** (3 connections) — `server/utils/rate_limiter.py`
- **Any** (1 connections)
- **Check if a user has exceeded the rate limit.          Args:             user_id:** (1 connections) — `server/utils/rate_limiter.py`
- **Get rate limit information for a user.          Args:             user_id: The u** (1 connections) — `server/utils/rate_limiter.py`
- **Enforce rate limiting for a user.          Args:             user_id: The user's** (1 connections) — `server/utils/rate_limiter.py`

## Relationships

- [Game Mechanics Service](Game_Mechanics_Service.md) (3 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (1 shared connections)

## Source Files

- `server/utils/rate_limiter.py`

## Audit Trail

- EXTRACTED: 16 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*