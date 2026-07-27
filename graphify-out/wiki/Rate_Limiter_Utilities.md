# Rate Limiter Utilities

> 35 nodes · cohesion 0.06

## Key Concepts

- **test_rate_limiter_utils.py** (21 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_rate_limiter_initialization()** (3 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **rate_limiter()** (3 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **Test RateLimiter initializes with correct limits.** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **Test get_rate_limit_info calculates reset time correctly.** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **Test get_rate_limit_info returns correct info for no requests.** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_character_creation_limiter_initialized()** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_check_rate_limit_different_users()** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_check_rate_limit_exceeds_limit()** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_check_rate_limit_first_request()** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_check_rate_limit_multiple_requests()** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_check_rate_limit_removes_old_requests()** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_enforce_rate_limit_allows_request()** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_enforce_rate_limit_includes_retry_after()** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_enforce_rate_limit_raises_when_exceeded()** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_get_rate_limit_info_calculates_reset_time()** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_get_rate_limit_info_calculates_retry_after()** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_get_rate_limit_info_filters_old_requests()** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_get_rate_limit_info_no_requests()** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_get_rate_limit_info_with_requests()** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_rate_limiter_initialization()** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_stats_roll_limiter_initialized()** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **Unit tests for rate limiting utilities.  Tests the simple in-memory rate limiter** (1 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **Test get_rate_limit_info filters out old requests.** (1 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **Test enforce_rate_limit allows request within limit.** (1 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- *... and 10 more nodes in this community*

## Relationships

- [[Rate Limiter]] (2 shared connections)
- [[Chat Rate Limiter]] (1 shared connections)
- [[Rate Limiter Service]] (1 shared connections)
- [[NPC Admin API]] (1 shared connections)
- [[Standardized Error Responses]] (1 shared connections)

## Source Files

- `server/tests/unit/services/test_rate_limiter.py`
- `server/tests/unit/utils/test_rate_limiter_utils.py`

## Audit Trail

- EXTRACTED: 78 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
