# server tests unit utils test

> 36 nodes

## Key Concepts

- **test_rate_limiter_utils.py** (23 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **rate_limiter()** (5 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_enforce_rate_limit_includes_retry_after()** (3 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_enforce_rate_limit_raises_when_exceeded()** (3 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_character_creation_limiter_initialized()** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_check_rate_limit_different_users()** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_check_rate_limit_exceeds_limit()** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_check_rate_limit_first_request()** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_check_rate_limit_multiple_requests()** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_check_rate_limit_removes_old_requests()** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_enforce_rate_limit_allows_request()** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_get_rate_limit_info_calculates_reset_time()** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_get_rate_limit_info_calculates_retry_after()** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_get_rate_limit_info_filters_old_requests()** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_get_rate_limit_info_no_requests()** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_get_rate_limit_info_with_requests()** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_rate_limiter_initialization()** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_stats_roll_limiter_initialized()** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **Test get_rate_limit_info returns correct info for no requests.** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **fixture** (1 connections)
- **Unit tests for rate limiting utilities. Tests the simple in-memory rate limiter…** (1 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **Test get_rate_limit_info calculates reset time correctly.** (1 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **Test get_rate_limit_info calculates retry_after correctly.** (1 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **Test get_rate_limit_info filters out old requests.** (1 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **Test enforce_rate_limit allows request within limit.** (1 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- *... and 11 more nodes in this community*

## Relationships

- [server error handlers pydantic error](server_error_handlers_pydantic_error.md) (3 shared connections)
- [server utils init](server_utils_init.md) (2 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [server realtime rate limiter ratelimiter](server_realtime_rate_limiter_ratelimiter.md) (1 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_rate_limiter_utils.py`

## Audit Trail

- EXTRACTED: 42 (93%)
- INFERRED: 3 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*