# test_rate_limiter_utils.py

> 50 nodes

## Key Concepts

- **test_rate_limiter_utils.py** (23 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **RateLimiter** (10 connections) — `server/utils/rate_limiter.py`
- **rate_limiter()** (5 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **.enforce_rate_limit()** (5 connections) — `server/utils/rate_limiter.py`
- **.get_rate_limit_info()** (4 connections) — `server/utils/rate_limiter.py`
- **test_enforce_rate_limit_includes_retry_after()** (3 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_enforce_rate_limit_raises_when_exceeded()** (3 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **.check_rate_limit()** (3 connections) — `server/utils/rate_limiter.py`
- **server/utils/__init__.py** (3 connections) — `server/utils/__init__.py`
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
- **.__init__()** (2 connections) — `server/utils/rate_limiter.py`
- **fixture** (1 connections)
- *... and 25 more nodes in this community*

## Relationships

- [api/character_creation.py](api-character_creation.py.md) (7 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (1 shared connections)
- [RateLimiter](RateLimiter.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [DatabaseError](DatabaseError.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_rate_limiter_utils.py`
- `server/utils/__init__.py`
- `server/utils/rate_limiter.py`

## Audit Trail

- EXTRACTED: 60 (95%)
- INFERRED: 3 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*