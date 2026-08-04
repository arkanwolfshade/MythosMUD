# rate limiter services

> 24 nodes

## Key Concepts

- **test_rate_limiter.py** (35 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_get_limit_existing()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_get_limit_default()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_check_rate_limit_exceeds_limit()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_check_rate_limit_disabled()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_check_rate_limit_error_handling()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_get_player_stats()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_reset_player_limits_specific_channel()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_reset_player_limits_all_channels()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_rate_limit_sliding_window()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_rate_limit_different_players()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_check_rate_limit_logs_violation()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **Unit tests for rate limiter service.  Tests the RateLimiter class which provides** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **Test get_limit returns configured limit.** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **Test get_limit returns default for unknown channel.** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **Test check_rate_limit returns False when limit exceeded.** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **Test check_rate_limit always returns True when disabled.** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **Test check_rate_limit handles errors gracefully (fails open).** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **Test get_player_stats returns correct statistics.** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **Test reset_player_limits resets specific channel.** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **Test reset_player_limits resets all channels when channel is None.** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **Test rate limiting uses sliding window correctly.** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **Test rate limiting is per-player.** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **Test check_rate_limit logs violation when limit exceeded.** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`

## Relationships

- [event events serialization](event_events_serialization.md) (4 shared connections)
- [taunt combat commands](taunt_combat_commands.md) (1 shared connections)
- [NPC Combat](NPC_Combat.md) (1 shared connections)
- [mock_config](mock_config.md) (1 shared connections)
- [test_check_rate_limit_within_limits](test_check_rate_limit_within_limits.md) (1 shared connections)
- [test_cleanup_old_entries](test_cleanup_old_entries.md) (1 shared connections)
- [test_get_player_stats_empty](test_get_player_stats_empty.md) (1 shared connections)
- [test_get_remaining_messages](test_get_remaining_messages.md) (1 shared connections)
- [test_get_remaining_messages_error_handling](test_get_remaining_messages_error_handling.md) (1 shared connections)
- [test_get_remaining_messages_zero](test_get_remaining_messages_zero.md) (1 shared connections)
- [test_get_system_stats](test_get_system_stats.md) (1 shared connections)
- [test_get_system_stats_no_players](test_get_system_stats_no_players.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_rate_limiter.py`

## Audit Trail

- EXTRACTED: 69 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*