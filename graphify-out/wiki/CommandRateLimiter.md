# CommandRateLimiter

> 32 nodes

## Key Concepts

- **CommandRateLimiter** (17 connections) — `server/middleware/command_rate_limiter.py`
- **test_command_rate_limiter.py** (11 connections) — `server/tests/unit/middleware/test_command_rate_limiter.py`
- **_fixed_clock()** (8 connections) — `server/tests/unit/middleware/test_command_rate_limiter.py`
- **datetime** (8 connections)
- **command_rate_limiter.py** (7 connections) — `server/middleware/command_rate_limiter.py`
- **test_get_stats_and_cleanup_inactive()** (4 connections) — `server/tests/unit/middleware/test_command_rate_limiter.py`
- **test_get_wait_time_when_rate_limited()** (4 connections) — `server/tests/unit/middleware/test_command_rate_limiter.py`
- **test_is_allowed_blocks_at_limit()** (4 connections) — `server/tests/unit/middleware/test_command_rate_limiter.py`
- **test_is_allowed_under_limit()** (4 connections) — `server/tests/unit/middleware/test_command_rate_limiter.py`
- **test_reset_player_and_all()** (4 connections) — `server/tests/unit/middleware/test_command_rate_limiter.py`
- **test_sliding_window_expires_old_commands()** (4 connections) — `server/tests/unit/middleware/test_command_rate_limiter.py`
- **.get_stats()** (3 connections) — `server/middleware/command_rate_limiter.py`
- **.__init__()** (3 connections) — `server/middleware/command_rate_limiter.py`
- **.cleanup_inactive_players()** (2 connections) — `server/middleware/command_rate_limiter.py`
- **.get_remaining_commands()** (2 connections) — `server/middleware/command_rate_limiter.py`
- **.get_wait_time()** (2 connections) — `server/middleware/command_rate_limiter.py`
- **.is_allowed()** (2 connections) — `server/middleware/command_rate_limiter.py`
- **.reset_all()** (2 connections) — `server/middleware/command_rate_limiter.py`
- **.reset_player()** (2 connections) — `server/middleware/command_rate_limiter.py`
- **datetime** (2 connections)
- **Any** (1 connections)
- **Per-player command rate limiting. Prevents command flooding and denial-of-…** (1 connections) — `server/middleware/command_rate_limiter.py`
- **Get number of commands player can still execute. Args: player_name: Player to…** (1 connections) — `server/middleware/command_rate_limiter.py`
- **Reset rate limit for a specific player. Useful for admin commands or when…** (1 connections) — `server/middleware/command_rate_limiter.py`
- **Reset rate limit for all players. Clears all accumulated timestamp data.…** (1 connections) — `server/middleware/command_rate_limiter.py`
- *... and 7 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (2 shared connections)
- [command_handler_unified.py](command_handler_unified.py.md) (1 shared connections)

## Source Files

- `server/middleware/command_rate_limiter.py`
- `server/tests/unit/middleware/test_command_rate_limiter.py`

## Audit Trail

- EXTRACTED: 49 (89%)
- INFERRED: 6 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*