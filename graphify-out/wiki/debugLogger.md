# debugLogger

> 26 nodes · cohesion 0.08

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

- [_StubPlayerRepo](_StubPlayerRepo.md) (3 shared connections)
- [🔴 CRITICAL ISSUES](🔴_CRITICAL_ISSUES.md) (2 shared connections)
- [test_container_persistence_async_helpers.py](test_container_persistence_async_helpers.py.md) (1 shared connections)
- [Room](Room.md) (1 shared connections)
- [test_handle_stop_command_no_player](test_handle_stop_command_no_player.md) (1 shared connections)
- [test_process_tick_regeneration_player_not_found](test_process_tick_regeneration_player_not_found.md) (1 shared connections)
- [test_process_tick_regeneration_calculates_max_from_power](test_process_tick_regeneration_calculates_max_from_power.md) (1 shared connections)
- [infrastructure/__init__.py](infrastructure-__init__.py.md) (1 shared connections)
- [test_announce_spell_cast_no_player_id](test_announce_spell_cast_no_player_id.md) (1 shared connections)
- [test_generate_room_id_from_zone_data_with_prefix](test_generate_room_id_from_zone_data_with_prefix.md) (1 shared connections)
- [test_handle_spell_command_wrapper_success](test_handle_spell_command_wrapper_success.md) (1 shared connections)
- [test_parse_exits_json_string_valid](test_parse_exits_json_string_valid.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_rate_limiter.py`

## Audit Trail

- EXTRACTED: 47 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*