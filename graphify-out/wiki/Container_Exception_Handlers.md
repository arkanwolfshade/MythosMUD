# Container Exception Handlers

> 36 nodes

## Key Concepts

- **test_rate_limiter_utils.py** (22 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **rate_limiter()** (3 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_enforce_rate_limit_raises_when_exceeded()** (3 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_enforce_rate_limit_includes_retry_after()** (3 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_rate_limiter_initialization()** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_check_rate_limit_first_request()** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_check_rate_limit_multiple_requests()** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_check_rate_limit_exceeds_limit()** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_check_rate_limit_different_users()** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_check_rate_limit_removes_old_requests()** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_get_rate_limit_info_no_requests()** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_get_rate_limit_info_with_requests()** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_get_rate_limit_info_calculates_reset_time()** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_get_rate_limit_info_calculates_retry_after()** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_get_rate_limit_info_filters_old_requests()** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_enforce_rate_limit_allows_request()** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_stats_roll_limiter_initialized()** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_character_creation_limiter_initialized()** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **Unit tests for rate limiting utilities.  Tests the simple in-memory rate limiter** (1 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **Create a RateLimiter instance for testing.** (1 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **Test RateLimiter initializes correctly.** (1 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **Test check_rate_limit allows first request.** (1 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **Test check_rate_limit allows multiple requests within limit.** (1 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **Test check_rate_limit returns False when limit exceeded.** (1 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **Test check_rate_limit tracks different users separately.** (1 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- *... and 11 more nodes in this community*

## Relationships

- [Standardized Error Responses](Standardized_Error_Responses.md) (3 shared connections)
- [Game Mechanics Service](Game_Mechanics_Service.md) (3 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_rate_limiter_utils.py`

## Audit Trail

- EXTRACTED: 75 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*