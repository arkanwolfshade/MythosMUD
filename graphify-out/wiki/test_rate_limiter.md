# test rate limiter

> 26 nodes

## Key Concepts

- **test_rate_limiter.py** (35 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_cleanup_old_entries()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_check_rate_limit_within_limits()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_check_rate_limit_exceeds_limit()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_check_rate_limit_error_handling()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_record_message_error_handling()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_get_player_stats_empty()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_reset_player_limits_nonexistent_player()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_get_system_stats()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_is_player_rate_limited_false()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_get_remaining_messages_zero()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_rate_limit_different_channels()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_check_rate_limit_logs_violation()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **Unit tests for rate limiter service.  Tests the RateLimiter class which provides** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **Test _cleanup_old_entries removes old timestamps.** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **Test check_rate_limit returns True when within limits.** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **Test check_rate_limit returns False when limit exceeded.** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **Test check_rate_limit handles errors gracefully (fails open).** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **Test record_message handles errors gracefully.** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **Test get_player_stats handles player with no messages.** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **Test reset_player_limits handles nonexistent player.** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **Test get_system_stats returns system-wide statistics.** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **Test is_player_rate_limited returns False when not rate limited.** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **Test get_remaining_messages returns 0 when at limit.** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **Test rate limiting is per-channel.** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`
- *... and 1 more nodes in this community*

## Relationships

- [RateLimiter](RateLimiter.md) (4 shared connections)
- [main()](main%28%29.md) (2 shared connections)
- [Test reset player limits resets](Test_reset_player_limits_resets.md) (2 shared connections)
- [mock config()](mock_config%28%29.md) (1 shared connections)
- [Test check rate limit always](Test_check_rate_limit_always.md) (1 shared connections)
- [Test get limit returns default](Test_get_limit_returns_default.md) (1 shared connections)
- [Test get limit returns configured](Test_get_limit_returns_configured.md) (1 shared connections)
- [Test get player stats returns](Test_get_player_stats_returns.md) (1 shared connections)
- [Test get remaining messages returns](Test_get_remaining_messages_returns.md) (1 shared connections)
- [Test get remaining messages handles](Test_get_remaining_messages_handles.md) (1 shared connections)
- [Test get system stats handles](Test_get_system_stats_handles.md) (1 shared connections)
- [Test is player rate limited](Test_is_player_rate_limited.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_rate_limiter.py`

## Audit Trail

- EXTRACTED: 72 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*