# test_rate_limiter.py

> 26 nodes

## Key Concepts

- **test_rate_limiter.py** (35 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_check_rate_limit_disabled()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_check_rate_limit_error_handling()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_check_rate_limit_logs_violation()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_get_limit_default()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_get_limit_existing()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_get_player_stats()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_get_player_stats_empty()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_get_remaining_messages()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_get_remaining_messages_zero()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_rate_limit_sliding_window()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_record_message_cleanup_old()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_reset_player_limits_nonexistent_player()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **Unit tests for rate limiter service. Tests the RateLimiter class which provides…** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **Test check_rate_limit always returns True when disabled.** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **Test check_rate_limit handles errors gracefully (fails open).** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **Test record_message cleans up old entries.** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **Test get_player_stats returns correct statistics.** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **Test get_player_stats handles player with no messages.** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **Test reset_player_limits handles nonexistent player.** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **Test get_remaining_messages returns correct count.** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **Test get_remaining_messages returns 0 when at limit.** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **Test rate limiting uses sliding window correctly.** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **Test check_rate_limit logs violation when limit exceeded.** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **Test get_limit returns configured limit.** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`
- *... and 1 more nodes in this community*

## Relationships

- [RateLimiter](RateLimiter.md) (3 shared connections)
- [rate_limiter](rate_limiter.md) (2 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [test_check_rate_limit_within_limits](test_check_rate_limit_within_limits.md) (1 shared connections)
- [test_check_rate_limit_exceeds_limit](test_check_rate_limit_exceeds_limit.md) (1 shared connections)
- [test_record_message](test_record_message.md) (1 shared connections)
- [test_record_message_error_handling](test_record_message_error_handling.md) (1 shared connections)
- [test_reset_player_limits_specific_channel](test_reset_player_limits_specific_channel.md) (1 shared connections)
- [test_reset_player_limits_all_channels](test_reset_player_limits_all_channels.md) (1 shared connections)
- [test_get_system_stats](test_get_system_stats.md) (1 shared connections)
- [test_get_system_stats_no_players](test_get_system_stats_no_players.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_rate_limiter.py`

## Audit Trail

- EXTRACTED: 47 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*