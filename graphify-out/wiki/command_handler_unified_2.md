# command handler unified

> 51 nodes

## Key Concepts

- **test_rate_limiter_utils.py** (22 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **RateLimiter** (10 connections) — `server/utils/rate_limiter.py`
- **rate_limiter.py** (9 connections) — `server/utils/rate_limiter.py`
- **.enforce_rate_limit()** (5 connections) — `server/utils/rate_limiter.py`
- **.get_rate_limit_info()** (4 connections) — `server/utils/rate_limiter.py`
- **rate_limiter()** (3 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_enforce_rate_limit_raises_when_exceeded()** (3 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_enforce_rate_limit_includes_retry_after()** (3 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **__init__.py** (3 connections) — `server/utils/__init__.py`
- **.check_rate_limit()** (3 connections) — `server/utils/rate_limiter.py`
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
- **.__init__()** (2 connections) — `server/utils/rate_limiter.py`
- *... and 26 more nodes in this community*

## Relationships

- [Error Handling Core](Error_Handling_Core.md) (5 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)
- [Exception Containers](Exception_Containers.md) (2 shared connections)
- [profession game service](profession_game_service.md) (1 shared connections)
- [models npc rationale](models_npc_rationale.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_rate_limiter_utils.py`
- `server/utils/__init__.py`
- `server/utils/rate_limiter.py`

## Audit Trail

- EXTRACTED: 119 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*