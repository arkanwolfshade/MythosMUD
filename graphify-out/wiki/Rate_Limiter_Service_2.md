# Rate Limiter Service

> 53 nodes · cohesion 0.04

## Key Concepts

- **test_rate_limiter.py** (33 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_check_rate_limit_error_handling()** (3 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_get_remaining_messages_error_handling()** (3 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_record_message_error_handling()** (3 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **mock_config()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **Test get_system_stats returns system-wide statistics.** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_check_rate_limit_disabled()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_check_rate_limit_logs_violation()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_cleanup_old_entries()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_get_limit_default()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_get_limit_existing()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_get_player_stats_empty()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_get_remaining_messages()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_get_remaining_messages_zero()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_get_system_stats()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_get_system_stats_no_players()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_is_player_rate_limited_false()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_is_player_rate_limited_true()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_rate_limit_different_channels()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_rate_limit_different_players()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_rate_limit_sliding_window()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_record_message()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_record_message_cleanup_old()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_reset_player_limits_all_channels()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_reset_player_limits_nonexistent_player()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- *... and 28 more nodes in this community*

## Relationships

- [[Database Manager Tests]] (4 shared connections)
- [[Chat Rate Limiter]] (3 shared connections)
- [[Services Rate Limiter]] (2 shared connections)
- [[Rate Limiter Utilities]] (1 shared connections)
- [[User Manager Mute Tests]] (1 shared connections)

## Source Files

- `server/tests/unit/services/test_rate_limiter.py`
- `server/tests/unit/services/test_user_manager.py`

## Audit Trail

- EXTRACTED: 112 (97%)
- INFERRED: 3 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
