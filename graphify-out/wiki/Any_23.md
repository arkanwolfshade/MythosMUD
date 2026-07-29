# Any

> 81 nodes

## Key Concepts

- **RateLimiter** (46 connections) — `server/realtime/rate_limiter.py`
- **test_connection_rate_limiter.py** (33 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **Test RateLimiter.cleanup_old_attempts() removes old attempts.** (4 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **.get_rate_limit_info()** (3 connections) — `server/realtime/rate_limiter.py`
- **Any** (3 connections)
- **.get_stats()** (3 connections) — `server/realtime/rate_limiter.py`
- **.get_message_rate_limit_info()** (3 connections) — `server/realtime/rate_limiter.py`
- **mock_manager()** (3 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **test_rate_limiter_init_defaults()** (3 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **test_rate_limiter_init_custom()** (3 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **test_rate_limiter_check_rate_limit_first_attempt()** (3 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **test_rate_limiter_check_rate_limit_within_limit()** (3 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **test_rate_limiter_check_rate_limit_exceeded()** (3 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **test_rate_limiter_check_rate_limit_old_attempts_removed()** (3 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **test_rate_limiter_get_rate_limit_info()** (3 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **test_rate_limiter_get_rate_limit_info_no_attempts()** (3 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **test_rate_limiter_cleanup_old_attempts()** (3 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **test_rate_limiter_cleanup_old_attempts_removes_empty()** (3 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **test_rate_limiter_cleanup_old_attempts_error()** (3 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **test_rate_limiter_cleanup_large_structures()** (3 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **test_rate_limiter_cleanup_large_structures_error()** (3 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **test_rate_limiter_remove_player_data()** (3 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **test_rate_limiter_remove_player_data_not_present()** (3 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **test_rate_limiter_remove_player_data_error()** (3 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **test_rate_limiter_get_stats()** (3 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- *... and 56 more nodes in this community*

## Relationships

- [main()](main%28%29.md) (4 shared connections)
- [connection disconnection](connection_disconnection.md) (2 shared connections)

## Source Files

- `server/realtime/rate_limiter.py`
- `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- `server/tests/unit/realtime/test_connection_rate_limiter.py`

## Audit Trail

- EXTRACTED: 238 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*