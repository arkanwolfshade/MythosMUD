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

- [game room service](game_room_service.md) (8 shared connections)
- [room game service](room_game_service.md) (5 shared connections)
- [rate limiter services](rate_limiter_services.md) (4 shared connections)
- [events event bus](events_event_bus.md) (2 shared connections)
- [time service rationale](time_service_rationale.md) (1 shared connections)
- [chat game message](chat_game_message.md) (1 shared connections)
- [event bus events](event_bus_events.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_rate_limiter.py`

## Audit Trail

- EXTRACTED: 72 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*