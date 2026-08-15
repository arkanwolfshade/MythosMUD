# test_rate_limiter_utils.py

> 12 nodes

## Key Concepts

- **test_rate_limiter_utils.py** (22 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_enforce_rate_limit_raises_when_exceeded()** (3 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_check_rate_limit_first_request()** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_get_rate_limit_info_calculates_reset_time()** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_get_rate_limit_info_no_requests()** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_rate_limiter_initialization()** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **Unit tests for rate limiting utilities. Tests the simple in-memory rate limiter…** (1 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **Test get_rate_limit_info calculates reset time correctly.** (1 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **Test enforce_rate_limit raises RateLimitError when limit exceeded.** (1 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **Test RateLimiter initializes correctly.** (1 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **Test check_rate_limit allows first request.** (1 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **Test get_rate_limit_info returns correct info for no requests.** (1 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`

## Relationships

- [MythosMUDError](MythosMUDError.md) (2 shared connections)
- [RateLimiter](RateLimiter.md) (2 shared connections)
- [DatabaseError](DatabaseError.md) (2 shared connections)
- [test_get_rate_limit_info_calculates_retry_after](test_get_rate_limit_info_calculates_retry_after.md) (1 shared connections)
- [test_get_rate_limit_info_filters_old_requests](test_get_rate_limit_info_filters_old_requests.md) (1 shared connections)
- [test_enforce_rate_limit_allows_request](test_enforce_rate_limit_allows_request.md) (1 shared connections)
- [test_enforce_rate_limit_includes_retry_after](test_enforce_rate_limit_includes_retry_after.md) (1 shared connections)
- [test_stats_roll_limiter_initialized](test_stats_roll_limiter_initialized.md) (1 shared connections)
- [test_character_creation_limiter_initialized](test_character_creation_limiter_initialized.md) (1 shared connections)
- [test_check_rate_limit_multiple_requests](test_check_rate_limit_multiple_requests.md) (1 shared connections)
- [test_check_rate_limit_exceeds_limit](test_check_rate_limit_exceeds_limit.md) (1 shared connections)
- [test_check_rate_limit_different_users](test_check_rate_limit_different_users.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_rate_limiter_utils.py`

## Audit Trail

- EXTRACTED: 27 (96%)
- INFERRED: 1 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*