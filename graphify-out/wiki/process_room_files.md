# process_room_files

> 14 nodes · cohesion 0.16

## Key Concepts

- **RateLimiter** (12 connections) — `server/utils/rate_limiter.py`
- **rate_limiter()** (5 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **.enforce_rate_limit()** (5 connections) — `server/utils/rate_limiter.py`
- **.get_rate_limit_info()** (4 connections) — `server/utils/rate_limiter.py`
- **.check_rate_limit()** (3 connections) — `server/utils/rate_limiter.py`
- **.__init__()** (2 connections) — `server/utils/rate_limiter.py`
- **fixture** (1 connections)
- **Create a RateLimiter instance for testing.** (1 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **Any** (1 connections)
- **Enforce rate limiting for a user. Args: user_id: The user's ID Raises:…** (1 connections) — `server/utils/rate_limiter.py`
- **Simple in-memory rate limiter for API endpoints. This rate limiter tracks…** (1 connections) — `server/utils/rate_limiter.py`
- **Initialize the rate limiter. Args: max_requests: Maximum number of requests…** (1 connections) — `server/utils/rate_limiter.py`
- **Check if a user has exceeded the rate limit. Args: user_id: The user's ID…** (1 connections) — `server/utils/rate_limiter.py`
- **Get rate limit information for a user. Args: user_id: The user's ID Returns:…** (1 connections) — `server/utils/rate_limiter.py`

## Relationships

- [test_room_subscription_manager_helpers.py](test_room_subscription_manager_helpers.py.md) (2 shared connections)
- [_PlayerCombatClearing](_PlayerCombatClearing.md) (2 shared connections)
- [Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\character_sheets  (2026-08-12)](Graph_Report_-_C-_Users_arkan_Proton_Drive_arkanwolfshade_My_files_Chaosium_character_sheets__2026-08-12.md) (2 shared connections)
- [test_container_persistence_async_helpers.py](test_container_persistence_async_helpers.py.md) (1 shared connections)
- [test_look_player.py](test_look_player.py.md) (1 shared connections)
- [AttributeError](AttributeError.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_rate_limiter_utils.py`
- `server/utils/rate_limiter.py`

## Audit Trail

- EXTRACTED: 23 (96%)
- INFERRED: 1 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*