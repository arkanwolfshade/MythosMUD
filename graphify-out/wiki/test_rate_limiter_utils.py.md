# test_rate_limiter_utils.py

> 59 nodes

## Key Concepts

- **test_rate_limiter_utils.py** (27 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **utils/rate_limiter.py** (13 connections) — `server/utils/rate_limiter.py`
- **RateLimiter** (12 connections) — `server/utils/rate_limiter.py`
- **auth_login_rate_limit_settings()** (7 connections) — `server/utils/rate_limiter.py`
- **rate_limiter()** (5 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **.enforce_rate_limit()** (5 connections) — `server/utils/rate_limiter.py`
- **.get_rate_limit_info()** (4 connections) — `server/utils/rate_limiter.py`
- **test_enforce_rate_limit_includes_retry_after()** (3 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_enforce_rate_limit_raises_when_exceeded()** (3 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **_positive_int_env()** (3 connections) — `server/utils/rate_limiter.py`
- **.check_rate_limit()** (3 connections) — `server/utils/rate_limiter.py`
- **server/utils/__init__.py** (3 connections) — `server/utils/__init__.py`
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
- *... and 34 more nodes in this community*

## Relationships

- [server/exceptions.py](server-exceptions.py.md) (7 shared connections)
- [test_auth_rate_limit.py](test_auth_rate_limit.py.md) (4 shared connections)
- [pytest.md](pytest.md.md) (3 shared connections)
- [connection_manager_methods.py](connection_manager_methods.py.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_rate_limiter_utils.py`
- `server/utils/__init__.py`
- `server/utils/rate_limiter.py`

## Audit Trail

- EXTRACTED: 82 (96%)
- INFERRED: 3 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*