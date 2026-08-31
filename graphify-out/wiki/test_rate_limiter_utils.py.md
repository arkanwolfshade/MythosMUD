# test_rate_limiter_utils.py

> 43 nodes

## Key Concepts

- **test_rate_limiter_utils.py** (27 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **utils/rate_limiter.py** (13 connections) — `server/utils/rate_limiter.py`
- **auth_login_rate_limit_settings()** (7 connections) — `server/utils/rate_limiter.py`
- **test_enforce_rate_limit_includes_retry_after()** (3 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_enforce_rate_limit_raises_when_exceeded()** (3 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **_positive_int_env()** (3 connections) — `server/utils/rate_limiter.py`
- **test_auth_login_limiter_matches_settings()** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_auth_login_rate_limit_settings_defaults()** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_auth_login_rate_limit_settings_from_env()** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
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
- **Unit tests for rate limiting utilities. Tests the simple in-memory rate limiter…** (1 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **Test get_rate_limit_info returns correct info with requests.** (1 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- *... and 18 more nodes in this community*

## Relationships

- [LoggedHTTPException](LoggedHTTPException.md) (5 shared connections)
- [RateLimiter](RateLimiter.md) (4 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [connection_manager.py](connection_manager.py.md) (1 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (1 shared connections)
- [auth_rate_limit.py](auth_rate_limit.py.md) (1 shared connections)
- [test_auth_rate_limit.py](test_auth_rate_limit.py.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_rate_limiter_utils.py`
- `server/utils/rate_limiter.py`

## Audit Trail

- EXTRACTED: 61 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*