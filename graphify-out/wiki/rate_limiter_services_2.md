# rate limiter services

> 89 nodes

## Key Concepts

- **test_rate_limiter.py** (35 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **RateLimiter** (17 connections) — `server/services/rate_limiter.py`
- **.get_limit()** (6 connections) — `server/services/rate_limiter.py`
- **._cleanup_old_entries()** (6 connections) — `server/services/rate_limiter.py`
- **.check_rate_limit()** (5 connections) — `server/services/rate_limiter.py`
- **.get_player_stats()** (5 connections) — `server/services/rate_limiter.py`
- **.__init__()** (4 connections) — `server/services/rate_limiter.py`
- **.record_message()** (4 connections) — `server/services/rate_limiter.py`
- **.get_remaining_messages()** (4 connections) — `server/services/rate_limiter.py`
- **.get_system_stats()** (3 connections) — `server/services/rate_limiter.py`
- **.is_player_rate_limited()** (3 connections) — `server/services/rate_limiter.py`
- **rate_limiter()** (3 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_rate_limiter_initialization()** (3 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_rate_limiter_legacy_config()** (3 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **.set_limit()** (2 connections) — `server/services/rate_limiter.py`
- **Any** (2 connections)
- **.reset_player_limits()** (2 connections) — `server/services/rate_limiter.py`
- **mock_config()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_set_limit()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_get_limit_existing()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_get_limit_default()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_cleanup_old_entries()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_check_rate_limit_within_limits()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_check_rate_limit_exceeds_limit()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_check_rate_limit_disabled()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- *... and 64 more nodes in this community*

## Relationships

- [models npc rationale](models_npc_rationale.md) (4 shared connections)
- [chat logger services](chat_logger_services.md) (1 shared connections)

## Source Files

- `server/services/rate_limiter.py`
- `server/tests/unit/services/test_rate_limiter.py`

## Audit Trail

- EXTRACTED: 206 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*