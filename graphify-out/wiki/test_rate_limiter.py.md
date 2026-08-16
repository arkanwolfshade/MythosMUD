# test_rate_limiter.py

> 26 nodes

## Key Concepts

- **test_rate_limiter.py** (36 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_check_rate_limit_error_handling()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_check_rate_limit_exceeds_limit()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_check_rate_limit_logs_violation()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_check_rate_limit_within_limits()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_get_remaining_messages()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_get_system_stats_no_players()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_is_player_rate_limited_false()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_rate_limit_different_channels()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_rate_limit_different_players()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_rate_limit_sliding_window()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_record_message()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_reset_player_limits_nonexistent_player()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **Unit tests for rate limiter service. Tests the RateLimiter class which provides…** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **Test check_rate_limit returns True when within limits.** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **Test check_rate_limit returns False when limit exceeded.** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **Test check_rate_limit handles errors gracefully (fails open).** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **Test record_message adds timestamp to window.** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **Test reset_player_limits handles nonexistent player.** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **Test get_system_stats handles no active players.** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **Test is_player_rate_limited returns False when not rate limited.** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **Test get_remaining_messages returns correct count.** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **Test rate limiting uses sliding window correctly.** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **Test rate limiting is per-channel.** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **Test rate limiting is per-player.** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`
- *... and 1 more nodes in this community*

## Relationships

- [RateLimiter](RateLimiter.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [rate_limiter](rate_limiter.md) (2 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [test_check_rate_limit_disabled](test_check_rate_limit_disabled.md) (1 shared connections)
- [test_record_message_cleanup_old](test_record_message_cleanup_old.md) (1 shared connections)
- [test_record_message_error_handling](test_record_message_error_handling.md) (1 shared connections)
- [test_get_player_stats](test_get_player_stats.md) (1 shared connections)
- [test_get_player_stats_empty](test_get_player_stats_empty.md) (1 shared connections)
- [test_reset_player_limits_specific_channel](test_reset_player_limits_specific_channel.md) (1 shared connections)
- [test_reset_player_limits_all_channels](test_reset_player_limits_all_channels.md) (1 shared connections)
- [test_get_system_stats](test_get_system_stats.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_rate_limiter.py`

## Audit Trail

- EXTRACTED: 48 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*