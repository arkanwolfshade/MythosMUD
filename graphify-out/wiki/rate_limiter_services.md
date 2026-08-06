# rate limiter services

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

- [event events serialization](event_events_serialization.md) (4 shared connections)
- [Error Conversion](Error_Conversion.md) (2 shared connections)
- [test_messaging_integration_init](test_messaging_integration_init.md) (1 shared connections)
- [test_resolve_connection_manager_from_container_no_manager](test_resolve_connection_manager_from_container_no_manager.md) (1 shared connections)
- [test_validate_combat_state_not_in_combat_required](test_validate_combat_state_not_in_combat_required.md) (1 shared connections)
- [test_validate_combat_state_in_combat_required](test_validate_combat_state_in_combat_required.md) (1 shared connections)
- [test_validate_combat_command_target_too_long](test_validate_combat_command_target_too_long.md) (1 shared connections)
- [test_validate_target_exists_partial_match](test_validate_target_exists_partial_match.md) (1 shared connections)
- [test_validate_target_exists_no_match](test_validate_target_exists_no_match.md) (1 shared connections)
- [test_validate_target_exists_exact_match](test_validate_target_exists_exact_match.md) (1 shared connections)
- [test_validate_target_exists_case_insensitive](test_validate_target_exists_case_insensitive.md) (1 shared connections)
- [test_validate_target_alive_alive](test_validate_target_alive_alive.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_rate_limiter.py`

## Audit Trail

- EXTRACTED: 72 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*