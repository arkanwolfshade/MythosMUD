# CommandRateLimiter

> 30 nodes

## Key Concepts

- **CommandRateLimiter** (17 connections) — `server/middleware/command_rate_limiter.py`
- **test_command_rate_limiter.py** (11 connections) — `server/tests/unit/middleware/test_command_rate_limiter.py`
- **_fixed_clock()** (8 connections) — `server/tests/unit/middleware/test_command_rate_limiter.py`
- **datetime** (8 connections)
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
- **Get number of commands player can still execute. Args: player_name: Player to…** (1 connections) — `server/middleware/command_rate_limiter.py`
- **Reset rate limit for a specific player. Useful for admin commands or when…** (1 connections) — `server/middleware/command_rate_limiter.py`
- **Reset rate limit for all players. Clears all accumulated timestamp data.…** (1 connections) — `server/middleware/command_rate_limiter.py`
- **Get system-wide rate limiting statistics. Returns: Dictionary containing rate…** (1 connections) — `server/middleware/command_rate_limiter.py`
- **Remove timestamp data for players who haven't been active recently. Prevents…** (1 connections) — `server/middleware/command_rate_limiter.py`
- *... and 5 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (3 shared connections)

## Source Files

- `server/middleware/command_rate_limiter.py`
- `server/tests/unit/middleware/test_command_rate_limiter.py`

## Audit Trail

- EXTRACTED: 45 (88%)
- INFERRED: 6 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*