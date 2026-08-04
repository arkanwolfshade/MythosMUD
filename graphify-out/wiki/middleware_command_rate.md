# middleware command rate

> 32 nodes

## Key Concepts

- **CommandRateLimiter** (17 connections) — `server/middleware/command_rate_limiter.py`
- **test_command_rate_limiter.py** (11 connections) — `server/tests/unit/middleware/test_command_rate_limiter.py`
- **_fixed_clock()** (8 connections) — `server/tests/unit/middleware/test_command_rate_limiter.py`
- **datetime** (8 connections)
- **command_rate_limiter.py** (7 connections) — `server/middleware/command_rate_limiter.py`
- **test_is_allowed_under_limit()** (4 connections) — `server/tests/unit/middleware/test_command_rate_limiter.py`
- **test_is_allowed_blocks_at_limit()** (4 connections) — `server/tests/unit/middleware/test_command_rate_limiter.py`
- **test_sliding_window_expires_old_commands()** (4 connections) — `server/tests/unit/middleware/test_command_rate_limiter.py`
- **test_get_wait_time_when_rate_limited()** (4 connections) — `server/tests/unit/middleware/test_command_rate_limiter.py`
- **test_reset_player_and_all()** (4 connections) — `server/tests/unit/middleware/test_command_rate_limiter.py`
- **test_get_stats_and_cleanup_inactive()** (4 connections) — `server/tests/unit/middleware/test_command_rate_limiter.py`
- **.__init__()** (3 connections) — `server/middleware/command_rate_limiter.py`
- **.get_stats()** (3 connections) — `server/middleware/command_rate_limiter.py`
- **datetime** (2 connections)
- **.is_allowed()** (2 connections) — `server/middleware/command_rate_limiter.py`
- **.get_wait_time()** (2 connections) — `server/middleware/command_rate_limiter.py`
- **.get_remaining_commands()** (2 connections) — `server/middleware/command_rate_limiter.py`
- **.reset_player()** (2 connections) — `server/middleware/command_rate_limiter.py`
- **.reset_all()** (2 connections) — `server/middleware/command_rate_limiter.py`
- **.cleanup_inactive_players()** (2 connections) — `server/middleware/command_rate_limiter.py`
- **Any** (1 connections)
- **Per-player command rate limiting.  Prevents command flooding and denial-of-servi** (1 connections) — `server/middleware/command_rate_limiter.py`
- **Per-player command rate limiting using sliding window algorithm.      Tracks com** (1 connections) — `server/middleware/command_rate_limiter.py`
- **Initialize command rate limiter.          Args:             max_commands: Maximu** (1 connections) — `server/middleware/command_rate_limiter.py`
- **Check if player can execute a command now.          Implements sliding window ra** (1 connections) — `server/middleware/command_rate_limiter.py`
- *... and 7 more nodes in this community*

## Relationships

- [NPC Combat](NPC_Combat.md) (2 shared connections)
- [command commands handler](command_commands_handler.md) (1 shared connections)

## Source Files

- `server/middleware/command_rate_limiter.py`
- `server/tests/unit/middleware/test_command_rate_limiter.py`

## Audit Trail

- EXTRACTED: 107 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*