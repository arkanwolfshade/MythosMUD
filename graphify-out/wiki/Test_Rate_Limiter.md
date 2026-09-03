# Test Rate Limiter

> 88 nodes

## Key Concepts

- **test_rate_limiter.py** (36 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **RateLimiter** (17 connections) — `server/services/rate_limiter.py`
- **._cleanup_old_entries()** (6 connections) — `server/services/rate_limiter.py`
- **.get_limit()** (6 connections) — `server/services/rate_limiter.py`
- **.check_rate_limit()** (5 connections) — `server/services/rate_limiter.py`
- **.get_player_stats()** (5 connections) — `server/services/rate_limiter.py`
- **rate_limiter()** (5 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **.get_remaining_messages()** (4 connections) — `server/services/rate_limiter.py`
- **.record_message()** (4 connections) — `server/services/rate_limiter.py`
- **test_rate_limiter_initialization()** (4 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_rate_limiter_legacy_config()** (4 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **.get_system_stats()** (3 connections) — `server/services/rate_limiter.py`
- **.is_player_rate_limited()** (3 connections) — `server/services/rate_limiter.py`
- **mock_config()** (3 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **.reset_player_limits()** (2 connections) — `server/services/rate_limiter.py`
- **.set_limit()** (2 connections) — `server/services/rate_limiter.py`
- **test_check_rate_limit_disabled()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_check_rate_limit_error_handling()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_check_rate_limit_exceeds_limit()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_check_rate_limit_logs_violation()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_check_rate_limit_within_limits()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_cleanup_old_entries()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_get_limit_default()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_get_limit_existing()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_get_player_stats()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- *... and 63 more nodes in this community*

## Relationships

- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (3 shared connections)
- [Test Connection Rate Limiter](Test_Connection_Rate_Limiter.md) (3 shared connections)
- [Chat Logger](Chat_Logger.md) (1 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)

## Source Files

- `server/services/rate_limiter.py`
- `server/tests/unit/services/test_rate_limiter.py`

## Audit Trail

- EXTRACTED: 106 (97%)
- INFERRED: 3 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*